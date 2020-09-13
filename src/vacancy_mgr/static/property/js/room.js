/*
System Name: Vasyworks
Project Name: vacancy_mgr
Encoding: UTF-8
Copyright (C) 2020 Yasuhiro Yamamoto
 */
function createRoomVue(
    activePage,
) {
    return new Vue({
        el: "#data-detail",
        delimiters: ["[[", "]]"],
        data: {
            activeTabPage: activePage,      // TABページ切り替え用
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

