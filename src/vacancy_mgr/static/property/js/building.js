/*
System Name: Vasyworks
Project Name: vacancy_mgr
Encoding: UTF-8
Copyright (C) 2020 - 2026 Yasuhiro Yamamoto
 */

function createBuildingVue(
    activePage,
    lat,
    lng,
) {
    return new Vue({
        el: "#data-detail",
        delimiters: ["[[", "]]"],
        data: {
            activeTabPage: activePage,      // TABページ切り替え用
            zoom: 17,
            center: L.latLng(lat, lng),
            url:'https://{s}.tile.osm.org/{z}/{x}/{y}.png',
            attribution:'&copy; <a href="https://osm.org/copyright">OpenStreetMap</a> contributors',
            marker: L.marker([lat, lng]),
            map: null,
        },
        mounted: function(event) {
            this.changeActivePage();
        },
        methods: {
            changeTabPage: function(pageName, event) {
                // タブページの切り替え
                this.activeTabPage = pageName;
                this.changeActivePage();
            },
            changeActivePage() {
                let item = this.$refs[this.activeTabPage + "_tab"];
                let items = item.parentNode.querySelectorAll(":scope > li");
                for (let i = 0; i < items.length; i++) {
                    items[i].className = items[i].className.replace("active", "").trim();
                }
                item.className = item.className + " active";

                // 地図タブの場合は地図を初期化
                if (this.activeTabPage === 'map_page') {
                    this.$nextTick(function() {
                        this.initMap(lat, lng);
                    });
                }
            },
            initMap: function(lat, lng) {
                if (lat > 0 && lng > 0) {
                    var mapEl = document.getElementById('id_map');
                    if (!mapEl) return;

                    if(this.map) {
                        this.map.remove();
                        this.map = null;
                    }
                    this.map = L.map('id_map').setView([lat, lng], this.zoom);
                    L.tileLayer(this.url, {
                        attribution: this.attribution
                    }).addTo(this.map);
                    this.marker.addTo(this.map);
                }
            }
        },
    });
}

