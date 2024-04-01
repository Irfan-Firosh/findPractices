import streamlit as st
from search import *
from streamlit_pdf_viewer import pdf_viewer
import time

st.title('Practice Quest')

st.write("Streamlines user learning by displaying subject relevant practice problems in one place")

st.divider()

if "title" not in st.session_state:
    st.session_state["title"] = False

if "files" not in st.session_state:
    st.session_state["files"] = False

def disable_title():
    clearDir()
    st.session_state["title"] = True

def files_present():
    time.sleep(5)
    st.session_state["files"] = True

query = st.text_input(
    label = "Enter your topic",
    placeholder = "Say Something.....",
    disabled = st.session_state["title"],
    on_change = disable_title
)

if st.session_state["title"]:
    path, citations = search_main(query)
    if path != None:
        files_present()
    col1, col2, col3 = st.columns(3, gap="large")
    if st.session_state["files"]:
        fileExt = query.split()[0]
        with col1:
            pdf_viewer(path[0], width = 200, height = 300)
            name = f"{fileExt}1.pdf"
            with open(path[0], "rb") as file:
                pdf = file.read()

            st.download_button(
                label = f"Download {name}",
                data = pdf,
                file_name = name,
                mime = "application/octet-stream"
            )
            st.write("Refer to the [source](%s)" % citations[0])

        with col2:
            pdf_viewer(path[1], width = 200, height = 300)
            name = f"{fileExt}2.pdf"
            with open(path[1], "rb") as file:
                pdf = file.read()

            st.download_button(
                label = f"Download {name}",
                data = pdf,
                file_name = name,
                mime = "application/octet-stream"
            )
            st.write("Refer to the [source](%s)" % citations[1])

        with col3:
            pdf_viewer(path[2], width = 200, height = 300)
            name = f"{fileExt}3.pdf"
            with open(path[2], "rb") as file:
                pdf = file.read()

            st.download_button(
                label = f"Download {name}",
                data = pdf,
                file_name = name,
                mime = "application/octet-stream"
            )
            st.write("Refer to the [source](%s)" % citations[2])