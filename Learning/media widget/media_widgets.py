import streamlit as st

st.image("image.jpg", caption="This is a caption: `st.image()`", width=300, use_column_width=False, clamp=False, channels="RGB", output_format="auto")


st.audio("audio.mp3", format="audio/mp3", start_time=0)


st.video("video.mp4", format="video/mp4", start_time=0)