"""
units converter tests.
"""
import unittest

from chargeback.utils.units_converter import SYMBOLS, SI_PREFIX, BINARY_PREFIX, extract_prefix

class TestUnitsConverter(unittest.TestCase):
    """
        Test units Converter.
    """

    def setUp(self):
        pass

    def test_extract_prefix(self):
        """
        Tests of extract_prefix method
        """
        """
        SI symbol prefixes should be extracted.
        """
        for sym in SYMBOLS:
            for si_prefix in SI_PREFIX:
                expected = si_prefix
                result   = extract_prefix(si_prefix + sym)
                self.assertEqual(
                    expected,
                    result
                )
        """
        BINARY symbol prefixes should be extracted
        """
        for sym in SYMBOLS:
            for si_prefix in BINARY_PREFIX:
                expected = si_prefix
                result   = extract_prefix(si_prefix + sym)
                self.assertEqual(
                    expected,
                    result
                )
