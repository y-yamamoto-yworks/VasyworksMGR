"""
System Name: Vasyworks
Project Name: vacancy_mgr
Encoding: UTF-8
Copyright (C) 2020 Yasuhiro Yamamoto
"""
from unittest import TestCase
from django.test import Client
from django.urls import reverse
from django.db import transaction
import warnings


class VacancyInputElectricViewTest(TestCase):
    """
    空室入力電気ビューのテスト
    """
    def setUp(self):
        warnings.simplefilter('ignore')
        self.client = Client()
        if transaction.get_autocommit():
            transaction.set_autocommit(False)

        response = self.client.post(
            reverse('login'),
            {'username': 't-kanri', 'password': 'guest1234', },
            follow=True
        )
        self.assertEqual(response.status_code, 200)

    def tearDown(self):
        transaction.rollback()

    def test_get_vacancy_input_electric_view(self):
        url = reverse(
            'vacancy_item_vacancy_input_electric',
            args=['MQ'],  # 選択可
        )
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        item = response.context['item']
        self.assertEqual(item.input_contents, '選択可')

    def test_post_vacancy_input_electric_view(self):
        url = reverse(
            'vacancy_item_vacancy_input_electric',
            args=['MQ'],  # 選択可
        )
        response = self.client.post(
            url,
            {
                'input_contents': '空室入力電気編集テスト',
                'priority': '10',
                'is_stopped': 'off',
            },
            follow=True,
        )
        self.assertEqual(response.status_code, 200)
        messages = list(response.context['messages'])
        self.assertEqual(str(messages[0]), '保存しました。')
