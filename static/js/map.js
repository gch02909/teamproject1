var mapContainer = document.getElementById('map'), // 지도를 표시할 div 
            mapOption = {
                center: new kakao.maps.LatLng(37.55827976290345, 126.94264157317063), // 마루 180 번지
                level: 4 // 지도의 확대 레벨 
            };

        var map = new kakao.maps.Map(mapContainer, mapOption); // 지도를 생성합니다

        var positions = [
            {
                title: 'PC지앵 이대역점',
                latlng: new kakao.maps.LatLng(37.55724505624856, 126.94568680240876)
            },
            {
                title: '인터넷월드 대흥점',
                latlng: new kakao.maps.LatLng(37.55638929061601, 126.94608353521951)
            },
            {
                title: '한빛온 PC방',
                latlng: new kakao.maps.LatLng(37.55777550545104, 126.94326443245869)
            },
            {
                title: '창천독수리PC방',
                latlng: new kakao.maps.LatLng(37.556701891374765, 126.94036796028044)
            },
            {
                title: 'VRIZ PC CAFE 신촌',
                latlng: new kakao.maps.LatLng(37.55611456423017, 126.94036796028044)
            },
            {
                title: '인터라켄PC방',
                latlng: new kakao.maps.LatLng(37.55728599853135, 126.93739096277841)
            },
            {
                title: '프리미엄PC방',
                latlng: new kakao.maps.LatLng(37.558322502931276, 126.93806916167563)
            },
            {
                title: '독수리PC',
                latlng: new kakao.maps.LatLng(37.55891799855328, 126.93806916167563)
            },
            {
                title: '리코스타PC방',
                latlng: new kakao.maps.LatLng(37.55925325406735, 126.9435009880987)
            },
            {
                title: '퍼플 pc방',
                latlng: new kakao.maps.LatLng(37.55922633227016, 126.94372736654722)
            },
        ];

        positions.map(x => displayMarker(x.latlng, x.title));

        function displayMarker(locPosition, message) {
            // 마커를 생성합니다
            var marker = new kakao.maps.Marker({
                map: map,
                position: locPosition,
                clickable: true
            });

            marker.setClickable(true);

            // 마커를 지도에 표시합니다.
            marker.setMap(map);

            // 인포윈도우를 생성합니다
            var infowindow = new kakao.maps.InfoWindow({
                content: message
            });

            kakao.maps.event.addListener(marker, 'click', makeClickListener(map, marker, infowindow));
            kakao.maps.event.addListener(marker, 'click', makeOutClickListener(infowindow));
            kakao.maps.event.addListener(marker, 'mouseover', makeOverListener(map, marker, infowindow));
            kakao.maps.event.addListener(marker, 'mouseout', makeOutListener(infowindow));
        }

        function makeClickListener(map, marker, infowindow) {
            return function () {
                document.location.href = '/detail/1';
            };
        }

        // 인포윈도우를 닫는 클로저를 만드는 함수입니다 
        function makeOutClickListener(infowindow) {
            return function () {
                infowindow.close();
            };
        }

        function makeOverListener(map, marker, infowindow) {
            return function () {
                infowindow.open(map, marker);
            };
        }

        // 인포윈도우를 닫는 클로저를 만드는 함수입니다 
        function makeOutListener(infowindow) {
            return function () {
                infowindow.close();
            };
        }