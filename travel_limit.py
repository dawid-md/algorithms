def num_countries_in_days(max_days, factor):
    time_left = max_days
    count = 0
    time_in_country = 1
    x = 0

    while x <= time_left:
        count += 1
        x = x + time_in_country
        time_in_country *= factor
    return  count - 1

def num_countries_in_days1(max_days, factor):
    time_left = max_days
    count = 0
    time_in_country = 1

    while time_left >= time_in_country:
        count += 1
        time_left -= time_in_country
        time_in_country *= factor
    return count

print(num_countries_in_days1(10, 1.2))