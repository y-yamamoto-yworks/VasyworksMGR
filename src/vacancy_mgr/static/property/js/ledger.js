/*
System Name: Vasyworks
Project Name: vacancy_mgr
Encoding: UTF-8
Copyright (C) 2020 Yasuhiro Yamamoto
 */
var { LMap, LTileLayer, LMarker } = Vue2Leaflet;

function createLedgerVue(
    lat,
    lng,
) {
    return new Vue({
        el: "#contents",
        delimiters: ["[[", "]]"],
        components: { LMap, LTileLayer, LMarker },
        data: {
            zoom: 16,
            center: L.latLng(lat, lng),
            url:'http://{s}.tile.osm.org/{z}/{x}/{y}.png',
            attribution:'&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors',
            marker: L.latLng(lat, lng),
            icon: L.icon({
                    iconUrl: "/static/vacancy_mgr/images/building_icon.png",
                    iconSize: [48, 48],
                    iconAnchor: [24, 24],
            }),
        },
        mounted: function(event) {
        },
        methods: {
        },
    });
}

