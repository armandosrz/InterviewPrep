import collections
import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

# Event is a tuple (start_time, end_time)
Event = collections.namedtuple('Event', ('start', 'finish'))

Endpoint = collections.namedtuple('Endpoint', ('time', 'is_start'))


def find_max_simultaneous_events(A):
    endpoints = [p for event in A for p in (Endpoint(event.start, True), Endpoint(event.finish, False))]
    
    endpoints.sort(key=lambda x : (x.time, not x.is_start))

    current, max_num = 0, 0
    for e in endpoints:
        if e.is_start:
            current += 1
            if current > max_num:
                max_num = current
        else:
            current -= 1
    
    return max_num



@enable_executor_hook
def find_max_simultaneous_events_wrapper(executor, events):
    events = [Event(*x) for x in events]
    return executor.run(
        functools.partial(find_max_simultaneous_events, events))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("calendar_rendering.py",
                                       'calendar_rendering.tsv',
                                       find_max_simultaneous_events_wrapper))
