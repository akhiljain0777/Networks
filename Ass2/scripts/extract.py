import sys
cnt=0
while True:
	a = sys.stdin.readline()
	if a=='':
		print('cnt=')
		print(cnt)
		break
	if(a[len(a)-9:len(a)-1]!="length 0"):
		print(a)
		cnt=cnt+1