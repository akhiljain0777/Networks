import os

list=[64,128,256,512,1024,2048,4096]
os.system("python /home/mininet/extract.py < h1_part2_tcp_d.txt > extract_h1_part2_tcp_d.txt")
os.system("python /home/mininet/extract.py < h2_part2_tcp_d.txt > extract_h2_part2_tcp_d.txt")
os.system("python /home/mininet/extract.py < s1_part2_tcp_eth1_d.txt > extract_s1_part2_tcp_eth1_d.txt")
os.system("python /home/mininet/extract.py < s1_part2_tcp_eth2_d.txt > extract_s1_part2_tcp_eth2_d.txt")
os.system("python /home/mininet/extract.py < s2_part2_tcp_eth1_d.txt > extract_s2_part2_tcp_eth1_d.txt")
os.system("python /home/mininet/extract.py < s2_part2_tcp_eth2_d.txt > extract_s2_part2_tcp_eth2_d.txt")
for bw in list:
	os.system("python /home/mininet/extract_udp.py < h1_part2_udp_d"+str(bw)+".txt > extract_h1_part2_udp_d"+str(bw)+".txt")
	os.system("python /home/mininet/extract_udp.py < h2_part2_udp_d"+str(bw)+".txt > extract_h2_part2_udp_d"+str(bw)+".txt")
	os.system("python /home/mininet/extract_udp.py < s1_part2_udp_eth1_d"+str(bw)+".txt > extract_s1_part2_udp_eth1_d"+str(bw)+".txt")
	os.system("python /home/mininet/extract_udp.py < s1_part2_udp_eth2_d"+str(bw)+".txt > extract_s1_part2_udp_eth2_d"+str(bw)+".txt")
	os.system("python /home/mininet/extract_udp.py < s2_part2_udp_eth1_d"+str(bw)+".txt > extract_s2_part2_udp_eth1_d"+str(bw)+".txt")
	os.system("python /home/mininet/extract_udp.py < s2_part2_udp_eth2_d"+str(bw)+".txt > extract_s2_part2_udp_eth2_d"+str(bw)+".txt")
    
