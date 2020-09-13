/*
System Name: Vasyworks
Project Name: vacancy_mgr
Encoding: UTF-8
Copyright (C) 2020 Yasuhiro Yamamoto
 */
function createSearchNameVue(
    buildingName,
) {
    return new Vue({
        el: "#search-conditions-form",
        delimiters: ["[[", "]]"],
        data: {
            building_name: buildingName,
        },
        mounted: function(event) {
        },
        methods: {
            clearConditions: function(event) {
                this.building_name = "";
            },
        },
    });
}
