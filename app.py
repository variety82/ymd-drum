import streamlit as st

st.title("YMD DRUM")

tab1, tab2, tab3 = st.tabs(['학원소개', '강사소개', 'Q&A'])

with tab1:
    st.header('학원소개')
    st.write('수원에 위치한 연무동에 최초로! 드럼 연습실, 레슨실이 생겼어요!  :)') 
    st.write('시원하게 드럼 연주하면서 쌓여왔던 모든 스트레스 날려버리시는 건 어떠신가요?!')


    st.image('https://search.pstatic.net/common/?src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20230120_21%2F1674194484479jhv8d_JPEG%2FYMD_%25C7%25C1%25B7%25CE%25C7%25CA_%25BB%25E7%25C1%25F8.JPG')
    st.image('https://search.pstatic.net/common/?src=https%3A%2F%2Fpup-review-phinf.pstatic.net%2FMjAyMzA5MDFfNTIg%2FMDAxNjkzNTU3NDgyODc2.cU5oUGUtBPAZrux1TrUtR12y1ogD-53uSDJTSu5Xv08g.EftFShIePTRazk9FIS6M8w5EiqcYGPGZ1080EMicoT4g.JPEG%2Fimage.jpg')
    st.image('https://search.pstatic.net/common/?src=https%3A%2F%2Fpup-review-phinf.pstatic.net%2FMjAyMzA4MTdfMTY3%2FMDAxNjkyMjU2MjM1Mjkx.7pzEn2Qv9p0mYg7nb-vXT0Trcjcg46zEt_V_Xw0ngiQg.NOFm87PCqpX3Qg4Pbh9q-NmmtI8AixyKXphKE9bq4KEg.JPEG%2F55FF37A9-FCCD-4BB7-9DB7-E4F09A96462F.jpeg')
with tab2:
    st.header('Tab2')

with tab3:
    st.header('Tab3')