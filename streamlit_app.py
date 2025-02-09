import streamlit as st

st.set_page_config(
    page_title="Muhammad Dhany Latief's Linktree",
    page_icon=":link:",
    layout="centered",
    initial_sidebar_state="auto"
)

def main():
    st.sidebar.title("Muhammad Dhany Latief's Linktree")
    page = st.sidebar.radio("Pages:", ["Home", "My Projects"])
    if page == "Home":
        show_home()
    elif page == "My Projects":
        show_projects()

def show_home():
    st.markdown(
        """
        <style>
        .stApp {
            background-image: url("https://cdn.pixabay.com/photo/2015/07/28/22/01/office-865091_1280.jpg");
            background-size: cover;
        }
        .link-box {
            background: rgba(255, 255, 255, 0.8);
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
            margin: 20px 0;
        }
        .link-box a {
            display: block;
            margin: 10px 0;
            font-size: 20px;
            text-decoration: none;
            color: #000;
        }
        .link-box a:hover {
            color: #0073e6;
        }
        .profile-pic {
            border-radius: 50%;
            width: 150px;
            height: 150px;
            object-fit: cover;
            margin: 20px auto;
        }
        </style>
        """,
        unsafe_allow_html=True
    )    

    st.markdown(
        """
        <div class="link-box"; style="text-align: center; color: black;">
            <img src="https://i.imgur.com/J7Thmac.jpeg" alt="Profile Picture" class="profile-pic">
            <h1>My Links</h1>
            <p>I am Muhammad Dhany Latief and welcome to my Linktree! Here are some my social links:</p>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    st.markdown(
        """
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css">
        """,
        unsafe_allow_html=True
    )

    links = {
        "LinkedIn": ("https://www.linkedin.com/in/dhany-latief-22a674241/", "fab fa-linkedin"),
        "GitHub": ("https://github.com/dhanylatief", "fab fa-github"),
        "Gmail": ("mailto:m.dhany.latief@gmail.com", "fas fa-envelope"),
        "Instagram": ("https://www.instagram.com/dhanylatief/", "fab fa-instagram"),
        "Medium": ("https://medium.com/@m.dhany.latief", "fab fa-medium"),
        "Tableau Public": ("https://public.tableau.com/app/profile/dhan.l/vizzes", "fas fa-chart-bar"),
        "Facebook": ("https://www.facebook.com/muhammad.d.latief.9", "fab fa-facebook")
    }

    for name, (url, icon) in links.items():
        st.markdown('<div class="link-box">'f'<a href="{url}" target="_blank"><i class="{icon}"></i> {name}</a>''</dif>', unsafe_allow_html=True)

def show_projects():
    st.markdown(
        """
        <style>
        .stApp {
            background-image: url("https://cdn.pixabay.com/photo/2020/04/30/17/52/network-5113928_960_720.jpg");
            background-size: cover;
        }
        .link-box {
            background: rgba(255, 255, 255, 0.8);
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
            margin: 20px 0;
        }
        .link-box a {
            display: block;
            margin: 10px 0;
            font-size: 20px;
            text-decoration: none;
            color: #000;
        }
        .link-box a:hover {
            color: #0073e6;
        }
        .profile-pic {
            border-radius: 50%;
            width: 150px;
            height: 150px;
            object-fit: cover;
            margin: 20px auto;
        }
        </style>
        """,
        unsafe_allow_html=True
    )    
    st.markdown(
        """
        <div class="link-box"; style="text-align: center; color: black;">
            <h1>My Projects</h1>
            <p>Coming soon...</p>
        </div>
        """,
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()