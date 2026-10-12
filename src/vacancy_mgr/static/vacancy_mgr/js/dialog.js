const dialogMixin = {
    methods: {
        showModal: function(refName) {
            const dialog = this.$refs[refName];
            if (dialog && typeof dialog.showModal === "function") {
                dialog.showModal();
            }
        },
        hideModal: function(refName) {
            const dialog = this.$refs[refName];
            if (dialog && typeof dialog.close === "function") {
                dialog.close();
            }
        }
    }
};
