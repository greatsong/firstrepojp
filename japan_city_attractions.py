import streamlit as st
import folium
from streamlit_folium import st_folium

# 일본 도시와 관광지 정보
city_attractions = {
    '도쿄': (
        '🇯🇵 **도쿄**\n'
        '일본의 수도인 도쿄는 현대성과 전통이 조화를 이루는 도시입니다.\n'
        '도쿄는 매력적인 문화, 풍부한 역사, 다양한 엔터테인먼트를 제공합니다.\n'
        '여기서 가볼 만한 관광지는:\n'
        '- **도쿄타워**: 1958년에 건설된 이 타워는 도쿄의 대표적인 랜드마크입니다. 방문객들은\n'
        '높은 전망대에서 도쿄 시내의 놀라운 전경을 감상할 수 있습니다. 더욱이, 야경이 아름다워\n'
        '야경 촬영 명소로 유명합니다.\n'
        '- **시부야 스크램블 교차로**: 일본에서 가장 바쁜 교차로 중 하나로, 매일 수많은 사람들이\n'
        '이곳을 지나갑니다. 다양한 상점과 레스토랑이 밀집해 있어 쇼핑과 외식을 즐기기에 좋습니다.\n'
        '- **아사쿠사와 센소지**: 도쿄에서 가장 오래된 사원인 센소지를 방문해 보세요. 전통과\n'
        '일본 문화를 느낄 수 있는 곳으로, 특히 신년이나 여름 축제에 많은 관광객이 찾는 명소입니다.\n'
        '- **빙고 나카미세 거리**: 센소지로 가는 길에 위치한 이 거리에서는 다양한 전통 간식과\n'
        '기념품을 구매할 수 있습니다. 일본식 과자인 '나쓰메'와 '타코야키'가 유명합니다.'
    ),
    '오사카': (
        '🍜 **오사카**\n'
        '음식의 도시 오사카는 맛있고 다양한 일본 요리로 유명합니다. 이 도시는\n'
        '경기, 쇼핑, 문화 체험이 가득한 활기찬 분위기를 자랑합니다.\n'
        '여기서 가볼 만한 관광지는:\n'
        '- **오사카 성**: 일본의 역사적인 성으로, 아름다운 정원과 함께 역사 박물관이 있습니다.\n'
        '성 주변의 공원은 벚꽃 시즌에 특히 아름답습니다. 성의 꼭대기에서 바라보는 경치는 일품입니다.\n'
        '- **도톤보리**: 활기찬 분위기의 거리로, 길게 늘어선 다양한 음식점이 있습니다. 오사카의 특산물인\n'
        '타코야키와 오카사카를 꼭 맛보세요. 화려한 광고판과 네온사인들로 가득 찬 이곳은 사진 찍기 좋은\n'
        '장소입니다.\n'
        '- **유니버설 스튜디오 재팬**: 인기 있는 영화들을 테마로 한 놀이공원으로, 가족 단위 관광객이\n'
        '많이 찾습니다. 다양한 놀이기구와 엔터테인먼트 쇼가 마련되어 있습니다.\n'
        '- **신세카이**: 일본의 전통적인 분위기를 남긴 지역으로, 다양한 전통 음식을 즐길 수 있습니다.\n'
        '특히 '쿠시카츠'라는 꼬치 튀김이 유명합니다.'
    ),
    '교토': (
        '⛩️ **교토**\n'
        '교토는 일본의 전통과 문화가 살아 숨쉬는 도시입니다. 많은 신사와 사원, 정원이\n'
        '있는 이곳은 일본의 아름다움을 체험할 수 있는 최상의 장소입니다.\n'
        '여기서 가볼 만한 관광지는:\n'
        '- **킨카쿠지(금각사)**: 세계문화유산으로 등록된 이 불교 사원은 금으로 덮인 외관이 특징입니다.\n'
        '자연 경관과 조화를 이루며 독특한 아름다움을 제공합니다. 사원을 둘러싼 정원도 아름답습니다.\n'
        '- **아라시야마 대나무 숲**: 대나무가 우거진 숲 속에서 자연을 느끼고, 조용한 산책을 즐길 수 있는 곳입니다.\n'
        '특히 한여름에는 시원한 그늘이 되어 주며, 대나무 사이를 지나갈 때 느껴지는 차가운 바람이 인상적입니다.\n'
        '- **기온 거리**: 교토에서 가장 유명한 지역 중 하나로, 전통 가옥과 게이샤가 있는 거리입니다.\n'
        '일본 전통 음식을 맛보거나, 기온에서 느긋하게 산책하는 것도 좋습니다. 특별한 경험으로 기온의\n'
        '게이샤와 스미마이당 공연을 관람할 수 있습니다.\n'
        '- **후시미 이나리 신사**: 수천 개의 주홍색 도리이가 이어진 이 신사는 굉장한 상징성을 지니고\n'
        '있으며, 일본의 경치와 전통을 잘 보여줍니다. 산을 오르는 길에도 아름다운 풍경이 펼쳐집니다.'
    ),
    '히로시마': (
        '🌸 **히로시마**\n'
        '히로시마는 일본 역사에서 중요한 의미를 지닌 도시입니다.\n'
        '조금의 슬픔과 회복의 상징이기도 하며, 아름다운 자연도 만끽할 수 있습니다.\n'
        '여기서 가볼 만한 관광지는:\n'
        '- **히로시마 평화 기념 공원**: 원자폭탄 투하로 인해 피해를 입은 지역에 세워진 공원으로,\n'
        '평화의 메시지를 전달합니다. 기념관과 기념비가 있어 역사에 관한 중요한 이야기를 들여다볼 수\n'
        '있는 기회를 제공합니다.\n'
        '- **미야지마섬**: 이곳의 이와지마 신사는 바다에 떠 있는 도리이가 인상적입니다. 관광객들은\n'
        '도리이에서 사진 촬영을 하며, 신사의 경내를 탐방할 수 있습니다. 계절마다 피는 꽃도 아름답습니다.\n'
        '- **히로시마 성**: 역사적인 성으로, hina 마스크 전통과 주변 자연이 어우러져 있습니다.\n'
        '전통 건축물과 아름다운 정원에서 일본의 아름다움을 느낄 수 있습니다.\n'
        '- **오카노미야끼 거리**: 히로시마의 대표 음식 중 하나인 오카노미야끼를 맛볼 수 있는 거리로,\n'
        '다양한 가게들이 밀집해 있어 현지인과 관광객 모두에게 인기가 많습니다.'
    ),
    '삿포로': (
        '❄️ **삿포로**\n'
        '홋카이도의 중심 도시인 삿포로는 맥주와 눈으로 유명합니다. 이곳은 스키 리조트와\n'
        '자연 경관이 매력적인 곳입니다.\n'
        '여기서 가볼 만한 관광지는:\n'
        '- **삿포로 맥주 박물관**: 일본 맥주의 역사를 배우고, 다양한 종류의 맥주를 시음할 수 있는\n'
        '장소입니다. 맥주 제조 과정에 대한 교육도 제공하여 흥미로운 경험이 될 것입니다.\n'
        '- **오도리 공원**: 삿포로 중심부에 위치한 이 공원은 사계절 내내 아름다운 풍경을 제공합니다.\n'
        '여름에는 꽃이 만발하고, 겨울에는 눈 조각 축제가 열리며, 많은 사람들이 방문합니다.\n'
        '- **삿포로 눈 축제**: 매년 겨울에 개최되는 이 축제는 눈과 얼음 조각들이 전시되며,\n'
        '대규모 눈 조각이 인상적입니다. 축제 기간에는 많은 관광객이 몰려와 겨울의 매력을 느낍니다.\n'
        '- **모에레누마 공원**: 세계적인 조각가인 이사무 노구치의 설계로 만들어진 현대적인 공원으로,\n'
        '예술과 자연이 만나는 공간에서 산책을 즐길 수 있습니다.'
    ),
}

# 도시 위치 데이터 (위도, 경도)
city_coordinates = {
    '도쿄': (35.682839, 139.759455),
    '오사카': (34.686315, 135.519585),
    '교토': (35.011636, 135.768029),
    '히로시마': (34.385202, 132.455292),
    '삿포로': (43.061368, 141.354376),
}

def main():
    st.title("일본 도시 관광지 선택기 🇯🇵")

    # 도시 선택 상자
    city = st.selectbox("가고 싶은 도시를 선택하세요:", list(city_attractions.keys()))

    # 선택된 도시의 관광지 정보 출력
    st.write("당신이 선택한 도시: **", city, "**")
    st.write("관광지 정보:\n", city_attractions[city])

    # 선택된 도시의 위치 표시
    st.write("위치 표시:")
    m = folium.Map(location=city_coordinates[city], zoom_start=12)
    folium.Marker(location=city_coordinates[city], popup=city, icon=folium.Icon(color='blue')).add_to(m)

    # Streamlit에서 Folium 맵 표시
    st_folium(m, width=700, height=500)

# 앱 실행
if __name__ == "__main__":
    main()
