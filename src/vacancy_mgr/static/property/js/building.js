/*
System Name: Vasyworks
Project Name: vacancy_mgr
Encoding: UTF-8
Copyright (C) 2020 Yasuhiro Yamamoto
 */
var { LMap, LTileLayer, LMarker } = Vue2Leaflet;

function createBuildingVue(
    activePage,
    lat,
    lng,
) {
    return new Vue({
        el: "#data-detail",
        delimiters: ["[[", "]]"],
        components: { LMap, LTileLayer, LMarker },
        data: {
            activeTabPage: activePage,      // TABページ切り替え用
            zoom: 17,
            center: L.latLng(lat, lng),
            url:'http://{s}.tile.osm.org/{z}/{x}/{y}.png',
            attribution:'&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors',
            marker: L.latLng(lat, lng),
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
            }
        },
    });
}

