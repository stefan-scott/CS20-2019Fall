import random

forecasts = []
#fill up with proportional options

for i in range(50):
    forecasts.append("Sun")

for i in range(25):
    forecasts.append("Clouds")

for i in range(20):
    forecasts.append("Rain")

for i in range(5):
    forecasts.append("Snow")
    
def weather():
    return random.choice(forecasts)

num_snows = 0
NUM_RUNS = 1000000
for i in range(NUM_RUNS):
    current_weather = weather()
    if current_weather == "Snow":
        num_snows += 1

print("Number of Snows:", num_snows)
print("Percentage:", float(num_snows)/NUM_RUNS*100)




