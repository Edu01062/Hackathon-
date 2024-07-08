import os
import platform
import shutil
from subprocess import call
import streamlit as st
import glob

system = platform.system()
person = ''  # Use the person variable to keep paths in order with multiple machines being used

if person == '':
    path = '/path/to/main_paper'  # Update this reference to your actual path

st.title("Process Automation for Empirical Papers")

if system == 'Windows':
    st.write("The script is not configured for Windows.")
else:
    if st.button("Clean Output and Temporary Folders"):
        st.write("Cleaning Output and Temporary Folders")
        for folder in ['/output', '/tmp']:
            folder_path = os.path.join(path, folder.strip('/'))
            if os.path.exists(folder_path):
                shutil.rmtree(folder_path)
            os.mkdir(folder_path)
        st.write("Output and Temporary Folders Cleaned")

    if st.button("Get Input Data"):
        st.write("Getting Input Data")
        call(['python', os.path.join(path, 'code/get_input.py')])
        st.write("Input Data Obtained")

    if st.button("Run Data Build"):
        st.write("Running Data Build")
        call(['python', os.path.join(path, 'code/build_data.py')])  # Replace with your actual build script
        for file in glob.glob(os.path.join(path, 'output/logs/*.log')):
            os.remove(file)
        st.write("Data Build Executed")

    if st.button("Run Analysis"):
        st.write("Running Analysis")
        call(['python', os.path.join(path, 'code/analysis.py')])  # Replace with your actual analysis script
        for file in glob.glob(os.path.join(path, 'output/logs/*.log')):
            os.remove(file)
        st.write("Analysis Executed")

    if st.button("Compile TeX Document"):
        st.write("Compiling TeX Document")
        call(['latexmk', os.path.join(path, 'products/paper/main_article.tex')])
        st.write("TeX Document Compiled")

    st.write("Congratulations, you have a shiny new paper!")