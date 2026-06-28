import streamlit as st


def show_home():
    st.title("📚 PaperLens")

    st.subheader("Read less. Understand more.")

    st.write(
        """
        PaperLens helps you understand research papers faster.
        Upload papers, generate concise briefings, chat with your sources,
        discover key findings, and uncover insights without spending hours
        reading every page.
        """
    )

    st.divider()

    st.write("### What can PaperLens do?")

    c1, c2, c3 = st.columns(3)

    with c1:
        with st.container(border=True):
            st.subheader("📄 Brief")
            st.caption("Generate concise summaries and key findings.")

    with c2:
        with st.container(border=True):
            st.subheader("💬 Chat")
            st.caption("Ask questions about your papers.")

    with c3:
        with st.container(border=True):
            st.subheader("🔍 Discover")
            st.caption("Generate flashcards, notes, and insights.")

    st.divider()

    col1, col2 = st.columns([3, 1])

    with col1:
        st.write("### Your Notebooks")

    with col2:
        if st.button("➕ Create Notebook", use_container_width=True, type="primary"):
            st.session_state.show_create_modal = True
            st.rerun()

    st.write("")

    notebooks = st.session_state.get("notebooks", [])

    if len(notebooks) == 0:
        st.info("No notebooks yet. Click 'Create Notebook' to get started!")
    else:
        for notebook in notebooks:
            with st.container(border=True):
                col1, col2, col3 = st.columns([3, 1, 1])
                
                with col1:
                    st.write(f"📔 **{notebook['name']}**")
                    st.caption(f"{notebook['sources']} sources · {notebook['date']}")
                
                with col2:
                    if st.button("Open", key=f"open_{notebook['id']}", use_container_width=True):
                        st.session_state.current_notebook = notebook['id']
                        st.session_state.page = "Studio"
                        st.rerun()
                
                with col3:
                    if st.button("Delete", key=f"delete_{notebook['id']}", use_container_width=True):
                        notebooks.remove(notebook)
                        st.rerun()
