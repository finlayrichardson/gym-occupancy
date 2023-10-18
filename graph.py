import matplotlib.pyplot as plt
import json

dictionary = json.load(open('results.json', 'r'))
for day in dictionary.items():
    x = [time for time, _ in day[1].items()]
    y = [int(value) for _, value in day[1].items()]
    plt.bar(x, y, color='maroon')
    plt.xlim(('06:30', '22:30'))
    plt.xticks(['06:30', '10:30', '14:30', '18:30', '22:30'])
    plt.xlabel('time')
    plt.ylabel('occupancy')
    plt.title(day[0])
    plt.savefig(f"./images/{day[0]}")
    plt.close()
