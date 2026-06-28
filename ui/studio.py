import streamlit as st
from datetime import datetime


def show_studio():
    
    notebook = st.session_state.get("current_notebook")
    
    if not notebook:
        st.error("No notebook selected")
        return
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.write("### 📔 Notebook Info")
        
        notebook_name = st.text_input(
            "Notebook Name",
            value=notebook.get("name", "Untitled notebook"),
            label_visibility="collapsed"
        )
        notebook["name"] = notebook_name
        
        sources_count = len(notebook.get("sources", []))
        st.metric("Sources", sources_count)
        
        notebook_date = notebook.get("date", datetime.now().strftime("%b %d, %Y"))
        st.caption(f"📅 {notebook_date}")
        
        st.divider()
        
        st.write("### 📚 Sources")
        
        if sources_count == 0:
            st.info("No sources added yet")
        else:
            for i, source in enumerate(notebook.get("sources", [])):
                with st.container(border=True):
                    st.write(f"**{source.get('name', 'Untitled')}**")
                    st.caption(source.get("type", "Unknown"))
                    
                    if st.button("Remove", key=f"remove_source_{i}"):
                        notebook["sources"].pop(i)
                        st.rerun()
        
        if st.button("➕ Add Source", use_container_width=True):
            st.session_state.show_source_modal = True
            st.rerun()
    
    with col2:
        st.write("### 🎬 Studio")
        
        languages = ["हिन्दी", "বাংলা", "ગુજરાતી", "ಕನ್ನಡ", "മലയാളം", "मराठी", "ਪੰਜਾਬੀ", "தமிழ்", "తెలుగు"]
        
        selected_language = st.selectbox(
            "Create an Audio Overview in:",
            languages,
            label_visibility="collapsed"
        )
        
        st.write("")
        
        st.write("**Available Tools:**")
        
        tool_col1, tool_col2 = st.columns(2)
        
        with tool_col1:
            if st.button("🎵 Audio Overview", use_container_width=True):
                st.session_state.selected_tool = "audio"
                st.rerun()
            
            if st.button("📊 Mind Map", use_container_width=True):
                st.session_state.selected_tool = "mindmap"
                st.rerun()
            
            if st.button("📋 Flashcards", use_container_width=True):
                st.session_state.selected_tool = "flashcards"
                st.rerun()
            
            if st.button("📈 Data Table", use_container_width=True):
                st.session_state.selected_tool = "datatable"
                st.rerun()
        
        with tool_col2:
            if st.button("🎥 Video Overview", use_container_width=True):
                st.session_state.selected_tool = "video"
                st.rerun()
            
            if st.button("📄 Reports", use_container_width=True):
                st.session_state.selected_tool = "reports"
                st.rerun()
            
            if st.button("❓ Quiz", use_container_width=True):
                st.session_state.selected_tool = "quiz"
                st.rerun()
        
        st.divider()
        
        st.write("### 📤 Studio Output")
        
        selected_tool = st.session_state.get("selected_tool")
        
        if selected_tool:
            st.info(f"Generating {selected_tool}... (coming soon)")
        else:
            st.caption("Select a tool above to start generating content")
