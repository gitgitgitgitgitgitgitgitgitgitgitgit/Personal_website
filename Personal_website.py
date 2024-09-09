import streamlit as st





# Create tabs for different sections of your portfolio
tab1, tab2, = st.tabs(["Home", "Projects"])

# Home Page
with tab1:
    st.title("Welcome to My Portfolio")
    # st.image("your_image.jpg", width=300)

    st.write("""I’m a high school student with a passion for creative problem-solving and defending against cyber threats. I love exploring innovative ways to outsmart threat actors and stay ahead in the ever-evolving world of cybersecurity. When I'm not doing schoolwork or working on projects, you can find me playing the bass, reading, or acting in musicals.

Through the Google Professional Cybersecurity Certification, I’m eager to build on my skills and gain the experience needed to make an impact in the field.""")


with tab2:
    st.title("Projects")
    st.write("Below are the projects that I have completed, are in progress, or are to-do:")

    # Completed Projects
    st.markdown("### Completed Projects")
    col1, col2 = st.columns(2)

    with col1:
        if st.button("Door Alarm"):
            st.link_button("Go to project", "https://www.example.com/door_alarm")
        st.write("A Python project utilizing two micro:bits and a computer to send a Telegram message when a door is opened or closed.")

    with col2:
        if st.button("Personal Website"):
            st.link_button("Go to project", "https://www.example.com/personal_website")
        st.write("A Streamlit website that showcases my projects and provides information about me.")

    st.markdown("---")  # Separator line

    # In Progress Projects
    st.markdown("### In Progress Projects")
    col3, col4 = st.columns(2)

    with col3:
        st.button("Cyberdeck portable offensive cyber tool")
           
        st.write("A portable Kali Linux machine that can be used for pentesting and other cybersecurity tasks.")

    with col4:
        st.button("Weather Alert Telegram Bot")
        
        st.write("A Telegram bot that sends weather alerts to a user based on their set location.")

    st.markdown("---")  # Separator line

    # To-Do Projects
    st.markdown("### To-Do Projects")
    col5, col6 = st.columns(2)

    with col5:
        st.button("SeedLock")
         
        st.write("Symmetric encryption and decryption program that uses a seed to encrypt the message.")

        st.button("google cyber portfolio piece 2")
         
        st.write("google cyber portfolio piece 2.")

        st.button("google cyber portfolio piece 3")
          
        st.write("google cyber portfolio piece 3.")

    with col6:
        st.button("google cyber portfolio piece 4")
          
        st.write("google cyber portfolio piece 4.")

        st.button("google cyber portfolio piece 5")
           
        st.write("google cyber portfolio piece 5.")

        st.button("google cyber portfolio piece 6")
           
        st.write("google cyber portfolio piece 6.")
    


    





# Sidebar with buttons
st.sidebar.title("Connect with Me")
st.sidebar.link_button("LinkedIn", "https://www.linkedin.com/in/mischa-nelson-4a60842a7")
st.sidebar.link_button("GitHub", "https://github.com/gitgitgitgitgitgitgitgitgitgitgitgit")
st.sidebar.link_button("Email", "mailto:mischa.nelson07@gmail.com")