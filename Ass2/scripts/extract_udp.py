import sys
cnt=0
while True:
	a = sys.stdin.readline()
	if a=='':
		print('cnt=')
		print(cnt)
		break
	if(a[len(a)-10:len(a)-1]!="length 28"):
		print(a)
		cnt=cnt+1