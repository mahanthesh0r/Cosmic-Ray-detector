import numpy as np
lst = [[[25,60,92],[23,22,22],[19,20,21]],[[35,60,92],[13,22,22],[49,20,21]],[[25,24,92],[23,12,22],[19,20,29]]]
lst = np.array(lst)
all_y = list(np.where(lst >= 21)[0])
all_x = list(np.where(lst >= 21)[1])
zipped = list(zip(all_x,all_y))
zipped.sort()
print(np.where(lst>=21))