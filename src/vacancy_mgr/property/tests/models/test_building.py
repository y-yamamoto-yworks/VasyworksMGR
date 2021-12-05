"""
System Name: Vasyworks
Project Name: vacancy_mgr
Encoding: UTF-8
Copyright (C) 2020 Yasuhiro Yamamoto
"""
from unittest import TestCase
from django.db import transaction
from property.models import Building
import warnings


class BuildingModelTest(TestCase):
    """
    建物モデルのテスト
    """
    def setUp(self):
        warnings.simplefilter('ignore')
        self.building = Building.objects.get(pk=2)      # 表示項目確認用マンション

        if transaction.get_autocommit():
            transaction.set_autocommit(False)

    def tearDown(self):
        transaction.rollback()

    def test_building_address(self):
        self.assertEqual(self.building.address, '京都府京都市上京区住所町域DEMO町番地DEMOデータ A棟')
        self.building.building_no = None
        self.assertEqual(self.building.address, '京都府京都市上京区住所町域DEMO町番地DEMOデータ')

    def test_building_nearest_stations(self):
        self.assertEqual(self.building.nearest_station1, '地下鉄烏丸線 北大路 駅まで徒歩5分')
        self.building.station1_id = 0
        self.assertIsNone(self.building.nearest_station1)

        self.assertEqual(self.building.nearest_station2, '地下鉄烏丸線 鞍馬口 駅までバス10分（バス停 北大路バスターミナルまで徒歩5分）')
        self.building.station2_id = 0
        self.assertIsNone(self.building.nearest_station2)

        self.assertEqual(self.building.nearest_station3, '京福電鉄北野線 北野白梅町 駅までバス15分（バス停 北大路バスターミナルまで徒歩5分）')
        self.building.station3_id = 0
        self.assertIsNone(self.building.nearest_station3)
