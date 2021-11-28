from unittest import TestCase
from users.models import VacancyUser
import warnings


class VacancyUserModelTest(TestCase):
    """
    空室情報ユーザモデルのテスト
    """
    def setUp(self):
        warnings.simplefilter('ignore')
        self.user = VacancyUser.objects.get(username='yworks')

    def test_full_name(self):
        self.assertEqual(self.user.full_name, 'ワイワークス不動産')
