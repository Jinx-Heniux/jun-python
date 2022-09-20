"""
week_temps_f is a string with a list of fahrenheit temperatures separated by the , sign. 
Write code that uses the accumulation pattern to compute the average 
(sum divided by number of items) and assigns it to avg_temp. 
Do not hard code your answer 
(i.e., make your code compute both the sum or the number of items in week_temps_f) 
(You should use the .split(",") function to split by "," and float() to cast to a float).
"""

week_temps_f = "75.1,77.7,83.2,82.5,81.0,79.5,85.7"

# lst = week_temps_f.split(",")
# lst = [float(item) for item in lst]

lst = [float(x) for x in week_temps_f.split(",")]

sum = 0.0
for i in lst:
    sum += i
avg_temp = sum / len(lst)

print(f"sum: {sum}, avg: {avg_temp}")

# sum: 564.7, avg: 80.67142857142858