import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


class Survey:
    def __init__(self):
        self.file_path = "csv/survey1.csv"

    def plot_data(self):
        try:
            data = pd.read_csv(self.file_path)
            selected_countries = ["United States", "Canada", "Australia", "United Kingdom", "Germany"]
            data = data[data["Country"].isin(selected_countries)]
            mh_consequence_counts = data.groupby(["Country", "mental_health_consequence"]).size().unstack(fill_value=0)
            tech_company_counts = data.groupby(["Country", "tech_company"]).size().unstack(fill_value=0)
            mh_consequence_counts = mh_consequence_counts.reindex(columns=["Yes", "No", "Maybe"], fill_value=0)
            tech_company_counts = tech_company_counts.reindex(columns=["Yes", "No"], fill_value=0)
            mh_percentage = mh_consequence_counts.div(mh_consequence_counts.sum(axis=1), axis=0) * 100
            tech_percentage = tech_company_counts.div(tech_company_counts.sum(axis=1), axis=0) * 100
            tech_percentage["No"] = 100 - tech_percentage["Yes"]
            combined_percentage = pd.concat([tech_percentage, mh_percentage], axis=1,
                                            keys=["Tech Company", "Mental Health"])

            mh_colors = {'Yes': 'green', 'No': 'red', 'Maybe': 'blue'}
            tech_colors = {'Yes': 'darkgreen', 'No': 'darkred'}
            fig, ax = plt.subplots(figsize=(18, 8))
            bar_width = 0.12
            countries = mh_percentage.index
            x_pos = np.arange(len(countries))

            for i, response in enumerate(['Yes', 'No']):
                if response in tech_percentage.columns:
                    ax.bar(x_pos - bar_width / 2 + i * bar_width, tech_percentage[response], width=bar_width,
                           label=f"Tech Company: {response}", color=tech_colors[response])

            for i, response in enumerate(['Yes', 'No', 'Maybe']):
                if response in mh_percentage.columns:
                    ax.bar(x_pos + bar_width / 2 + i * bar_width, mh_percentage[response], width=bar_width,
                           label=f"Mental Health: {response}", color=mh_colors[response])

            ax.set_title("Tech Company and Mental Health Consequences by Country (Percentage)", fontsize=18)
            ax.set_ylabel("Percentage", fontsize=14)
            ax.set_xlabel("Country", fontsize=14)
            ax.set_xticks(x_pos)
            ax.set_xticklabels(countries, rotation=45, ha='right', fontsize=12)
            ax.grid(True)
            ax.legend(title="Category", bbox_to_anchor=(1.05, 1), loc="upper left", fontsize=12)
            plt.tight_layout()
            st.pyplot(fig)

        except FileNotFoundError:
            st.error("The file was not found. Ensure 'survey1.csv' is in the correct directory.")
        except Exception as e:
            st.error(f"An error occurred: {e}")

    def app(self):
        st.title("Survey Data Analysis")

        st.write("Visualizing data from 'survey1.csv'...")
        self.plot_data()

if __name__ == '__main__':
    Survey= Survey()
    Survey.app()

