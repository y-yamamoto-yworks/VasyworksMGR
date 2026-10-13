/*
System Name: Vasyworks
Project Name: vacancy_mgr
Encoding: UTF-8
Copyright (C) 2020 - 2026 Yasuhiro Yamamoto
 */
function createSearchNameVue(
    ownerName,
) {
    return Vue.createApp({
        delimiters: ["[[", "]]"],
        data() {
            return {
                owner_name: ownerName,
            };
        },
        mounted: function(event) {
        },
        methods: {
            clearConditions: function(event) {
                this.owner_name = "";
            },
        },
    }).mount("#search-conditions-form");
}
