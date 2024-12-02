import streamlit as st


class Introduction:
    def __init__(self):
        pass

    def app(self):
        st.title('Introduction to the project')
        st.write("---")
        st.write("""

                 This project is aimed at expanding our understanding in dataframe analysis.
                 For this module, our group of three have created different visualizations through the use of
                 libraries that have been explored during ISTA 131 course, such as:
                 
                 - Pandas
                 - Matplotlib
                 - Numpy
                 
                 As well as auxiliary required libraries:
                 
                 - Streamlit
                 
                 """

                 )
        st.write("---")
        st.subheader("Used environment")
        st.write("""
                 In order to offer the easier perception of our visualizations, we've
                 decided to use the streamlit framework, which allowed us to organize
                 our work through the use of several pages, one for every member of
                 our team. 

                 """)
        st.write("---")
        st.subheader("Repository information")
        st.write("""
                        If you wish to review the structure of the content as well as
                        check the sequence of our git actions, you can visit our github
                        repository at: 
                        """)
        st.write("[Github link >](https://github.com/ligushka789/ista131_Fp)")

        st.markdown(
            """
            <style>
            
            
            h1 {
                color: #4CAF50;
                font-size: 30px;
                text-align: center;
                font-family: Avantgarde, TeX Gyre Adventor, URW Gothic L, sans-serif;
            }

            </style>
            """,
            unsafe_allow_html=True,
        )