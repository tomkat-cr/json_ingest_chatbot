from dotenv import load_dotenv

import streamlit as st
from htmlcss import bot_template, user_template, css

from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from langchain.indexes import VectorstoreIndexCreator

from json_reader import get_json_files
from git_reader import get_repo_data


def handle_userinput(user_question):
    if st.session_state.conversation is None:
        return

    response = st.session_state.conversation({'question': user_question})
    st.session_state.chat_history = response['chat_history']

    for i, message in enumerate(st.session_state.chat_history):
        if i % 2 == 0:
            st.write(user_template.replace(
                "{{MSG}}", message.content), unsafe_allow_html=True)
        else:
            st.write(bot_template.replace(
                "{{MSG}}", message.content), unsafe_allow_html=True)


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


def main():
    load_dotenv()

    st.set_page_config(
        page_title="Chat with JSON files and Git repos",
        page_icon=":card_index_dividers:"
    )
    st.write(css, unsafe_allow_html=True)

    if "conversation" not in st.session_state:
        st.session_state.conversation = None
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = None

    st.header(
        "Chat with JSON files and Git repos"
    )

    # user_question = st.text_input(
    user_question = st.chat_input(
        "Ask something to the JSON or Git files:"
    )
    if user_question:
        handle_userinput(user_question)

    with st.sidebar:
        st.subheader("JSON files")
        json_docs = st.file_uploader(
            "Upload the JSON file(s) here and click on 'Process'",
            accept_multiple_files=True
        )

        st.subheader("Git repo URL")
        repo_url = st.text_input(
            "Enter the Git repo URL here and click on 'Process'",
            value="",
            # max_chars=80,
            placeholder="https://github.com/username/repo.git"
        )
        branch = st.text_input(
            "Git brach [main]:",
            value="",
            # max_chars=80,
            placeholder="main"
        )

        st.subheader("Model Configuration")
        gpt_model = st.selectbox(
            'Model',
            ('gpt-3.5-turbo', 'gpt-4')
        )
        gpt_temperature = st.slider('Temperature', 0.00, 1.00, 0.7)

        if st.button("Process"):
            with st.spinner("Procesing..."):
                if branch == "":
                    branch = "main"
                repo_data = get_repo_data(repo_url, branch)
                all_json_files = get_json_files(json_docs)
                index = VectorstoreIndexCreator().from_documents(
                    all_json_files + repo_data
                )
                st.session_state.conversation = get_conversation_chain(
                    index.vectorstore,
                    gpt_model,
                    gpt_temperature
                )

        st.markdown('Click on **Process** to load the ' +
                    'JSON files and/or the Git repo.')


if __name__ == '__main__':
    main()
