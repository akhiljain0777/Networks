import os

bw=raw_input()
os.system("python /home/mininet/extract.py < h1_part2_tcp-b.txt > extract_h1_part2_tcp-b.txt")
os.system("python /home/mininet/extract.py < h2_part2_tcp-b.txt > extract_h2_part2_tcp-b.txt")
os.system("python /home/mininet/extract.py < s1_part2_tcp_eth1-b.txt > extract_s1_part2_tcp_eth1-b.txt")
os.system("python /home/mininet/extract.py < s1_part2_tcp_eth2-b.txt > extract_s1_part2_tcp_eth2-b.txt")
os.system("python /home/mininet/extract.py < s2_part2_tcp_eth1-b.txt > extract_s2_part2_tcp_eth1-b.txt")
os.system("python /home/mininet/extract.py < s2_part2_tcp_eth2-b.txt > extract_s2_part2_tcp_eth2-b.txt")
os.system("python /home/mininet/extract_udp.py < h1_part2_udp-b"+str(bw)+".txt > extract_h1_part2_udp-b"+str(bw)+".txt")
os.system("python /home/mininet/extract_udp.py < h2_part2_udp-b"+str(bw)+".txt > extract_h2_part2_udp-b"+str(bw)+".txt")
os.system("python /home/mininet/extract_udp.py < s1_part2_udp_eth1-b"+str(bw)+".txt > extract_s1_part2_udp_eth1-b"+str(bw)+".txt")
os.system("python /home/mininet/extract_udp.py < s1_part2_udp_eth2-b"+str(bw)+".txt > extract_s1_part2_udp_eth2-b"+str(bw)+".txt")
os.system("python /home/mininet/extract_udp.py < s2_part2_udp_eth1-b"+str(bw)+".txt > extract_s2_part2_udp_eth1-b"+str(bw)+".txt")
os.system("python /home/mininet/extract_udp.py < s2_part2_udp_eth2-b"+str(bw)+".txt > extract_s2_part2_udp_eth2-b"+str(bw)+".txt")
    
