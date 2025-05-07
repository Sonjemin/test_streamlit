import streamlit as st
from openai import OpenAI

api_key= st.text_input("OpenAI API Key", type="password")
client = OpenAI(api_key="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")

st.title("OpenAI GPT model")

prompt = st.text_area("User prompt")

if st.button("Ask!", disabled=(len(prompt)==0)):
    response = client.responses.create(
        model="gpt-4.1-mini",
        input=prompt
    )

    st.write(response.output_text)
