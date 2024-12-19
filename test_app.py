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

# 사이드바 메뉴와 상태 초기화
if "current_page" not in st.session_state:
    st.session_state["current_page"] = "수업 소개"

# 사이드바 메뉴 생성
selected_page = st.sidebar.selectbox(
    "페이지를 선택하세요",
    ["수업 소개", "편의점 지도", "예산 확인", "마트 예절", "물건 구매", "구매 성공"]
)

# 선택한 페이지를 상태에 저장
st.session_state["current_page"] = selected_page

# 페이지 렌더링
if st.session_state["current_page"] == "수업 소개":
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

elif st.session_state["current_page"] == "편의점 지도":
    st.title("서울경운학교 주변 편의점 지도")
    st.write("서울경운학교 주변의 편의점을 알아봅시다.")

    # HTML 코드로 Google 지도 렌더링
    html_code = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
        <title>편의점 지도</title>
        <script src="https://maps.googleapis.com/maps/api/js?key=AIzaSyD7lt0KSanRvYmQaJ3CQ0gZGVS-y1urcNI&libraries=places"></script>
        <style>
            #map {{
                width: 100%;
                height: 500px;
                margin: 0 auto;
            }}
        </style>
    </head>
    <body>
        <div id="map"></div>
        <script>
            function initMap() {{
                const geocoder = new google.maps.Geocoder();
                const address = "대한민국 서울특별시 종로구 삼일대로 454";

                geocoder.geocode({{ address: address }}, (results, status) => {{
                    if (status === "OK") {{
                        const schoolPosition = results[0].geometry.location;
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

                        const schoolInfoWindow = new google.maps.InfoWindow({{
                            content: `<div style="text-align:center;padding:10px;font-weight:bold;">서울경운학교</div>`
                        }});

                        schoolMarker.addListener("click", () => {{
                            schoolInfoWindow.open(map, schoolMarker);
                        }});

                        const service = new google.maps.places.PlacesService(map);
                        const request = {{
                            location: schoolPosition,
                            radius: '500',
                            keyword: '편의점'
                        }};

                        service.nearbySearch(request, (results, status) => {{
                            if (status === google.maps.places.PlacesServiceStatus.OK) {{
                                results.forEach((place) => {{
                                    const storeMarker = new google.maps.Marker({{
                                        position: place.geometry.location,
                                        map: map,
                                        title: place.name
                                    }});

                                    const infoWindow = new google.maps.InfoWindow({{
                                        content: `<div style="text-align:center;padding:10px;">${{place.name}}</div>`
                                    }});

                                    storeMarker.addListener("click", () => {{
                                        infoWindow.open(map, storeMarker);
                                    }});
                                }});
                            }} else {{
                                console.error('PlacesService request failed due to: ' + status);
                            }}
                        }});
                    }} else {{
                        document.getElementById('map').innerHTML = "<div style='color:red;text-align:center;'>주소를 찾을 수 없습니다.</div>";
                    }}
                }});
            }}
            initMap();
        </script>
    </body>
    </html>
    """

    st.components.v1.html(html_code, height=600)

    google_maps_url = "https://www.google.com/maps/search/convenience+stores+near+대한민국+서울특별시+종로구+삼일대로+454/"
    st.markdown(
        f"""
        <p style="text-align:center; margin-top: 20px;">
            <a href="{google_maps_url}" target="_blank" 
               style="display:inline-block; padding:10px 20px; background-color:#4285F4; color:white; text-decoration:none; 
               border-radius:5px; font-size:16px; text-align:center;">
               👉 Google 지도 바로가기
            </a>
        </p>
        """,
        unsafe_allow_html=True
    )

elif st.session_state["current_page"] == "예산 확인":
    st.title("예산 확인")
    st.write("현재 예산은 총 **10,000원**입니다.")

    st.subheader("예산 구성")
    st.write("- 10,000원 한 장")
    st.image(load_image("만원.png"), width=200, caption="10,000원")

    st.write("- 5,000원 두 장")
    st.image(load_image("오천원.png"), width=200, caption="5,000원 X 2")
    st.image(load_image("오천원.png"), width=200)

elif st.session_state["current_page"] == "마트 예절":
    st.title("마트에서 지켜야 할 예절")
    st.write("마트에서 물건을 구매할 때 지켜야 할 기본적인 예절을 배워봅시다!")

    st.subheader("1. 줄을 설 때")
    st.write("다른 사람을 밀거나 끼어들지 않고 차례대로 줄을 섭니다.")

elif st.session_state["current_page"] == "물건 구매":
    st.title("물건 구매 시뮬레이터")
    items = {
        "가나초콜릿": (2000, "가나초콜릿.png"),
        "코카콜라": (2500, "코카콜라.png")
    }

    total = sum(price for name, (price, _) in items.items())
    st.write(f"총합: {total}")

elif st.session_state["current_page"] == "구매 성공":
    st.title("구매 성공!")
    st.success("예산 내에서 성공적으로 물건을 구매했습니다.")
