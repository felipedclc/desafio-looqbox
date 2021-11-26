# Libraries
from typing import Counter
import numpy as np
import matplotlib.pyplot as plt

from read import Reader


read = Reader()
arr = read.read_JSON("data/top_20_scify_imdb_reportlooqbox_challenge.json")
# films = []
years = []
for dicts in arr:
    for film, year in dicts.items():
        # films.append(film)
        years.append(year)

count_of_years = []
years_of_films = []
for year, count in Counter(years).items():
    count_of_years.append(count)
    years_of_films.append(year)


# Make a random dataset:
y_pos = np.arange(len(count_of_years))

# Create bars
plt.bar(y_pos, count_of_years)

# Create names on the x-axis
plt.xticks(y_pos, years_of_films)

# Show graphic
plt.show()
