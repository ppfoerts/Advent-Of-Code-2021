# source: https://chaudhary1337.com/advent-of-code-2021-day-6-solutions-in-python3/
# study later
from collections import defaultdict

def get_input():
    data = []
    with open("input.txt") as f:
        data = f.readlines()
    return data


def solve(data):
    current_timers = list(map(int, data[0].split(',')))
    # stores frequency of each time
    # aka counter[time]: #fishes
    # or the number of fishes at the given time, "time"
    counter = defaultdict(int)
    for time in current_timers: counter[time] += 1

    TIMER_START = 6
    for _ in range(256):
        new_counter = defaultdict(int)
        # for all the new fishes that have spawned
        for time in counter:
            if time == 0:
                # all the current fishes at time 0 restart their counters
                # from TIMER_START &&
                # they spawn new fishes with timer starting from TIMER_START+2
                new_counter[TIMER_START+2] += counter[0]
                new_counter[TIMER_START] += counter[0]
            else:
                # we move the counts from THIS time to the PREVIOUS time
                new_counter[time-1] += counter[time]
        
        counter = new_counter

    return sum(counter.values())

print(solve(get_input()))