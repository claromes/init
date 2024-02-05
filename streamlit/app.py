import streamlit as st

# page config
st.set_page_config(
    page_title='Title',
    page_icon='🔥',
    layout='wide',
    menu_items={
        'About': '''

        -------
        ''',
        'Get help': '',
        'Report a bug': '',
    }
)

# https://discuss.streamlit.io/t/remove-hide-running-man-animation-on-top-of-page/21773/3
hide_streamlit_style = '''
<style>
    div[data-testid="stStatusWidget"] {
        visibility: hidden;
    }
    .st-emotion-cache-1so2gm1 {
        border-style: none;
    }
    div[data-testid="stExpander"] details summary svg {
        display: none;
    }
</style>
'''

st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# title
st.title("""
Title

Description
""", anchor=False)