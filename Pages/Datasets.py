import streamlit as st
import pandas as pd

class Datasets:
    def __init__(self):
        pass

    def app(self):
        st.title('Datasets')

        # Define a dictionary with custom dataset names and corresponding file names
        datasets = {
            "Survey about mental health": "survey1.csv",
            "Dataset about GDP per capita for 4 states for time period 1997 - 2022": "USA_GDP_dataset_updated.csv",
            "Dataset about movies throughout the years and their ratings": "tmdb_5000_movies_rfw.csv"
        }

        # Create a selectbox to choose a dataset by its display name
        dataset_name = st.selectbox("Choose a dataset", list(datasets.keys()))

        # Get the corresponding file name based on the selected display name
        file_name = datasets[dataset_name]



        # Function to load data from a file
        def load_data(file_path):
            data = pd.read_csv(file_path)
            return data

        # Load the selected dataset
        file_path = f"csv/{file_name}"
        df = load_data(file_path)

        if df is not None:
            st.dataframe(df, height=400, width=600)

            # Allow the user to filter by a column
            column = st.selectbox("Choose column for filter", df.columns)

            if column:
                unique_values = df[column].unique()
                selected_values = st.multiselect(f"Select values for {column}", options=unique_values,
                                                 default=unique_values)

                filtered_df = df[df[column].isin(selected_values)]
                st.dataframe(filtered_df, height=400, width=600)
        else:
            st.warning("Could not load dataset")

        st.markdown("""
            <style>
            h1 {
                color: #4CAF50;
                font-size: 30px;
                text-align: center;
                font-family: Avantgarde, TeX Gyre Adventor, URW Gothic L, sans-serif;
            }
            </style>
        """, unsafe_allow_html=True)
