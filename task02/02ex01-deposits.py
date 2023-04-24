#!/usr/bin/env python3

"""Calculate deposit percent yield based on time period.

Imagine your friend wants to put money on a deposit.
He has got many offers from different banks:
- First bank declares +A% each day;
- Second bank promises +B% each month;
- Third bank offers +C% by the end of the year;
- The 4th bank promotes +D% in a 10-year term;
- ... and so on ...

Your friend gets a terrible headache calculating all this stuff,
and asks you to help checking everything. You quickly realize
it is a common task and having a simple script is a great idea.

Let's implement this.

A simplified task:
Given the SUM amount of money, and PERCENT yield promised in a
FIXED_PERIOD of time, calculate the TOTAL equivalent of money
in a SET_PERIOD of time.

Math formula:
p = PERCENT / 100
TOTAL = SUM * ((1 + p) ** (SET_PERIOD / FIXED_PERIOD))
"""

# TODO: add lines to calculate yields for some common periods
#       of time (e.g. 1 month, 1 year, 5 years, 10 years)
# TODO: change the script to output the 1-year percent yield
#       as well
# TODO: (extra) Output only percents if the initial SUM is
#       not known at the moment the script is run


USAGE = """USAGE: {script} initial_sum percent fixed_period set_period

\tCalculate deposit yield. See script source for more details.
"""
USAGE = USAGE.strip()


def deposit(initial_sum, percent, fixed_period, set_period):
    """Calculate deposit yield."""
    per = percent / 100
    growth = (1 + per) ** (set_period / fixed_period)
    return growth


def main(args):
    """Gets called when run as a script."""
    if len(args) < 3 + 1 or len(args) > 4 + 1:
        exit(USAGE.format(script=args[0]))
    elif len(args) == 3 + 1:
        initial_sum = 0
        args = args[1:]
        percent, fixed_period, set_period = map(float, args)
    else:
        args = args[1:]
        initial_sum, percent, fixed_period, set_period = map(float, args)

    # Calculate growth for common periods
    yearly_growth = deposit(initial_sum, percent, fixed_period, 1)
    monthly_growth = deposit(initial_sum, percent, fixed_period, 1/12)
    five_year_growth = deposit(initial_sum, percent, fixed_period, 5)
    ten_year_growth = deposit(initial_sum, percent, fixed_period, 10)

    # Calculate yield for common periods
    yearly_yield = initial_sum * yearly_growth
    monthly_yield = initial_sum * monthly_growth
    five_year_yield = initial_sum * five_year_growth
    ten_year_yield = initial_sum * ten_year_growth

    # f-strings for common output results
    one_year = "1-year yield: ", f"{yearly_yield:.2f}, ", f"in percentage +{yearly_growth - 1:.0%}"
    one_month = "Monthly yield: ", f"{monthly_yield:.2f}, ", f"in percentage +{monthly_growth - 1:.0%}"
    five_year = "5-year yield: ", f"{five_year_yield:.2f}, ", f"in percentage +{five_year_growth - 1:.0%}"
    ten_year = "10-year yield: ", f"{ten_year_yield:.2f}, ", f"in percentage +{ten_year_growth - 1:.0%}"

    if initial_sum > 0:
        i = 1
    else :
        i = 2    

    # Output yields for common periods
    print(*one_year[0::i])
    print(*one_month[0::i])
    print(*five_year[0::i])
    print(*ten_year[0::i])

    # Output total yield
    total_growth = deposit(initial_sum, percent, fixed_period, set_period)
    total_yield = initial_sum * total_growth
    total = "total yield: ", f"{total_yield:.2f}, ", f"in percentage +{total_growth - 1:.0%}"

    print("\n")
    print(*total[0::i])


if __name__ == '__main__':
    import sys

    main(sys.argv)
