# Time converter

from datetime import datetime,date

VALID_INTERVAL_UNITS = ["hourly", "daily",  "weekly",  "monthly",  "yearly"]

MINUTELY = 60
HOURLY = 60 * MINUTELY
DAILY  = 24 * HOURLY
WEEKLY = 7 * DAILY

# Days of a Month-Year
daysOfMonth = lambda y,m: (date(y, m + 1, 1) - date(y, m, 1)).days

# Days of a Year
daysOfYear  = lambda y:   (date(y + 1, 1, 1) - date(y, 1, 1)).days

MONTHLY = DAILY * daysOfMonth(datetime.now().year, datetime.now().month)
YEARLY  = DAILY * daysOfYear(datetime.now().year)

# Calculate the number of intervals
def number_of_intervals(period, interval, calculation_date = datetime.now(), days_in_month = None, days_in_year= None):
    # Period: time period as input (end_time - start_time)
    # interval: base interval to calculate against (i.e 'daily', 'monthly', default: 'monthly')
    # Calculation_date: used to calculate taking into account the #days in month
    # It always return at least 1 as the event exists
    if period == 0:
        return 1
    if interval == '':
        return 0
    time_span = ''
    if interval == 'monthly' or interval == 'yearly':
        if interval == 'monthly':
            if days_in_month is None:
                time_span = daysOfMonth(calculation_date.year, calculation_date.month) * DAILY
            else:
                time_span = days_in_month * DAILY
        else:
            if days_in_year is None:
                time_span = daysOfYear(calculation_date.year) * DAILY
            else:
                time_span = days_in_year * DAILY
    else:
        if interval == 'minutely':
            time_span = MINUTELY
        elif interval == 'hourly':
            time_span = HOURLY
        elif interval == 'daily':
            time_span = DAILY
        elif interval == 'weekly':
            time_span = WEEKLY
        else:
            time_span = 0

    remain = 0
    if period % time_span != 0:
        remain = 1
    return int((period/time_span) + remain)