from mininet.topo import Topo
from mininet.net import Mininet
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel
from mininet.node import CPULimitedHost
from mininet.link import TCLink

class MyTopo( Topo ):
    
    def __init__( self ):
        Topo.__init__( self )
        h1host=self.addHost('h1')
        h2host=self.addHost('h2')
        s1switch=self.addSwitch('s1')
        self.addLink(h1host,s1switch,bw=q,delay='1ms')
        self.addLink(s1switch,h2host,bw=1,delay='1ms')

        

topos = { 'mytopo': ( lambda: MyTopo() ) }
