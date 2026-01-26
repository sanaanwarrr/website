import streamlit as st


flex = st.container(horizontal=True)
flex.title("sana anwar | سناء أنور")
flex.image("sana.jpg")

st.space("small")

st.header("about me")
st.text("hi! i'm sana, an aspiring AI/ML engineer.")
st.text("when i'm not coding, i love making art and exploring new cafe spots!")

st.space("small")

st.header("industry experience")
st.subheader("software engineering intern @ Hiyllo")
st.text("Princeton, NJ | January 2025 - May 2025")
st.text("front-end. fixed bugs using Playwright and JavaScript in pre-release and production stages")

st.space("small")

st.header("academic experience")
st.subheader("research assistant @ NJIT Department of Informatics")
st.text("developing custom AI interfaces using Python and Streamlit for multiple courses in NJIT")
st.subheader("research assistant @ NJIT Department of Humanities & Social Sciences")
st.text("enhancing conversational AI in digital banking apps for dementia users")

st.space("small")

st.header("projects")
st.subheader("personal website")
st.text("designed a personalized + responsive portfolio using Python and Streamlit")

st.space("small")

st.header("let's connect!")
socials = st.container(horizontal = True)
socials.link_button("linkedin", "https://www.linkedin.com/in/sanaanwarrr/")
socials.link_button("github", "https://github.com/sanaanwarrr")
socials.link_button("email", "mailto:sfa33@njit.edu")