from mininet.topo import Topo
from mininet.node import RemoteController
from mininet.cli import CLI
from mininet.net import Mininet


REMOTE_CONTROLLER_IP = "192.168.1.34"

class MyTopo( Topo ):

    print("Simple topology example.")
    def __init__( self ):
        "Create custom topo."

        # Initialize topology
        Topo.__init__( self )

        # Add hosts and switches
        # endTest = True
        # while endTest:
            
        Host1 = self.addHost( 'h1' )
        Host2 = self.addHost( 'h2' )
        Host3 = self.addHost( 'h3' )
        Host4 = self.addHost( 'h4' )
        Host5 = self.addHost( 'h5' )
        Host6 = self.addHost( 'h6' )
        Switch0 = self.addSwitch('s0')
        Switch1 = self.addSwitch('s1')
        Switch2 = self.addSwitch('s2')
            # endTest = False
        # Add links
        self.addLink( Host1, Switch0 )
        self.addLink( Host2, Switch0 )
        self.addLink( Host3, Switch0 )
        self.addLink( Host4, Switch1 )

        self.addLink( Host5, Switch1 )
        self.addLink( Host6, Switch1 )
        self.addLink( Switch0, Switch2 )
        self.addLink( Switch2, Switch1 )
topos = { 'mytopo': ( lambda: MyTopo() ) }


if __name__ == '__main__':
# Tell mininet to print useful information
    # setLogLevel('info')
    # simpleTest()
    print("Controller exec")
    topo = topos
    net = Mininet(topo=topo,
    controller=None,
    autoStaticArp=True)
    net.addController("c0",
    controller=RemoteController,
    ip=REMOTE_CONTROLLER_IP,
    port=6633)
    net.start()
    CLI(net)
    net.stop()
# net = Mininet(topo=topos,
#     controller=None,
#     autoStaticArp=True)
# net.addController("c0",
#     controller=RemoteController,
#     ip=REMOTE_CONTROLLER_IP,
#     port=6633)