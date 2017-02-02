import os

bw=raw_input()
os.system("python /home/mininet/extract.py < h1_part2_tcp_c.txt > extract_h1_part2_tcp_c.txt")
os.system("python /home/mininet/extract.py < h2_part2_tcp_c.txt > extract_h2_part2_tcp_c.txt")
os.system("python /home/mininet/extract.py < s1_part2_tcp_eth1_c.txt > extract_s1_part2_tcp_eth1_c.txt")
os.system("python /home/mininet/extract.py < s1_part2_tcp_eth2_c.txt > extract_s1_part2_tcp_eth2_c.txt")
os.system("python /home/mininet/extract.py < s2_part2_tcp_eth1_c.txt > extract_s2_part2_tcp_eth1_c.txt")
os.system("python /home/mininet/extract.py < s2_part2_tcp_eth2_c.txt > extract_s2_part2_tcp_eth2_c.txt")
os.system("python /home/mininet/extract_udp.py < h1_part2_udp_c"+str(bw)+".txt > extract_h1_part2_udp_c"+str(bw)+".txt")
os.system("python /home/mininet/extract_udp.py < h2_part2_udp_c"+str(bw)+".txt > extract_h2_part2_udp_c"+str(bw)+".txt")
os.system("python /home/mininet/extract_udp.py < s1_part2_udp_eth1_c"+str(bw)+".txt > extract_s1_part2_udp_eth1_c"+str(bw)+".txt")
os.system("python /home/mininet/extract_udp.py < s1_part2_udp_eth2_c"+str(bw)+".txt > extract_s1_part2_udp_eth2_c"+str(bw)+".txt")
os.system("python /home/mininet/extract_udp.py < s2_part2_udp_eth1_c"+str(bw)+".txt > extract_s2_part2_udp_eth1_c"+str(bw)+".txt")
os.system("python /home/mininet/extract_udp.py < s2_part2_udp_eth2_c"+str(bw)+".txt > extract_s2_part2_udp_eth2_c"+str(bw)+".txt")
    
