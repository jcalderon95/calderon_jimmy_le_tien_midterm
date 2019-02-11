import numpy as np
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt; plt.rcdefaults()

 
# data to plot
n_groups = 5
rainbow_trout = (100000, 150000, 100000, 50000, 150000)
brown_trout = (100000, 80000, 70000, 80000, 100000)
 
# create plot
fig, ax = plt.subplots()
index = np.arange(n_groups)
bar_width = 0.35
opacity = 0.7
 
rects1 = plt.bar(index, rainbow_trout, bar_width,
alpha=opacity,
color='green',
label='Rainbow Trout')
 
rects2 = plt.bar(index + bar_width, brown_trout, bar_width,
alpha=opacity,
color='grey',
label='Brown Trout')
 
plt.xlabel('Years')
plt.ylabel('Number of eggs received')
plt.title('Number of eggs received from 2014 to 2018')
plt.xticks(index + bar_width, ('2014', '2015', '2016', '2017','2018'))
plt.legend()
 
plt.tight_layout()
plt.show()