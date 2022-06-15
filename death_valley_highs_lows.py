import csv
from datetime import datetime
import matplotlib.pyplot as plt


filename='data/death_valley_2018_simple.csv'
with open(filename) as f:
    reader=csv.reader(f)
    header_row=next(reader)

#Bu dosyadan en yüksek ve en düşük sıcaklıkları al.
    highs,lows,dates =[],[],[]

    for row in reader:
        high=int(row[4])
        low=int(row[4])
        current_date=datetime.strptime(row[2],'%Y-%m-%d')

        highs.append(high)
        lows.append(low)
        dates.append(current_date)

#En yüksek sıcaklıkları ve en düşük sıcaklıkları tarihlere göre çizdir.
plt.style.use('seaborn')
fig, ax=plt.subplots()
ax.plot(dates,highs,c='red',alpha=0.5)
ax.plot(dates,lows,c='blue',alpha=0.5)
plt.fill_between(dates,highs,lows,facecolor='blue',alpha=0.1)

#Grafiği formatla
plt.title("Daily high and low temperatures - 2018", fontsize=24)
plt.xlabel('',fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)",fontsize=16)
plt.tick_params(axis='both',which='major',labelsize=16)

plt.show()