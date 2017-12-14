import os.path
import git
import sys
import matplotlib.pyplot as plt
import sqlite3

x = []
y = []
connection = sqlite3.connect('results.db')
cursor1 = connection.execute("SELECT WORKER, TimeTaken FROM WORKERS")
for row in cursor1.fetchall():
    x.append(row[0])
    y.append(row[1])
        #print x
        #print y

print x
print y

    #y_pos = np.arange(len(x))
plt.plot(x, y, 'r')
plt.xlabel('Number of Workers')
plt.ylabel('Time')
plt.title('Performance of Workers')
plt.bar(x, y)
plt.show()
