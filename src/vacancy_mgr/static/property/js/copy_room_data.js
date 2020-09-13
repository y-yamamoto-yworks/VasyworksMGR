/*
System Name: Vasyworks
Project Name: vacancy_mgr
Encoding: UTF-8
Copyright (C) 2020 Yasuhiro Yamamoto
 */
function copyRoomDataVue(
) {
    return new Vue({
        el: "#copy-form",
        delimiters: ["[[", "]]"],
        data: {
        },
        mounted: function(event) {
        },
        methods: {
            selectAllTarget: function(event) {
                // コピー対象フラグの全選択
                this.$refs.base.checked = true;
                this.$refs.layout.checked = true;
                this.$refs.features.checked = true;
                this.$refs.vacancy.checked = true;
                this.$refs.web.checked = true;
                this.$refs.monthly_cost.checked = true;
                this.$refs.initial_cost.checked = true;
                this.$refs.renewal_cost.checked = true;
            },
            clearAllTarget: function(event) {
                // コピー対象フラグの全クリア
                this.$refs.base.checked = false;
                this.$refs.layout.checked = false;
                this.$refs.features.checked = false;
                this.$refs.vacancy.checked = false;
                this.$refs.web.checked = false;
                this.$refs.monthly_cost.checked = false;
                this.$refs.initial_cost.checked = false;
                this.$refs.renewal_cost.checked = false;
            },
        },
    });
}

