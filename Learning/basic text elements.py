import streamlit as st

st.title("Basic Text Elements: st.title()")
st.subheader("This is a subheader: st.subheader()")
st.header("This is a header: st.header()")
st.text("This is a text. I can write paragraphs: st.text()")

st.markdown("""This is a markdown: 
            ```markdown
            st.markdown()
            ```
            """)

st.subheader("Latex: st.latex()")
st.latex(r''' e^{i\pi} + 1 = 0 ''')

st.subheader("Json: st.json()")
json = {"a":1, "b":2, "c":3}
st.json(json)


st.subheader("Code: st.code()")
st.code('''
    def hello():
        print("Hello, Streamlit!")
    ''', 
    language='python')


st.subheader("Run the streamlit app from the terminal: streamlit run app.py")
