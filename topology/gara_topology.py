from mininet.net import Mininet
from mininet.node import OVSSwitch
from mininet.cli import CLI
from mininet.link import TCLink
from mininet.log import setLogLevel

def build():
    net = Mininet(controller=None, switch=OVSSwitch, link=TCLink)

    s1 = net.addSwitch('s1', failMode='standalone')
    s2 = net.addSwitch('s2', failMode='standalone')
    s3 = net.addSwitch('s3', failMode='standalone')
    s4 = net.addSwitch('s4', failMode='standalone')

    h1 = net.addHost('h1', ip='10.0.1.10/8')
    h2 = net.addHost('h2', ip='10.0.1.20/8')
    h3 = net.addHost('h3', ip='10.0.2.10/8')
    h4 = net.addHost('h4', ip='10.0.3.10/8')
    h5 = net.addHost('h5', ip='10.0.3.20/8')
    h6 = net.addHost('h6', ip='10.0.4.10/8')

    net.addLink(h1, s1)
    net.addLink(h2, s1)
    net.addLink(h3, s2)
    net.addLink(h4, s3)
    net.addLink(h5, s3)
    net.addLink(h6, s4)

    net.addLink(s1, s2)
    net.addLink(s2, s3)
    net.addLink(s3, s4)

    net.start()
    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    build()
