from langchain_core.runnables import RunnableSerializable, RunnableLambda
from utils_graph.langchain_utils import LLMChain
from pydantic import BaseModel, Field
from typing import Dict, Any
import logging

import re

def clean_script_for_voice(text: str) -> str:
    text = re.sub(r"(\*\*|\*)", "", text)
    text = re.sub(r"#+ ", "", text)
    text = re.sub(r"\(.*?\)", "", text)
    return text.strip()


class SummaryAgent(RunnableSerializable, BaseModel):
    name: str = Field(default="summary_agent", description="Name of the agent")
    model_name: str = Field(default="llama-3.3-70b-versatile", description="Groq Llama model name")
    temperature: float = Field(default=0.3, description="Generation temperature")
    max_tokens: int = Field(default=200, description="Maximum tokens for summary")


    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.__name__ = self.name

    def invoke(self, input: Dict[str, Any], config: Dict[str, Any] = None) -> Dict[str, Any]:
        if "script" not in input:
            return {"summary": None, "success": False, "message": "Missing 'script' in input."}

        try:
            chain_builder = LLMChain(
                model_name=self.model_name,
                temperature=self.temperature,
                max_tokens=self.max_tokens
            )

            chain = chain_builder.build_chain(
                "Summarize the following narration in 2 or 3 clear, concise and fluent sentences:\n\n{script}"
            )

            

            chain = chain | RunnableLambda(clean_script_for_voice)

            summary = chain.invoke(input)
            logging.debug(f"\n🧪 [summary_agent] Résultat brut de chain.invoke(input):\n👉 type = {type(summary)}\n📄 contenu = {summary}\n")

            return {
                "summary": summary,
                "success": True,
                "message": "Summary generated successfully."
            }

        except Exception as e:
            
            logging.error(f"[summary_agent] Failed to generate summary: {str(e)}")
            return {
                "summary": None,
                "success": False,
                "message": f"Failed to generate summary: {str(e)}"
            }