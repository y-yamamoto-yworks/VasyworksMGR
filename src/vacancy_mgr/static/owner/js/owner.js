/*
System Name: Vasyworks
Project Name: vacancy_mgr
Encoding: UTF-8
Copyright (C) 2020 Yasuhiro Yamamoto
 */
Vue.use(window["vue-js-modal"].default);

function createOwnerVue(
    key,    // キー
    staffId,   // スタッフID
    staffName,     // スタッフ名
) {
    return new Vue({
        el: "#data-form",
        delimiters: ["[[", "]]"],
        data: {
            key: key,       // APIデータ取得用
            staff: staffId,
            staffName: staffName,
            selectStaffs: [],      // スタッフ選択用
            selectStaffHint: "",      // スタッフ選択用
            selectedStaff: 0,      // スタッフ選択用
        },
        methods: {
            openStaffModal: function(event) {
                // スタッフ選択モーダル画面を開く
                this.reloadStaffs();
                this.selectedStaff = this.staff;
                this.$modal.show("select-staff");
            },
            okCloseStaffModal: function(event) {
                // スタッフ選択画面のOKの処理
                this.staff = this.selectedStaff;
                this.staffName = this.selectStaffs.find(
                    (staff) => staff.id === this.selectedStaff
                ).staff_name;
                this.selectStaffHint = "";
                this.$modal.hide("select-staff");
            },
            cancelCloseStaffModal: function(event) {
                // スタッフ選択画面のキャンセルの処理
                this.selectStaffHint = "";
                this.$modal.hide("select-staff");
            },
            narrowDownStaffs: function(event) {
                // スタッフ選択用リスト絞り込みの処理
                this.reloadStaffs();
            },
            reloadStaffs : function() {
                // スタッフ選択用リストを書き換える。
                let that = this;

                let url = "/api/staffs/" + this.key;
                if (this.selectStaffHint) {
                    let hint = this.selectStaffHint.trim();
                    if (hint !== "") url += "/" + encodeURI(hint);
                }

                axios.get(url)
                    .then(function(res) {
                        that.selectStaffs = res.data;
                    })
                    .catch(function (error) {
                        alert("スタッフデータの取得に失敗しました。");
                    });
            },
        },
    });
}

