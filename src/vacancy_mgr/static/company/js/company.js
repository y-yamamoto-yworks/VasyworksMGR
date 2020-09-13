/*
System Name: Vasyworks
Project Name: vacancy_mgr
Encoding: UTF-8
Copyright (C) 2020 Yasuhiro Yamamoto
 */
Vue.use(window["vue-js-modal"].default);

function createCompanyVue(
    key,    // キー
    apiKey,     // APIキー（設定用）
    internalApiKey,     // 内部APIキー（設定用）
) {
    return new Vue({
        el: "#data-form",
        delimiters: ["[[", "]]"],
        data: {
            key: key,       // APIデータ取得用
            apiKey: apiKey,
            internalApiKey: internalApiKey,
        },
        methods: {
            openChangeApiKeyModal: function(event) {
                // APIキー変更確認モーダル画面を開く
                this.$modal.show("change-api-key");
            },
            okCloseChangeApiKeyModal: function(event) {
                // APIキー変更確認画面のOKの処理
                let that = this;
                axios.get("/api/new_key/" + this.key + "/")
                    .then(function(res) {
                        that.apiKey = res.data;
                    })
                    .catch(function (error) {
                        alert("新規キーの取得に失敗しました。");
                    });

                this.$modal.hide("change-api-key");
            },
            cancelCloseChangeApiKeyModal: function(event) {
                // APIキー変更確認画面のキャンセルの処理
                this.$modal.hide("change-api-key");
            },
            openChangeInternalApiKeyModal: function(event) {
                // 内部APIキー変更確認モーダル画面を開く
                this.$modal.show("change-internal-api-key");
            },
            okCloseChangeInternalApiKeyModal: function(event) {
                // 内部APIキー変更確認画面のOKの処理
                let that = this;
                axios.get("/api/new_key/" + this.key + "/")
                    .then(function(res) {
                        that.internalApiKey = res.data;
                    })
                    .catch(function (error) {
                        alert("新規キーの取得に失敗しました。");
                    });

                this.$modal.hide("change-internal-api-key");
            },
            cancelCloseChangeInternalApiKeyModal: function(event) {
                // 内部APIキー変更確認画面のキャンセルの処理
                this.$modal.hide("change-internal-api-key");
            },
        },
    });
}
