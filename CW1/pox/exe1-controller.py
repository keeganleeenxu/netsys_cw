# Part 3 of Coursework 1
#
# based on Project 1 from UW's CSEP-561

from pox.core import core
import pox.openflow.libopenflow_01 as of
from pox.lib.packet.ethernet import ethernet
from pox.lib.packet.ipv4 import ipv4

log = core.getLogger()


class Firewall(object):
    """
    A Firewall object is created for each switch that connects.
    A Connection object for that switch is passed to the __init__ function.
    """

    def __init__(self, connection):
        # Keep track of the connection to the switch so that we can
        # send it messages!
        self.connection = connection

        # This binds our PacketIn event listener
        connection.addListeners(self)

        # add switch rules here
        self.rules()
        
    def rules(self):
        # allow ARP packets
        arp = of.ofp_flow_mod()
        arp.priority = 100
        arp.match.dl_type = ethernet.ARP_TYPE
        arp.actions.append(of.ofp_action_output(port=of.OFPP_FLOOD))
        self.connection.send(arp)
        log.debug("Rule added: allow ARP packets")
        
        # allow ICMP packets for IPV4
        icmp = of.ofp_flow_mod()
        icmp.priority = 90
        icmp.match.dl_type = ethernet.IP_TYPE
        icmp.match.nw_proto = ipv4.ICMP_PROTOCOL
        icmp.actions.append(of.ofp_action_output(port=of.OFPP_FLOOD))
        self.connection.send(icmp)
        log.debug("Rule added: allow ICMP packets for IPV4")
        
        # drop all other packets
        other = of.ofp_flow_mod()
        other.priority = 10
        self.connection.send(other)
        log.debug("Rule added: drop all other packets")
        
        
    def _handle_PacketIn(self, event):
        """
        Packets not handled by the router rules will be
        forwarded to this method to be handled by the controller
        """

        packet = event.parsed  # This is the parsed packet data.
        if not packet.parsed:
            log.warning("Ignoring incomplete packet")
            return

        packet_in = event.ofp  # The actual ofp_packet_in message.
        print("Unhandled packet :" + str(packet.dump()))


def launch():
    """
    Starts the component
    """

    def start_switch(event):
        log.debug("Controlling %s" % (event.connection,))
        Firewall(event.connection)

    core.openflow.addListenerByName("ConnectionUp", start_switch)
