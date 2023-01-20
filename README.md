## Creación de topologías por medio de un script en python


### Remover todols las topologías y enlaces
```
sudo mn -c
```

### Ejecutar el archivo `single_topo.py`
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

<hr>

### Ejecutar OpenDaylight
```
sudo -E karaf
```

### Crear una topología y ver en ODL
```
sudo mn --topo linear,3 --mac --controller=remote,ip=192.168.1.34,port=6633 --switch ovs,protocols=OpenFlow13
```

### multihost

```
sudo mn --custom ./mininet/custom/multi-hosts.py --topo=mytopo
```
