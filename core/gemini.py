from google import genai
import streamlit as st


def get_client():

    return genai.Client(
        api_key=st.secrets["GEMINI_API_KEY"]
    )


def ask(prompt):

    client = get_client()

    response = client.models.generate_content(
        model="gemini-3.1-flash-lite",
        contents=prompt
    )

    return response.text


def stream_ask(prompt):

    client = get_client()

    response = client.models.generate_content_stream(
        model="gemini-3.1-flash-lite",
        contents=prompt
    )

    for chunk in response:

        if chunk.text:
            yield chunk.text
