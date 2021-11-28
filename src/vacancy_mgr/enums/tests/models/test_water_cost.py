from unittest import TestCase
from enums.models import WaterCostType
import warnings


class WaterCostTypeModelTest(TestCase):
    """
    水道費種別モデルのテスト
    """
    def setUp(self):
        warnings.simplefilter('ignore')

    def test_is_money(self):
        self.assertFalse(WaterCostType.objects.get(pk=0).is_money)
        self.assertFalse(WaterCostType.objects.get(pk=10).is_money)
        self.assertTrue(WaterCostType.objects.get(pk=20).is_money)
        self.assertFalse(WaterCostType.objects.get(pk=30).is_money)
        self.assertFalse(WaterCostType.objects.get(pk=31).is_money)
