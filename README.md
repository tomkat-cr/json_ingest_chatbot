# json_ingest_chatbot

<p align="center"><img src="https://socialify.git.ci/tomkat-cr/json_ingest_chatbot/image?description=0&amp;font=Inter&amp;language=1&amp;name=1&amp;owner=1&amp;pattern=Plus&amp;stargazers=0&amp;theme=Light" alt="project-image"></p>

JSON ingest chatbot using Python, Langchain and OpenAI GPT models

This repository contains the source code for a chatbot application that interacts with multiple JSON data documents. The application uses `OpenAI` GPT models to generate conversational responses based on the contents of the JSON files, and `streamlit` for the web interface.

<!---
![Chat with Multiple JSONs](assets/screen.png)
-->

## Repository Contents

- `src/htmlcss.py`: Contains the HTML and CSS templates used to structure and style the web application.

- `src/json.py`: This script runs the main part of the application. It includes functionalities such as extracting data from JSON files, handling user inputs, generating conversational responses, and setting up the Streamlit application.

## How to Run the Application

To run the application, execute the following command in the terminal:

```bash
streamlit run src/json.py
```

You will also need to provide your own API key to access OpenAI.

## Instructions for Use

1. Run the application with the command above.

2. Navigate to the browser window that opens.

3. In the sidebar, upload the JSON files you want the chatbot to interact with.

4. Configure the GPT model and temperature options as desired.

5. Click "Process" and wait for the JSON files to be processed.

6. Enter your questions in the input box and receive responses from the chatbot.

## Contributors

[Your Name] - [Your Email]

[Contributor Name] - [Contributor Email]

Please feel free to suggest improvements, report bugs, or make a contribution to the code.

## License

This project is licensed under the terms of the MIT license.

## Acknowledgements

This project uses OpenAI's GPT models and Streamlit. We appreciate their contributions to the open-source community.
Readme generate by [The AI Readme Generator](https://github.com/tomkat-cr/ai_readme_generator/)