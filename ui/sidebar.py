import streamlit as st


def show_sidebar():
    st.sidebar.title("📚 PaperLens")
    st.sidebar.markdown("---")
    
    col1, col2 = st.sidebar.columns(2)
    
    with col1:
        if st.button("🏠 Home", use_container_width=True):
            st.session_state.page = "Home"
            st.rerun()
    
    with col2:
        if st.button("🎬 Studio", use_container_width=True):
            st.session_state.page = "Studio"
            st.rerun()
    
    st.sidebar.markdown("---")
    
    st.sidebar.header("📊 Quick Stats")
    st.sidebar.metric("Notebooks", len(st.session_state.get("notebooks", [])))
    st.sidebar.metric("Total Sources", sum(len(n.get("sources", [])) for n in st.session_state.get("notebooks", [])))
    
    st.sidebar.markdown("---")
    
    st.sidebar.header("⚙️ Settings")
    
    if st.sidebar.checkbox("Dark Mode"):
        st.session_state.dark_mode = True
    else:
        st.session_state.dark_mode = False
    
    st.sidebar.markdown("---")
    
    st.sidebar.markdown("⚡ Powered by :rainbow[Gemini 3.1 Flash Lite]")
    
    st.sidebar.markdown("---")
    
    st.sidebar.markdown("""
    **About PaperLens**
    - Transform papers into learning tools
    - Generate flashcards, quizzes, mindmaps
    - AI-powered educational assistant
    """)
    
    st.sidebar.markdown("---")
    
    st.sidebar.caption("Made with ❤️ for students")
