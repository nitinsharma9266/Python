"""from datetime import date
fdate=date(2026,3,11)
ldate=date(2026,3,20)
z=ldate-fdate
print(z.days)"""

import streamlit as st

# Page settings
st.set_page_config(page_title="Nitin Sharma Portfolio", layout="wide")

# Sidebar
st.sidebar.title("Navigation")
page = st.sidebar.radio(
    "Go to",
    ["Home", "About", "Skills", "Projects", "Contact"]
)

# HOME
if page == "Home":
    st.title("👨‍💻 Nitin Sharma")
    st.subheader("Python Developer | AI Enthusiast")

    st.write("""
    Welcome to my portfolio website.
    I am a B.Tech student and Python developer interested in
    Artificial Intelligence, Machine Learning and Web Development.
    """)

# ABOUT
elif page == "About":
    st.title("About Me")

    st.write("""
    My name is **Nitin Sharma**.
    
    I am currently pursuing **B.Tech (2nd Year)**.
    
    I enjoy building:
    - Python applications
    - AI tools
    - Web apps
    """)

# SKILLS
elif page == "Skills":
    st.title("My Skills")

    st.write("### Programming")
    st.progress(80)
    st.write("Python")

    st.write("### Web Development")
    st.progress(70)
    st.write("HTML, CSS")

    st.write("### Data Science")
    st.progress(60)
    st.write("Pandas, NumPy")

# PROJECTS
elif page == "Projects":
    st.title("My Projects")

    st.subheader("🤖 AI Chatbot")
    st.write("A chatbot built using Python and AI APIs.")

    st.subheader("🗣 Jarvis Voice Assistant")
    st.write("A personal voice assistant like Jarvis.")

    st.subheader("🎮 Snake Water Gun Game")
    st.write("A simple Python game using logic.")

# CONTACT
elif page == "Contact":
    st.title("Contact Me")

    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    message = st.text_area("Message")

    if st.button("Send"):
        st.success("Message Sent Successfully!")

    st.write("📧 Email: nitinsharma926614@gmail.com")
    st.write("💻 GitHub: https://github.com/")
