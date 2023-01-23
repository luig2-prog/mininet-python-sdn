## Creación de topologías por medio de un script en python

### Para mas información visitar http://mininet.org/

# Para ejecutar una topología personalizada ejecutar el siguiente comando

```
sudo mn --custom multi-hosts.py --topo=mytopo
```
### Para ejecutar una topología personalizada y agregar mi controlador remoto de OpenDaylight ejecutar el siguiente comando

En el parámetro `IP_OPENDAYLIGHT` agregar la ip del servidor OpenDayLight

```
sudo mn --custom multi-host.py --topo=mytopo --controller=remote,ip=IP_OPENDAYLIGHT,port=6633 --switch ovs,protocols=OpenFlow13
```

<hr>

## Para ejecutar el script `single_topo.py` utilice el siguiente comando

```
sudo python single_topo.py
```

### obtendrá una salida de la siguiente manera:
```
*** Creating network
*** Adding controller
*** Adding hosts:
h1 h2 h3 h4
*** Adding switches:
s1
*** Adding links:
(h1, s1) (h2, s1) (h3, s1) (h4, s1)
*** Configuring hosts
h1 h2 h3 h4
*** Starting controller
c0
*** Starting 1 switches
s1 ...
Dumping host connections
h1 h1-eth0:s1-eth1
h2 h2-eth0:s1-eth2
h3 h3-eth0:s1-eth3
h4 h4-eth0:s1-eth4
Testing network connectivity
*** Ping: testing ping reachability
h1 -> h2 h3 h4
h2 -> h1 h3 h4
h3 -> h1 h2 h4
h4 -> h1 h2 h3
*** Results: 0% dropped (12/12 received)
*** Stopping 1 controllers
c0
*** Stopping 4 links
....
*** Stopping 1 switches
s1
*** Stopping 4 hosts
h1 h2 h3 h4
*** Done
```

## Crear una topología líneal y agregar mi controlador OpenDaylight
```
sudo mn --topo linear,3 --mac --controller=remote,ip=ipOpenDaylight,port=6633 --switch ovs,protocols=OpenFlow13
```

### Para instalar y ejecutar OpenDaylight seguir los siguientes pasos

Pasos para la instalacción en el sitio [oficial](https://docs.opendaylight.org/en/stable-sulfur/getting-started-guide/installing_opendaylight.html)

<hr>

# Extras

### Ejecución ODL
```
sudo -E karaf
```

### Acceder y ver por consola los datos de un nodo 
```
tcpdump -i s1-eth1
```

### Remover todas las topologías y enlaces
```
sudo mn -c
```