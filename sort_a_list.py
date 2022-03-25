import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

#Animate histogram
# n = 1000
# number_of_frames = 100
# data = np.random.rand(n, number_of_frames)
#
# def update_hist(num, data):
#     plt.cla()
#     plt.hist(data[num])
#
# fig = plt.figure()
# hist = plt.hist(data[0])
#
# animation = animation.FuncAnimation(fig, update_hist, number_of_frames, fargs=(data, ) )
# plt.show()




number_of_frames = 9
for i in range(10):
    list = [3,1,2,4,3*i,5,7,9,0,6,3,2,7,i*2,4,8,9,3,2,1,4,10,i]
    fig = plt.figure()
    hist = plt.hist(list)
    animation = animation.FuncAnimation(fig, hist, 9, fargs=(list, ))
plt.show()



fig = plt.figure()
hist = plt.hist(list)


plt.show()


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
