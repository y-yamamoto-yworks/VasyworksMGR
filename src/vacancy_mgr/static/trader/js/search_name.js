/*
System Name: Vasyworks
Project Name: vacancy_mgr
Encoding: UTF-8
Copyright (C) 2020 - 2026 Yasuhiro Yamamoto
 */
function createSearchNameVue(
    traderName,
) {
    return Vue.createApp({
        delimiters: ["[[", "]]"],
        data() {
            return {
                trader_name: traderName,
            };
        },
        mounted: function(event) {
        },
        methods: {
            clearConditions: function(event) {
                this.trader_name = "";
            },
        },
    }).mount("#search-conditions-form");
}
