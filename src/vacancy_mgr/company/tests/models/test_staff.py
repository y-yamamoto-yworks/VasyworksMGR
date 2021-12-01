"""
System Name: Vasyworks
Project Name: vacancy_mgr
Encoding: UTF-8
Copyright (C) 2020 Yasuhiro Yamamoto
"""
from unittest import TestCase
from company.models import Staff
import warnings


class StaffModelTest(TestCase):
    """
    スタッフモデルのテスト
    """
    def setUp(self):
        warnings.simplefilter('ignore')
        self.Staff = Staff.objects.get(pk=2)      # 管理 太郎

    def test_full_name(self):
        self.assertEqual(self.Staff.full_name, '管理 太郎')

    def test_staff_name(self):
        self.assertEqual(self.Staff.staff_name, '管理 太郎 (部署:賃貸管理部)')
