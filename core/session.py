import streamlit as st


def initialize_session():

    defaults = {
        "current_page": "home",
        "notebooks": [],
        "current_notebook": None,
        "sources": [],
        "active_tool": None,
        "chat_history": [],
        "mindmap_data": None,
        "report_data": None,
        "flashcards_data": [],
        "quiz_data": [],
        "slides_data": [],
        "datatable_data": None,
        "audio_script": None,
        "video_script": None,
        "doubt_predictions": [],
        "misconceptions": [],
        "learning_roadmap": [],
        "teach_me_output": []
    }

    for key, value in defaults.items():

        if key not in st.session_state:
            st.session_state[key] = value
