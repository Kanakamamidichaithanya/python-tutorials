""""function to create a array using input"""
# def create_array():
#     array = []
#     arr_len = int(input("enter the length of the array:"))
#     for i in range(arr_len):
#         element = array.append(int(input(f"Enter element {i + 1}: ")))   
#     return array
# array1 = create_array()
# print(array1)

""""function for finding the max of the array"""""
# def creating_array():
#     array = []
#     arr_len = int(input("enter the length of the array"))  
#     for i in range(arr_len):
#         element = array.append(int(input(f"enter the {i+1} element ")))
#     return array
# def finding_max(array):
#     if not array:
#         return None
#     maximum_number = array[0]
#     if array:
#         for num in array:
#             if num > maximum_number:
#                 maximum_number = num
#         return maximum_number
# array = creating_array()
# max = finding_max(array)
# print(array)
# print(max)


'''finding the minimum number in the array'''
# array = []
# arr_len = int(input("enter the length of the array:"))
# for i in range(arr_len):
#     array.append(int(input(f"enter the elemnt {i+1}:")))
# print(array)
# def finding_min(array):
#     if not array:  # Check if the array is empty
#         print("Array is empty")
#         return None
#     minimum_number =array[0]
#     for i in array:
#         if i < minimum_number:
#             minimum_number = i
#     return minimum_number
# min = finding_min(array)
# print(min)


# import array as arr
# array = arr.array("i",[4,2,3,4])
# minimum_number = array[0]
# for i in array:
#     if i < minimum_number:
#         minimum_number= i
# print(minimum_number)


'''program for removing a desired element'''
# import array as arr
# array = arr.array("i",[4,2,3,4])
# element = int(input("enter hte element to remove:"))
# for i in array:
#     if i == element:
#         new_array = arr.array("i",[i for i in array if i!= element])
# print(new_array)


'''program to append elemnt into the array'''
# import array as arr
# array = arr.array("i",[4,2,3,4])
# element = int(input("enter hte element to add:"))
# index = int(input("enter the index of the element:"))
# new_array = arr.array("i", [])
# for i in range(len(array)):
#     if index == i:
#         new_array.append(element)  # Insert the new number
#     new_array.append(array[i])
# print("Array after insertion:", new_array)


# '''program for accessing the elements in the array'''
# import array as arr
# array = arr.array("i",[4,2,3,4])
# element = int(input("enter the elemnt to access:"))
# for i in range(len(array)):
#     if i == element:
#         print("Element at index {}: {}".format(i, array[i]))
#         break

'''program for slicing'''
# import array as arr
# my_array = arr.array("i", [10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
# print("Original array:", my_array)
# start_index = int(input("Enter the start index for slicing (0 to {}): ".format(len(my_array) - 1)))
# end_index = int(input("Enter the end index for slicing ({} to {}): ".format(start_index, len(my_array) - 1)))
# sliced_array = my_array[start_index:end_index]
# print("Sliced array:", sliced_array)

'''program for updating the element'''
# import array as arr
# array = arr.array("i",[4,2,3,4])
# number = int(input("enter the number to update:"))
# index = int(input("enter the index to update"))
# if 0<= index < len(array):
#     array[index] = number
#     print(array)


'''program for counting the occurence of the element in an array'''
# import array as arr
# array = arr.array("i",[4,2,3,4])
# number = int(input("enter the element you want to count:"))
# count = 0
# for i in array:
#     if i == number:
#         count = count+1
# print(count)


'''program for reversing the array'''
# import array as arr
# array = arr.array("i",[4,2,3,5])
# rev_array = arr.array("i",[])
# for i in range(len(array)):
#     rev_array.append(array[len(array)-1 -i]) 
# print(rev_array)




        
