import math
import os
import random
import re
import sys
from typing import Iterable

#
# Complete the 'canConstruct' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY a as parameter.
#

def canConstruct(a: Iterable[int]) -> str:
    remainder = 0
    for num in a:
        remainder = (remainder + num) % 3
    return "Yes" if remainder == 0 else "No"

# Test
print(canConstruct([1, 2, 3]))
print(canConstruct([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])) 