import streamlit as st

st.title("타이틀")
st.header("헤더")
st.subheader("서브헤더")
st.markdown(''':red[마크다운]''')
st.write("롸이트")

isClicked = st.button("버튼")
if isClicked :
  st.write("클릭함")
