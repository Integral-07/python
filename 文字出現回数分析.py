strings = input("Input: ")

dict = {}
for s in strings:

    last = True
    for t in dict.keys():
        if s == t:
            dict[s] += 1
            last = False
            break

    if(last):
        dict[s] = 1


for u in dict.keys():
    print(f"{u} {dict[u]}")