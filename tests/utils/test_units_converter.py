"""
units converter tests.
"""
import unittest

from chargeback.utils.units_converter import *

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
        """
        Not found prefixes should return the full unit
        """
        self.assertEqual(
            'UNKNOWN',
            extract_prefix('UNKNOWN')
        )
        """
        None unit returns empty string
        """
        self.assertEqual(
            '',
            extract_prefix(None)
        )

    def test_distance(self):
        """
        Tests of distance method
        """
        """
        SI symbol returns distance to base unit
        """
        for si_pr in SI_PREFIX:
            self.assertEqual(
                SI_PREFIX[si_pr]['value'],
                distance(si_pr)
            )
        """
        BINARY symbol returns distance to base unit
        """
        for bi_pr in BINARY_PREFIX:
            self.assertEqual(
                BINARY_PREFIX[bi_pr]['value'],
                distance(bi_pr, '', 'BINARY_PREFIX')
            )
            self.assertEqual(
                BINARY_PREFIX[bi_pr]['value'],
                distance(bi_pr, '', BINARY_PREFIX)
            )
        """
        ALL_PREFIXES (default) symbol returns distance to base unit
        """
        for all_pr in ALL_PREFIXES:
            self.assertEqual(
                ALL_PREFIXES[all_pr]['value'],
                distance(all_pr, '', 'ALL_PREFIXES')
            )
            self.assertEqual(
                ALL_PREFIXES[all_pr]['value'],
                distance(all_pr)
            )
        """
        returns nil if origin or destination are not found
        """
        for all_pr in ALL_PREFIXES:
            self.assertEqual(
                None,
                distance(all_pr, 'UNKNOWN')
            )
            self.assertEqual(
                None,
                distance('UNKNOWN', all_pr)
            )
        """
        SI symbol returns distance between symbols
        """
        origin = finish = ['', 'K', 'M']
        for x in origin:
            for y in finish:
                self.assertEqual(
                    SI_PREFIX[x]['value']/SI_PREFIX[y]['value'],
                    distance(x, y)
                )
        """
        BINARY symbol returns distance between symbols
        """
        origin = finish = ['', 'Ki', 'Mi']
        for x in origin:
            for y in finish:
                self.assertEqual(
                    BINARY_PREFIX[x]['value'] / BINARY_PREFIX[y]['value'],
                    distance(x, y, 'BINARY_PREFIX')
                )
        """
        Default symbols returns distance between symbols
        """
        origin = ['', 'K', 'M']
        finish = ['', 'Ki', 'Mi']
        for x in origin:
            for y in finish:
                self.assertEqual(
                    ALL_PREFIXES[x]['value'] / ALL_PREFIXES[y]['value'],
                    distance(x, y)
                )

    def test_to_unit(self):
        """
        Test of to_unit method
        """

        """
        SI symbol returns value in base unit
        """
        self.assertEqual(
            7,
            to_unit(7, )
        )
        self.assertEqual(
            7000,
            to_unit(7, 'Kb')
        )
        """
        BINARY symbol returns value in base unit
        """
        self.assertEqual(
            7168,
            to_unit(7, 'KiB', '', 'BINARY_PREFIX')
        )
        self.assertEqual(
            7168,
            to_unit(7, 'KiB', '', BINARY_PREFIX)
        )
        """
        SI symbol returns value in destination unit
        """
        self.assertEqual(
            7000,
            to_unit(7, 'MB', 'KB')
        )
        """
        BINARY symbol returns value in destination unit
        """
        self.assertEqual(
            7168,
            to_unit(7, 'PiB', 'TiB', 'BINARY_PREFIX')
        )
        self.assertEqual(
            7168,
            to_unit(7, 'PiB', 'TiB', BINARY_PREFIX)
        )
        """
        SI symbol returns value in destination unit
        """
        self.assertEqual(
            6366.462912410498,
            to_unit(7, 'PB', 'TiB')
        )


