times_of_inputting = input()
diction = dict()
for i in range(int(times_of_inputting)):
    name = input()
    score = int(input())
    diction[name] = score
result_list = sorted(set(diction.values()))
print(result_list)
namee = sorted([k for k, v in diction.items() if v == result_list[1]])
print(namee)
for iii in namee:
    print(iii)

# this is the opposite version of the above: Find the second maximum score

# if __name__ == '__main__':
#     n = int(input())
#     arr = list(map(int, input().split()))
#     maximum = max(arr)
#     max_after_maximum = list()
#     for ind in range(len(arr)):
#         if (arr[ind] < maximum): 
#             max_after_maximum.append(arr[ind])
#     print(max(max_after_maximum))
                    
