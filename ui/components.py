import streamlit as st
from datetime import datetime


def create_notebook_modal():
    st.write("### 🎯 Create Audio and Video Overviews")
    st.write("from websites, your documents")
    
    st.divider()
    
    tab1, tab2, tab3 = st.tabs(["📄 Upload Files", "🔗 Add URL", "🔍 Search Web"])
    
    with tab1:
        st.write("**Drop your files**")
        st.write("Supported: PDF, TXT")
        
        uploaded_files = st.file_uploader(
            "Choose files",
            type=["pdf", "txt"],
            accept_multiple_files=True,
            label_visibility="collapsed"
        )
        
        if uploaded_files:
            for file in uploaded_files:
                st.success(f"✅ {file.name}")
    
    with tab2:
        url = st.text_input("Enter URL")
        if url:
            st.success(f"✅ URL added: {url}")
    
    with tab3:
        search_query = st.text_input("Search for sources")
        if search_query:
            st.info(f"Searching for: {search_query}")


def notebook_card(notebook):
    with st.container(border=True):
        col1, col2, col3 = st.columns([3, 1, 1])
        
        with col1:
            st.write(f"📔 **{notebook['name']}**")
            st.caption(f"{notebook['sources']} sources · {notebook['date']}")
        
        with col2:
            return st.button("Open", key=f"open_{notebook['id']}", use_container_width=True)
        
        with col3:
            return st.button("Delete", key=f"delete_{notebook['id']}", use_container_width=True)


def source_card(source, index):
    with st.container(border=True):
        col1, col2 = st.columns([3, 1])
        
        with col1:
            st.write(f"**{source.get('name', 'Untitled')}**")
            st.caption(source.get("type", "Unknown"))
        
        with col2:
            if st.button("Remove", key=f"remove_source_{index}"):
                return True
    
    return False


def tool_button(label, icon, key):
    return st.button(f"{icon} {label}", use_container_width=True, key=key)
