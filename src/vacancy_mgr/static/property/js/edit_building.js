/*
System Name: Vasyworks
Project Name: vacancy_mgr
Encoding: UTF-8
Copyright (C) 2020 Yasuhiro Yamamoto
 */
Vue.use(window["vue-js-modal"].default);

function createEditBuildingVue(
    key,    // キー
    prefId,    // 都道府県ID
    cityId,     // 市区町村ID
    townAddress,   // 町域住所
    townName,  // 町域名（ポータル用）
    areaId,    // エリアID
    elementarySchoolId,   // 小学校区ID
    juniorHighSchoolId,  // 中学校区ID
    railwayId1,    // 沿線ID1
    stationId1,    // 駅ID1
    railwayId2,    // 沿線ID2
    stationId2,    // 駅ID2
    railwayId3,    // 沿線ID3
    stationId3,    // 駅ID3
    departmentId,   // 管理部署ID
    departmentName,     // 管理部署名
    agencyDepartmentId,   // 仲介部署ID
    agencyDepartmentName,     // 仲介部署名
    staffId1,   // スタッフID1
    staffName1,     // スタッフ名1
    staffId2,   // スタッフID2
    staffName2,     // スタッフ名2
    ownerId,   // オーナーID
    ownerName,     // オーナー名
    traderId,  // 賃貸管理業者ID
    traderName,    // 賃貸管理業者名
) {
    return new Vue({
        el: "#data-form",
        delimiters: ["[[", "]]"],
        data: {
            key: key,       // APIデータ取得用
            pref: prefId,
            city: cityId,
            townAddress: townAddress,
            townName: townName,
            area: areaId,
            elementarySchool: elementarySchoolId,
            juniorHighSchool: juniorHighSchoolId,
            railway1: railwayId1,
            station1: stationId1,
            railway2: railwayId2,
            station2: stationId2,
            railway3: railwayId3,
            station3: stationId3,
            department: departmentId,
            departmentName: departmentName,
            selectDepartments: [],      // 管理部署選択用
            selectedDepartment: 0,      // 管理部署選択用
            agencyDepartment: agencyDepartmentId,
            agencyDepartmentName: agencyDepartmentName,
            selectAgencyDepartments: [],      // 仲介部署選択用
            selectedAgencyDepartment: 0,      // 仲介部署選択用
            staff1: staffId1,
            staffName1: staffName1,
            selectStaffs1: [],      // スタッフ1選択用
            selectStaffHint1: "",      // スタッフ1選択用
            selectedStaff1: 0,      // スタッフ1選択用
            staff2: staffId2,
            staffName2: staffName2,
            selectStaffs2: [],      // スタッフ2選択用
            selectStaffHint2: "",      // スタッフ2選択用
            selectedStaff2: 0,      // スタッフ2選択用
            owner: ownerId,
            ownerName: ownerName,
            selectOwners: [],      // オーナー選択用
            selectOwnerHint: "",      // オーナー選択用
            selectedOwner: 0,      // オーナー選択用
            trader: traderId,
            traderName: traderName,
            selectTraders: [],     // 賃貸管理業者選択用
            selectTraderHint: "",     // 賃貸管理業者選択用
            selectedTrader: 0,     // 賃貸管理業者選択用
            inputWater: "",        // 水道費定型入力用
            inputWaters: [],       // 水道費定型入力用
            inputElectric: "",        // 電気定型入力用
            inputElectrics: [],       // 電気定型入力用
            inputGas: "",        // ガス定型入力用
            inputGases: [],       // ガス定型入力用
            inputInternet: "",        // インターネット定型入力用
            inputInternets: [],       // インターネット定型入力用
            inputCancelNotice: "",        // 解約通知定型入力用
            inputCancelNotices: [],       // 解約通知定型入力用
            inputShortCancel: "",        // 短期解約定型入力用
            inputShortCancels: [],       // 短期解約定型入力用
            inputPayment: "",        // 賃料支払い定型入力用
            inputPayments: [],       // 賃料支払い定型入力用
            inputGuarantee: "",        // 保証会社定型入力用
            inputGuarantees: [],       // 保証会社定型入力用
            inputInsurance: "",        // 火災保険定型入力用
            inputInsurances: [],       // 火災保険定型入力用
            inputGuarantorLimit: "",        // 保証人極度額定型入力用
            inputGuarantorLimits: [],       // 保証人極度額定型入力用
            inputDocumentPrice: "",        // 入居時書類代定型入力用
            inputDocumentPrices: [],       // 入居時書類代定型入力用
            inputRenewalCharge: "",        // 更新事務手数料定型入力用
            inputRenewalCharges: [],       // 更新事務手数料定型入力用
            inputGarage: "",        // 駐車場定型入力用
            inputGarages: [],       // 駐車場定型入力用
            inputBikeParking: "",        // 駐輪場定型入力用
            inputBikeParkings: [],       // 駐輪場定型入力用
            inputCleaning: "",        // 退去時清掃定型入力用
            inputCleanings: [],       // 退去時清掃定型入力用
            inputChangeLock: "",        // 鍵交換定型入力用
            inputChangeLocks: [],       // 鍵交換定型入力用
            inputPortal: "",        // ポータル掲載定型入力用
            inputPortals: [],       // ポータル掲載定型入力用
        },
        mounted: function(event) {
            this.reloadCities();
            this.reloadAreas();
            this.reloadElementarySchools();
            this.reloadJuniorHighSchools();
            this.reloadStations1();
            this.reloadStations2();
            this.reloadStations3();
        },
        methods: {
            searchAddress: function(event) {
                // 郵便番号から住所情報を取得
                let postalCode = this.$refs.postal_code.value.trim();
                if(postalCode !== "")
                {
                    let that = this;
                    axios.get("/api/postal_code/" + this.key + "/" + postalCode)
                        .then(function(res) {
                            let item = res.data;
                            that.pref = item.pref.id;
                            that.city = item.city.id;
                            that.townAddress = item.town_name;
                            that.townName = item.town_name;

                            that.reloadAreas();
                            that.reloadElementarySchools();
                            that.reloadJuniorHighSchools();
                        })
                        .catch(function (error) {
                            alert("郵便番号データの取得に失敗しました。");
                        });
                }
            },
            changePref: function(event) {
                // 都道府県変更時の処理
                this.reloadCities();
            },
            changeCity: function(event) {
                // 市区町村変更時の処理
                this.area = 0;
                this.elementarySchool = 0;
                this.juniorHighSchool = 0;

                this.reloadAreas();
                this.reloadElementarySchools();
                this.reloadJuniorHighSchools();
            },
            changeRailway1: function(event) {
                // 沿線1変更時の処理
                this.station1 = 0;
                this.reloadStations1();
            },
            changeRailway2: function(event) {
                // 沿線2変更時の処理
                this.station2 = 0;
                this.reloadStations2();
            },
            changeRailway3: function(event) {
                // 沿線3変更時の処理
                this.station3 = 0;
                this.reloadStations3();
            },
            openDepartmentModal: function(event) {
                // 管理部署選択モーダル画面を開く
                this.reloadDepartments();
                this.selectedDepartment = this.department;
                this.$modal.show("select-department");
            },
            okCloseDepartmentModal: function(event) {
                // 管理部署選択画面のOKの処理
                this.department = this.selectedDepartment;
                this.departmentName = this.selectDepartments.find(
                    (department) => department.id === this.selectedDepartment
                ).department_name;
                this.$modal.hide("select-department");
            },
            cancelCloseDepartmentModal: function(event) {
                // 管理部署選択画面のキャンセルの処理
                this.$modal.hide("select-department");
            },
            openAgencyDepartmentModal: function(event) {
                // 仲介部署選択モーダル画面を開く
                this.reloadAgencyDepartments();
                this.selectedAgencyDepartment = this.agencyDepartment;
                this.$modal.show("select-agency-department");
            },
            okCloseAgencyDepartmentModal: function(event) {
                // 仲介部署選択画面のOKの処理
                this.agencyDepartment = this.selectedAgencyDepartment;
                this.agencyDepartmentName = this.selectAgencyDepartments.find(
                    (department) => department.id === this.selectedAgencyDepartment
                ).department_name;
                this.$modal.hide("select-agency-department");
            },
            cancelCloseAgencyDepartmentModal: function(event) {
                // 仲介部署選択画面のキャンセルの処理
                this.select_agency_department_hint = "";
                this.$modal.hide("select-agency-department");
            },
            openStaff1Modal: function(event) {
                // スタッフ1選択モーダル画面を開く
                this.reloadStaffs1();
                this.selectedStaff1 = this.staff1;
                this.$modal.show("select-staff1");
            },
            okCloseStaff1Modal: function(event) {
                // スタッフ1選択画面のOKの処理
                this.staff1 = this.selectedStaff1;
                this.staffName1 = this.selectStaffs1.find(
                    (staff) => staff.id === this.selectedStaff1
                ).staff_name;
                this.selectStaffHint1 = "";
                this.$modal.hide("select-staff1");
            },
            cancelCloseStaff1Modal: function(event) {
                // スタッフ1選択画面のキャンセルの処理
                this.selectStaffHint1 = "";
                this.$modal.hide("select-staff1");
            },
            narrowDownStaffs1: function(event) {
                // スタッフ1選択用リスト絞り込みの処理
                this.reloadStaffs1();
            },
            openStaff2Modal: function(event) {
                // スタッフ2選択モーダル画面を開く
                this.reloadStaffs2();
                this.selectedStaff2 = this.staff2;
                this.$modal.show("select-staff2");
            },
            okCloseStaff2Modal: function(event) {
                // スタッフ2選択画面のOKの処理
                this.staff2 = this.selectedStaff2;
                this.staffName2 = this.selectStaffs2.find(
                    (staff) => staff.id === this.selectedStaff2
                ).staff_name;
                this.selectStaffHint2 = "";
                this.$modal.hide("select-staff2");
            },
            cancelCloseStaff2Modal: function(event) {
                // スタッフ2選択画面のキャンセルの処理
                this.selectStaffHint2 = "";
                this.$modal.hide("select-staff2");
            },
            narrowDownStaffs2: function(event) {
                // スタッフ2選択用リスト絞り込みの処理
                this.reloadStaffs2();
            },
            openOwnerModal: function(event) {
                // オーナー選択モーダル画面を開く
                this.reloadOwners();
                this.selectedOwner = this.owner;
                this.$modal.show("select-owner");
            },
            okCloseOwnerModal: function(event) {
                // オーナー選択画面のOKの処理
                this.owner = this.selectedOwner;
                this.ownerName = this.selectOwners.find(
                    (owner) => owner.id === this.selectedOwner
                ).owner_name;
                this.selectOwnerHint = "";
                this.$modal.hide("select-owner");
            },
            cancelCloseOwnerModal: function(event) {
                // オーナー選択画面のキャンセルの処理
                this.selectOwnerHint = "";
                this.$modal.hide("select-owner");
            },
            narrowDownOwners: function(event) {
                // オーナー選択用リスト絞り込みの処理
                this.reloadOwners();
            },
            openTraderModal: function(event) {
                // 賃貸管理業者選択モーダル画面を開く
                this.reloadTraders();
                this.selectedTrader = this.trader;
                this.$modal.show("select-trader");
            },
            okCloseTraderModal: function(event) {
                // 賃貸管理業者選択画面のOKの処理
                this.trader = this.selectedTrader;
                this.traderName = this.selectTraders.find(
                    (trader) => trader.id === this.selectedTrader
                ).trader_name;
                this.selectTraderHint = "";
                this.$modal.hide("select-trader");
            },
            cancelCloseTraderModal: function(event) {
                // 賃貸管理業者選択画面のキャンセルの処理
                this.selectTraderHint = "";
                this.$modal.hide("select-trader");
            },
            narrowDownTraders: function(event) {
                // 賃貸管理業者選択用リスト絞り込みの処理
                this.reloadTraders();
            },
            openInputWaterModal: function(event) {
                // 水道費定型入力モーダル画面を開く
                this.reloadInputWaters();
                this.$modal.show("input-water");
            },
            okCloseInputWaterModal: function(event) {
                // 水道費定型入力画面のOKの処理
                this.$refs.vacancy_water_comment.value = this.inputWater;
                this.inputWater = "";
                this.$modal.hide("input-water");
            },
            cancelCloseInputWaterModal: function(event) {
                // 水道費定型入力画面のキャンセルの処理
                this.inputWater = "";
                this.$modal.hide("input-water");
            },
            openInputElectricModal: function(event) {
                // 電気定型入力モーダル画面を開く
                this.reloadInputElectrics();
                this.$modal.show("input-electric");
            },
            okCloseInputElectricModal: function(event) {
                // 電気定型入力画面のOKの処理
                this.$refs.vacancy_electric_comment.value = this.inputElectric;
                this.inputElectric = "";
                this.$modal.hide("input-electric");
            },
            cancelCloseInputElectricModal: function(event) {
                // 電気定型入力画面のキャンセルの処理
                this.inputElectric = "";
                this.$modal.hide("input-electric");
            },
            openInputGasModal: function(event) {
                // ガス定型入力モーダル画面を開く
                this.reloadInputGases();
                this.$modal.show("input-gas");
            },
            okCloseInputGasModal: function(event) {
                // ガス定型入力画面のOKの処理
                this.$refs.vacancy_gas_comment.value = this.inputGas;
                this.inputGas = "";
                this.$modal.hide("input-gas");
            },
            cancelCloseInputGasModal: function(event) {
                // ガス定型入力画面のキャンセルの処理
                this.inputGas = "";
                this.$modal.hide("input-gas");
            },
            openInputInternetModal: function(event) {
                // インターネット定型入力モーダル画面を開く
                this.reloadInputInternets();
                this.$modal.show("input-internet");
            },
            okCloseInputInternetModal: function(event) {
                // インターネット定型入力画面のOKの処理
                this.$refs.vacancy_internet_comment.value = this.inputInternet;
                this.inputInternet = "";
                this.$modal.hide("input-internet");
            },
            cancelCloseInputInternetModal: function(event) {
                // インターネット定型入力画面のキャンセルの処理
                this.inputInternet = "";
                this.$modal.hide("input-internet");
            },
            openInputCancelNoticeModal: function(event) {
                // 解約通知定型入力モーダル画面を開く
                this.reloadInputCancelNotices();
                this.$modal.show("input-cancel-notice");
            },
            okCloseInputCancelNoticeModal: function(event) {
                // 解約通知定型入力画面のOKの処理
                this.$refs.vacancy_cancel_notice_comment.value = this.inputCancelNotice;
                this.inputCancelNotice = "";
                this.$modal.hide("input-cancel-notice");
            },
            cancelCloseInputCancelNoticeModal: function(event) {
                // 解約通知定型入力画面のキャンセルの処理
                this.inputCancelNotice = "";
                this.$modal.hide("input-cancel-notice");
            },
            openInputShortCancelModal: function(event) {
                // 短期解約定型入力モーダル画面を開く
                this.reloadInputShortCancels();
                this.$modal.show("input-short-cancel");
            },
            okCloseInputShortCancelModal: function(event) {
                // 短期解約定型入力画面のOKの処理
                this.$refs.vacancy_short_cancel_comment.value = this.inputShortCancel;
                this.inputShortCancel = "";
                this.$modal.hide("input-short-cancel");
            },
            cancelCloseInputShortCancelModal: function(event) {
                // 短期解約定型入力画面のキャンセルの処理
                this.inputShortCancel = "";
                this.$modal.hide("input-short-cancel");
            },
            openInputPaymentModal: function(event) {
                // 賃料支払い定型入力モーダル画面を開く
                this.reloadInputPayments();
                this.$modal.show("input-payment");
            },
            okCloseInputPaymentModal: function(event) {
                // 賃料支払い定型入力画面のOKの処理
                this.$refs.vacancy_payment_comment.value = this.inputPayment;
                this.inputPayment = "";
                this.$modal.hide("input-payment");
            },
            cancelCloseInputPaymentModal: function(event) {
                // 賃料支払い定型入力画面のキャンセルの処理
                this.inputPayment = "";
                this.$modal.hide("input-payment");
            },
            openInputGuaranteeModal: function(event) {
                // 保証会社定型入力モーダル画面を開く
                this.reloadInputGuarantees();
                this.$modal.show("input-guarantee");
            },
            okCloseInputGuaranteeModal: function(event) {
                // 保証会社定型入力画面のOKの処理
                this.$refs.vacancy_guarantee_comment.value = this.inputGuarantee;
                this.inputGuarantee = "";
                this.$modal.hide("input-guarantee");
            },
            cancelCloseInputGuaranteeModal: function(event) {
                // 保証会社定型入力画面のキャンセルの処理
                this.inputGuarantee = "";
                this.$modal.hide("input-guarantee");
            },
            openInputInsuranceModal: function(event) {
                // 火災保険定型入力モーダル画面を開く
                this.reloadInputInsurances();
                this.$modal.show("input-insurance");
            },
            okCloseInputInsuranceModal: function(event) {
                // 火災保険定型入力画面のOKの処理
                this.$refs.vacancy_insurance_comment.value = this.inputInsurance;
                this.inputInsurance = "";
                this.$modal.hide("input-insurance");
            },
            cancelCloseInputInsuranceModal: function(event) {
                // 火災保険定型入力画面のキャンセルの処理
                this.inputInsurance = "";
                this.$modal.hide("input-insurance");
            },
            openInputGuarantorLimitModal: function(event) {
                // 保証人極度額定型入力モーダル画面を開く
                this.reloadInputGuarantorLimits();
                this.$modal.show("input-guarantor-limit");
            },
            okCloseInputGuarantorLimitModal: function(event) {
                // 保証人極度額定型入力画面のOKの処理
                this.$refs.vacancy_guarantor_limit_comment.value = this.inputGuarantorLimit;
                this.inputGuarantorLimit = "";
                this.$modal.hide("input-guarantor-limit");
            },
            cancelCloseInputGuarantorLimitModal: function(event) {
                // 保証人極度額定型入力画面のキャンセルの処理
                this.inputGuarantorLimit = "";
                this.$modal.hide("input-guarantor-limit");
            },
            openInputDocumentPriceModal: function(event) {
                // 入居時書類代定型入力モーダル画面を開く
                this.reloadInputDocumentPrices();
                this.$modal.show("input-document-price");
            },
            okCloseInputDocumentPriceModal: function(event) {
                // 入居時書類代定型入力画面のOKの処理
                this.$refs.vacancy_document_price_comment.value = this.inputDocumentPrice;
                this.inputDocumentPrice = "";
                this.$modal.hide("input-document-price");
            },
            cancelCloseInputDocumentPriceModal: function(event) {
                // 入居時書類代定型入力画面のキャンセルの処理
                this.inputDocumentPrice = "";
                this.$modal.hide("input-document-price");
            },
            openInputRenewalChargeModal: function(event) {
                // 更新事務手数料定型入力モーダル画面を開く
                this.reloadInputRenewalCharges();
                this.$modal.show("input-renewal-charge");
            },
            okCloseInputRenewalChargeModal: function(event) {
                // 更新事務手数料定型入力画面のOKの処理
                this.$refs.vacancy_renewal_charge_comment.value = this.inputRenewalCharge;
                this.inputRenewalCharge = "";
                this.$modal.hide("input-renewal-charge");
            },
            cancelCloseInputRenewalChargeModal: function(event) {
                // 更新事務手数料定型入力画面のキャンセルの処理
                this.inputRenewalCharge = "";
                this.$modal.hide("input-renewal-charge");
            },
            openInputGarageModal: function(event) {
                // 駐車場定型入力モーダル画面を開く
                this.reloadInputGarages();
                this.$modal.show("input-garage");
            },
            okCloseInputGarageModal: function(event) {
                // 駐車場定型入力画面のOKの処理
                this.$refs.vacancy_garage_comment.value = this.inputGarage;
                this.inputGarage = "";
                this.$modal.hide("input-garage");
            },
            cancelCloseInputGarageModal: function(event) {
                // 駐車場定型入力画面のキャンセルの処理
                this.inputGarage = "";
                this.$modal.hide("input-garage");
            },
            openInputBikeParkingModal: function(event) {
                // 駐輪場定型入力モーダル画面を開く
                this.reloadInputBikeParkings();
                this.$modal.show("input-bike-parking");
            },
            okCloseInputBikeParkingModal: function(event) {
                // 駐輪場定型入力画面のOKの処理
                this.$refs.vacancy_bike_parking_comment.value = this.inputBikeParking;
                this.inputBikeParking = "";
                this.$modal.hide("input-bike-parking");
            },
            cancelCloseInputBikeParkingModal: function(event) {
                // 駐輪場定型入力画面のキャンセルの処理
                this.inputBikeParking = "";
                this.$modal.hide("input-bike-parking");
            },
            openInputCleaningModal: function(event) {
                // 退去時清掃定型入力モーダル画面を開く
                this.reloadInputCleanings();
                this.$modal.show("input-cleaning");
            },
            okCloseInputCleaningModal: function(event) {
                // 退去時清掃定型入力画面のOKの処理
                this.$refs.vacancy_cleaning_comment.value = this.inputCleaning;
                this.inputCleaning = "";
                this.$modal.hide("input-cleaning");
            },
            cancelCloseInputCleaningModal: function(event) {
                // 退去時清掃定型入力画面のキャンセルの処理
                this.inputCleaning = "";
                this.$modal.hide("input-cleaning");
            },
            openInputChangeLockModal: function(event) {
                // 鍵交換定型入力モーダル画面を開く
                this.reloadInputChangeLocks();
                this.$modal.show("input-change-lock");
            },
            okCloseInputChangeLockModal: function(event) {
                // 鍵交換定型入力画面のOKの処理
                this.$refs.vacancy_change_lock_comment.value = this.inputChangeLock;
                this.inputChangeLock = "";
                this.$modal.hide("input-change-lock");
            },
            cancelCloseInputChangeLockModal: function(event) {
                // 鍵交換定型入力画面のキャンセルの処理
                this.inputChangeLock = "";
                this.$modal.hide("input-change-lock");
            },
            openInputPortalModal: function(event) {
                // ポータル掲載定型入力モーダル画面を開く
                this.reloadInputPortals();
                this.$modal.show("input-portal");
            },
            okCloseInputPortalModal: function(event) {
                // ポータル掲載定型入力画面のOKの処理
                this.$refs.vacancy_portal_note.value = this.inputPortal;
                this.inputPortal = "";
                this.$modal.hide("input-portal");
            },
            cancelCloseInputPortalModal: function(event) {
                // ポータル掲載定型入力画面のキャンセルの処理
                this.inputPortal = "";
                this.$modal.hide("input-portal");
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
            reloadCities: function() {
                // 市区町村のリストを書き換える。
                if(this.pref !== 0 && this.pref !== "") {
                    let that = this;
                    axios.get("/api/cities/" + this.key + "/" + this.pref)
                        .then(function(res) {
                            let items = res.data;
                            that.reloadSelectOptions(that.$refs.city, items, that.city)
                        })
                        .catch(function (error) {
                            alert("市区町村データの取得に失敗しました。");
                        });
                }
            },
            reloadAreas: function() {
                // エリアのリストを書き換える。
                if(this.city !== 0 && this.city !== "") {
                    let that = this;
                    axios.get("/api/areas/" + this.key + "/" + this.city)
                        .then(function(res) {
                            let items = res.data;
                            that.reloadSelectOptions(that.$refs.area, items, that.area)
                        })
                        .catch(function (error) {
                            alert("エリアデータの取得に失敗しました。");
                        });
                }
            },
            reloadElementarySchools: function() {
                // 小学校区のリストを書き換える。
                if(this.city !== 0 && this.city !== "") {
                    let that = this;
                    axios.get("/api/elementary_schools/" + this.key + "/" + this.city)
                        .then(function(res) {
                            let items = res.data;
                            that.reloadSelectOptions(that.$refs.elementary_school, items, that.elementarySchool)
                        })
                        .catch(function (error) {
                            alert("小学校区データの取得に失敗しました。");
                        });
                }
            },
            reloadJuniorHighSchools: function() {
                // 中学校区のリストを書き換える。
                if(this.city !== 0 && this.city !== "") {
                    let that = this;
                    axios.get("/api/junior_high_schools/" + this.key + "/" + this.city)
                        .then(function(res) {
                            let items = res.data;
                            that.reloadSelectOptions(that.$refs.junior_high_school, items, that.juniorHighSchool)
                        })
                        .catch(function (error) {
                            alert("中学校区データの取得に失敗しました。");
                        });
                }
            },
            reloadStations: function(elm, railway, station) {
                // 駅リスト書き換え用の内部メソッド
                if(railway !== 0) {
                    let that = this;
                    axios.get("/api/stations/" + this.key + "/" + railway)
                        .then(function(res) {
                            let items = res.data;
                            that.reloadSelectOptions(elm, items, station)
                        })
                        .catch(function (error) {
                            alert("駅データの取得に失敗しました。");
                        });
                }
            },
            reloadStations1: function() {
                // 駅1のリストを書き換える。
                this.reloadStations(this.$refs.station1, this.railway1,this.station1);
            },
            reloadStations2: function() {
                // 駅2のリストを書き換える。
                this.reloadStations(this.$refs.station2, this.railway2,this.station2);
            },
            reloadStations3: function() {
                // 駅3のリストを書き換える。
                this.reloadStations(this.$refs.station3, this.railway3,this.station3);
            },
            reloadDepartments : function() {
                // 管理部署選択用リストを書き換える。
                let that = this;

                let url = "/api/departments/" + this.key;

                axios.get(url)
                    .then(function(res) {
                        that.selectDepartments = res.data;
                    })
                    .catch(function (error) {
                        alert("管理部署データの取得に失敗しました。");
                    });
            },
            reloadAgencyDepartments : function() {
                // 仲介部署選択用リストを書き換える。
                let that = this;

                let url = "/api/departments/" + this.key;

                axios.get(url)
                    .then(function(res) {
                        that.selectAgencyDepartments = res.data;
                    })
                    .catch(function (error) {
                        alert("仲介部署データの取得に失敗しました。");
                    });
            },
            reloadStaffs1 : function() {
                // スタッフ1選択用リストを書き換える。
                let that = this;

                let url = "/api/staffs/" + this.key;
                if (this.selectStaffHint1) {
                    let hint = this.selectStaffHint1.trim();
                    if (hint !== "") url += "/" + encodeURI(hint);
                }

                axios.get(url)
                    .then(function(res) {
                        that.selectStaffs1 = res.data;
                    })
                    .catch(function (error) {
                        alert("スタッフ1データの取得に失敗しました。");
                    });
            },
            reloadStaffs2 : function() {
                // スタッフ2選択用リストを書き換える。
                let that = this;

                let url = "/api/staffs/" + this.key;
                if (this.selectStaffHint2) {
                    let hint = this.selectStaffHint2.trim();
                    if (hint !== "") url += "/" + encodeURI(hint);
                }

                axios.get(url)
                    .then(function(res) {
                        that.selectStaffs2 = res.data;
                    })
                    .catch(function (error) {
                        alert("スタッフ2データの取得に失敗しました。");
                    });
            },
            reloadOwners : function() {
                // オーナー選択用リストを書き換える。
                let that = this;

                let url = "/api/owners/" + this.key;
                if (this.selectOwnerHint) {
                    let hint = this.selectOwnerHint.trim();
                    if (hint !== "") url += "/" + encodeURI(hint);
                }

                axios.get(url)
                    .then(function(res) {
                        that.selectOwners = res.data;
                    })
                    .catch(function (error) {
                        alert("オーナーデータの取得に失敗しました。");
                    });
            },
            reloadTraders : function() {
                // 賃貸管理業者選択用リストを書き換える。
                let that = this;

                let url = "/api/traders/" + this.key;
                if (this.selectTraderHint) {
                    let hint = this.selectTraderHint.trim();
                    if (hint !== "") url += "/" + encodeURI(hint);
                }

                axios.get(url)
                    .then(function(res) {
                        that.selectTraders = res.data;
                    })
                    .catch(function (error) {
                        alert("賃貸管理業者データの取得に失敗しました。");
                    });
            },
            reloadInputWaters : function() {
                // 水道費定型入力用リストを書き換える。
                let that = this;

                let url = "/api/vacancy_input_waters/" + this.key;

                axios.get(url)
                    .then(function(res) {
                        that.inputWaters = res.data;
                    })
                    .catch(function (error) {
                        alert("水道費定型入力データの取得に失敗しました。");
                    });
            },
            reloadInputElectrics : function() {
                // 電気定型入力用リストを書き換える。
                let that = this;

                let url = "/api/vacancy_input_electrics/" + this.key;

                axios.get(url)
                    .then(function(res) {
                        that.inputElectrics = res.data;
                    })
                    .catch(function (error) {
                        alert("電気定型入力データの取得に失敗しました。");
                    });
            },
            reloadInputGases : function() {
                // ガス定型入力用リストを書き換える。
                let that = this;

                let url = "/api/vacancy_input_gases/" + this.key;

                axios.get(url)
                    .then(function(res) {
                        that.inputGases = res.data;
                    })
                    .catch(function (error) {
                        alert("ガス定型入力データの取得に失敗しました。");
                    });
            },
            reloadInputInternets : function() {
                // インターネット定型入力用リストを書き換える。
                let that = this;

                let url = "/api/vacancy_input_internets/" + this.key;

                axios.get(url)
                    .then(function(res) {
                        that.inputInternets = res.data;
                    })
                    .catch(function (error) {
                        alert("インターネット定型入力データの取得に失敗しました。");
                    });
            },
            reloadInputCancelNotices : function() {
                // 解約通知定型入力用リストを書き換える。
                let that = this;

                let url = "/api/vacancy_input_cancel_notices/" + this.key;

                axios.get(url)
                    .then(function(res) {
                        that.inputCancelNotices = res.data;
                    })
                    .catch(function (error) {
                        alert("解約通知定型入力データの取得に失敗しました。");
                    });
            },
            reloadInputShortCancels : function() {
                // 短期解約定型入力用リストを書き換える。
                let that = this;

                let url = "/api/vacancy_input_short_cancels/" + this.key;

                axios.get(url)
                    .then(function(res) {
                        that.inputShortCancels = res.data;
                    })
                    .catch(function (error) {
                        alert("短期解約定型入力データの取得に失敗しました。");
                    });
            },
            reloadInputPayments : function() {
                // 賃料支払い定型入力用リストを書き換える。
                let that = this;

                let url = "/api/vacancy_input_payments/" + this.key;

                axios.get(url)
                    .then(function(res) {
                        that.inputPayments = res.data;
                    })
                    .catch(function (error) {
                        alert("賃料支払い定型入力データの取得に失敗しました。");
                    });
            },
            reloadInputGuarantees : function() {
                // 保証会社定型入力用リストを書き換える。
                let that = this;

                let url = "/api/vacancy_input_guarantees/" + this.key;

                axios.get(url)
                    .then(function(res) {
                        that.inputGuarantees = res.data;
                    })
                    .catch(function (error) {
                        alert("保証会社定型入力データの取得に失敗しました。");
                    });
            },
            reloadInputInsurances : function() {
                // 火災保険定型入力用リストを書き換える。
                let that = this;

                let url = "/api/vacancy_input_insurances/" + this.key;

                axios.get(url)
                    .then(function(res) {
                        that.inputInsurances = res.data;
                    })
                    .catch(function (error) {
                        alert("火災保険定型入力データの取得に失敗しました。");
                    });
            },
            reloadInputGuarantorLimits : function() {
                // 保証人極度額定型入力用リストを書き換える。
                let that = this;

                let url = "/api/vacancy_input_guarantor_limits/" + this.key;

                axios.get(url)
                    .then(function(res) {
                        that.inputGuarantorLimits = res.data;
                    })
                    .catch(function (error) {
                        alert("保証人極度額定型入力データの取得に失敗しました。");
                    });
            },
            reloadInputDocumentPrices : function() {
                // 入居時書類代定型入力用リストを書き換える。
                let that = this;

                let url = "/api/vacancy_input_document_prices/" + this.key;

                axios.get(url)
                    .then(function(res) {
                        that.inputDocumentPrices = res.data;
                    })
                    .catch(function (error) {
                        alert("入居時書類代定型入力データの取得に失敗しました。");
                    });
            },
            reloadInputRenewalCharges : function() {
                // 更新事務手数料定型入力用リストを書き換える。
                let that = this;

                let url = "/api/vacancy_input_renewal_charges/" + this.key;

                axios.get(url)
                    .then(function(res) {
                        that.inputRenewalCharges = res.data;
                    })
                    .catch(function (error) {
                        alert("更新事務手数料定型入力データの取得に失敗しました。");
                    });
            },
            reloadInputGarages : function() {
                // 駐車場定型入力用リストを書き換える。
                let that = this;

                let url = "/api/vacancy_input_garages/" + this.key;

                axios.get(url)
                    .then(function(res) {
                        that.inputGarages = res.data;
                    })
                    .catch(function (error) {
                        alert("駐車場定型入力データの取得に失敗しました。");
                    });
            },
            reloadInputBikeParkings : function() {
                // 駐輪場定型入力用リストを書き換える。
                let that = this;

                let url = "/api/vacancy_input_bike_parkings/" + this.key;

                axios.get(url)
                    .then(function(res) {
                        that.inputBikeParkings = res.data;
                    })
                    .catch(function (error) {
                        alert("駐輪場定型入力データの取得に失敗しました。");
                    });
            },
            reloadInputCleanings : function() {
                // 退去時清掃定型入力用リストを書き換える。
                let that = this;

                let url = "/api/vacancy_input_cleanings/" + this.key;

                axios.get(url)
                    .then(function(res) {
                        that.inputCleanings = res.data;
                    })
                    .catch(function (error) {
                        alert("退去時清掃定型入力データの取得に失敗しました。");
                    });
            },
            reloadInputChangeLocks : function() {
                // 鍵交換定型入力用リストを書き換える。
                let that = this;

                let url = "/api/vacancy_input_change_locks/" + this.key;

                axios.get(url)
                    .then(function(res) {
                        that.inputChangeLocks = res.data;
                    })
                    .catch(function (error) {
                        alert("鍵交換定型入力データの取得に失敗しました。");
                    });
            },
            reloadInputPortals : function() {
                // ポータル掲載定型入力用リストを書き換える。
                let that = this;

                let url = "/api/vacancy_input_portals/" + this.key;

                axios.get(url)
                    .then(function(res) {
                        that.inputPortals = res.data;
                    })
                    .catch(function (error) {
                        alert("ポータル掲載定型入力データの取得に失敗しました。");
                    });
            },
        },
    });
}
