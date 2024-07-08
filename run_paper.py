import os
import platform
import shutil
from subprocess import call
import streamlit as st
import glob

system = platform.system()
person = ''  # Use the person variable to keep paths in order with multiple machines being used

if person == '':
    path = '/path/to/main_paper'  # Update this to your actual path

st.title("Process Automation")

if system == 'Windows':
    st.write("The script is not configured for Windows.")
else:
    if st.button("Clean Output and Temporary"):
        st.write("Cleaning Output and Temporary")
        for folder in ['/output', '/tmp']:
            folder_path = os.path.join(path, folder.strip('/'))
            if os.path.exists(folder_path):
                shutil.rmtree(folder_path)
            os.mkdir(folder_path)
        st.write("Output and Temporary Cleaned")

    if st.button("Get Input"):
        st.write("Getting Input")
        call(['python', os.path.join(path, 'code/get_input.py')])
        st.write("Input Obtained")

    if st.button("Run Build"):
        st.write("Running Build")
        call(['stata', '-b', 'do', os.path.join(path, 'code/build.do')])
        for file in glob.glob(os.path.join(path, '*.log')):
            os.remove(file)
        st.write("Build Executed")

    if st.button("Run Analysis"):
        st.write("Running Analysis")
        call(['stata', '-b', 'do', os.path.join(path, 'code/analysis.do')])
        for file in glob.glob(os.path.join(path, '*.log')):
            os.remove(file)
        st.write("Analysis Executed")

    if st.button("Compile TeX"):
        st.write("Compiling TeX")
        call(['latexmk', os.path.join(path, 'products/paper/main_article.tex')])
        st.write("TeX Compiled")

    st.write("Congratulations, you have a shiny new paper!")
