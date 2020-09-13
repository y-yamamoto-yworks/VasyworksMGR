/*
System Name: Vasyworks
Project Name: vacancy_mgr
Encoding: UTF-8
Copyright (C) 2020 Yasuhiro Yamamoto
 */
Vue.use(window["vue-js-modal"].default);

function createEditRoomVue(
    key,    // キー
    condoOwnerId,   // 分譲オーナーID
    condoOwnerName,     // 分譲オーナー名
    condoTraderId,  // 分譲賃貸管理業者ID
    condoTraderName,    // 分譲賃貸管理業者名
) {
    return new Vue({
        el: "#data-form",
        delimiters: ["[[", "]]"],
        data: {
            key: key,       // APIデータ取得用
            condoOwner: condoOwnerId,
            condoOwnerName: condoOwnerName,
            selectCondoOwners: [],      // 分譲オーナー選択用
            selectCondoOwnerHint: "",      // 分譲オーナー選択用
            selectedCondoOwner: 0,      // 分譲オーナー選択用
            condoTrader: condoTraderId,
            condoTraderName: condoTraderName,
            selectCondoTraders: [],     // 分譲賃貸管理業者選択用
            selectCondoTraderHint: "",     // 分譲賃貸管理業者選択用
            selectedCondoTrader: 0,     // 分譲賃貸管理業者選択用
            inputGuaranteeCompany: "",        // 保証会社入力用
            inputGuaranteeCompanies: [],       // 保証会社入力用
            inputInsuranceCompany: "",        // 火災保険会社入力用
            inputInsuranceCompanies: [],       // 火災保険会社入力用
        },
        mounted: function(event) {
        },
        methods: {
            openCondoOwnerModal: function(event) {
                // オーナー選択モーダル画面を開く
                this.reloadCondoOwners();
                this.selectedCondoOwner = this.condoOwner;
                this.$modal.show("select-condo-owner");
            },
            okCloseCondoOwnerModal: function(event) {
                // オーナー選択画面のOKの処理
                this.condoOwner = this.selectedCondoOwner;
                this.condoOwnerName = this.selectCondoOwners.find(
                    (owner) => owner.id === this.selectedCondoOwner
                ).owner_name;
                this.selectOwnerHint = "";
                this.$modal.hide("select-condo-owner");
            },
            cancelCloseCondoOwnerModal: function(event) {
                // オーナー選択画面のキャンセルの処理
                this.selectCondoOwnerHint = "";
                this.$modal.hide("select-condo-owner");
            },
            narrowDownCondoOwners: function(event) {
                // オーナー選択用リスト絞り込みの処理
                this.reloadCondoOwners();
            },
            openCondoTraderModal: function(event) {
                // 賃貸管理業者選択モーダル画面を開く
                this.reloadCondoTraders();
                this.selectedCondoTrader = this.condoTrader;
                this.$modal.show("select-condo-trader");
            },
            okCloseCondoTraderModal: function(event) {
                // 賃貸管理業者選択画面のOKの処理
                this.condoTrader = this.selectedCondoTrader;
                this.condoTraderName = this.selectCondoTraders.find(
                    (trader) => trader.id === this.selectedCondoTrader
                ).trader_name;
                this.selectCondoTraderHint = "";
                this.$modal.hide("select-condo-trader");
            },
            cancelCloseCondoTraderModal: function(event) {
                // 賃貸管理業者選択画面のキャンセルの処理
                this.selectCondoTraderHint = "";
                this.$modal.hide("select-condo-trader");
            },
            narrowDownCondoTraders: function(event) {
                // 賃貸管理業者選択用リスト絞り込みの処理
                this.reloadCondoTraders();
            },
            openInputGuaranteeCompanyModal: function(event) {
                // 保証会社入力モーダル画面を開く
                this.reloadInputGuaranteeCompanies();
                this.$modal.show("input-guarantee-company");
            },
            okCloseInputGuaranteeCompanyModal: function(event) {
                // 保証会社入力画面のOKの処理
                this.$refs.guarantee_company.value = this.inputGuaranteeCompany;
                this.inputGuaranteeCompany = "";
                this.$modal.hide("input-guarantee-company");
            },
            cancelCloseInputGuaranteeCompanyModal: function(event) {
                // 保証会社入力画面のキャンセルの処理
                this.inputGuaranteeCompany = "";
                this.$modal.hide("input-guarantee-company");
            },
            openInputInsuranceCompanyModal: function(event) {
                // 火災保険会社入力モーダル画面を開く
                this.reloadInputInsuranceCompanies();
                this.$modal.show("input-insurance-company");
            },
            okCloseInputInsuranceCompanyModal: function(event) {
                // 火災保険会社入力画面のOKの処理
                this.$refs.insurance_company.value = this.inputInsuranceCompany;
                this.inputInsuranceCompany = "";
                this.$modal.hide("input-insurance-company");
            },
            cancelCloseInputInsuranceCompanyModal: function(event) {
                // 火災保険会社入力画面のキャンセルの処理
                this.inputInsuranceCompany = "";
                this.$modal.hide("input-insurance-company");
            },
            reloadCondoOwners : function() {
                // オーナー選択用リストを書き換える。
                let that = this;

                let url = "/api/owners/" + this.key;
                if (this.selectCondoOwnerHint) {
                    let hint = this.selectCondoOwnerHint.trim();
                    if (hint !== "") url += "/" + encodeURI(hint);
                }

                axios.get(url)
                    .then(function(res) {
                        that.selectCondoOwners = res.data;
                    })
                    .catch(function (error) {
                        alert("分譲オーナーデータの取得に失敗しました。");
                    });
            },
            reloadCondoTraders : function() {
                // 賃貸管理業者選択用リストを書き換える。
                let that = this;

                let url = "/api/traders/" + this.key;
                if (this.selectCondoTraderHint) {
                    let hint = this.selectCondoTraderHint.trim();
                    if (hint !== "") url += "/" + encodeURI(hint);
                }

                axios.get(url)
                    .then(function(res) {
                        that.selectCondoTraders = res.data;
                    })
                    .catch(function (error) {
                        alert("分譲賃貸管理業者データの取得に失敗しました。");
                    });
            },
            reloadInputGuaranteeCompanies : function() {
                // 保証会社入力用リストを書き換える。
                let that = this;

                let url = "/api/guarantee_companies/" + this.key;

                axios.get(url)
                    .then(function(res) {
                        that.inputGuaranteeCompanies = res.data;
                    })
                    .catch(function (error) {
                        alert("保証会社入力データの取得に失敗しました。");
                    });
            },
            reloadInputInsuranceCompanies : function() {
                // 火災保険会社入力用リストを書き換える。
                let that = this;

                let url = "/api/insurance_companies/" + this.key;

                axios.get(url)
                    .then(function(res) {
                        that.inputInsuranceCompanies = res.data;
                    })
                    .catch(function (error) {
                        alert("火災保険会社入力データの取得に失敗しました。");
                    });
            },
        },
    });
}

