import json
import streamlit as st
from dotenv import load_dotenv
from htmlcss import bot_template, user_template, css
from langchain.document_loaders.json_loader import JSONLoader
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from langchain.indexes import VectorstoreIndexCreator


def get_page_content_attr(filename):
    attr_value = filename
    if filename == "general_ingredients.json":
        attr_value = "general ingredients table"
    elif filename == "food_times.json":
        attr_value = "meal type"
    elif filename == "user_ingredients.json":
        attr_value = "my favorite ingredients"
    elif filename == "food_history.json":
        attr_value = "feeding history, dietary preferences"
    elif filename == "user.json":
        attr_value = "my personal information, dietary restrictions, " + \
            "and any specific dietary goals"
    return attr_value


def get_json_files(json_files):
    attr_name = 'page_content'
    all_pages = []
    for json_file in json_files:
        print(f"json_file: {json_file}")
        output_file_spec = f"./downloads/{json_file.name}"
        with open(output_file_spec, 'wb') as output_file:
            json_content = json_file.getvalue()
            json_dict = {
                'content': json.loads(json_content)
            }
            json_dict[attr_name] = get_page_content_attr(json_file.name)
            json_content = bytes(json.dumps(json_dict), 'UTF8')
            print(f"json_content: {json_content}")
            output_file.write(json_content)
        loader = JSONLoader(
            output_file_spec,
            # jq_schema=f'.[].{attr_name}'
            jq_schema=f'.{attr_name}'
        )
        json_pages = loader.load()
        all_pages += json_pages
    return all_pages


def handle_userinput(user_question):
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
        page_title="Chat con multiples JSONs",
        page_icon=":books:"
    )
    st.write(css, unsafe_allow_html=True)

    if "conversation" not in st.session_state:
        st.session_state.conversation = None
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = None

    st.header(
        "Chat con multiples JSONs :books:"
    )

    user_question = st.text_input(
        "Pregúntale lo que quieras a tus documentos JSON:"
    )
    if user_question:
        handle_userinput(user_question)

    with st.sidebar:

        st.subheader("Configuración del Modelo")
        gpt_model = st.selectbox(
            'Modelo',
            ('gpt-3.5-turbo', 'gpt-4')
        )
        gpt_temperature = st.slider('Temperatura', 0.00, 1.00, 0.7)

        st.subheader("Tus archivos")
        json_docs = st.file_uploader(
            "Sube tus Json aquí y haz click en 'Procesar'",
            accept_multiple_files=True
        )
        if st.button("Procesar"):
            with st.spinner("Procesando..."):
                all_json_files = get_json_files(json_docs)
                index = VectorstoreIndexCreator().from_documents(
                    all_json_files
                )
                st.session_state.conversation = get_conversation_chain(
                    index.vectorstore,
                    gpt_model,
                    gpt_temperature
                )


if __name__ == '__main__':
    main()
