import numpy as np

data = []
with open("test.txt", encoding="utf-8") as of:
    lines = of.readlines()
    for i in lines:
        sp = i.split(" ")
        print(i)
        for k in sp:
            data.append(int(k))

a = np.array(data)
a = a.reshape([3,3])
print(np.linalg.inv(a))