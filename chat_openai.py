from llama_index.core import SimpleDirectoryReader, VectorStoreIndex, StorageContext, load_index_from_storage
from llama_index.llms.openai import OpenAI
import os
from timeit import default_timer as timer

start = timer()

# ------------------------------------------
# ------------ CONFIGURAR A LLM ------------
# ------------------------------------------
os.environ["OPENAI_API_KEY"] = "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"
llm = OpenAI(model="gpt-3.5-turbo")
# ------------------------------------------

# # ----------------------------------------------------------------------
# # ------------ CRIAR A VECTOR STORE A PARTIR DOS DOCUMENTOS ------------
# # ----------------------------------------------------------------------
# # Carregar documentos...
# documents = SimpleDirectoryReader("./data").load_data()

# # Criar vector store index
# index = VectorStoreIndex.from_documents(documents)
# # Persistir VectorStore em disco
# index.storage_context.persist(persist_dir="vectorstorage")
# # ----------------------------------------------------------------------

# -----------------------------------------------------------------
# ------------ CARREGAR VECTOR STORE A PARTIR DO DISCO ------------
# -----------------------------------------------------------------
storage_context = StorageContext.from_defaults(persist_dir="vectorstorage")
index = load_index_from_storage(storage_context)
# -----------------------------------------------------------------

# -------------------------------------------------
# ------------ PREPARAR A CHAT ENGINE ------------
# -------------------------------------------------
chat_engine = index.as_chat_engine(llm=llm, streaming=True)
# -------------------------------------------------

# -------------------------------------------------------------------
# ------------ GERAR A RESPOSTA A PARTIR DA QUERY ENGINE ------------
# -------------------------------------------------------------------
response = chat_engine.chat("E deste nome completo, qual o sobrenome?")
print(response)
# -------------------------------------------------------------------

# ------- Get response Metadata -------
if hasattr(response, 'metadata'):
    print(response.metadata)

end = timer()
print('Execution time: {}'.format(end - start))