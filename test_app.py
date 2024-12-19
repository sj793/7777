# 페이지 설정
st.set_page_config(page_title="편의점에서 물건 구매하기", layout="wide")

# 페이지 상태 관리
if "current_page" not in st.session_state:
    st.session_state.current_page = "수업 소개"  # 기본 페이지 설정

# 선택 메뉴 (항상 세션 상태와 동기화)
selected_page = st.sidebar.selectbox(
    "페이지를 선택하세요", 
    ["수업 소개", "편의점 지도", "예산 확인", "마트 예절", "물건 구매", "구매 성공"]
)
st.session_state.current_page = selected_page

# 각 페이지 구현
if st.session_state.current_page == "수업 소개":
    st.title("편의점에서 물건 구매하기")
    st.write("""
        이 수업은 학생들이 실제 편의점에서 물건을 구매하며 필요한 사회적 기술과 
        계산 능력을 익히는 것을 목표로 합니다.
    """)
    st.image(load_image("서울경운학교.png"), caption="서울경운학교", width=600)

elif st.session_state.current_page == "편의점 지도":
    st.title("서울경운학교 주변 편의점 지도")
    st.write("서울경운학교 주변의 편의점을 알아봅시다.")
    # Google 지도 HTML 코드 삽입 (생략)

elif st.session_state.current_page == "예산 확인":
    st.title("예산 확인")
    st.write("현재 예산은 총 **10,000원**입니다.")
    # 예산 구성 내용 (생략)

elif st.session_state.current_page == "마트 예절":
    st.title("마트에서 지켜야 할 예절")
    st.write("마트에서 물건을 구매할 때 지켜야 할 기본적인 예절을 배워봅시다!")
    # 마트 예절 내용 (생략)

elif st.session_state.current_page == "물건 구매":
    st.title("물건 구매 시뮬레이터")
    items = {
        "가나초콜릿": (2000, "가나초콜릿.png"),
        "코카콜라": (2500, "코카콜라.png"),
        "지우개": (1000, "지우개.png"),
        "부루마블": (9000, "부루마블.png"),
        "서울우유": (1500, "서울우유.png"),
        "필통": (4000, "필통.png"),
        "허니버터칩": (3000, "허니버터칩.png"),
        "귤": (1000, "귤.png"),
        "바나나": (1500, "바나나.png"),
    }

    selected_items = []
    col1, col2 = st.columns([3, 1])

    with col1:
        st.subheader("구매할 물건을 선택하세요:")
        item_keys = list(items.keys())
        rows = len(item_keys) // 3 + (1 if len(item_keys) % 3 != 0 else 0)
        for i in range(rows):
            cols = st.columns(3)
            for col, item_key in zip(cols, item_keys[i * 3 : (i + 1) * 3]):
                price, img_name = items[item_key]
                with col:
                    st.image(load_image(img_name), width=150)
                    if st.checkbox(f"{item_key} - {price}", key=f"checkbox_{item_key}"):
                        selected_items.append(item_key)

        total = sum(items[item][0] for item in selected_items if item in items)
        if st.button("구매"):
            if total <= 10000:
                st.session_state.current_page = "구매 성공"  # 성공 페이지로 이동
            else:
                st.error("구매 금액이 예산(10,000원)을 초과했습니다. 항목을 조정해주세요.")

    with col2:
        fig, ax = plt.subplots(figsize=(3, 4))
        bar_color = "green" if total <= 10000 else "red"
        bars = ax.bar(["Total"], [total], color=bar_color)
        ax.axhline(10000, color="blue", linestyle="--")
        for bar in bars:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width() / 2, height + 500, f"{int(height)}", ha='center', va='bottom')
        ax.set_ylim(0, 15000)
        ax.set_yticks([0, 5000, 10000, 15000])
        st.pyplot(fig)

elif st.session_state.current_page == "구매 성공":
    st.title("구매 성공!")
    st.success("예산 내에서 성공적으로 물건을 구매했습니다.")
    st.image(load_image("참잘했어요.png"), caption="잘했어요! 🎉", width=800)
    if st.button("다시 구매하기"):
        st.session_state.current_page = "물건 구매"  # 구매 페이지로 이동
