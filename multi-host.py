from mininet.topo import Topo
from mininet.node import RemoteController
from mininet.net import Mininet
from mininet.cli import CLI

MESSAGE_0 = 'Digite 0 para no agregar'
MESSAGE_1 = 'Digite 1 para agregar'
SEPARATED = '***************************************'
REMOTE_CONTROLLER_IP = "192.168.1.34"

def add_hosts_and_switchs(self, n_hosts, n_switch):
    for x in range(int(n_hosts)):
        host = 'h' + str(x + 1)
        self.addHost(host)

    for s in range(int(n_switch)):
        swith = 's' + str(s)
        print(swith)
        self.addSwitch(swith)

def add_links_to_switch(self, n_hosts, actual_switch):
    print(SEPARATED)
    print('Enlacemos los hosts al swith ' + actual_switch)
    print(SEPARATED)
    for host_i in range(int(n_hosts)):
        actual_host = 'h' + str(host_i + 1)
        print('Desea agregar el enlace del host ' + actual_host + 
        ' al switch ' + actual_switch + ' = ' + actual_host + '->' + 
        actual_switch + '?')
        print(MESSAGE_0)
        print(MESSAGE_1)
        swith_question = input('')
        if int(swith_question) == 1:
            print(actual_host, actual_switch)
            self.addLink( actual_host, actual_switch )

def add_links_switch_to_switch(self, actual_switch, n_switch):
    for swith_i in range(int(n_switch)):
        temp_switch = 's' + str(swith_i)
        print('Agregue el enlace del switch ' + temp_switch + ' al switch ' + 
        actual_switch + ' ' + temp_switch + '->' + actual_switch + '?')
        print(MESSAGE_0)
        print(MESSAGE_1)
        swith_question = input('')
        if int(swith_question) == 1:
            self.addLink( temp_switch, actual_switch )

class MyTopo( Topo ):

    print("Simple topology example.")
    def __init__( self ):
        "Create custom topo."

        # Initialize topology
        Topo.__init__( self )

        # Add hosts and switches

        print('¿Ingrese la cantidad de host a crear?')
        n_hosts = input('')
        print(SEPARATED)
        print('¿Ingrese la cantidad de switch a crear?')
        n_switch = input('')
        print(SEPARATED)

        add_hosts_and_switchs(self, n_hosts, n_switch)

        for swith in range(int(n_switch)):
            actual_switch = 's' + str(swith)
            print('Configuremos el switch ' + actual_switch)
            print(SEPARATED)
            print('¿Desea agregar algún host al switch ' + actual_switch + '?')
            print(MESSAGE_0)
            print(MESSAGE_1)
            question_host_n = input('')
            if question_host_n == 1:
               add_links_to_switch(self, n_hosts, actual_switch) 

            print(SEPARATED)

            print('Desea agregar algún switch al presente switch (' + actual_switch + ')' )
            print(MESSAGE_0)
            print(MESSAGE_1)
            response = input('')
            if int(response) == 1:
                add_links_switch_to_switch(self, actual_switch, n_switch)


# topos = { 'mytopo': ( lambda: MyTopo() ) }


if __name__ == '__main__':
# Tell mininet to print useful information
    # setLogLevel('info')
    # simpleTest()
    topo = MyTopo()
    net = Mininet(topo=topo,
    controller=None,
    autoStaticArp=True)
    net.addController("c0",
    controller=RemoteController,
    ip=REMOTE_CONTROLLER_IP,
    port=6633)
    net.start()
    CLI(net)
    # net.stop()