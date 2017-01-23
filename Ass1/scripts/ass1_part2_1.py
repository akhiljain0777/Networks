from mininet.topo import Topo
from mininet.net import Mininet
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel
from mininet.node import CPULimitedHost
from mininet.link import TCLink

class MyTopo( Topo ):
    
    def __init__( self ):
        Topo.__init__( self )
        bandWidth=[0.512,1,2]
        DELAYS=['1ms','10ms','100ms']
        h1host=self.addHost('h1')
        h2host=self.addHost('h2')
        s1switch=self.addSwitch('s1')
        s2switch=self.addSwitch('s2')
        self.addLink(h1host,s1switch,bw=3,delay='1ms')
        self.addLink(h2host,s2switch,bw=3,delay='1ms')
        self.addLink(s1switch,s2switch,bw=0.5,delay='1ms')

        

topos = { 'mytopo': ( lambda: MyTopo() ) }
