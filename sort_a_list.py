import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def sort_a_list(list, string):
    if string == "adj":
        state = True
        i = 0
        run = 0
        while state:
            run = run + 1
            if run == 9000:
                state = False
                print(list)
            elif i == (len(list) - 1):
                i = 0
            elif list[i] > list[i+1]:
                val1 = list[i]
                val2 = list[i+1]
                list[i] = val2
                list[i+1] = val1
            else:
                i = i + 1
    elif string == "desc":
        state = True
        i = 0
        run = 0
        while state:
            run = run + 1
            if run == 9000:
                state = False
                print(list)
            elif i == (len(list) - 1):
                i = 0
            elif list[i] < list[i+1]:
                val1 = list[i]
                val2 = list[i+1]
                list[i] = val2
                list[i+1] = val1
            else:
                i = i + 1
    else:
        print(list)

#Animation
