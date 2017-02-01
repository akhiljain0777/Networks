 #!/usr/bin/python

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel
from mininet.node import CPULimitedHost
from mininet.link import TCLink



class MyTopo( Topo ):
	print "Simple topology example."

	def __init__( self ):
		"Create custom topo."

		# Initialize topology
		Topo.__init__( self )
		n=0
		switch1 = self.addSwitch('s1')
		host1= self.addHost('h1')
		host2= self.addHost('h2')

		self.addLink(host1,switch1,bw=1, delay='1ms',loss=1)
		self.addLink(host2,switch1,bw=1, delay='1ms',loss=2)
		


topos = { 'mytopo': ( lambda: MyTopo() ) }
