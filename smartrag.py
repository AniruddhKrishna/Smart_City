
!pip install transformers sentence-transformers torch faiss-gpu

!pip install langchain

!pip install -U langchain-community

!pip install streamlit

# Import necessary libraries
import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer
from sentence_transformers import SentenceTransformer
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.document_loaders import TextLoader
from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA
from langchain.llms import HuggingFacePipeline
from transformers import pipeline

import streamlit as st
from transformers import GPT2LMHeadModel, GPT2Tokenizer, pipeline
from sentence_transformers import SentenceTransformer
from langchain.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.llms import HuggingFacePipeline
from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA
import os
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
from sentence_transformers import SentenceTransformer
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain.llms import HuggingFacePipeline

print('cuda' if torch.cuda.is_available() else 'cpu')

def load_and_process_document(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )
    return text_splitter.split_text(text)

def create_vector_store(texts):
    model_name = "sentence-transformers/all-MiniLM-L6-v2"
    model_kwargs = {'device': 'cuda' if torch.cuda.is_available() else 'cpu'}
    embeddings = HuggingFaceEmbeddings(model_name=model_name, model_kwargs=model_kwargs)
    return FAISS.from_texts(texts, embeddings)

def setup_language_model():
    model_name = "gpt2"  # You can use "gpt2-medium", "gpt2-large", or "gpt2-xl" for larger models
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name).to('cuda' if torch.cuda.is_available() else 'cpu')

    pipe = pipeline(
        "text-generation",
        model=model,
        tokenizer=tokenizer,
        device=0 if torch.cuda.is_available() else -1,
        max_length=1000,  # Adjust this if needed
        max_new_tokens=150  # Number of tokens to generate after the input
    )

    return HuggingFacePipeline(pipeline=pipe)

def setup_qa_system(docsearch, local_llm):
    return RetrievalQA.from_chain_type(llm=local_llm, chain_type="stuff", retriever=docsearch.as_retriever())

def ask_question(qa, question):
    return qa.run(question)

import os
def main():
    # Directory containing the text files
    directory = "/content"  # Replace with your actual directory path

    # Load and process multiple documents
    texts = []
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            file_path = os.path.join(directory, filename)
            texts.extend(load_and_process_document(file_path))

    # Create vector store
    docsearch = create_vector_store(texts)

    # Set up language model
    local_llm = setup_language_model()

    # Set up QA system
    qa = setup_qa_system(docsearch, local_llm)

    # Example usage
    while True:
        question = input("Enter your question (or 'quit' to exit): ")
        if question.lower() == 'quit':
            break
        answer = ask_question(qa, question)
        print(f"Answer: {answer}\n")

if __name__ == "__main__":
    main()
