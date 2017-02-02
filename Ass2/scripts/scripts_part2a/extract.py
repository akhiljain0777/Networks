import sys
from datetime import datetime
import re
cnt=0
start=0
finish=0
data=0
while True:
	a = sys.stdin.readline()
	if a=='':
		print(int(data[0]))
		print((finish-start))
		print("no of packets=%d",cnt)
		print("throughput=%lf",float(data[0])/float((finish-start).total_seconds()))
		break
	if(a[len(a)-9:len(a)-1]!="length 0" and a[len(a)-10:len(a)-1]!="length 28" and a!="\n" ):
		if(cnt==0):
			start=datetime.strptime(a[0:14], '%H:%M:%S.%f')
		finish=datetime.strptime(a[0:14], '%H:%M:%S.%f')
		a=(a[a.find("seq"):len(a)])
		a=a[a.find(":"):len(a)]
		a=a[0:a.find(",")]
		cnt=cnt+1
		data=re.findall(r'\d+', a)