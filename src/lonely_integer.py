import math
import os
import random
import re
import sys
from typing import List

def lonely_integer(array: List[str]):
    occurencies = {}

    for item in array:
        if item not in occurencies.keys():
            occurencies[item] = 0

        occurencies[item] += 1

    for key, value in occurencies.items():
        if value == 1:
            return key
    
    return None

result = lonely_integer([1, 2, 2, 3, 3, 4, 4, 5])
print(result)
