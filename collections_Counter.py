# from collections import Counter 
# import sys

# ls = list()
# for linn in sys.stdin:
#     for line in linn.split("\n"):
#         if line.strip() != '':
#             ls.append(line.split(" "))

# bill = 0
# for line in ls[3:]:
#     if line[0] in ls[1]:
#         bill += int(line[1])
#         ls[1].remove(line[0])
        
# print(bill)

# numbr = list([5, 7, 6, 4, 2, 1, 0, 3])
# order = list()
# for ele in range(len(numbr)):
#     for eleme in numbr:
#         if eleme == min(numbr):
#             # numbr.remove(eleme)
#             # order.append(eleme)
#             numbr[ele] = eleme
#         print(numbr)
# print(numbr)

for i in range(5):
    bricks = "# " * i
    print(bricks)