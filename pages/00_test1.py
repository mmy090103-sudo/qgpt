import streamlit as st
st.title('첫 사이트 제작하기!!')
name = st.text_input('이름을 입력해주세요 : ')
menu = st.selectbox('가장 최근에 본 영화가 뭔가요?:', ['체인소맨','보스','귀멸의칼날','좀비딸'])
if st.button('인사말 생성') : 
  st.write(name+'님! 당신이 좋아하는 음식은 '+menu+'이군요?! 저도 좋아요!!')
