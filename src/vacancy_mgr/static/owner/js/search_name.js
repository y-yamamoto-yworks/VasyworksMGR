/*
System Name: Vasyworks
Project Name: vacancy_mgr
Encoding: UTF-8
Copyright (C) 2020 Yasuhiro Yamamoto
 */
function createSearchNameVue(
    ownerName,
) {
    return new Vue({
        el: "#search-conditions-form",
        delimiters: ["[[", "]]"],
        data: {
            owner_name: ownerName,
        },
        mounted: function(event) {
        },
        methods: {
            clearConditions: function(event) {
                this.owner_name = "";
            },
        },
    });
}
