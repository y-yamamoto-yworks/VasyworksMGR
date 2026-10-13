/*
System Name: Vasyworks
Project Name: vacancy_mgr
Encoding: UTF-8
Copyright (C) 2020 - 2026 Yasuhiro Yamamoto
 */
function createSearchNameVue(
    buildingName,
) {
    return Vue.createApp({
        delimiters: ["[[", "]]"],
        data() {
            return {
                building_name: buildingName,
            };
        },
        mounted: function(event) {
        },
        methods: {
            clearConditions: function(event) {
                this.building_name = "";
            },
        },
    }).mount("#search-conditions-form");
}
