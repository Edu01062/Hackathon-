import streamlit as st
import pandas as pd

# I have provided most of what you need for to use streamlit here and in README.md
# You can also check the streamlit docs at https://docs.streamlit.io/get-started
# Also, you can check a simple example from class:
# Page: https://simpson-dashboard-class.streamlit.app/
# GitHub Repo: https://github.com/RodrigoGrijalba/python-dashboard-class

st.set_page_config(page_title = "<<Grupo 1 - Advertising>>", layout = "wide")

tab1, tab2, tab3, tab4 = st.tabs(["Original Paper", "Proposed Extention", "Extension Results", "References"])

with tab1:
    st.markdown("""
    ### Design description
    Based around 8 Features on content on bank loan advertisement.
    -Photography, Suggestions, Etc.
    This is for a single bank in South Africa. 

    ### Data
    South Africa - Bank Loan RCT - 53,650 Observations

    ### Original results
    <<Your description here, in Markdown>>
    """
    )
    # st.image("<<path to image from project's root, if needed>>") # uncomment this line if you would like to add an image

with tab2:

    st.markdown("""
    ### Proposed extension

    Casual Forest and Double Lasson with partialling Out

    ### Justification
    <<Generally we can say that it is helpful for heteregenous effect and finding the particular effect
    of one treatment effect. In this case, we will be studying being a high-risk creditor to the outcome
    of applying to the offered loan.>>
    """
    )
    # st.image("<<path to image from project's root, if needed>>") # uncomment this line if you would like to add an image
    # table = pd.read_csv("<<path/to/table.csv>>") # load a table from csv to show it on the page
    # st.table(table) # show table


with tab3:

    st.markdown("""
    ### Extension results

    <<We find that interest rate is generally one of the major factors in the average treatment effect.>>
    """
    )
    st.image("CATE.png")
    table = pd.read_csv("table_forest.csv")
    st.table(table)

    st.markdown('''<<However, we also find that the ATE is negative given the following. 
    This could be explained due to the fact that high risk borrowers are less likely to take on more loans.>>)''')
    st.image("ATE_final.png")
    # st.image("<<path to image from project's root, if needed>>") # uncomment this line if you would like to add an image

with tab4:

    st.markdown("""
    <<Your description here, in Markdown>>
    """
    )
    # st.image("<<path to image from project's root, if needed>>") # uncomment this line if you would like to add an image

