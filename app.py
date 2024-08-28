import streamlit as st

st.title("타이틀")
st.header("헤더")
st.subheader("서브헤더")
st.markdown(''':rainbow[뭔가 엄청난 말
번쩍번쩍 빛나는 말]''')
st.write("롸이트")

isClicked = st.button("버튼")
if isClicked :
  st.write("클릭함")
