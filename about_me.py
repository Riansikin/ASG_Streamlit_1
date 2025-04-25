import streamlit as st

def show_about_me():
    col1, col2 = st.columns(2, gap="small", vertical_alignment="center")
    with col1:
        st.image("./Assets/ProflePFP.png", width=250)
    with col2:
        st.title("Muhammad Wahyu Sikin Febriansyah", anchor=False)
        st.write("Active 7th-semester student in the Bachelor’s Program of Computer Science at Bina Nusantara University. Skilled in data processing within Database Technology, front-end and back-end web development, and database management. Possesses strong communication skills and is a capable team member. Currently focused on enhancing expertise in data processing, data management, and web development.")
        st.write("**Contact Me:**")
        st.markdown(
            "[![LinkedIn](https://img.shields.io/badge/LinkedIn-Profile-blue)](https://www.linkedin.com/in/mwahyusikinf/)"
        )
        st.markdown(
            "[![GitHub](https://img.shields.io/badge/GitHub-Profile-blue)](https://github.com/Riansikin)"
        )
        st.write("📧 Email: riansikin7@gmail.com")
    
    st.write("\n")
    st.subheader("Experience", anchor=False)
    st.write("---")
    st.write(
        """
        **Department of Logistics and Facilities Management Intern** \n
        Bank Indonesia- Jakarta, Indonesia
        - Participated in the Kampus Merdeka Bank Indonesia (KMBI) internship program as a programmer in the Logistics and Facilities Management Department (DPLF)
        - Analyzed vendor contract mapping to facilitate easier vendor data retrieval.
        - Developed a website for tracking minutes of meetings and invoices, to be used by the admin for updating every document movement using JavaScript.
        """
    )

    st.write("\n")
    st.subheader("Skills", anchor=False)
    st.write("---")
    st.write(
        """
        **Technical Skills:** \n
        - Python
        - MySQL
        - Power BI
        - Figma
        - JavaScript
        - Microsoft Office

        **Soft Skills:** \n
        - Problem Analysis
        - Public Speaking
        - Team Communication
        - Project Management
        

        """
    )