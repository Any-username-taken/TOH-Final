import random

# from Classes import *

var = ['0/12234', "1", "2", "3", "4"]
thing = "4"

for i in range(len(var)):
    print(var[i].split("/")[0])
    if thing in var[i].split("/")[0]:
        print(" num 1 in")

