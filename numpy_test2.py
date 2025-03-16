# n = 121
# temp = n
# pal = 0
# while temp>0:
#     rem = temp % 10
#     pal = pal * 10 + rem
#     temp = temp//10
# if pal == n:
#     print("is apalindrome")
# else:
#     print("no")


# n = 5
# fact = 1
# for i in range(1,6):
#     fact = i * fact
# print(fact)



# n = 5
# a = 0
# b = 1
# while n > 0:
#     print(a)
#     c = a+b
#     a = b
#     b = c
#     n = n-1

# a = "chaithu"
# print(a.title())

# lst = [1,34,3,2,3,4,44,444]
# lst = list(dict.fromkeys(lst))
# print(lst)

# def remove_dupliactes(lst):
#     unique_list = []
#     for items in lst:
#         if items not in unique_list:
#             unique_list.append(items)
#     return unique_list
# lst = list(map(int,input("enter the list").split()))
# print(remove_dupliactes(lst))

# def reverse_list(lst):
#     reverse_lst = []
#     for i in range(len(lst) -1 ,-1,-1):
#         reverse_lst.append(lst[i])
#     return reverse_lst
# lst = list(map(int,input("enter the list").split()))
# print(reverse_list(lst))

# def anagrams():
#     str1 = []
#     str2 = []
#     for i in string1:
#         for j in string2:
#             str2.append(string2)
#     str1.append(string1)
#     if str1 == str2:
#         print("is a anagram")
#     else:
#         print("not an anagram")
# string1 = list.sort(input("enter any string"))
# string2 =list.sort( input("enter any string"))


########numpy#########

# import numpy as np
# array = np.random[(5,5)]
# print(array)

# import numpy as np
# lst = [1,2,3,4,45,6,7]
# array = np.array(lst)
# array[array % 2 == 0] = -1
# print(array)


# import numpy as np
# lst = [1,2,3,4,5,6]
# arr = np.array(lst)
# d = np.mean(arr)
# print(d)

# import numpy as np
# lst = [1,2,3,4,5]
# arr = np.array(lst)
# normalized = (arr - arr.min()) / (arr.max() - arr.min())
# print(normalized)

# import numpy as np
# arr = np.zeros([4,4])
# arr[0,:] = 1
# arr[3,:] = 1
# arr[:,0] = 1
# arr[:,3] = 1
# print(arr)

# import numpy as np
# lst1,lst2 = [1,2,3,4,5,6] , [4,5,6,7,8,9]
# arr1 , arr2 = np.array(lst1) , np.array(lst2)
# print(arr1)
# print(arr2)
# for i in arr1:
#     for j in arr2:
#         if i == j:
#             print(i)


# import numpy as np
# array = np.zeros((5,5))
# array[:,1] = 1
# array[:,2] = 2
# array[:,3] = 3
# array[:,4] = 4
# print(array)

# import numpy as np
# arr1 = np.arange(5)
# arr2 = np.arange(1,10,2)
# arr3 = np.swapaxes(arr1,arr2)
# print(arr3)


# import numpy as np
# arr = np.array([[1, 2, 3],
#                 [4, 5, 6],
#                 [7, 8, 9]])
# print(np.maximum(arr,5))


# import numpy as np
# toss_list = []
# heads_count = 0
# tails_count = 0
# for i in range(0,1000):
#     x = np.random.randint(1,3)
#     if x == 1:
#         toss_list.append("heads")
#         heads_count = heads_count +1
#         print("heads")
#     else:
#         toss_list.append("tails")
#         tails_count = tails_count + 1
#         print("tails")
# print(toss_list)
# print(heads_count)
# print(tails_count)
# print("the probability for heads over tails is", heads_count / tails_count)


# import numpy as np
# list = np.random.rand(2,5,5)
# list_1d = list.flatten()
# # for i in list:
# #     for j in list:
# #         list_1d.append(j)
# #     list_1d.append(i)
# # array_1d  = np.array(list_1d)
# print(list_1d)
# # print(array_1d)

# import numpy as np
# die1 = np.random.randint(1,7,10000)
# die2 = np.random.randint(1,7,10000)
# sum = die1 + die2
# count_7 = []
# for i in sum:
#     if i == 7:
#         count_7.append(i)
# print(count_7.count(7))
# print("the probability of 7 is:", count_7.count(7) / 10000)

# import numpy_test2 as np
# array = np.arange(0,10)
# sort = np.sort(array)[::-1]
# print(sort[1])