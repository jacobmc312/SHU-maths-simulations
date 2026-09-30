import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime

filename = "Carbon_Intensity_Data.csv"
data = np.genfromtxt(filename, delimiter=',', dtype=str, skip_header=1)
fields = np.genfromtxt(filename, delimiter=',', dtype=str, max_rows=1)
print(fields)

dates = []
actual_carbon = []

for row in data:
    dates.append(datetime.strptime(row[0], '%Y-%m-%dT%H:%MZ'))
    actual_carbon.append(int(row[1]))

plt.plot(dates, actual_carbon)
plt.xlabel('Date/time')
plt.ylabel('Actual Carbon')
plt.title('Carbon Intensity Data')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


