"""
System Name: Vasyworks
Project Name: vacancy_mgr
Encoding: UTF-8
Copyright (C) 2020 Yasuhiro Yamamoto
"""
import uuid
from django.conf import settings
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_text
from django.utils import timezone
from .convert import *
from users.models import User
from property.models import Room, RoomPicture, RoomEquipment


class RoomCopyHelper:
    """部屋データコピーヘルパークラス"""

    @staticmethod
    def copy_room_data(
            source: Room,
            destination_room: Room,
            user: User,
            all=False,
            base=False,
            vacancy=False,
            web=False,
            layout=False,
            monthly_cost=False,
            initial_cost=False,
            renewal_cost=False,
            features=False,
    ):
        """部屋データのコピー"""
        is_changed = False

        if all or base:
            destination_room.room_auth_level = source.room_auth_level
            destination_room.rental_type = source.rental_type
            destination_room.is_sublease = source.is_sublease
            destination_room.is_condo_management = source.is_condo_management
            destination_room.is_entrusted = source.is_entrusted
            destination_room.room_area = source.room_area
            destination_room.direction = source.direction
            destination_room.balcony_type = source.balcony_type
            destination_room.balcony_area = source.balcony_area
            destination_room.contract_years = source.contract_years
            destination_room.contract_months = source.contract_months
            destination_room.is_auto_renewal = source.is_auto_renewal
            destination_room.free_rent_type = source.free_rent_type
            destination_room.free_rent_months = source.free_rent_months
            destination_room.free_rent_limit_year = source.free_rent_limit_year
            destination_room.free_rent_limit_month = source.free_rent_limit_month
            destination_room.cancel_notice_limit = source.cancel_notice_limit
            destination_room.cancel_note = source.cancel_note
            destination_room.short_cancel_note = source.short_cancel_note
            destination_room.cleaning_type = source.cleaning_type
            destination_room.cleaning_cost = source.cleaning_cost
            destination_room.cleaning_cost_tax_type = source.cleaning_cost_tax_type
            destination_room.cleaning_note = source.cleaning_note
            destination_room.special_agreement = source.special_agreement
            destination_room.trader_publish_type = source.trader_publish_type
            destination_room.trader_publish_note = source.trader_publish_note
            destination_room.trader_portal_type = source.trader_portal_type
            destination_room.trader_portal_note = source.trader_portal_note
            destination_room.ad_type = source.ad_type
            destination_room.ad_value = source.ad_value
            destination_room.ad_tax_type = source.ad_tax_type
            destination_room.trader_ad_type = source.trader_ad_type
            destination_room.trader_ad_value = source.trader_ad_value
            destination_room.trader_ad_tax_type = source.trader_ad_tax_type
            destination_room.owner_fee_type = source.owner_fee_type
            destination_room.key_place_note = source.key_place_note
            destination_room.private_note = source.private_note
            destination_room.management_note = source.management_note
            is_changed = True

        if all or vacancy:
            destination_room.is_publish_vacancy = source.is_publish_vacancy
            destination_room.vacancy_catch_copy = source.vacancy_catch_copy
            destination_room.vacancy_appeal = source.vacancy_appeal
            destination_room.vacancy_note = source.vacancy_note
            is_changed = True

        if all or web:
            destination_room.is_publish_web = source.is_publish_web
            destination_room.web_catch_copy = source.web_catch_copy
            destination_room.web_appeal = source.web_appeal
            destination_room.web_note = source.web_note
            is_changed = True

        if all or layout:
            destination_room.layout_type = source.layout_type
            destination_room.western_style_room1 = source.western_style_room1
            destination_room.western_style_room2 = source.western_style_room2
            destination_room.western_style_room3 = source.western_style_room3
            destination_room.western_style_room4 = source.western_style_room4
            destination_room.western_style_room5 = source.western_style_room5
            destination_room.western_style_room6 = source.western_style_room6
            destination_room.western_style_room7 = source.western_style_room7
            destination_room.western_style_room8 = source.western_style_room8
            destination_room.western_style_room9 = source.western_style_room9
            destination_room.western_style_room10 = source.western_style_room10
            destination_room.japanese_style_room1 = source.japanese_style_room1
            destination_room.japanese_style_room2 = source.japanese_style_room2
            destination_room.japanese_style_room3 = source.japanese_style_room3
            destination_room.japanese_style_room4 = source.japanese_style_room4
            destination_room.japanese_style_room5 = source.japanese_style_room5
            destination_room.japanese_style_room6 = source.japanese_style_room6
            destination_room.japanese_style_room7 = source.japanese_style_room7
            destination_room.japanese_style_room8 = source.japanese_style_room8
            destination_room.japanese_style_room9 = source.japanese_style_room9
            destination_room.japanese_style_room10 = source.japanese_style_room10
            destination_room.kitchen_type1 = source.kitchen_type1
            destination_room.kitchen1 = source.kitchen1
            destination_room.kitchen_type2 = source.kitchen_type2
            destination_room.kitchen2 = source.kitchen2
            destination_room.kitchen_type3 = source.kitchen_type3
            destination_room.kitchen3 = source.kitchen3
            destination_room.store_room1 = source.store_room1
            destination_room.store_room2 = source.store_room2
            destination_room.store_room3 = source.store_room3
            destination_room.loft1 = source.loft1
            destination_room.loft2 = source.loft2
            destination_room.sun_room1 = source.sun_room1
            destination_room.sun_room2 = source.sun_room2
            destination_room.layout_note = source.layout_note
            is_changed = True

        if all or monthly_cost:
            destination_room.rent = source.rent
            destination_room.rent_upper = source.rent_upper
            destination_room.trader_rent = source.trader_rent
            destination_room.rent_tax_type = source.rent_tax_type
            destination_room.rent_hidden = source.rent_hidden
            destination_room.condo_fees_type = source.condo_fees_type
            destination_room.condo_fees = source.condo_fees
            destination_room.condo_fees_tax_type = source.condo_fees_tax_type
            destination_room.water_cost_type = source.water_cost_type
            destination_room.water_cost = source.water_cost
            destination_room.water_check_type = source.water_check_type
            destination_room.payment_type = source.payment_type
            destination_room.payment_fee_type = source.payment_fee_type
            destination_room.payment_fee = source.payment_fee
            destination_room.payment_fee_tax_type = source.payment_fee_tax_type
            destination_room.monthly_cost_name1 = source.monthly_cost_name1
            destination_room.monthly_cost1 = source.monthly_cost1
            destination_room.monthly_cost_tax_type1 = source.monthly_cost_tax_type1
            destination_room.monthly_cost_name2 = source.monthly_cost_name2
            destination_room.monthly_cost2 = source.monthly_cost2
            destination_room.monthly_cost_tax_type2 = source.monthly_cost_tax_type2
            destination_room.monthly_cost_name3 = source.monthly_cost_name3
            destination_room.monthly_cost3 = source.monthly_cost3
            destination_room.monthly_cost_tax_type3 = source.monthly_cost_tax_type3
            destination_room.monthly_cost_name4 = source.monthly_cost_name4
            destination_room.monthly_cost4 = source.monthly_cost4
            destination_room.monthly_cost_tax_type4 = source.monthly_cost_tax_type4
            destination_room.monthly_cost_name5 = source.monthly_cost_name5
            destination_room.monthly_cost5 = source.monthly_cost5
            destination_room.monthly_cost_tax_type5 = source.monthly_cost_tax_type5
            destination_room.monthly_cost_name6 = source.monthly_cost_name6
            destination_room.monthly_cost6 = source.monthly_cost6
            destination_room.monthly_cost_tax_type6 = source.monthly_cost_tax_type6
            destination_room.monthly_cost_name7 = source.monthly_cost_name7
            destination_room.monthly_cost7 = source.monthly_cost7
            destination_room.monthly_cost_tax_type7 = source.monthly_cost_tax_type7
            destination_room.monthly_cost_name8 = source.monthly_cost_name8
            destination_room.monthly_cost8 = source.monthly_cost8
            destination_room.monthly_cost_tax_type8 = source.monthly_cost_tax_type8
            destination_room.monthly_cost_name9 = source.monthly_cost_name9
            destination_room.monthly_cost9 = source.monthly_cost9
            destination_room.monthly_cost_tax_type9 = source.monthly_cost_tax_type9
            destination_room.monthly_cost_name10 = source.monthly_cost_name10
            destination_room.monthly_cost10 = source.monthly_cost10
            destination_room.monthly_cost_tax_type10 = source.monthly_cost_tax_type10
            destination_room.monthly_cost_note = source.monthly_cost_note
            is_changed = True

        if all or initial_cost:
            destination_room.deposit_type1 = source.deposit_type1
            destination_room.deposit_notation1 = source.deposit_notation1
            destination_room.deposit_value1 = source.deposit_value1
            destination_room.deposit_tax_type1 = source.deposit_tax_type1
            destination_room.deposit_comment1 = source.deposit_comment1
            destination_room.deposit_type2 = source.deposit_type2
            destination_room.deposit_notation2 = source.deposit_notation2
            destination_room.deposit_value2 = source.deposit_value2
            destination_room.deposit_tax_type2 = source.deposit_tax_type2
            destination_room.deposit_comment2 = source.deposit_comment2
            destination_room.key_money_type1 = source.key_money_type1
            destination_room.key_money_notation1 = source.key_money_notation1
            destination_room.key_money_value1 = source.key_money_value1
            destination_room.key_money_tax_type1 = source.key_money_tax_type1
            destination_room.key_money_comment1 = source.key_money_comment1
            destination_room.key_money_type2 = source.key_money_type2
            destination_room.key_money_notation2 = source.key_money_notation2
            destination_room.key_money_value2 = source.key_money_value2
            destination_room.key_money_tax_type2 = source.key_money_tax_type2
            destination_room.key_money_comment2 = source.key_money_comment2
            destination_room.insurance_type = source.insurance_type
            destination_room.insurance_company = source.insurance_company
            destination_room.insurance_years = source.insurance_years
            destination_room.insurance_fee = source.insurance_fee
            destination_room.insurance_fee_tax_type = source.insurance_fee_tax_type
            destination_room.guarantee_type = source.guarantee_type
            destination_room.guarantee_company = source.guarantee_company
            destination_room.guarantee_fee = source.guarantee_fee
            destination_room.document_cost_existence = source.document_cost_existence
            destination_room.document_cost = source.document_cost
            destination_room.document_cost_tax_type = source.document_cost_tax_type
            destination_room.document_cost_comment = source.document_cost_comment
            destination_room.key_change_cost_existence = source.key_change_cost_existence
            destination_room.key_change_cost = source.key_change_cost
            destination_room.key_change_cost_tax_type = source.key_change_cost_tax_type
            destination_room.key_change_comment = source.key_change_comment
            destination_room.initial_cost_name1 = source.initial_cost_name1
            destination_room.initial_cost1 = source.initial_cost1
            destination_room.initial_cost_tax_type1 = source.initial_cost_tax_type1
            destination_room.initial_cost_name2 = source.initial_cost_name2
            destination_room.initial_cost2 = source.initial_cost2
            destination_room.initial_cost_tax_type2 = source.initial_cost_tax_type2
            destination_room.initial_cost_name3 = source.initial_cost_name3
            destination_room.initial_cost3 = source.initial_cost3
            destination_room.initial_cost_tax_type3 = source.initial_cost_tax_type3
            destination_room.initial_cost_name4 = source.initial_cost_name4
            destination_room.initial_cost4 = source.initial_cost4
            destination_room.initial_cost_tax_type4 = source.initial_cost_tax_type4
            destination_room.initial_cost_name5 = source.initial_cost_name5
            destination_room.initial_cost5 = source.initial_cost5
            destination_room.initial_cost_tax_type5 = source.initial_cost_tax_type5
            destination_room.initial_cost_name6 = source.initial_cost_name6
            destination_room.initial_cost6 = source.initial_cost6
            destination_room.initial_cost_tax_type6 = source.initial_cost_tax_type6
            destination_room.initial_cost_name7 = source.initial_cost_name7
            destination_room.initial_cost7 = source.initial_cost7
            destination_room.initial_cost_tax_type7 = source.initial_cost_tax_type7
            destination_room.initial_cost_name8 = source.initial_cost_name8
            destination_room.initial_cost8 = source.initial_cost8
            destination_room.initial_cost_tax_type8 = source.initial_cost_tax_type8
            destination_room.initial_cost_name9 = source.initial_cost_name9
            destination_room.initial_cost9 = source.initial_cost9
            destination_room.initial_cost_tax_type9 = source.initial_cost_tax_type9
            destination_room.initial_cost_name10 = source.initial_cost_name10
            destination_room.initial_cost10 = source.initial_cost10
            destination_room.initial_cost_tax_type10 = source.initial_cost_tax_type10
            destination_room.initial_cost_note = source.initial_cost_note
            is_changed = True

        if all or renewal_cost:
            destination_room.renewal_fee_notation = source.renewal_fee_notation
            destination_room.renewal_fee_value = source.renewal_fee_value
            destination_room.renewal_fee_tax_type = source.renewal_fee_tax_type
            destination_room.renewal_charge_existence = source.renewal_charge_existence
            destination_room.renewal_charge = source.renewal_charge
            destination_room.renewal_charge_tax_type = source.renewal_charge_tax_type
            destination_room.renewal_note = source.renewal_note
            destination_room.recontract_fee_existence = source.recontract_fee_existence
            destination_room.recontract_fee = source.recontract_fee
            destination_room.recontract_fee_tax_type = source.recontract_fee_tax_type
            destination_room.recontract_note = source.recontract_note
            is_changed = True

        if all or features:
            destination_room.electric_type = source.electric_type
            destination_room.electric_comment = source.electric_comment
            destination_room.gas_type = source.gas_type
            destination_room.gas_comment = source.gas_comment
            destination_room.bath_type = source.bath_type
            destination_room.bath_comment = source.bath_comment
            destination_room.toilet_type = source.toilet_type
            destination_room.toilet_comment = source.toilet_comment
            destination_room.kitchen_range_type = source.kitchen_range_type
            destination_room.kitchen_range_comment = source.kitchen_range_comment
            destination_room.internet_type = source.internet_type
            destination_room.internet_comment = source.internet_comment
            destination_room.washer_type = source.washer_type
            destination_room.washer_comment = source.washer_comment
            destination_room.pet_type = source.pet_type
            destination_room.pet_comment = source.pet_comment
            destination_room.instrument_type = source.instrument_type
            destination_room.live_together_type = source.live_together_type
            destination_room.children_type = source.children_type
            destination_room.share_type = source.share_type
            destination_room.non_japanese_type = source.non_japanese_type
            destination_room.only_woman_type = source.only_woman_type
            destination_room.only_man_type = source.only_man_type
            destination_room.corp_contract_type = source.corp_contract_type
            destination_room.student_type = source.student_type
            destination_room.new_student_type = source.new_student_type
            destination_room.welfare_type = source.welfare_type
            destination_room.office_use_type = source.office_use_type
            destination_room.constraint_note = source.constraint_note
            is_changed = True

        if is_changed:
            destination_room.created_at = timezone.now()
            destination_room.created_user = user
            destination_room.updated_at = timezone.now()
            destination_room.updated_user = user

            destination_room.save()

    @staticmethod
    def copy_room_equipments(source_room: Room, destination_room: Room, user: User):
        """部屋設備のコピー"""
        if settings.DEMO:
            return

        if source_room and destination_room:
            source_equipments = RoomEquipment.objects.filter(
                room=source_room,
                is_deleted=False,
            ).order_by('priority', 'equipment__category__priority', 'equipment__priority', 'id').all()

            destination_equipments = RoomEquipment.objects.filter(
                room=destination_room,
            ).order_by('priority', 'equipment__category__priority', 'equipment__priority', 'id').all()

            for item in destination_equipments:
                # 一旦、登録済み設備を全て削除
                item.is_deleted = True
                item.updated_at = timezone.now()
                item.updated_user = user
                item.save()

            for source in source_equipments:
                is_exists = False
                for item in destination_equipments:
                    if item.equipment.id == source.equipment.id:
                        # 既に登録済みなら追加しない
                        is_exists = True
                        # 削除されているデータを復活させる
                        item.is_deleted = False
                        item.is_remained = source.is_remained
                        item.note = source.note
                        item.priority = source.priority
                        item.updated_at = timezone.now()
                        item.updated_user = user
                        item.save()

                        break

                if not is_exists:
                    data = RoomEquipment()
                    data.equipment = source.equipment
                    data.is_remained = source.is_remained
                    data.priority = source.priority
                    data.note = source.note
                    data.room = destination_room
                    data.building = destination_room.building

                    data.created_at = timezone.now()
                    data.created_user = user
                    data.updated_at = timezone.now()
                    data.updated_user = user

                    data.save()

    @staticmethod
    def copy_room_pictures(picture_ids, destination_room: Room, user: User):
        """部屋画像のコピー"""
        if settings.DEMO:
            return

        room_pictures = RoomPicture.objects.filter(
            room=destination_room,
        ).all()

        for picture_id in picture_ids:
            source = RoomPicture.objects.get(pk=picture_id)
            if source:
                is_exists = False
                for item in room_pictures:
                    if item.file_name == source.file_name:
                        # 既に登録済みなら追加しない
                        is_exists = True
                        if item.is_deleted:
                            # 削除されている場合は復活させる
                            item.is_deleted = False
                            item.picture_type = source.picture_type
                            item.is_publish_vacancy = source.is_publish_vacancy
                            item.is_publish_web = source.is_publish_web
                            item.comment = source.comment
                            item.note = source.note
                            item.updated_at = timezone.now()
                            item.updated_user = user
                            item.save()

                        break

                if not is_exists:
                    data = RoomPicture()
                    data.file_name = source.file_name
                    data.cache_name_thumb = source.cache_name_thumb
                    data.cache_name_s = source.cache_name_s
                    data.cache_name_m = source.cache_name_m
                    data.cache_name_l = source.cache_name_l
                    data.cache_name_org = source.cache_name_org
                    data.picture_type = source.picture_type
                    data.is_publish_vacancy = source.is_publish_vacancy
                    data.is_publish_web = source.is_publish_web
                    data.comment = source.comment
                    data.note = source.note
                    data.room = destination_room
                    data.building = destination_room.building

                    data.created_at = timezone.now()
                    data.created_user = user
                    data.updated_at = timezone.now()
                    data.updated_user = user

                    data.save()
