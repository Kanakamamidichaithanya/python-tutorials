# import pandas as pd
# names = ["chaithu", "naani", "mom", "dad"]
# ages = [20,24,48,54]
# seri = pd.Series(data = names)
# print(seri)



# import numpy as np
# import pandas as pd
# df = np.random.randn(5,4)
# dataframe = pd.DataFrame(df, ["a","b","c","d","e"],["q","w","e","r"])
# dataframe["new"] = dataframe["w"] + dataframe["e"]
# print(dataframe)

# import numpy as np
# import pandas as pd
# df = np.random.randn(5,4)
# dataframe = pd.DataFrame(df, index = ["a","b","c","d","e"],columns=["q","w","e","r"])
# dataframe["new"] = dataframe["w"] + dataframe["e"]
# dataframe.drop("new" , axis = 1, inplace=True)
# print(dataframe.iloc[2])


# import numpy as np
# import pandas as pd
# df = np.random.randn(5,4)
# dataframe = pd.DataFrame(df, index = ["a","b","c","d","e"],columns=["q","w","e","r"])
# print(dataframe)
# result = (dataframe[dataframe["w"] < 0 ])
# print(result)


# import pandas as pd
# dataframe = pd.DataFrame({"a" : [1,2,3,4], "b" : [1,3,4,3]})
# dataframe["new"] = dataframe["a"] + dataframe["b"]
# print(dataframe)

# import pandas as pd
# dataframe = pd.DataFrame({"a" : [1,2,3,4], "b" : [1,3,4,3]})
# dataframe.insert(1, "python" , dataframe["a"][:1])
# print(dataframe)

# import pandas as pd
# dataframe = pd.DataFrame({"a" : [1,2,3,4], "b" : [1,3,4,3]})
# dataframe.insert(1, "python" , dataframe["a"])
# dataframe.to_csv("test_file.csv")


# import pandas as pd
# csv_1 = pd.read_csv("C:\\Users\\kanak\\Documents\\Chaithanya Education\\Personal Projects\\python-tutorials\\customers-100.csv")
# csv_1.loc[1,"Customer Id"] = "chaithu"
# print(csv_1)

# import pandas as pd
# var = pd.read_csv("C:\\Users\\kanak\\Documents\\Chaithanya Education\\Personal Projects\\python-tutorials\\missing_values_data.csv")
# var = var.interpolate()
# print(var)

# import pandas as pd
# var1 = pd.DataFrame({"A" : [1,2,3,4], "B" : [5,6,7,8]})
# var2 = pd.DataFrame({"A" : [1,2,3,5], "C" : [10,20,30,40]})
# var3  = pd.merge(var1,var2,how = "left",indicator=True)
# print(var3)


# import pandas as pd
# var = pd.DataFrame({"name" : ["a","b","c","d","a","b","c","d"] , "marks" : [1,3,2,4,3,2,5,2]})
# var1 = var.groupby("marks")
# for x,y in var1:
#     print(x)
#     print(y)
#     print()

 
# import pandas as pd
# var1 = pd.read_csv("C:\\Users\\kanak\\Documents\\Chaithanya Education\\Personal Projects\\python-tutorials\\missing_values_data.csv")
# print(var1.head())

# import pandas as pd
# var1 = pd.read_csv("C:\\Users\\kanak\\Documents\\Chaithanya Education\\sample_data.csv")
# print(var1)


# import pandas as pd
# import numpy as np
# var1 = pd.DataFrame(np.random.randint(1,101,size=(1000,5)),columns = ["A","B","C","D","E"])
# var1.to_csv("random_data.csv",index = False)

# import pandas as pd
# import numpy as np
# var1 = pd.read_csv("C:\\Users\\kanak\\Documents\\Chaithanya Education\\Personal Projects\\python-tutorials\\random_data.csv")
# var1[["A", "B", "C", "D", "E"]] = var1[["A", "B", "C", "D", "E"]].applymap(lambda x: np.nan if x%2 ==0 else x )
# print(var1.head())
# var1.to_csv("random_values.csv", index = False)

# import pandas as pd
# import numpy as np
# var1 = pd.read_csv("C:\\Users\\kanak\\Documents\\Chaithanya Education\\Personal Projects\\python-tutorials\\random_values.csv")
# var2 = var1.fillna(var1.mean())
# print(var2)

# import pandas as pd
# var1 = pd.read_csv("C:\\Users\\kanak\\Downloads\\titanic\\test.csv")
# print(var1.isna().sum())

# import pandas as pd
# var1 = pd.read_csv("C:\\Users\\kanak\\Downloads\\titanic\\test.csv")
# var1["Family_size"] = var1["SibSp"] + var1["Parch"]
# print(var1)


# import pandas as pd
# data = {
#     "name": ["Alice", "Bob", "Charlie", "David", "Eve", "Frank"],
#     "salary": [50000, 70000, 60000, 90000, 75000, 65000],
#     "department": ["HR", "IT", "HR", "Finance", "IT", "Finance"]}
# df = pd.DataFrame(data)
# higest_paid = df["salary"].max()
# average_salary = df["salary"].mean()
# most_paid_dept = df.loc[df["salary"].idxmax(), "department"]
# print(most_paid_dept)

# import pandas as pd
# data = {
#     "date": pd.date_range(start="2024-03-01", periods=10, freq="D"),
#     "product": ["Laptop", "Mouse", "Keyboard", "Monitor", "Laptop", 
#                 "Mouse", "Keyboard", "Monitor", "Laptop", "Mouse"],
#     "quantity": [2, 5, 3, 1, 4, 7, 2, 3, 1, 8],
#     "price": [800, 25, 50, 200, 850, 20, 55, 190, 900, 30]
# }
# df = pd.DataFrame(data)
# df["revenue"] = df["quantity"] * df["price"]
# product_revenue = df.groupby("product")["revenue"].sum()
# top_3_products = product_revenue.nlargest(3)
# print(top_3_products)


# import pandas as pd
# data = {
#     "date": pd.date_range(start="2024-03-01", periods=10, freq="D"),
#     "product": ["Laptop", "Mouse", "Keyboard", "Monitor", "Laptop", 
#                 "Mouse", "Keyboard", "Monitor", "Laptop", "Mouse"],
#     "quantity": [2, 5, 3, 1, 4, 7, 2, 3, 1, 8],
#     "price": [800, 25, 50, 200, 850, 20, 55, 190, 900, 30]
# }
# df = pd.DataFrame(data)
# df["revenue"] = df["quantity"] * df["price"]



# import pandas as pd

# # Creating the 'orders' DataFrame
# orders_data = {
#     "order_id": [101, 102, 103, 104, 105],
#     "customer_id": [1, 2, 1, 3, 2],
#     "amount": [250, 400, 150, 300, 200],
#     "order_date": ["2024-03-01", "2024-03-02", "2024-03-03", "2024-03-04", "2024-03-05"]
# }
# orders = pd.DataFrame(orders_data)
# customers_data = {
#     "customer_id": [1, 2, 3],
#     "customer_name": ["Alice", "Bob", "Charlie"],
#     "city": ["New York", "Los Angeles", "Chicago"]
# }
# customers = pd.DataFrame(customers_data)
# df = pd.merge(orders,customers,on = "customer_id")
# order_amount = df.groupby("customer_name")["amount"].sum().reset_index()
# print(order_amount)


# import pandas as pd
# import seaborn as sns
# flights = sns.load_dataset("flights")
# flights["date"] = pd.to_datetime(flights["year"].astype(str) + "-" + flights["month"].astype(str))
# flights = flights.sort_values("date")
# flights["rolling_avg"] = flights["passengers"].rolling(window=3).mean()
# print(flights.head(10))


# import pandas as pd
# data = {
#     "date": pd.date_range(start="2024-03-01", periods=10, freq="D"),
#     "region": ["North", "South", "East", "West", "North", "South", "East", "West", "North", "South"],
#     "sales": [1000, 1500, 1200, 1800, 1600, 1400, 1300, 1700, 1100, 1550]
# }
# df = pd.DataFrame(data)
# df_pivot = df.pivot(index="date", columns="region", values="sales")
# perc = df_pivot.pct_change() * 100
# print(perc)

# import pandas as pd 
# import seaborn as sns
# df = sns.load_dataset("iris")
# print(df.melt())

# import pandas as pd
# import numpy as np
# date_range = pd.date_range(start="2020-01-01", end="2025-01-01", freq="D")
# np.random.seed(42) 
# random_values = np.random.randint(50, 500, size=len(date_range)) 
# df = pd.DataFrame({"date": date_range, "value": random_values})
# df["moving average"] = df["value"].rolling(window = 7).mean()
# highest = df.max()
# lowest = df.min()
# print(highest,lowest)

# import pandas as pd
# import numpy as np
# date_range = pd.date_range(start="2024-01-01", end="2024-03-01", freq="D")
# np.random.seed(42)
# stocks = ["AAPL", "GOOGL", "MSFT"]
# data = []
# for stock in stocks:
#     prices = np.random.randint(100, 500, size=len(date_range))
#     for date, price in zip(date_range, prices):
#         data.append([date, stock, price])
# df = pd.DataFrame(data, columns=["date", "stock", "price"])
# df["moving average"] = df["price"].rolling(window = 90).mean()
# print(df.head())
