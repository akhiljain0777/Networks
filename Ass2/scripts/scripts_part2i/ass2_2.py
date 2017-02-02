import os

list=[64,128,256,512,1024,2048,4096]
os.system("python /home/mininet/extract.py < h1_part2_tcp_i.txt > extract_i1_part2_tcp_i.txt")
os.system("python /home/mininet/extract.py < h2_part2_tcp_i.txt > extract_i2_part2_tcp_i.txt")
os.system("python /home/mininet/extract.py < s1_part2_tcp_ith1_i.txt > extract_s1_part2_tcp_ith1_i.txt")
os.system("python /home/mininet/extract.py < s1_part2_tcp_ith2_i.txt > extract_s1_part2_tcp_ith2_i.txt")
os.system("python /home/mininet/extract.py < s2_part2_tcp_ith1_i.txt > extract_s2_part2_tcp_ith1_i.txt")
os.system("python /home/mininet/extract.py < s2_part2_tcp_ith2_i.txt > extract_s2_part2_tcp_ith2_i.txt")
for bw in list:
	os.system("python /home/mininet/extract_udp.py < h1_part2_udp_i"+str(bw)+".txt > extract_i1_part2_udp_i"+str(bw)+".txt")
	os.system("python /home/mininet/extract_udp.py < h2_part2_udp_i"+str(bw)+".txt > extract_i2_part2_udp_i"+str(bw)+".txt")
	os.system("python /home/mininet/extract_udp.py < s1_part2_udp_ith1_i"+str(bw)+".txt > extract_s1_part2_udp_ith1_i"+str(bw)+".txt")
	os.system("python /home/mininet/extract_udp.py < s1_part2_udp_ith2_i"+str(bw)+".txt > extract_s1_part2_udp_ith2_i"+str(bw)+".txt")
	os.system("python /home/mininet/extract_udp.py < s2_part2_udp_ith1_i"+str(bw)+".txt > extract_s2_part2_udp_ith1_i"+str(bw)+".txt")
	os.system("python /home/mininet/extract_udp.py < s2_part2_udp_ith2_i"+str(bw)+".txt > extract_s2_part2_udp_ith2_i"+str(bw)+".txt")
    
