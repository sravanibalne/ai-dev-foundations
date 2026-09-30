import os
from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
from langchain_pinecone import PineconeVectorStore

load_dotenv()

embeddings = OpenAIEmbeddings(
    model="text-embedding-3-small",
    dimensions=512,
    openai_api_key=os.getenv("OPENAI_API_KEY")
)

vectorstore = PineconeVectorStore(
    index_name="pulseapi-docs",
    embedding=embeddings,
    pinecone_api_key=os.getenv("PINECONE_API_KEY")
)

query = "how do I stop getting rate limited?"
#query = "What does a 400 error mean?"
results = vectorstore.similarity_search(query, k=2)

for i, doc in enumerate(results):
    print(f"--- Match {i+1} ---")
    print(doc.page_content)
    print()