import os

list=[64,128,256,512,1024,2048,4096]
os.system("python /home/mininet/extract.py < h1_part2_tcp_g.txt > extract_h1_part2_tcp_g.txt")
os.system("python /home/mininet/extract.py < h2_part2_tcp_g.txt > extract_h2_part2_tcp_g.txt")
os.system("python /home/mininet/extract.py < s1_part2_tcp_gth1_g.txt > extract_s1_part2_tcp_gth1_g.txt")
os.system("python /home/mininet/extract.py < s1_part2_tcp_gth2_g.txt > extract_s1_part2_tcp_gth2_g.txt")
os.system("python /home/mininet/extract.py < s2_part2_tcp_gth1_g.txt > extract_s2_part2_tcp_gth1_g.txt")
os.system("python /home/mininet/extract.py < s2_part2_tcp_gth2_g.txt > extract_s2_part2_tcp_gth2_g.txt")
for bw in list:
	os.system("python /home/mininet/extract_udp.py < h1_part2_udp_g"+str(bw)+".txt > extract_h1_part2_udp_g"+str(bw)+".txt")
	os.system("python /home/mininet/extract_udp.py < h2_part2_udp_g"+str(bw)+".txt > extract_h2_part2_udp_g"+str(bw)+".txt")
	os.system("python /home/mininet/extract_udp.py < s1_part2_udp_gth1_g"+str(bw)+".txt > extract_s1_part2_udp_gth1_g"+str(bw)+".txt")
	os.system("python /home/mininet/extract_udp.py < s1_part2_udp_gth2_g"+str(bw)+".txt > extract_s1_part2_udp_gth2_g"+str(bw)+".txt")
	os.system("python /home/mininet/extract_udp.py < s2_part2_udp_gth1_g"+str(bw)+".txt > extract_s2_part2_udp_gth1_g"+str(bw)+".txt")
	os.system("python /home/mininet/extract_udp.py < s2_part2_udp_gth2_g"+str(bw)+".txt > extract_s2_part2_udp_gth2_g"+str(bw)+".txt")
    
