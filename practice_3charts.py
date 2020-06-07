# three_charts.py

#
# CHART 1 (PIE)
#

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

pie_data = [
    {"company": "Company X", "market_share": 0.55},
    {"company": "Company Y", "market_share": 0.30},
    {"company": "Company Z", "market_share": 0.15}]

# market_share = [1, 2, 3]
# company = ["Company X", "Company Y", "Company Z"]
market_share_one = []
company_name = []

for m in pie_data:
    market_share_one.append(m["market_share"])
    company_name.append(m["company"])

print("----------------")
print("GENERATING PIE CHART...")
print(pie_data)  # TODO: create a pie chart based on the pie_data)


plt.pie(market_share_one, labels=company_name,

        autopct='% 1.1f %%', shadow=True, startangle=90)
plt.title("Market_Share_Data")
plt.show()


#
# CHART 2 (LINE)
#
line_data = [
    {"date": "2019-01-01", "stock_price_usd": 100.00},
    {"date": "2019-01-02", "stock_price_usd": 101.01},
    {"date": "2019-01-03", "stock_price_usd": 120.20},
    {"date": "2019-01-04", "stock_price_usd": 107.07},
    {"date": "2019-01-05", "stock_price_usd": 142.42},
    {"date": "2019-01-06", "stock_price_usd": 135.35},
    {"date": "2019-01-07", "stock_price_usd": 160.60},
    {"date": "2019-01-08", "stock_price_usd": 162.62},
]

date_time = []
stock_price = []

print("----------------")
print("GENERATING LINE GRAPH...")
print(line_data)  # TODO: create a line graph based on the line_data

for l in line_data:
    date_time.append(l["date"])
    stock_price.append(l["stock_price_usd"])

plt.plot(date_time, stock_price)


plt.xlabel("date_time")
plt.ylabel("stock_price")
plt.title("My_Line_Chart")

plt.show()


#
# CHART 3 (HORIZONTAL BAR)
#

bar_data = [
    {"genre": "Thriller", "viewers": 123456},
    {"genre": "Mystery", "viewers": 234567},
    {"genre": "Sci-Fi", "viewers": 987654},
    {"genre": "Fantasy", "viewers": 876543},
    {"genre": "Documentary", "viewers": 283105},
    {"genre": "Action", "viewers": 544099},
    {"genre": "Romantic Comedy", "viewers": 121212}
]


genre_name = []
viewers = []
print("----------------")
print("GENERATING BAR CHART...")
print(bar_data)  # TODO: create a horizontal bar chart based on the bar_data

for m in bar_data:
    genre_name.append(m["genre"])
    viewers.append(m["viewers"])


# y_pos = np.arange(genre_name)
# x_pos = np.arange(viewers)

plt.barh(genre_name, viewers)

plt.xlabel("number_of_viewers")
plt.ylabel("genre")
plt.title("Box_Office")


plt.show()
