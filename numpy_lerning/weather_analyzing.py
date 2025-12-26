import numpy as np

weather = np.random.randint(15,45, size=(4,7))
print("Temperatures:\n", weather)

# Averages
avg_city = np.round(np.average(weather, axis=0), 2)
avg_day  = np.round(np.average(weather, axis=1), 2)

print("Average per city:", avg_city)
print("Average per day:", avg_day)

# Max values
max_city = np.max(weather, axis=0)
day_max  = np.max(weather, axis=1)

# Hottest day
hottest_day_index = np.argmax(day_max)
hottest_temp = day_max[hottest_day_index]

print("Hottest day index:", hottest_day_index)
print("Hottest temperature:", hottest_temp)

# Heatwave days (all cities > 40)
heatwave_days = (weather > 40).all(axis=1)
print("Heatwave days:", heatwave_days)

# Heatwave cities (any day > 40)
heatwave_city = (weather > 40).any(axis=0)
print("Heatwave cities:", heatwave_city)

# Reduce extreme temperature
weather[weather >= 42] -= 2

# Hottest city (total)
total_city = np.sum(weather, axis=0)
hottest_city_index = np.argmax(total_city)
hottest_city_total = total_city[hottest_city_index]

print("Hottest city index:", hottest_city_index)
print("Total temp of hottest city:", hottest_city_total)
