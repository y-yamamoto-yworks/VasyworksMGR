/*
System Name: Vasyworks
Project Name: vacancy_mgr
Encoding: UTF-8
Copyright (C) 2020 Yasuhiro Yamamoto
 */
function copyRoomPictureVue(
    key,    // キー
) {
    return new Vue({
        el: "#copy-form",
        delimiters: ["[[", "]]"],
        data: {
            key: key,       // APIデータ取得用
            selectedRoom: 0,        // 選択されている部屋
            pictures: [],           // 選択されている部屋の画像リスト
            checkedPictures:[],      // チェックされている画像アイテムリスト
        },
        mounted: function(event) {
        },
        methods: {
            changeSelectedRoom: function(event) {
                // 部屋選択の変更時の処理
                this.showRoomPicture();
            },
            showRoomPicture: function() {
                // 部屋画像の表示
                if(this.selectedRoom !== "") {
                    let that = this;
                    let url = "/api/room_pictures/" + this.key + "/" + this.selectedRoom;
                    axios.get(url)
                        .then(function(res) {
                            that.pictures = res.data;
                            that.checkedItems = [];
                        })
                        .catch(function (error) {
                            alert("画像データの取得に失敗しました。");
                        });
                }
            },
            selectAllPictures: function(event) {
                // 画像コピー対象フラグの全選択
                this.checkedPictures = [];
                let that = this;
                this.pictures.forEach(function(picture){
                    that.checkedPictures.push(picture.id);
                });
            },
            clearAllPictures: function(event) {
                // 画像コピー対象フラグの全クリア
                this.checkedPictures = [];
            },
        },
    });
}

