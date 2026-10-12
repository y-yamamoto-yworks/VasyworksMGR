/*
System Name: Vasyworks
Project Name: vacancy_mgr
Encoding: UTF-8
Copyright (C) 2020 - 2026 Yasuhiro Yamamoto
 */

function createCompanyVue(
    key,    // キー
    apiKey,     // APIキー（設定用）
    internalApiKey,     // 内部APIキー（設定用）
) {
    return new Vue({
        el: "#data-form",
        delimiters: ["[[", "]]"],
        mixins: [dialogMixin],
        data: {
            key: key,       // APIデータ取得用
            apiKey: apiKey,
            internalApiKey: internalApiKey,
        },
        methods: {
            openChangeApiKeyModal: function(event) {
                // APIキー変更確認モーダル画面を開く
                this.showModal("changeApiKeyModal");
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

                this.hideModal("changeApiKeyModal");
            },
            cancelCloseChangeApiKeyModal: function(event) {
                // APIキー変更確認画面のキャンセルの処理
                this.hideModal("changeApiKeyModal");
            },
            openChangeInternalApiKeyModal: function(event) {
                // 内部APIキー変更確認モーダル画面を開く
                this.showModal("changeInternalApiKeyModal");
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

                this.hideModal("changeInternalApiKeyModal");
            },
            cancelCloseChangeInternalApiKeyModal: function(event) {
                // 内部APIキー変更確認画面のキャンセルの処理
                this.hideModal("changeInternalApiKeyModal");
            },
        },
    });
}
