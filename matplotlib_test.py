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


# import matplotlib.pyplot as plt

# x = [0, 2, 4, 6, 8]
# y = [0, 4, 16, 36, 64]

# fig, ax = plt.subplots()  
# ax.plot(x, y, marker='o', label="Data Points")

# ax.set_title("Basic Components of Matplotlib Figure")
# ax.set_xlabel("X-Axis") 
# ax.set_ylabel("Y-Axis")  

# plt.show()

# import matplotlib.pyplot as plt

# a = [1,2,3,4,5,6]
# b = [7,8,9,10,11,12]
# c = [13,14,15,16,17,18]

# fig = plt.figure(figsize = [10,10])

# s1 = plt.subplot(1,2,1)
# s2 = plt.subplot(1,2,2)

# s1.plot(a,color= "m", marker = "+")
# s1.set_xticks(list(range(0,10,2)))

# s2.plot(b,"sb")
# s2.set_xticks(list(range(6,15,8)))

# plt.show()

# import matplotlib.pyplot as plt

# a = [1,2,3,4,5,6]
# b = [7,8,9,10,11,12]
# c = [13,14,15,16,17,18]
# plt.plot(a,b,color = "b", marker = "*", label = "Data Points")
# plt.plot(c, color = "r", label = "extra line")
# plt.fill_between(a,b,c, color = "green", alpha = 0.4)
# for a, b in zip(a,b):
#     plt.annotate( f"({a},{b})", (a,b),textcoords="offset points",
#                 xytext=(0, 10),
#                 ha='center')

# plt.xlabel("X-AXIS")
# plt.ylabel("Y-AXIS")
# plt.title("TEST")
# plt.legend()
# plt.grid(True)
# plt.savefig("TEST.png")


# import matplotlib.pyplot as plt
# import numpy as np

# barwidth = 0.25
# a = [1,2,3,4,5,6]
# b = [7,8,9,10,11,12]
# c = [13,14,15,16,17,18]

# br1 = np.arange(len(a))
# br2 = [x + barwidth for x in br1]
# br3 = [x + barwidth for x in br2]

# plt.bar(br1, a, color = "red", edgecolor = "black", width= barwidth, label = "one")
# plt.bar(br2, b, color = "yellow", edgecolor = "black", width= barwidth, label = "second")
# plt.bar(br3, c, color = "blue", edgecolor = "black", width= barwidth, label = "third")

# plt.xlabel('Branch', fontweight ='bold', fontsize = 15)
# plt.ylabel("students passed", fontweight ='bold', fontsize = 15)
# plt.xticks([r + barwidth for r in range(len(a))], 
#         ['2015', '2016', '2017', '2018', '2019', '2020'])
# plt.legend()

# plt.show()


# import matplotlib.pyplot as plt
# import numpy as np

# N = 5

# boys = (20, 35, 30, 35, 27)
# girls = (25, 32, 34, 20, 25)
# boyStd = (2, 3, 4, 1, 2)
# girlStd = (3, 5, 2, 3, 3)
# ind = np.arange(N)
# barwidth = 0.35

# p1 = plt.bar(ind , boys, width = barwidth, yerr = boyStd)
# p2 = plt.bar(ind , girls,bottom= boys, width = barwidth, yerr = girlStd)

# plt.ylabel('Contribution')
# plt.title('Contribution by the teams')
# plt.xticks(ind, ('T1', 'T2', 'T3', 'T4', 'T5'))
# plt.yticks(np.arange(0, 81, 10))
# plt.legend((p1[0], p2[0]), ('boys', 'girls'))

# plt.savefig("new.png")


# import numpy as np
# import matplotlib.pyplot as plt
# data = np.random.randn(1000)
# plt.hist(data, bins  = 30, color = "skyblue", edgecolor = "red")
# plt.show()


# import numpy as np
# import matplotlib.pyplot as plt
# import seaborn as sns
# data = np.random.randn(1000)
# sns.histplot(data, bins = 30, color = "red"  , edgecolor = "black", kde= True)
# plt.show()


# import matplotlib.pyplot as plt
# import numpy as np
# from matplotlib import colors
# n_bins = 20

# fig = plt.subplots(1, 1, figsize=(10, 7), tight_layout=True)
# axs = plt.subplots(1, 1, figsize=(10, 7), tight_layout=True)
# np.random.seed(42)
# x = np.random.randn(1000)
# for s in ['top', 'bottom', 'left', 'right']:
#     axs.spines[s].set_visible(False)
# axs.xaxis.set_ticks_position("none")
# axs.yaxis.set_ticks_position("none")
# axs.xaxis.set_tick_params(pad=5)
# axs.yaxis.set_tick_params(pad=5)
# fig.text(0.9,0.5, "CHAITHANYA", color = "red", alpha = 0.7)
# N, bins, patches = axs.hist(x, bins=n_bins)
# fracs = ((N ** (1 / 5)) / N.max())
# norm = colors.Normalize(fracs.min(), fracs.max())

# for thisfrac, thispatch in zip(fracs, patches):
#     color = plt.cm.viridis(norm(thisfrac))
#     thispatch.set_facecolor(color)
# plt.grid(True, linestyle = "--", color = "grey", linewidth = 0.5)
# plt.ylabel("Y-AXIS")
# plt.xlabel("X-AXIS")
# plt.title("CUSTOM HISTOGRAM")
# plt.legend()
# plt.show()

# import matplotlib.pyplot as plt
# import numpy as np
# a = np.array([20, 35, 30, 35, 27])
# b = np.array([25, 32, 34, 20, 25])
# c = np.array([2, 3, 4, 1, 2])
# d = np.array([3, 5, 2, 3, 3])
# fig = plt.figure(figsize = (10,10))
# sb1 = plt.subplot(1,2,1)
# sb2 = plt.subplot(1,2,2)
# sb1.hist(a, color = "blue")
# plt.show()


# import matplotlib.pyplot as plt
# import numpy as np
# cars = ["AUDI", "MERC", "SUZUKI", "TOYOTA"]
# count = [100,60,200,500]
# color = ("orange", "brown", "pink", "yellow")
# blast = (0.1, 0, 0.2, 0.3)
# wp = {'linewidth' : 1, 'edgecolor' : "green"}

# def func(pct, allvalues):
#     absolute = int(pct/100.*np.sum(allvalues))
#     return "{:.f}%\n{:d}g)". format(pct,allvalues)



from matplotlib import style 
import matplotlib.pyplot as plt 
print(plt.style.available)