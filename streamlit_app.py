import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd

# Create a connection object.
conn = st.connection("gsheets", type=GSheetsConnection)

df = conn.read()

df.drop(10, inplace=True)
df = pd.DataFrame(df)

col1, col2 = st.columns([50, 50])

with col1:
    st.header("Demographics section")
    unique_country = df["Country"].value_counts()
    st.line_chart(unique_country)
    exp1 = st.expander("See more")
    exp1.write("This column was created to plot data regarding country of origin")

with col2:
    st.header("RunVsBike")
    st.scatter_chart(df, x="Bike Rank", y= "Run Rank")

st.write("---")

exp2 = st.expander("Single athlete data")
exp2.write("In thi section you can visualize a single athlete's data")
ath_name = exp2.selectbox("Select you athlete", df.Name)
a = (df.Name == ath_name)
ath_data = df.iloc[a]
exp2.dataframe(ath_data)
exp2.write(f"Athlete race number: {ath_data.Bib}")
exp2.write(f"Athlete name: {ath_data.Name}")
exp2.write(f"Athlete age group: {ath_data.Division}")
exp2.write(f"Athlete country of origin: {ath_data.Country}")
OR = ath_data["Overall Rank"]
exp2.write(f"Athlete overall rank: {OR}")

expdf = st.expander("Full dataframe")
expdf.dataframe(df)
