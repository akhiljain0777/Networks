
from mininet.topo import Topo

from mininet.net import Mininet
from mininet.node import CPULimitedHost
from mininet.link import TCLink
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel
from mininet.cli import CLI


class SingleSwitchTopo(Topo):

    "Single switch connected to n hosts."
    def build(self, n=2):
        s1 = self.addSwitch('s1')
  #  s2 = self.addSwitch('s2')
        h1 = self.addHost('h1',cpu=.25)
        h2 = self.addHost('h2',cpu=.25)  
#        for h in range(n):
            # Each host gets 50%/n of system CPU
#            host = self.addHost('h%s' % (h + 1),
#               cpu=.5/n)
            # 10 Mbps, 5ms delay, 10% loss, 1000 packet queue
            #self.addLink(host, switch,
             #  bw=10, delay='5ms', loss=10, max_queue_size=1000, use_htb=True)
        self.addLink(h1,s1,bw=1,delay='1ms',loss=1,use_htb=True)
        self.addLink(h2,s1,bw=1,delay='1ms',loss=2,use_htb=True)
   # self.addLink(s1,s2,bw=1,delay='1ms',loss=loss,use_htb=True)

def perfTest():
    "Create network and run simple performance test"
    topo = SingleSwitchTopo()
    net = Mininet(topo=topo, 
                  host=CPULimitedHost, link=TCLink)
    net.start()
#    CLI(net)
#    print "Dumping host connections"
#    dumpNodeConnections(net.hosts)
   # print "Testing network connectivity",lost
#    net.pingAll()
   # print "Testing bandwidth between h2 and h1"
    h2, h1 = net.get('h2', 'h1')
    h1.cmd('sudo tcpdump -n -i h1-eth0 > h1_tcp.txt &')
    h2.cmd('sudo tcpdump -n -i h2-eth0 > h2_tcp.txt &')
    net.iperf((h2, h1))
    #print "Testing udp"
    for k in range(8):
        h1.cmd('sudo tcpdump -n -i h1-eth0 > h1_udp_'+ str(k) +'_1.txt &')
        h2.cmd('sudo tcpdump -n -i h2-eth0 > h2_udp_'+ str(k) +'_1.txt &')
        stat = 64 * pow(2,k)
        print "udp bandwidth",stat
        net.iperf((h2,h1),'UDP',str(stat)+'K')
                
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    #perfTest(0.5,'1ms')
    #pe
    perfTest()    
