####################  BAR PLOT   #####################
# import matplotlib.pyplot as plt
# x = ["chaithanya","naani","mom","dad"]
# y = [20,25,30,50]
# z = [10,20,30,40]
# c = ["r","g","b","m"]
# plt.xlabel("names")
# plt.ylabel("ages")
# plt.title("family")
# plt.bar(x,y,width= 0.4, alpha = 1,color = "r", label =  ["chaithanya","naani","mom","dad"])
# plt.bar(x,z,width= 0.4, alpha = 1,color = "y", label =  ["chaithanya","naani","mom","dad"])
# plt.legend()
# plt.show()
# import numpy as np
# import matplotlib.pyplot as plt
# categories = ['A', 'B', 'C', 'D']
# values1 = [5, 7, 3, 8]
# values2 = [6, 4, 7, 5]
# x = np.arange(len(categories))  
# width = 0.3  
# plt.bar(x - width/2, values1, width=width, label='Dataset 1', color='blue')
# plt.bar(x + width/2, values2, width=width, label='Dataset 2', color='orange')
# plt.xlabel('Categories')
# plt.ylabel('Values')
# plt.title('Side-by-Side Bar Graph')
# plt.xticks(x, categories)
# plt.legend()
# plt.show()

#####################  SCATTER PLOT  #####################
# import matplotlib.pyplot as plt
# names = ["jack", "john" , "mike" , "mickey"]
# salary = [10000,40000,23402,23324]
# colour = ["r","g","b","m"]
# size = [20,30,10,50]
# plt.xlabel("names")
# plt.ylabel("salary")
# plt.title("salaries",fontsize = 20)
# plt.scatter(names , salary , color = colour , s = size)
# plt.show()

##################  HISTOGRAM  ######################
# import matplotlib.pyplot as plt
# import numpy as np
# import random
# number = [25, 34, 36, 11, 33, 27, 25, 47, 21, 33, 25, 49, 25, 48, 33, 38, 33, 17, 30, 43]
# plt.hist(number, rwidth=0.5)
# plt.show()


#################  PIE PLOT  #########################
# import matplotlib.pyplot as plt
# x = [20000,30000,40000,50000]
# y = ["john" , "sammy", "ori", "david"]
# ex = [0.4,0.0,0.0,0.0]
# plt.pie(x, radius = 1.5)
# plt.pie([1], colors = "w")
# plt.show()


####################  STEM PLOT   #####################
# import matplotlib.pyplot as plt
# x = [1,2,3,4,5,6]
# y = [3,4,2,5,6,1]
# plt.stem(x,y,linefmt= ":" , markerfmt= "r+")
# plt.show()


################  BOX PLOT    ####################
# import matplotlib.pyplot as plt
# x = [10,20,30,40,50,60,70]
# plt.boxplot(x, boxprops= dict(color = "r"), capprops=dict(color = "r"), whiskerprops=dict(color = "r"))
# plt.show()

# import matplotlib.pyplot as plt
# x = [1,2,3,4,5]
# area = [3,2,4,5,6]
# plt.stackplot(x, area)
# plt.show()

#############  FILL BETWEEN PLOTS  #############
# import matplotlib.pyplot as plt
# import numpy as np
# x = np.array([1,2,3,4,5,6,7])
# area = np.array([1,2,3,4,5,6,7])
# plt.fill_between(x,area,color = "g",where= (x>=2) & (x <=4))
# plt.plot(x,area)
# plt.show()

#############  PRACTISE   ##############
# import matplotlib.pyplot as plt
# import numpy as np

# # Define x values
# x = np.linspace(-10, 10, 100)  # 100 points between -10 and 10

# # Define the function y = 2x + 3
# y = 2 * x + 3

# # Plot the line graph
# plt.plot(x, y, label="y = 2x + 3", color="blue", linewidth=2)

# # Add labels and title
# plt.xlabel("X-axis")
# plt.ylabel("Y-axis")
# plt.title("Line Graph of y = 2x + 3")

# # Add grid and legend
# plt.grid(True)
# plt.legend()

# # Show the plot
# plt.show()


# import matplotlib.pyplot as plt
# import numpy as np
# x = np.linspace(0,100,100)
# y = np.linspace(0,100,100)
# plt.scatter(x,y, linewidth= 0.1)
# plt.show()


# import matplotlib.pyplot as plt
# cities = ["Hyderabad", "Chennai", "Bangalore", "Pune", "Mumbai"]
# population = [10000, 30000, 20000, 50000, 10000] 
# plt.bar(cities, population, color="skyblue")
# plt.xlabel("Cities")
# plt.ylabel("Population")
# plt.title("Population of Different Cities")
# plt.show()

# import matplotlib.pyplot as plt
# import numpy as np
# x = np.random.randint(0,100,1000)
# plt.hist(x,bins = 20, edgecolor = "black")
# print(x)
# plt.show()

# import matplotlib.pyplot as plt
# brands = ["samsung","nokia","iphone","iqoo","vivo"]
# sales = [10000,20000,5000,2000,5500]
# plt.pie(sales,labels=brands, startangle=140)
# plt.legend(loc = "upper left")
# plt.show()

# import matplotlib.pyplot as plt

# # Sample x values
# x = [1000, 2000, 1500, 2400, 5400]
# y = range(len(x))  # Generating y values (default indices)

# # Plot the line graph
# plt.plot(y, x, marker="o", linestyle="-", color="blue")

# # Add labels and title
# plt.xlabel("Index")
# plt.ylabel("Values")
# plt.title("Example")

# # Enable grid
# plt.grid(True)

# # Show the plot
# plt.show()



# import matplotlib.pyplot as plt

# # Sample Data
# cities = ["Hyderabad", "Chennai", "Bangalore", "Pune", "Mumbai"]
# population = [10000, 30000, 20000, 50000, 10000]

# # Create Bar Chart
# plt.bar(cities, population, color="skyblue")

# # Customize x-tick labels with rotation
# plt.xticks(rotation=45)  # Rotates tick labels by 45 degrees

# # Add labels and title
# plt.xlabel("Cities")
# plt.ylabel("Population")
# plt.title("City Population Bar Chart")

# # Show the plot
# plt.show()



# import matplotlib.pyplot as plt
# cities = ["Hyderabad", "Chennai", "Bangalore", "Pune", "Mumbai"]
# population = [10000, 30000, 20000, 50000, 10000]
# plt.scatter(cities,population, marker="*")
# plt.show()

# import matplotlib.pyplot as plt
# import numpy as np
# x = [1000, 2000, 1500, 2400, 5400]
# y = range(len(x)) 
# plt.plot(y, x, marker="o", linestyle="-", color="blue")
# plt.xlabel("Index")
# plt.ylabel("Values")
# plt.title("Example")
# plt.grid(True)
# plt.subplot(1,2,1)

# z = np.random.randint(0,100,1000)
# plt.hist(z,bins = 20, edgecolor = "black")
# plt.show()
# plt.subplot(1,2,2)
# plt.show()

# import numpy as np
# import matplotlib.pyplot as plt
# products = ["Laptops", "Mobiles", "Tablets", "Headphones", "Smartwatches"]
# x = np.arange(len(products))
# sales_2021 = [500, 900, 400, 600, 300]
# sales_2022 = [700, 1100, 500, 750, 400]
# sales_2023 = [800, 1200, 600, 900, 500]
# plt.stackplot(products,sales_2021,sales_2022,sales_2023)
# plt.xticks(x, products)  # Set product names on x-axis
# plt.show()


# import numpy as np
# import matplotlib.pyplot as plt
# import seaborn as sns
# x = np.random.randint(0,100,100)
# y = x.reshape([10,10])
# sns.heatmap(y)
# plt.show()

# import numpy as np
# import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D
# x = np.linspace(-5, 5, 50)
# y = np.linspace(-5, 5, 50)
# X, Y = np.meshgrid(x, y)
# Z = np.sin(np.sqrt(X**2 + Y**2))
# fig = plt.figure(figsize=(8, 6))
# ax = fig.add_subplot(111, projection='3d')
# surf = ax.plot_surface(X, Y, Z, cmap='viridis')
# ax.set_xlabel('X axis')
# ax.set_ylabel('Y axis')
# ax.set_zlabel('Z axis')
# ax.set_title('3D Surface Plot')
# fig.colorbar(surf)
# plt.show()



# import numpy as np
# import matplotlib.pyplot as plt
# import matplotlib.animation as animation
# fig, ax = plt.subplots()
# x = np.linspace(0, 2*np.pi, 100)  # X values from 0 to 2π
# line, = ax.plot(x, np.sin(x))  # Initial sine wave
# def update(frame):
#     line.set_ydata(np.sin(x + frame / 10.0))  # Shift wave over time
#     return line,
# ani = animation.FuncAnimation(fig, update, frames=100, interval=50, blit=True)
# plt.title("Animated Sine Wave")
# plt.xlabel("X values")
# plt.ylabel("Sine Wave")
# plt.show()


