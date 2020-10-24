/*
System Name: Vasyworks
Project Name: vacancy_mgr
Encoding: UTF-8
Copyright (C) 2020 Yasuhiro Yamamoto
 */
function createSearchStaffVue(
    lastName,
) {
    return new Vue({
        el: "#search-conditions-form",
        delimiters: ["[[", "]]"],
        data: {
            last_name: lastName,
        },
        mounted: function(event) {
        },
        methods: {
            clearConditions: function(event) {
                this.last_name = "";
            },
        },
    });
}
