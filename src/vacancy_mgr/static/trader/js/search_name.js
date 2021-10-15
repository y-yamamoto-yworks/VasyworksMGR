/*
System Name: Vasyworks
Project Name: vacancy_mgr
Encoding: UTF-8
Copyright (C) 2020 Yasuhiro Yamamoto
 */
function createSearchNameVue(
    traderName,
) {
    return new Vue({
        el: "#search-conditions-form",
        delimiters: ["[[", "]]"],
        data: {
            trader_name: traderName,
        },
        mounted: function(event) {
        },
        methods: {
            clearConditions: function(event) {
                this.trader_name = "";
            },
        },
    });
}
