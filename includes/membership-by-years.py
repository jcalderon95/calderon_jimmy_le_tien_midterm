import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
 
years = ('2002', '2003', '2004', '2005','2006', '2007', '2008', '2009','2010', '2011','2012', '2013', '2014', '2015','2016', '2017','2018')
y_pos = np.arange(len(years))
membership = [52,
48,
67,
45,
45,
50,
55,
67,
65,
70,
60,
60,
55,
60,
65,
75,
80]
 
plt.bar(y_pos, membership, align='center', alpha=0.5, color='green')
plt.xticks(y_pos, years)
plt.ylabel('Number of members')
plt.xlabel('Years')
plt.title('Number of Membership by years')
 
plt.show()