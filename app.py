import streamlit as st

st.title("타이틀임")
st.header("헤더임")
st.subheader("서브헤더임")
st.markdown(''':rainbow[뭔가 엄청나고 번쩍번쩍 빛나는 말]''')
st.write("ㅋ")

isClicked = st.button("버튼임")
if isClicked :
  st.write("클릭함")
