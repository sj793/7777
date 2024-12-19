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

# 세션 상태 초기화
if "current_page" not in st.session_state:
    st.session_state.current_page = "수업 소개"  # 기본 페이지

# 사이드바 메뉴와 페이지 전환 동기화
menu_options = ["수업 소개", "편의점 지도", "예산 확인", "마트 예절", "물건 구매", "구매 성공"]
selected_page = st.sidebar.radio("페이지를 선택하세요", menu_options)

# 세션 상태의 현재 페이지를 업데이트
st.session_state.current_page = selected_page

# 각 페이지별 코드
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

    # Google 지도 HTML 코드 삽입
    html_code = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
        <title>편의점 지도</title>
        <script src="https://maps.googleapis.com/maps/api/js?key=YOUR_GOOGLE_MAPS_API_KEY&libraries=places"></script>
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
            function initMap() {{
                const schoolPosition = {{ lat: 37.5750938, lng: 126.9876033 }};  // 서울경운학교 좌표
                const mapOptions = {{
                    center: schoolPosition,
                    zoom: 15
                }};
                const map = new google.maps.Map(document.getElementById('map'), mapOptions);

                const schoolMarker = new google.maps.Marker({{
                    position: schoolPosition,
                    map: map,
                    title: "서울경운학교",
                    icon: "https://maps.google.com/mapfiles/ms/icons/blue-dot.png"
                }});

                const service = new google.maps.places.PlacesService(map);
                const request = {{
                    location: schoolPosition,
                    radius: 500,
                    keyword: "편의점"
                }};
                service.nearbySearch(request, (results, status) => {{
                    if (status === google.maps.places.PlacesServiceStatus.OK) {{
                        results.forEach((place) => {{
                            const storeMarker = new google.maps.Marker({{
                                position: place.geometry.location,
                                map: map,
                                title: place.name
                            }});
                        }});
                    }}
                }});
            }}
            initMap();
        </script>
    </body>
    </html>
    """
    st.components.v1.html(html_code, height=600)

elif st.session_state.current_page == "예산 확인":
    st.title("예산 확인")
    st.write("현재 예산은 총 **10,000원**입니다.")
    st.image(load_image("만원.png"), width=200, caption="10,000원")
    st.image(load_image("오천원.png"), width=200, caption="5,000원 X 2")
    st.image(load_image("천원.png"), width=200, caption="1,000원 X 5")

elif st.session_state.current_page == "마트 예절":
    st.title("마트에서 지켜야 할 예절")
    st.write("마트에서 물건을 구매할 때 지켜야 할 기본적인 예절을 배워봅시다!")
    st.image(load_image("마트예절.png"), caption="마트에서 예절을 지키는 모습", width=800)

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
    total = sum(items[item][0] for item in selected_items if item in items)

    col1, col2 = st.columns([3, 1])
    with col1:
        for item, (price, img_name) in items.items():
            st.image(load_image(img_name), width=150)
            if st.checkbox(f"{item} - {price}", key=f"checkbox_{item}"):
                selected_items.append(item)
    with col2:
        if st.button("구매"):
            if total <= 10000:
                st.session_state.current_page = "구매 성공"
            else:
                st.error("구매 금액이 예산을 초과했습니다.")

elif st.session_state.current_page == "구매 성공":
    st.title("구매 성공!")
    st.success("예산 내에서 성공적으로 물건을 구매했습니다.")
    st.image(load_image("참잘했어요.png"), caption="잘했어요! 🎉", width=800)
    if st.button("다시 구매하기"):
        st.session_state.current_page = "물건 구매"
