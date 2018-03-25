"""
time converter tests.
"""
import unittest
from datetime import datetime, timedelta

from chargeback.utils.time_converter import *

class TestTimeConverter(unittest.TestCase):
    """
        Test units Converter.
    """

    def setUp(self):
        pass

    def test_number_of_intervals_on_this_month(self):
        """
        Tests number of intervals on this month
        """
        time_values = [
            0,
            15 * MINUTELY,
            45 * MINUTELY,
            HOURLY,
            90 * MINUTELY,
            5 * HOURLY,
            1 * DAILY,
            1 * DAILY + 12 * HOURLY,
            WEEKLY,
            WEEKLY + 2 * DAILY + 19 * HOURLY + 12 * MINUTELY,
            MONTHLY - 1
        ]
        """
        Minutely
        """
        interval = 'minutely'
        results = [1, 15, 45, 60, 90, 300, 24 * 60, 15 * 24 * 6, 7 * 24 * 60, 14 * 7 * 24 * 6,
                   24 * 60 * daysOfMonth(datetime.now().year, datetime.now().month)]
        self.assertEqual(
            len(time_values),
            len(results)
        )
        start_t = datetime.now().replace(minute=0, hour=0, second=0, day=1, microsecond=0)

        for tindex, tvalue in enumerate(time_values):
            end_t = start_t + timedelta(seconds = tvalue)
            if start_t.month != end_t.month:
                continue;
            else:
                conversion = number_of_intervals( int((end_t - start_t).total_seconds()), interval)
                self.assertEqual(
                    results[tindex],
                    conversion,
                    "Expected with %s for %d s to match %d, start: %s, end: %s, got: %d" % (interval, tvalue, results[tindex], start_t, end_t, conversion)
                )
        """
        Hourly
        """
        interval = 'hourly'
        results = [1, 1, 1, 1, 2, 5, 24, 36, 168, 236,
                   24 * daysOfMonth(datetime.now().year, datetime.now().month)]
        self.assertEqual(
            len(time_values),
            len(results)
        )
        start_t = datetime.now().replace(minute=0, hour=0, second=0, day=1, microsecond=0)

        for tindex, tvalue in enumerate(time_values):
            end_t = start_t + timedelta(seconds=tvalue)
            if start_t.month != end_t.month:
                continue;
            else:
                conversion = number_of_intervals(int((end_t - start_t).total_seconds()), interval)
                self.assertEqual(
                    results[tindex],
                    conversion,
                    "Expected with %s for %d s to match %d, start: %s, end: %s, got: %d" % (
                    interval, tvalue, results[tindex], start_t, end_t, conversion)
                )
        """
        Daily
        """
        interval = 'daily'
        results = [1, 1, 1, 1, 1, 1, 1, 2, 7, 10,
                   daysOfMonth(datetime.now().year, datetime.now().month)]
        self.assertEqual(
            len(time_values),
            len(results)
        )
        start_t = datetime.now().replace(minute=0, hour=0, second=0, day=1, microsecond=0)

        for tindex, tvalue in enumerate(time_values):
            end_t = start_t + timedelta(seconds=tvalue)
            if start_t.month != end_t.month:
                continue;
            else:
                conversion = number_of_intervals(int((end_t - start_t).total_seconds()), interval)
                self.assertEqual(
                    results[tindex],
                    conversion,
                    "Expected with %s for %d s to match %d, start: %s, end: %s, got: %d" % (
                        interval, tvalue, results[tindex], start_t, end_t, conversion)
                )
        """
        Weekly
        """
        interval = 'weekly'
        results = [1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 5]
        self.assertEqual(
            len(time_values),
            len(results)
        )
        start_t = datetime.now().replace(minute=0, hour=0, second=0, day=1, microsecond=0)

        for tindex, tvalue in enumerate(time_values):
            end_t = start_t + timedelta(seconds=tvalue)
            if start_t.month != end_t.month:
                continue;
            else:
                conversion = number_of_intervals(int((end_t - start_t).total_seconds()), interval)
                self.assertEqual(
                    results[tindex],
                    conversion,
                    "Expected with %s for %d s to match %d, start: %s, end: %s, got: %d" % (
                        interval, tvalue, results[tindex], start_t, end_t, conversion)
                )

        """
        Monthly
        """
        interval = 'monthly'
        results = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        self.assertEqual(
            len(time_values),
            len(results)
        )
        start_t = datetime.now().replace(minute=0, hour=0, second=0, day=1, microsecond=0)

        for tindex, tvalue in enumerate(time_values):
            end_t = start_t + timedelta(seconds=tvalue)
            if start_t.month != end_t.month:
                continue;
            else:
                conversion = number_of_intervals(int((end_t - start_t).total_seconds()), interval)
                self.assertEqual(
                    results[tindex],
                    conversion,
                    "Expected with %s for %d s to match %d, start: %s, end: %s, got: %d" % (
                        interval, tvalue, results[tindex], start_t, end_t, conversion)
                )
        """
        Yearly
        """
        interval = 'yearly'
        results = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        self.assertEqual(
            len(time_values),
            len(results)
        )
        start_t = datetime.now().replace(minute=0, hour=0, second=0, day=1, microsecond=0)

        for tindex, tvalue in enumerate(time_values):
            end_t = start_t + timedelta(seconds=tvalue)
            if start_t.month != end_t.month:
                continue;
            else:
                conversion = number_of_intervals(int((end_t - start_t).total_seconds()), interval)
                self.assertEqual(
                    results[tindex],
                    conversion,
                    "Expected with %s for %d s to match %d, start: %s, end: %s, got: %d" % (
                        interval, tvalue, results[tindex], start_t, end_t, conversion)
                )

    def test_number_of_intervals__different_month(self):
        """
        Tests calculating for a different month than current
        """
        time_values = [
            0,
            15 * MINUTELY,
            45 * MINUTELY,
            HOURLY,
            90 * MINUTELY,
            5 * HOURLY,
            1 * DAILY,
            1 * DAILY + 12 * HOURLY,
            WEEKLY,
            WEEKLY + 2 * DAILY + 19 * HOURLY + 12 * MINUTELY,
            28 * DAILY - 1
        ]
        """
        Hourly
        """
        interval = 'hourly'
        results = [1, 1, 1, 1, 2, 5, 24, 36, 168, 236, 28 * 24]
        self.assertEqual(
            len(time_values),
            len(results)
        )
        start_t = datetime.now().replace(year=2017, month=2, day=1, minute=0, hour=0, second=1, microsecond=0)

        for tindex, tvalue in enumerate(time_values):
            end_t = start_t + timedelta(seconds=tvalue)
            if start_t.month != end_t.month:
                continue;
            else:
                conversion = number_of_intervals(int((end_t - start_t).total_seconds()), interval, start_t)
                self.assertEqual(
                    results[tindex],
                    conversion,
                    "Expected with %s for %d s to match %d, start: %s, end: %s, got: %d" % (
                        interval, tvalue, results[tindex], start_t, end_t, conversion)
                )

    def test_number_of_intervals_with_given_lengths(self):
        """
        Tests calculating for a different month than current
        """
        time_values = [
            0,
            15 * MINUTELY,
            45 * MINUTELY,
            HOURLY,
            90 * MINUTELY,
            5 * HOURLY,
            1 * DAILY,
            1 * DAILY + 12 * HOURLY,
            WEEKLY,
            WEEKLY + 2 * DAILY + 19 * HOURLY + 12 * MINUTELY,
            28 * DAILY - 1
        ]
        """
        Monthly
        """
        interval = 'monthly'
        days_in_month = 7
        results = [1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 4]
        self.assertEqual(
            len(time_values),
            len(results)
        )
        start_t = datetime.now().replace(minute=0, hour=0, second=0, day=1, microsecond=0)

        for tindex, tvalue in enumerate(time_values):
            end_t = start_t + timedelta(seconds=tvalue)
            if start_t.month != end_t.month:
                continue;
            else:
                conversion = number_of_intervals(int((end_t - start_t).total_seconds()), interval, days_in_month = days_in_month)
                self.assertEqual(
                    results[tindex],
                    conversion,
                    "Expected with %s for %d s to match %d, start: %s, end: %s, got: %d" % (
                        interval, tvalue, results[tindex], start_t, end_t, conversion)
                )