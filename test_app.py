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

# 선택 메뉴
page = st.sidebar.selectbox(
    "페이지를 선택하세요", 
    ["수업 소개", "편의점 지도", "예산 확인", "마트 예절", "물건 구매", "구매 성공"]
)

# 페이지 별 코드
if page == "수업 소개":
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

elif page == "편의점 지도":
    st.title("종로3가역 주변 편의점 지도")
    st.write("학교 주변의 편의점을 알아봅시다.")

    # 네이버 지도 API JavaScript Key
    naver_map_api_key = "m16vbixgmx"  # 발급받은 JavaScript API Key

    # HTML 코드
    html_code = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>네이버 지도</title>
        <script type="text/javascript" src="https://openapi.map.naver.com/openapi/v3/maps.js?ncpClientId={naver_map_api_key}"></script>
        <style>
            #map {{
                width: 100%;
                height: 500px;
            }}
        </style>
    </head>
    <body>
        <div id="map"></div>
        <script>
            document.addEventListener("DOMContentLoaded", function() {{
                var mapOptions = {{
                    center: new naver.maps.LatLng(37.570028, 126.987080),
                    zoom: 14
                }};
                var map = new naver.maps.Map('map', mapOptions);

                var marker = new naver.maps.Marker({{
                    position: new naver.maps.LatLng(37.570028, 126.987080),
                    map: map
                }});

                var infowindow = new naver.maps.InfoWindow({{
                    content: "<div style='width:150px;text-align:center;'>종로3가역</div>"
                }});

                naver.maps.Event.addListener(marker, "click", function() {{
                    if (infowindow.getMap()) {{
                        infowindow.close();
                    }} else {{
                        infowindow.open(map, marker);
                    }}
                }});
            }});
        </script>
    </body>
    </html>
    """
    st.components.v1.html(html_code, height=600)




elif page == "예산 확인":
    st.title("예산 확인")
    st.write("현재 예산은 총 **10,000원**입니다.")

    st.subheader("예산 구성")
    st.write("- 10,000원 한 장")
    st.image(load_image("만원.png"), width=200, caption="10,000원")

    st.write("- 5,000원 두 장")
    st.image(load_image("오천원.png"), width=200, caption="5,000원 X 2")
    st.image(load_image("오천원.png"), width=200)

    st.write("- 5,000원 한 장과 1,000원 다섯 장")
    st.image(load_image("오천원.png"), width=200, caption="5,000원")
    cols = st.columns(5)
    for col in cols:
        col.image(load_image("천원.png"), width=200, caption="1,000원")


elif page == "마트 예절":
    # 네 번째 페이지: 마트 예절
    st.title("마트에서 지켜야 할 예절")
    st.write("마트에서 물건을 구매할 때 지켜야 할 기본적인 예절을 배워봅시다!")

    st.subheader("1. 줄을 설 때")
    st.write("다른 사람을 밀거나 끼어들지 않고 차례대로 줄을 섭니다.")

    st.subheader("2. 물건을 고를 때")
    st.write(
        """
        - 필요 없는 물건은 함부로 만지지 않습니다.
        - 원래 자리에 있던 물건은 다시 제자리에 놓습니다.
        """
    )

    st.subheader("3. 계산할 때")
    st.write(
        """
        - 계산대에서 점원에게 밝고 친절하게 인사합니다.
        - 돈을 정확히 계산하고 차례를 기다립니다.
        """
    )

    st.subheader("4. 주변 사람들에게")
    st.write(
        """
        - 조용히 행동하며 소리를 지르지 않습니다.
        - 다른 사람의 물건을 만지지 않습니다.
        """
    )
    st.image(load_image("마트예절.png"), caption="마트에서 예절을 지키는 모습", width=800)

elif page == "물건 구매":
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

    col1, col2 = st.columns([3, 1])
    with col1:
        st.subheader("구매할 물건을 선택하세요:")
        selected_items = []
        for item, (price, img_name) in items.items():
            with st.container():
                sub_col1, sub_col2 = st.columns([1, 5])
                with sub_col1:
                    st.image(load_image(img_name), width=200)
                with sub_col2:
                    if st.checkbox(f"{item} - {price}", key=f"checkbox_{item}"):
                        selected_items.append(item)
                st.markdown("---")

    total = sum(items[item][0] for item in selected_items if item in items)
    with col2:
        fig, ax = plt.subplots(figsize=(3, 4))
        bar_color = "green" if total <= 10000 else "red"
        bars = ax.bar(["Total"], [total], color=bar_color)

        # 기준선 추가
        ax.axhline(10000, color="blue", linestyle="--")

        # 막대 위에 값 표시
        for bar in bars:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width() / 2, height + 500, f"{int(height)}", ha='center', va='bottom')

        # 축 및 스타일 설정
        ax.set_ylim(0, 15000)  # 최대 값을 15,000으로 고정
        ax.set_yticks([0, 5000, 10000, 15000])  # y축 눈금 설정
        st.pyplot(fig)

    st.markdown(f"**{total}**")


elif page == "구매 성공":
    st.title("구매 성공!")
    st.write("축하합니다! 예산 내에서 성공적으로 물건을 구매했습니다.")
    st.image(load_image("참잘했어요.png"), caption="잘했어요! 🎉", width=800)
