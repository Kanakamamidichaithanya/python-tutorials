# import numpy as np
# arr = np.array([1,2,3,4] , dtype = int)
# arr_2 = np.array([[1, 2], [3, 4]])
# print(type(arr))
# print(arr)
# print(arr_2)

# import numpy as np
# l= []
# for i in range (1,5):
#     int_1 = int (input("enter :"))
#     l.append(int_1)
# print (np.array(l))

# import numpy as np
# arr = np.ones((3,5), dtype = int)
# print(arr)

# import numpy as np
# arr = np.eye((2,3))
# print(arr)


# import numpy as np
# arr1 = np.array([1,2,3,4])
# arr2 = np.array([5,6,7,8])
# eq = np.mul(arr1,arr2)
# print(eq)

# import numpy as np
# arr = np.array([1,2,3,4,5])
# print(arr[1:4])

# import numpy
# def arrays(arr):
#     # Convert the list of strings to a NumPy array with type float and reverse it
#     return numpy.array(arr, dtype=float)[::-1]

# # Taking space-separated input from user
# arr = input().strip().split(' ')

# # Calling the function and printing the result
# print(arrays(arr))


# import numpy as np 
# var = [1,2,3,4,5,6,7,8,9]
# l = np.array(var)
# s = np.reshape(l,[3,3])
# print(s)


# import numpy_test2 as np 
# var = [1, 2, 3, 4]
# arr = np.array(var)
# shaping = np.reshape(arr,[2,2])
# transpose = np.transpose(shaping)
# print(transpose)
# print(transpose.flatten)

# import pikepdf

# pdf_path = r"C:\Users\kanak\Documents\kanakamamidi chaithanya.pdf"
# output_path = r"C:\Users\kanak\Documents\kanakamamidi_chaithanya_cleaned.pdf"

# with pikepdf.open(pdf_path) as pdf:
#     # Access the metadata dictionary
#     pdf.docinfo.clear()  # Removes all document info fields (Author, Title, etc.)
#     pdf.save(output_path)

# print("✅ All metadata cleared and saved as cleaned PDF.")


# import numpy as np
# arr = np.array([1,2,3,4,5])
# print(arr)

import numpy as np
arr = np.arange(0,9).reshape(3,3)
arr1 = np.arange(10,19).reshape(3,3)
print(np.hsplit(arr,3))