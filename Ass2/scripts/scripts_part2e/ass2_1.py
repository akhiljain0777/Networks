 #!/usr/bin/python


from mininet.topo import Topo

from mininet.net import Mininet
from mininet.node import CPULimitedHost
from mininet.link import TCLink
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel
from mininet.cli import CLI
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel
from mininet.node import CPULimitedHost
from mininet.link import TCLink
import os


class MyTopo( Topo ):
	print "Simple topology example."

	def __init__( self ):
		"Create custom topo."

		# Initialize topology
		Topo.__init__( self )

		switch1 = self.addSwitch('s1')
		switch2 = self.addSwitch('s2')
		host1= self.addHost('h1')
		host2= self.addHost('h2')

		self.addLink(host1,switch1,bw=3, delay='1ms',loss=1)
		self.addLink(switch1,switch2,bw=1, delay='10ms',loss=1)
		self.addLink(switch2,host2,bw=3, delay='1ms',loss=2)
		

def perf_udp():
    bw=raw_input()
    topo = MyTopo()
    net = Mininet(topo=topo, 
                  host=CPULimitedHost, link=TCLink)
    net.start()
    h1,h2,s1,s2=net.get('h1','h2','s1','s2')
    h1.cmd('net')
    h1.cmd('sudo tcpdump -n -i h1-eth0 > h1_part2_udp_e'+str(bw)+'.txt &')
    h2.cmd('sudo tcpdump -n -i h2-eth0 > h2_part2_udp_e'+str(bw)+'.txt &')
    s1.cmd('sudo tcpdump -n -i s1-eth1 > s1_part2_udp_eth1_e'+str(bw)+'.txt &')
    s1.cmd('sudo tcpdump -n -i s1-eth2 > s1_part2_udp_eth2_e'+str(bw)+'.txt &')
    s2.cmd('sudo tcpdump -n -i s2-eth1 > s2_part2_udp_eth1_e'+str(bw)+'.txt &')
    s2.cmd('sudo tcpdump -n -i s2-eth2 > s2_part2_udp_eth2_e'+str(bw)+'.txt &')
    net.iperf((h1,h2),'UDP',str(bw)+'K')
    net.stop()
    
def perf():
    topo = MyTopo()
    net = Mininet(topo=topo, 
                  host=CPULimitedHost, link=TCLink)
    net.start()
    
    h1,h2,s1,s2=net.get('h1','h2','s1','s2')
    h1.cmd('sudo tcpdump -n -i h1-eth0 > h1_part2_tcp_e.txt &')
    h2.cmd('sudo tcpdump -n -i h2-eth0 > h2_part2_tcp_e.txt &')
    s1.cmd('sudo tcpdump -n -i s1-eth1 > s1_part2_tcp_eth1_e.txt &')
    s1.cmd('sudo tcpdump -n -i s1-eth2 > s1_part2_tcp_eth2_e.txt &')
    s2.cmd('sudo tcpdump -n -i s2-eth1 > s2_part2_tcp_eth1_e.txt &')
    s2.cmd('sudo tcpdump -n -i s2-eth2 > s2_part2_tcp_eth2_e.txt &')
    net.iperf((h1,h2))
    net.stop()

    

#perf()
perf_udp()