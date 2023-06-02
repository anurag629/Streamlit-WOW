import streamlit as st
import pandas as pd
import numpy as np
import pickle
from sklearn.ensemble import RandomForestClassifier

st.write("""
# Penguin Gender Prediction App

This app predicts the **Penguin** Gender!
""")

st.sidebar.header('User Input Features')

st.sidebar.markdown("""
[Example CSV input file](https://github.com/anurag629/Streamlit-WOW/blob/main/Penguin%20Classification/example.csv?plain=1)
""")


# Collects user input features into dataframe
uploaded_file = st.sidebar.file_uploader(
    "Upload your input CSV file", type=["csv"])

if uploaded_file is not None:
    input_df = pd.read_csv(uploaded_file)
else:
    def user_input_features():
        species = st.sidebar.selectbox(
            'Species', ('Adelie', 'Chinstrap', 'Gentoo'))
        island = st.sidebar.selectbox(
            'Island', ('Biscoe', 'Dream', 'Torgersen'))
        culmen_length_mm = st.sidebar.slider(
            'Culmen Length (mm)', 32.1, 59.6, 43.9)
        culmen_depth_mm = st.sidebar.slider(
            'Culmen Depth (mm)', 13.1, 21.5, 17.2)
        flipper_length_mm = st.sidebar.slider(
            'Flipper Length (mm)', 172.0, 231.0, 201.0)
        body_mass_g = st.sidebar.slider(
            'Body Mass (g)', 2700.0, 6300.0, 4207.0)
        data = {'species': species,
                'island': island,
                'culmen_length_mm': culmen_length_mm,
                'culmen_depth_mm': culmen_depth_mm,
                'flipper_length_mm': flipper_length_mm,
                'body_mass_g': body_mass_g}
        features = pd.DataFrame(data, index=[0])
        return features

    input_df = user_input_features()

# Combines user input features with entire penguins dataset
# This will be useful for the encoding phase
penguins_raw = pd.read_csv('penguins_cleaned.csv')
penguins = penguins_raw.drop(columns=['sex'])
df = pd.concat([input_df, penguins], axis=0)

# Encoding of ordinal features
encode = ['species', 'island']
for col in encode:
    dummy = pd.get_dummies(df[col], prefix=col)
    df = pd.concat([df, dummy], axis=1)
    del df[col]
df = df[:1]  # Selects only the first row (the user input data)

# Displays the user input features
st.subheader('User Input features')
if uploaded_file is not None:
    st.write(df)
else:
    st.write(
        'Awaiting CSV file to be uploaded. Currently using example input parameters (shown below).')
    st.write(df)

# Reads in saved classification model
load_clf = pickle.load(open('penguins_clf.pkl', 'rb'))

# Apply model to make predictions
prediction = load_clf.predict(df)
prediction_proba = load_clf.predict_proba(df)


st.subheader('Prediction')
penguins_gender = np.array(['MALE', 'FEMALE'])
st.write(penguins_gender[prediction])

st.subheader('Prediction Probability')
st.write(prediction_proba)
