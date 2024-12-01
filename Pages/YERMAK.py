import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

class Raymond:
    def __init__(self):
        pass
    def load_data(self,file):
        if file is not None:
            data=pd.read_csv(file)
            return data
        return None
    def clean_and_convert_values(self,df,column):
        df[column] = df [column].astype(str)
        df[column] = df[column].replace({',':'.'}, regex=True)
        df[column] = df[column].str.replace(r'\s+','',regex=True)
        df[column] = pd.to_numeric(df[column], errors='coerce')


        return df
    def plot_bar_chart(self,df, category_column, value_column):
        df= self.clean_and_convert_values(df,value_column)

        if df[category_column].dtype == 'object' or df[category_column].dtype.name == 'category':
            if df[value_column].dtype in ['int64', 'float64']:
                category_mean = df.groupby(category_column)[value_column].mean()

                colors = plt.cm.get_cmap('tab20', len(category_mean))

                fig,ax = plt.subplots()
                category_mean.plot(kind='bar',ax=ax, color=colors(np.arange(len(category_mean))))
                ax.set_title(f'Mean {value_column} by {category_column}')
                ax.set_xlabel(category_column)
                ax.set_ylabel(f'Mean {value_column}')
                st.pyplot(fig)

                st.write(f'Mean {value_column} by {category_column}:')
                st.dataframe(category_mean)
            else:
                st.warning(f'{value_column} eto ne cifrovaya colonka chel... Uberi etot pozor')
        else:
            st.warning(f'{category_column} boje chel nu eto je ne categorical column. chto za ubezhishe bozhe')


    def app(self):
        st.title('Sozdayom Dataframeek))')

        upload = st.file_uploader("CSV FILE UPLOADER.....bibls")
        if upload is not None:
            df = self.load_data(upload)
            st.dataframe(df, height=400, width=600)

            category_column = st.selectbox("Pu-pu-pu berem category colonku 8_8",df.columns)
            value_column= st.selectbox("Colonka dlya znaacheniy zaeybal", df.columns)

            if category_column and value_column:
                st.subheader(f"Bar chart and mean of {value_column} by {category_column}")
                self.plot_bar_chart(df,category_column, value_column)

        else:
            st.warning("Load the CSV file")

        st.markdown("""<style>
                    h1 {
                    color:darkblue;
                    font-size:20px;
                    text-align:center;
                    }
                    </style>""", unsafe_allow_html=True)

if __name__ == '__main__':
    Raymond= Raymond()
    Raymond.app()

