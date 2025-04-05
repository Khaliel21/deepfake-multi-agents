from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from pydantic import BaseModel, Field
from langchain_groq import ChatGroq



class LLMChain(BaseModel):
    model_name: str = Field(default="llama-3.3-70b-versatile", description="Groq Llama model name")
    temperature: float = Field(default=0.3, description="Model temperature")
    max_tokens: int = Field(default=500, description="Maximum tokens for the output")

    def build_chain(self, prompt_template: str):
        llm = ChatGroq(
            model=self.model_name,
            temperature=self.temperature,
            max_tokens=self.max_tokens
        )

        prompt = ChatPromptTemplate.from_template(prompt_template)

        print("$$$$$$$$$$$$$$ HELLO FROM LLMCHAINENNNNNNNNNNNNNNNNNNNNNN")

        return (
            RunnablePassthrough()
            | prompt
            | llm
            | StrOutputParser()
        )