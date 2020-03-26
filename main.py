import os
import re
from datetime import datetime
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import collections

dic = {}
regex = re.compile(
    '((Jan)|(Feb)|(Mar)|(Apr)|(May)|(Jun)|(Jul)|(Aug)|(Sep)|(Oct)|(Nov)|(Dec)) ([1-3][0-9]|[1-9]), (201[1-9]),')
root = 'F:\\CS\\New folder\\messages\\inbox'
filename = 'message_1.html'
for root, dirs, files in os.walk("F:\\CS\\New folder\\messages\\inbox"):
    for filename in files:
        filepath = root + os.sep + filename
        if(filename.endswith(".html")):
            f = open(filepath, "r", encoding="utf8")
            text = f.read()
            f.close()
            clean = re.sub('<[^>]+>', '|', text)
            clean = re.sub('{[^>]+}', '@', clean)
            clean = re.sub('\|+', '\n', clean)
            f = open(filepath+'.txt', "w",
                     encoding="utf8")
            f.write(clean)
            f.close()
            with open(filepath+'.txt', "r",
                      encoding="utf8") as f:
                for line in f:
                    if (line.startswith('Brian Li')):
                        found = 0
                        while not (found):
                            line = next(f)
                            if (regex.match(line)):
                                date = line.split(' ')
                                date = [date[0], date[2][:-1]]
                                date = ' '.join(date)
                                date = datetime.strptime(date, '%b %Y')
                                if (date in dic.keys()):
                                    dic[date] = dic[date] + 1
                                else:
                                    dic[date] = 1
                                found = 1
            f.close()
l = sorted(dic.items(), key=lambda x: x[0])
dates = [x[0] for x in l]
occ = [x[1] for x in l]
print(dates)
print(occ)
plt.bar(dates, occ, width=10, color='b')
plt.xticks(rotation=90)
plt.xlabel('Date')
plt.ylabel('No of Message Exchanges')
plt.title('Message Exchanges over time')
plt.show()


