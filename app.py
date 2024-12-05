import streamlit as st
import pandas as pd
import os
from PIL import Image
from datetime import datetime

st.title("마른 김 등급 판별")

st.sidebar.title('AI 모델')

select_species = st.sidebar.selectbox(
    '확인하고 싶은 단계를 선택하세요',
    ['메인', '불순물','구멍끼','색택, NIR(단백질)', '등급']
)

if select_species == '메인':
    tab1, tab2, tab3 = st.tabs(["이미지 업로드", "상관관계", "PCA"])

    with tab1:
        st.subheader('이미지 업로드')
        img_file = st.file_uploader('',type=['png', 'jpg', 'jpeg'])

        if img_file is not None:

            # 이미지명이 고유하도록 시간을 활용하여 변경
            current_time = datetime.now()
            filename = current_time.isoformat().replace(":", "_")
            img_file.name = filename + '.jpg'

            # 실제로 저장
            if not os.path.exists('image'):
                os.makedirs('image')
                
            with open(os.path.join('image', img_file.name), 'wb') as f:
                f.write(img_file.getbuffer())

            # 경로로 이미지 출력
            st.subheader('김 이미지')
            img = Image.open('image/'+img_file.name)
            st.image(img)

            st.success('파일 업로드 성공')

    with tab2:
        st.markdown(f'ss')

# col1, col2 = st.columns(2)

# with col1:
#    st.header("김 이미지 업로드")

