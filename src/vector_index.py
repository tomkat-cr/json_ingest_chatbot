from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from langchain.indexes import VectorstoreIndexCreator


class VectorEntry():
    def __init__(self, page_content, metadata={}):
        # Example: page_content='The loaded git repo name is myrepo'
        self.page_content = page_content
        #  Example: metadata={'source': 'path/to/file.py',
        # 'file_path': 'path/to/file.py', 'file_name': 'file.py',
        # 'file_type': '.py'}
        self.metadata = metadata


def get_vector_index(vectorstore):
    index = VectorstoreIndexCreator().from_documents(
        vectorstore
    )
    return index


def get_conversation_chain(
    vectorstore, gpt_model, gpt_temperature
):
    llm = ChatOpenAI(
        model=gpt_model,
        temperature=gpt_temperature
    )
    memory = ConversationBufferMemory(
        memory_key='chat_history', return_messages=True
    )
    conversation_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vectorstore.as_retriever(),
        memory=memory
    )
    return conversation_chain
