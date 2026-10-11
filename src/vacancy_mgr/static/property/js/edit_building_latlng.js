/*
System Name: Vasyworks
Project Name: vacancy_mgr
Encoding: UTF-8
Copyright (C) 2020 - 2026 Yasuhiro Yamamoto
 */

function createBuildingLatLngVue(
    lat,
    lng,
) {
    return new Vue({
        el: "#data-form",
        delimiters: ["[[", "]]"],
        data: {
            zoom: 17,
            center: L.latLng(lat, lng),
            url: 'https://{s}.tile.osm.org/{z}/{x}/{y}.png',
            attribution: '&copy; <a href="https://osm.org/copyright">OpenStreetMap</a> contributors',
            icon: L.icon({
                    iconUrl: "/static/property/images/center.png",
                    iconSize: [39, 39],
                    iconAnchor: [20, 20],
            }),
            marker: null,
            map: null,
        },
        mounted: function(event) {
            if (lat > 0 && lng > 0) {
                var mapEl = document.getElementById('id_map');
                if (!mapEl) return;
                this.map = L.map('id_map').setView([lat, lng], this.zoom);
                L.tileLayer(this.url, {
                    attribution: this.attribution
                }).addTo(this.map);
                this.marker = L.marker([lat, lng], {icon: this.icon})
                this.marker.addTo(this.map);

                this.map.on('move', () => {
                    var newCenter = this.map.getCenter();
                    this.updateCenter(newCenter);
                });
            }
        },
        methods: {
            updateCenter(center) {
                this.$refs.lat.value = center.lat;
                this.$refs.lng.value = center.lng;
                this.marker.setLatLng(center);
            },
        },
    });
}
