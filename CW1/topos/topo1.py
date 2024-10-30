#!/usr/bin/python3

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.util import dumpNodeConnections
from mininet.cli import CLI
# from mininet.node import OVSController

class part1_topo(Topo):
    def build(self):
        switch1 = self.addSwitch('switch1')
        host1 = self.addHost('host1', mac='00:00:00:00:00:01', ip='192.168.0.1/24')
        host2 = self.addHost('host2', mac='00:00:00:00:00:02', ip='192.168.0.2/24')
        host3 = self.addHost('host3', mac='00:00:00:00:00:03', ip='192.168.0.3/24')
        host4 = self.addHost('host4', mac='00:00:00:00:00:04', ip='192.168.0.4/24')
        self.addLink(host1, switch1)
        self.addLink(host2, switch1)
        self.addLink(host3, switch1)
        self.addLink(host4, switch1)


topos = {"part1": part1_topo}

if __name__ == "__main__":
    t = part1_topo()
    net = Mininet(topo=t
                #   , controller=OVSController
                  )
    net.start()
    CLI(net)
    net.stop()
