from llama_index.core import SimpleDirectoryReader, VectorStoreIndex, StorageContext, load_index_from_storage
from llama_index.llms.openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

class RagClient:
    def __init__(self):
        os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
        self.llm = OpenAI(model="gpt-3.5-turbo")
        storage_context = StorageContext.from_defaults(persist_dir="vectorstorage")
        self.index = load_index_from_storage(storage_context)
        self.chat_engine = self.index.as_chat_engine(llm=self.llm)

    def askChat(self, message):
        response = self.chat_engine.chat(message)
        return response
