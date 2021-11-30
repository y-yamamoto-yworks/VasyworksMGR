from unittest import TestCase
from enums.models import TaxType
import warnings


class TaxTypeModelTest(TestCase):
    """
    税種別モデルのテスト
    """
    def setUp(self):
        warnings.simplefilter('ignore')

    def test_is_excluding(self):
        self.assertFalse(TaxType.objects.get(pk=0).is_excluding)
        self.assertTrue(TaxType.objects.get(pk=1).is_excluding)
        self.assertFalse(TaxType.objects.get(pk=2).is_excluding)
        self.assertFalse(TaxType.objects.get(pk=3).is_excluding)

    def test_is_including(self):
        self.assertFalse(TaxType.objects.get(pk=0).is_including)
        self.assertFalse(TaxType.objects.get(pk=1).is_including)
        self.assertTrue(TaxType.objects.get(pk=2).is_including)
        self.assertFalse(TaxType.objects.get(pk=3).is_including)

    def test_text(self):
        self.assertEqual(TaxType.objects.get(pk=0).text, '')
        self.assertEqual(TaxType.objects.get(pk=1).text, '税別')
        self.assertEqual(TaxType.objects.get(pk=2).text, '税込')
        self.assertEqual(TaxType.objects.get(pk=3).text, '')