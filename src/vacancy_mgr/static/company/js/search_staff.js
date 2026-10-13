/*
System Name: Vasyworks
Project Name: vacancy_mgr
Encoding: UTF-8
Copyright (C) 2020 - 2026 Yasuhiro Yamamoto
 */
function createSearchStaffVue(
    lastName,
) {
    return Vue.createApp({
        delimiters: ["[[", "]]"],
        data() {
            return {
                last_name: lastName,
            };
        },
        mounted: function(event) {
        },
        methods: {
            clearConditions: function(event) {
                this.last_name = "";
            },
        },
    }).mount("#search-conditions-form");
}
