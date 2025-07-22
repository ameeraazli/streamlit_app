from openai import OpenAI
import streamlit as st
import base64

st.set_page_config(layout = "wide")

st.title("File Analyzer")

model_name = "gpt-4.1"

# display the password text input 
api_key = 

if api_key:
    try:
        client = OpenAI(api_key = api_key)

        # initialize the session state if not exists

        
        # display all history contents based on the role 

        
        # display the chat input with placeholder, and the types of files accepted
        if
            content = []
            display_content = ""

            if prompt.files:
                file = prompt.files[0]

                display_content += f"Uploaded {file.name}"

                # create pdf
                if 

                # create images
                else:
                    
            
            if prompt.text and prompt.files: display_content += "<br>"
            
            if prompt.text:
                text = prompt.text
                display_content += text
                content.append({"type": "text", "text": text})

            # store all history user content in session state

            # display the user content 

            # display the assistant content 

            # store all history assistant content in session state

    except Exception as e:
        st.info(e)