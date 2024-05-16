import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image


# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")

# ---- LOAD ASSETS ----
lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")
img_etl = Image.open("images/ETL.png")
img_sftp = Image.open("images/SFTP.png")
img_nifi = Image.open("images/NIFI.png")

# ---- HEADER SECTION ----
with st.container():
    st.subheader("Hi, I am Shyam :wave:")
    st.title("A Data Engineer From India")
    st.write(
        "I am passionate about finding ways to use Python,Pyspark,Mysql and AWS technologies to be more efficient and effective in business settings."
    )
    st.write("[Learn More >](https://www.linkedin.com/in/shyam-kumar-870821171/)")

# ---- WHAT I DO ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write(
            """
            - Build data-intensive, highly scalable end-to-end data pipelines for handling business use cases.
            - Provide clean & transformed data to be consumed by analytics and data science teams.
            - Contribute to data mart strategy and dimensional modelling.
            - Innovate and Automate the existing processes in the organization frameworks."

            If this sounds interesting to you, message me if you think, so you don't miss my assistance.
            """
        )
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")

# ---- PROJECTS ----
with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        new_image = img_sftp.resize((325, 150))
        st.image(new_image)
    with text_column:
        st.subheader("Transfer Files from One server to Another using Pyspark SFTP protocol")
        st.write(
            """
            The file will be moved to the destination server using the User credentials.
            """
        )
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        new_image1 = img_etl.resize((325, 150))
        st.image(new_image1)
    with text_column:
        st.subheader("Will be developing the ETL procedure according to client specifications")
        st.write(
            """
            First, data is extracted from a data source. Then it’s transformed into a relevant format. Finally, the data is loaded into a destination repository, such              as a data warehouse or a data mart.
            """
        )
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        new_image2 = img_nifi.resize((325, 150))
        st.image(new_image2)
    with text_column:
        st.subheader("Developed a Python script using the NIFI restAPI that could create and execute an NIFI processor")
        st.write(
            """
            The Python script establishes the Processor based on a unique ID and then initiates the Processor, passing arguments to the Bash script.   
            """
        )

# ---- CONTACT ----
with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")

    # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
    contact_form = """
    <form action="https://formsubmit.co/shyamvimal98@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()
