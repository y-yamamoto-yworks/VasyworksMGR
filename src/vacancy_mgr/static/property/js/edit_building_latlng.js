/*
System Name: Vasyworks
Project Name: vacancy_mgr
Encoding: UTF-8
Copyright (C) 2020 Yasuhiro Yamamoto
 */
var { LMap, LTileLayer, LMarker, LIcon } = Vue2Leaflet;

function createBuildingLatLngVue(
    lat,
    lng,
) {
    return new Vue({
        el: "#data-form",
        delimiters: ["[[", "]]"],
        components: { LMap, LTileLayer, LMarker, LIcon },
        data: {
            zoom: 17,
            center: L.latLng(lat, lng),
            url: 'http://{s}.tile.osm.org/{z}/{x}/{y}.png',
            attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors',
            marker: L.latLng(lat, lng),
            icon: L.icon({
                    iconUrl: "/static/property/images/center.png",
                    iconSize: [39, 39],
                    iconAnchor: [20, 20],
            }),
        },
        methods: {
            updateCenter(center) {
                this.$refs.lat.value = center.lat;
                this.$refs.lng.value = center.lng;
                this.marker = center;
            },
        },
    });
}
