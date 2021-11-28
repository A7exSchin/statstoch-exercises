# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
"""
Spyder Editor

This is a temporary script file.
"""
def calcSum(n, k):
    result = 0
    for j in range(1, 7):
        for x in table:
            if (x[0] == n-1 and x[1] == k-j):
                result += x[2]
    return result

n = list(range(1, 41))

table = []

# Triple (n, k, P(W_n = k))
# insert n=1 manually
for i in range(1, 7):
    table.append((1, i, 1/6))

for i in range(2, 41):
    for k in range(1, i * 6 + 1):
        sum = 1/6 * calcSum(i, k)
        table.append((i, k, sum)) 

table = pd.DataFrame(table,columns=('n','k','P(W_n = k)'))

print(table)
p = 0.1

# Step 1: get k*(n) for all n
# Step 2: Calc e, e:tilde
# Step 3: Plot Tschebyescheff withe, e:tilde
