import streamlit as st
import openai
from streamlit.components.v1 import html

st.set_page_config(page_title="Movement Screens & Baseball")


html_temp = """
                <div style="background-color:{};padding:1px">
                
                </div>
                """



with st.sidebar:
    st.markdown("""
    # About 
    Q&A over a few papers that studied the relationship between movement screens and baseball performance 
    """)
    st.markdown(html_temp.format("rgba(55, 53, 47, 0.16)"),unsafe_allow_html=True)
    st.markdown("""
    # How does it work
    Try asking a question related to the papers found here: [Google Drive](https://drive.google.com/drive/folders/1rbpPzWBIl7LLsWSh5hcJcLpMgQl4oCTd?usp=share_link)
    """)
    st.markdown(html_temp.format("rgba(55, 53, 47, 0.16)"),unsafe_allow_html=True)
    st.markdown("""
    Made by [@upliftlabs](https://uplift.ai)
    """,
    unsafe_allow_html=True,
    )


input_text = None
if 'output' not in st.session_state:
    st.session_state['output'] = 0

if st.session_state['output'] <=2:
    st.markdown("""
    # Movement Screens & Baseball
    """)
    input_text = st.text_input("Ask your question", disabled=False, placeholder="are preseason FMS scores related to overuse severity scores?")
    st.session_state['output'] = st.session_state['output'] + 1
else:
    st.info("Thank you! Refresh for more Q&A")


hide="""
<style>
footer{
    visibility: hidden;
    position: relative;
}
.viewerBadge_container__1QSob{
    visibility: hidden;
}
#MainMenu{
    visibility: hidden;
}
<style>
"""
st.markdown(hide, unsafe_allow_html=True)

st.markdown(
    """
    <style>
        iframe[width="220"] {
            position: fixed;
            bottom: 60px;
            right: 40px;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

from llama_index import GPTSimpleVectorIndex, SimpleDirectoryReader

index = GPTSimpleVectorIndex.load_from_disk('index.json')

if input_text:
    response = index.query(input_text)
    st.info(response)
