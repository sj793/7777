import streamlit as st
import matplotlib.pyplot as plt
from matplotlib import rc
from PIL import Image

# 글꼴 설정
rc('font', family='Malgun Gothic')  # Windows 환경
plt.rcParams['axes.unicode_minus'] = False

# 이미지 로드 함수
def load_image(image_name):
    return Image.open(f"images/{image_name}")

# 페이지 설정
st.set_page_config(page_title="편의점에서 물건 구매하기", layout="wide")

# 선택 메뉴 및 페이지 상태 설정
if "current_page" not in st.session_state:
    st.session_state.current_page = "수업 소개"

# 사이드바에서 페이지 선택
selected_page = st.sidebar.selectbox(
    "페이지를 선택하세요",
    ["수업 소개", "편의점 지도", "예산 확인", "마트 예절", "물건 구매", "구매 성공"]
)
st.session_state.current_page = selected_page

# 페이지 별 코드
if st.session_state.current_page == "수업 소개":
    st.title("편의점에서 물건 구매하기")
    st.write("""
        이 수업은 학생들이 실제 편의점에서 물건을 구매하며 필요한 사회적 기술과 
        계산 능력을 익히는 것을 목표로 합니다.
    """)
    st.image(load_image("서울경운학교.png"), caption="서울경운학교", width=600)

    st.subheader("수업 목표")
    st.write("""
        - 실제 생활에서 필요한 금전 관리 기술을 배웁니다.
        - 타인과의 대화 및 기본적인 예의 표현을 익힙니다.
        - 물건을 선택하고 계산하는 과정에서 의사결정을 연습합니다.
    """)

elif st.session_state.current_page == "편의점 지도":
    st.title("서울경운학교 주변 편의점 지도")
    st.write("서울경운학교 주변의 편의점을 알아봅시다.")

    # 지도 렌더링 코드 생략...

elif st.session_state.current_page == "예산 확인":
    st.title("예산 확인")
    st.write("현재 예산은 총 **10,000원**입니다.")
    # 예산 관련 코드 생략...

elif st.session_state.current_page == "마트 예절":
    st.title("마트에서 지켜야 할 예절")
    st.write("마트에서 물건을 구매할 때 지켜야 할 기본적인 예절을 배워봅시다!")
    # 예절 관련 코드 생략...

elif st.session_state.current_page == "물건 구매":
    st.title("물건 구매 시뮬레이터")
    items = {
        "가나초콜릿": (2000, "가나초콜릿.png"),
        # ... 다른 아이템 생략
    }
    # 구매 시뮬레이터 관련 코드 생략...

elif st.session_state.current_page == "구매 성공":
    st.title("구매 성공!")
    st.success("예산 내에서 성공적으로 물건을 구매했습니다.")
    st.image(load_image("참잘했어요.png"), caption="잘했어요! 🎉", width=800)
    if st.button("다시 구매하기"):
        st.session_state.current_page = "물건 구매"  # Navigate back to purchase page
