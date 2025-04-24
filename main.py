import streamlit as st
import pandas as pd

st.set_page_config(page_title="ASG", layout="wide", page_icon=":star:")

st.sidebar.title("Navigasi")
page = st.sidebar.radio("Pilih Halaman", ["About Me", "Project", "Contact"])

if page == "About Me":
    import about_me
    about_me.show_about_me()
if page == "Project":
    import project
    project.show_project()
if page == "Contact":
    import contact
    contact.show_contact()
