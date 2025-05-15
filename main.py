import numpy as np
import matplotlib.pyplot as plt
"""
X_data = np.random.random(1000) * 100
y_data = np.random.random(1000) * 100

#print(X_data, y_data)

plt.scatter(X_data, y_data, c="#FF00FF", marker='*', alpha=0.3)
plt.show()
"""

"""
years = [2006 + x for x in range(16)]
weights = [80, 83, 84, 85, 86, 82, 81, 79,
           83, 80, 82, 82, 83, 81, 80, 79]


plt.plot(years, weights, "r--", lw=10)
plt.show()
"""

"""
x = ["C++", "C#", "Python", "Java", "Go"]
y = [20, 50, 140, 1, 45]

plt.bar(x, y, color='c', width=0.9, edgecolor='g')
plt.show()
"""

"""
ages = np.random.normal(20, 1.5, 1000)
#print(ages)

plt.hist(ages,
         bins=20,
         cumulative=True)
plt.show()
"""

"""
langs = ["Python", "C++", "Java", "C#", "Go"]
votes = [50, 24, 14, 6, 17]
#explodes = [vote / sum(votes) for vote in votes]
explodes = [0, 0, 0, 0.2, 0]

plt.pie(votes, labels=langs, explode=explodes,
        autopct="%.2f%%", pctdistance=1.3, startangle=90)
plt.show()
"""

"""
#heights = np.random.normal(172, 8, 300)
#print(heights)

first = np.linspace(0, 10, 25)
second = np.linspace(10, 200, 25)
third = np.linspace(200, 210, 25)
fourth = np.linspace(210, 230, 25)

data = np.concatenate((first, second, third, fourth))

plt.boxplot(data)
plt.show()
"""

"""
years = [2014, 2015, 2016, 2017,
        2018, 2019, 2020, 2021]
income = [55, 56, 62, 61,
          72, 72, 73, 75]

income_ticks = list(range(50, 81, 2))

plt.plot(years, income)
plt.title("Income of John (in $USD)", fontsize=24, fontname="FreeSerif")
plt.xlabel("Year")
plt.ylabel("Yearly income in USD")
plt.yticks(income_ticks, [f"{x}k USD" for x in income_ticks])

plt.show()
"""