import pandas
data = pandas.read_csv("data.csv")
color_data = data["Primary Fur Color"].tolist()
grey_count = len([item for item in color_data if item == "Gray"])
cinnamon_count = len([item for item in color_data if item == "Cinnamon"])
black_count = len([item for item in color_data if item == "Black"])

squirrel_data = {"Fur Color": ["grey", "red", "black"], "Count": [grey_count, cinnamon_count, black_count]}

df = pandas.DataFrame(data=squirrel_data).to_csv("squirrel_count.csv")


# Expertise code doing the same thing !!
# squirrel_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# squirrel_series = squirrel_data["Primary Fur Color"].value_counts()
# squirrel_dict = squirrel_series.to_dict()
#
# # Create a squirrel dataframe
# squirrel_count_dict = {
#     "Fur Color": ["grey", "red", "black"],
#     "Count": [squirrel_dict["Gray"], squirrel_dict["Cinnamon"], squirrel_dict["Black"]]
# }
#
# data = pandas.DataFrame(squirrel_count_dict)
# data.to_csv("squirrel_count.csv")