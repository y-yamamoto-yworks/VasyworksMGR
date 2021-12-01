"""
System Name: Vasyworks
Project Name: vacancy_mgr
Encoding: UTF-8
Copyright (C) 2020 Yasuhiro Yamamoto
"""
from unittest import TestCase
from users.models import User
import warnings


class UserModelTest(TestCase):
    """
    ユーザモデルのテスト
    """
    def setUp(self):
        warnings.simplefilter('ignore')
        self.user = User.objects.get(username='t-kanri')

    def test_full_name(self):
        self.assertEqual(self.user.full_name, '管理 太郎')
