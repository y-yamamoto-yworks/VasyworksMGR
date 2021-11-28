from unittest import TestCase
from enums.models import PaymentFeeType
import warnings


class PaymentFeeTypeModelTest(TestCase):
    """
    支払手数料種別モデルのテスト
    """
    def setUp(self):
        warnings.simplefilter('ignore')

    def test_is_money(self):
        self.assertFalse(PaymentFeeType.objects.get(pk=0).is_money)
        self.assertTrue(PaymentFeeType.objects.get(pk=10).is_money)
        self.assertTrue(PaymentFeeType.objects.get(pk=20).is_money)
        self.assertTrue(PaymentFeeType.objects.get(pk=30).is_money)
