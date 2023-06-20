import streamlit as st

st.subheader("Display Elements: `st.write()`")
st.write("This is a write: `st.write()`")
st.text("Write is a streamlit element which can be used to display text: `st.text()`")


st.subheader("Display Elements: `st.table()`")
st.table({"a":[1,2,3], "b":[4,5,6]})
st.text("Table is a streamlit element which can be used to display tables: `st.table()`")

st.subheader("Display Elements: `st.dataframe()`")
st.dataframe({"a":[1,2,3], "b":[4,5,6]})
st.text("Dataframe is a streamlit element which can be used to display dataframes: `st.dataframe()`")


st.subheader("Display Elements: `st.metric()`")
st.text("For negative delta values, the metric turns red.")
st.metric(label="Wind Speed", value="120ms⁻²", delta="-10ms⁻²")
st.text("For positive delta values, the metric turns green.")
st.metric(label="Wind Speed", value="120ms⁻²", delta="10ms⁻²")
st.text("Metric is a streamlit element which can be used to display metrics: `st.metric()`")