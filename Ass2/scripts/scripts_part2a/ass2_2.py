import os

bw=raw_input()
os.system("python /home/mininet/extract.py < h1_part2_tcp_a.txt > extract_h1_part2_tcp_a.txt")
os.system("python /home/mininet/extract.py < h2_part2_tcp_a.txt > extract_h2_part2_tcp_a.txt")
os.system("python /home/mininet/extract.py < s1_part2_tcp_eth1_a.txt > extract_s1_part2_tcp_eth1_a.txt")
os.system("python /home/mininet/extract.py < s1_part2_tcp_eth2_a.txt > extract_s1_part2_tcp_eth2_a.txt")
os.system("python /home/mininet/extract.py < s2_part2_tcp_eth1_a.txt > extract_s2_part2_tcp_eth1_a.txt")
os.system("python /home/mininet/extract.py < s2_part2_tcp_eth2_a.txt > extract_s2_part2_tcp_eth2_a.txt")
os.system("python /home/mininet/extract_udp.py < h1_part2_udp_a"+str(bw)+".txt > extract_h1_part2_udp_a"+str(bw)+".txt")
os.system("python /home/mininet/extract_udp.py < h2_part2_udp_a"+str(bw)+".txt > extract_h2_part2_udp_a"+str(bw)+".txt")
os.system("python /home/mininet/extract_udp.py < s1_part2_udp_eth1_a"+str(bw)+".txt > extract_s1_part2_udp_eth1_a"+str(bw)+".txt")
os.system("python /home/mininet/extract_udp.py < s1_part2_udp_eth2_a"+str(bw)+".txt > extract_s1_part2_udp_eth2_a"+str(bw)+".txt")
os.system("python /home/mininet/extract_udp.py < s2_part2_udp_eth1_a"+str(bw)+".txt > extract_s2_part2_udp_eth1_a"+str(bw)+".txt")
os.system("python /home/mininet/extract_udp.py < s2_part2_udp_eth2_a"+str(bw)+".txt > extract_s2_part2_udp_eth2_a"+str(bw)+".txt")
    
