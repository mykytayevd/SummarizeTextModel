from fastapi import FastAPI, HTTPException
from models.summarize import SummarizeResponse, SummarizeRequest
from transformers import pipeline
from langchain.chains import LLMChain
from langchain_core.prompts import PromptTemplate
from langchain.llms import HuggingFacePipeline
import uvicorn

app = FastAPI()

# Initialize the summarizer with a pre-trained model from Hugging Face and the summarization pipeline
summarization_pipeline = pipeline("summarization")
llm = HuggingFacePipeline(pipeline=summarization_pipeline)

# Define a simple prompt template for summarization
prompt_template = PromptTemplate(template="{text}", input_variables=["text"])

# Create an LLMChain for the summarization task
summarization_chain = LLMChain(llm=llm, prompt=prompt_template)


@app.post("/summarize", response_model=SummarizeResponse)
async def summarize(request: SummarizeRequest):
    if not request.text:
        raise HTTPException(status_code=400, detail="Input text is required.")

    # Use the summarization chain to generate a summary
    summary = summarization_chain.run(text=request.text)
    return SummarizeResponse(summary=summary)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
