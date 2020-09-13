/*
System Name: Vasyworks
Project Name: vacancy_mgr
Encoding: UTF-8
Copyright (C) 2020 Yasuhiro Yamamoto
 */

function createBuildingLandmarkVue(
    key,    // キー
    landmarkType,   // ランドマーク種別
) {
    return new Vue({
        el: "#create-form",
        delimiters: ["[[", "]]"],
        data: {
            key: key,       // APIデータ取得用
            landmarkType: landmarkType,
            landmark: 0,
        },
        mounted: function(event) {
            this.reloadLandmarks();
        },
        methods: {
            changeLandmarkType: function(event) {
                // ランドマーク変更時の処理
                this.reloadLandmarks();
            },
            reloadSelectOptions: function(elm, items, value) {
                // サーバサイドで自動生成される選択リスト向け
                // 選択リスト書き換え用の内部メソッド
                if(!elm || !items) return;

                // 対象リストをクリア
                let elm_options = elm.querySelectorAll("option");
                for(let i = elm_options.length - 1; i >= 0; i--) {
                    elm_options[i].remove();
                }

                // 対象リストの再構築
                for(let i = 0; i < items.length; i++) {
                    let option = document.createElement("option");
                    option.text = items[i].name;
                    option.value = items[i].id;
                    if(option.value === value.toString()) option.selected = true;
                    elm.appendChild(option);
                }
            },
            reloadLandmarks: function() {
                // ランドマークのリストを書き換える。
                if(this.landmarkType !== 0) {
                    let that = this;
                    axios.get("/api/landmarks/" + this.key + "/" + this.landmarkType)
                        .then(function(res) {
                            let items = res.data;
                            that.reloadSelectOptions(that.$refs.landmark, items, that.landmark)
                        })
                        .catch(function (error) {
                            alert("ランドマークデータの取得に失敗しました。");
                        });
                }
            },

        },
    });
}
