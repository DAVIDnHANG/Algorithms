#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution

from collections import deque


def eating_cookies(length):
    count = 0  # Global count

    def calcuate(remaining_length):
        # 0 means success
        # 1 means only 1 option is available (hop 1)
        if remaining_length < 2:
            nonlocal count  # Refer to outer count
            count += 1
            return

        # Calculates, removing the length already passed.
        # For 1...4 or remaining_length+1 if it's less than 4.
        # deque(, maxlen=0) is the fastest way of consuming an iterator
        # without also keeping it's data. This is the most efficient both
        # memory-wise and clock-wise
        deque((calcuate(remaining_length-i)
              for i in range(1, min(4, remaining_length+1))), maxlen=0)

    calcuate(length)
    return count

# the cookie-monster ate one cookie. There is one way to eat the cookie.

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')