print("hello")

from langchain_core.runnables import RunnableSerializable, RunnablePassthrough
from utils_graph.langchain_utils import LLMChain
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI
from pydantic import BaseModel, Field
from typing import Dict, Any
import logging

class ScriptAgent(RunnableSerializable, BaseModel):
    name: str = Field(default="script_agent", description="Name of the agent")
    model_name: str = Field(default="llama-3.3-70b-versatile", description="Groq Llama model name")
    temperature: float = Field(default=0.3, description="Model temperature")
    max_tokens: int = Field(default=500, description="Maximum tokens for the output")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.__name__ = self.name

    def invoke(self, input: Dict[str, Any], config: Dict[str, Any] = None) -> Dict[str, Any]:
        logging.debug("Invoking ScriptAgent...")
        topic = input.get("topic", "")
        if not topic:
            return {"script": None, "success": False, "message": "Missing 'topic' in input."}
               
        topic = input["topic"]
        logging.debug(f"Received topic: {topic}")

        try:
            chain_builder = LLMChain(
                model_name=self.model_name,
                temperature=self.temperature,
                max_tokens=self.max_tokens
            )

            chain = chain_builder.build_chain(
                "You are a professional scriptwriter. Generate a clear, engaging and fluent narration based on the following topic: {topic}"
            )

            result = chain.invoke({"topic": topic})
            logging.debug(f"ScriptAgent output: {result}")

            return {
                "script": result,
                "success": True,
                "message": "Script generated successfully."
            }

        except Exception as e:
            return {
                "script": None,
                "success": False,
                "message": f"Failed to generate script: {str(e)}"
            }