import functools

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

MPG = 20

import collections
# gallons[i] is the amount of gas in city i, and distances[i] is the
# distance city i to the next city.
def find_ample_city(gallons, distances):
    remaining = 0
    CG = collections.namedtuple('CG', ('city', 'gas'))
    min_cg = CG(0, 0)
    cities = len(gallons)

    for i in range(1, cities):
        remaining += gallons[i-1] - distances[i-1] // MPG
        if remaining < min_cg.gas:
            min_cg = CG(i, remaining)
    
    return min_cg.city


@enable_executor_hook
def find_ample_city_wrapper(executor, gallons, distances):
    result = executor.run(
        functools.partial(find_ample_city, gallons, distances))
    num_cities = len(gallons)
    tank = 0
    for i in range(num_cities):
        city = (result + i) % num_cities
        tank += gallons[city] * MPG - distances[city]
        if tank < 0:
            raise TestFailure('Out of gas on city {}'.format(i))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("refueling_schedule.py",
                                       'refueling_schedule.tsv',
                                       find_ample_city_wrapper))
