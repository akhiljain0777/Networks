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
		print((finish-start))
		print("no of packets=",cnt)
		print("data=",cnt*1470)
		print("throughput=",float(cnt*1470)/float((finish-start).total_seconds()))
		break
	if(a[len(a)-9:len(a)-1]!="length 0" and a[len(a)-10:len(a)-1]!="length 28" and a!="\n" ):
		if(cnt==0):
			start=datetime.strptime(a[0:14], '%H:%M:%S.%f')
		finish=datetime.strptime(a[0:14], '%H:%M:%S.%f')
		cnt=cnt+1