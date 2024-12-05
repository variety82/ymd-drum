import streamlit as st
import pandas as pd
import os
from PIL import Image

def display_image_2(image_num):
    col1, col2, col3 = st.columns(3)
    print(st.session_state.image)
    if st.session_state.image == image_num:
        with col1:
            img = Image.open(f'image/{image_num}-1_origin.png')
            st.image(img)
            st.markdown(
            "<h3 style='text-align: center;'>Input</h3>",
            unsafe_allow_html=True
            )
        with col2:
            img = Image.open(f'image/arr.png')
            st.image(img)
        with col3:
            img = Image.open(f'image/{image_num}-2_detect.png')
            st.image(img)
            if st.session_state.image == '2':
                st.markdown(
                "<h3 style='text-align: center;'>Output : 존재</h3>",
                unsafe_allow_html=True
                )
            else:
                st.markdown(
                "<h3 style='text-align: center;'>Output : 미존재</h3>",
                unsafe_allow_html=True
                )

# 구멍끼 분류
def display_image_3(image_num):
    col1, col2, col3 = st.columns(3)
    print(st.session_state.image)
    if st.session_state.image == image_num:
        with col1:
            img = Image.open(f'image/{image_num}-1_origin.png')
            st.image(img)
            st.markdown(
            "<h3 style='text-align: center;'>Input</h3>",
            unsafe_allow_html=True
            )
        with col2:
            img = Image.open(f'image/arr.png')
            st.image(img)
        with col3:
            img = Image.open(f'image/{image_num}-3_contour.png')
            st.image(img)
            if st.session_state.image == '1':
                st.markdown(
                "<h4 style='text-align: center;'>Output : 상(0.03%)</h4>",
                unsafe_allow_html=True
                )
            elif st.session_state.image == '2':
                st.markdown(
                "<h4 style='text-align: center;'>Output : 중(0.12%)</h4>",
                unsafe_allow_html=True
                )
            elif st.session_state.image == '3':
                st.markdown(
                "<h4 style='text-align: center;'>Output : 하(6.22%)</h4>",
                unsafe_allow_html=True
                )
            elif st.session_state.image == '4':
                st.markdown(
                "<h4 style='text-align: center;'>Output : 중(3.34%)</h4>",
                unsafe_allow_html=True
                )
            elif st.session_state.image == '5':
                st.markdown(
                "<h4 style='text-align: center;'>Output : 상(0.02%)</h4>",
                unsafe_allow_html=True
                )
            elif st.session_state.image == '6':
                st.markdown(
                "<h4 style='text-align: center;'>Output : 상(0.09%)</h4>",
                unsafe_allow_html=True
                )

def display_image_4(image_num):
    col1, col2, col3 = st.columns(3)
    print(st.session_state.image)
    if st.session_state.image == image_num:
        with col1:
            img = Image.open(f'image/{image_num}-1_origin.png')
            st.image(img)
            st.markdown(
            "<h3 style='text-align: center;'>Input</h3>",
            unsafe_allow_html=True
            )
        with col2:
            img = Image.open(f'image/arr.png')
            st.image(img)
        with col3:
            img = Image.open(f'image/{image_num}-4_nir.png')
            st.image(img)
            if st.session_state.image == '1':
                st.markdown(
                "<h4 style='text-align: center;'>Output :<br> NIR(C1), 색택(G1)</h4>",   
                unsafe_allow_html=True
                )
            elif st.session_state.image == '2':
                st.markdown(
                "<h4 style='text-align: center;'>Output :<br> NIR(C3), 색택(G1)</h4>",
                unsafe_allow_html=True
                )
            elif st.session_state.image == '3':
                st.markdown(
                "<h4 style='text-align: center;'>Output :<br> NIR(C2), 색택(G3)</h4>",
                unsafe_allow_html=True
                )
            elif st.session_state.image == '4':
                st.markdown(
                "<h4 style='text-align: center;'>Output :<br> NIR(C0), 색택(G3)</h4>",
                unsafe_allow_html=True
                )
            elif st.session_state.image == '5':
                st.markdown(
                "<h4 style='text-align: center;'>Output :<br> NIR(C4), 색택(G2)</h4>",
                unsafe_allow_html=True
                )
            elif st.session_state.image == '6':
                st.markdown(
                "<h4 style='text-align: center;'>Output :<br> NIR(C4), 색택(G1)</h4>",
                unsafe_allow_html=True
                )

def display_image_5(image_num):
    data = pd.read_csv('./image/data_sample.csv')
    if st.session_state.image == '1':
        sliced_df = data.iloc[0:1, 1:]
        st.dataframe(sliced_df)

    elif st.session_state.image == '2':
        sliced_df = data.iloc[1:2, 1:]
        st.dataframe(sliced_df)

    elif st.session_state.image == '3':
        sliced_df = data.iloc[2:3, 1:]
        st.dataframe(sliced_df)

    elif st.session_state.image == '4':
        sliced_df = data.iloc[3:4, 1:]
        st.dataframe(sliced_df)

    elif st.session_state.image == '5':
        sliced_df = data.iloc[4:5, 1:]
        st.dataframe(sliced_df)

    elif st.session_state.image == '6':
        sliced_df = data.iloc[5:6, 1:]
        st.dataframe(sliced_df)

st.title("마른 김 등급 판별")

if "current_step" not in st.session_state:
    st.session_state.current_step = 1

if "image" not in st.session_state:
    st.session_state.image = '1'


# 탭 라디오 버튼으로 선택 (탭처럼 보이게)
tab_labels = ["이미지 업로드", "불순물 존재", "구멍끼 분류", "색택, NIR(단백질)", "등급판정"]
selected_tab = st.radio("", range(1, len(tab_labels) + 1), 
                        format_func=lambda x: tab_labels[x - 1], 
                        index=st.session_state.current_step - 1, 
                        horizontal=True)


# 선택된 탭에 따라 상태 변경
st.session_state.current_step = selected_tab

# 각 탭에 대한 내용 출력
if st.session_state.current_step == 1:
    img_file = st.file_uploader('',type=['png', 'jpg', 'jpeg'])

    if img_file is not None:
        filename = str(img_file.name)
        img_file.name = filename

        # 실제로 저장
        if not os.path.exists('image'):
            os.makedirs('image')
            
        with open(os.path.join('image', img_file.name), 'wb') as f:
            f.write(img_file.getbuffer())

        # 경로로 이미지 출력
        img = Image.open('image/' + img_file.name)
        st.image(img)
        # 사진마다 state 변경
        st.session_state.image = img_file.name[0]
        st.success('파일 업로드 성공')
        st.write("진행 상태")
        print(st.session_state.image)

elif st.session_state.current_step == 2:
    st.markdown(
    "<h1 style='text-align: center;'>불순물 존재</h1>",
    unsafe_allow_html=True
    )
    display_image_2(st.session_state.image)
    st.write("진행 상태")


elif st.session_state.current_step == 3:
    st.markdown(
    "<h1 style='text-align: center;'>구멍끼 분류</h1>",
    unsafe_allow_html=True
    )
    display_image_3(st.session_state.image)
    st.write("진행 상태")
elif st.session_state.current_step == 4:
    st.markdown(
    "<h1 style='text-align: center;'>NIR</h1>",
    unsafe_allow_html=True
    )
    display_image_4(st.session_state.image)
    st.write("진행 상태")

elif st.session_state.current_step == 5:
    st.markdown(
    "<h1 style='text-align: center;'>최종 등급</h1>",
    unsafe_allow_html=True
    )
    display_image_5(st.session_state.image)
    st.write("진행 상태")


# 프로그레스 바 동적 업데이트
st.progress(st.session_state.current_step / len(tab_labels))



