import streamlit as st
from run_paper import clean_directories, get_input, run_build, run_analysis, compile_tex

base_path = '/path/to/main_paper'  # Update this to your actual path

st.title("Process Automation for Empirical Papers")

if st.button("Clean Output and Temporary Folders"):
    clean_directories(base_path)
    st.write("Output and Temporary Folders Cleaned")

if st.button("Get Input Data"):
    get_input(base_path)
    st.write("Input Data Obtained")

if st.button("Run Data Build"):
    run_build(base_path)
    st.write("Data Build Executed")

if st.button("Run Analysis"):
    run_analysis(base_path)
    st.write("Analysis Executed")

if st.button("Compile TeX Document"):
    pdf_file = compile_tex(base_path)
    if pdf_file:
        with open(pdf_file, "rb") as f:
            st.download_button(label="Download PDF", data=f, file_name="main_article.pdf")
        st.write("TeX Document Compiled and Ready for Download")
    else:
        st.write("TeX Compilation Failed")

st.write("Congratulations, you have a shiny new paper!")
