# Topologia Proyecto
from mininet.topo import Topo

class MyTopo( Topo ):
    "Simple topology example." 
	def __init__( self ):
        "Create custom topo."

        # Initialize topology
        Topo.__init__( self )

        # Add hosts and switches
        Host1 = self.addHost( 'h1' )
        Host2 = self.addHost( 'h2' )
        Host3 = self.addHost( 'h3' )
        Host4 = self.addHost( 'h4' )
	SrvWeb = self.addHost( 'SrvWeb' )	
        Switch1 = self.addSwitch( 's1' )
        Switch2 = self.addSwitch( 's2' )

        # Add links
        self.addLink( Host1, Switch1 )
        self.addLink( Host2, Switch1 )	
	self.addLink( Host3, Switch1 )
        self.addLink( Switch1, Switch2 )
        self.addLink( Switch2, Host4 )
        self.addLink( Switch2, SrvWeb )

topos = { 'mytopo': ( lambda: MyTopo() ) }
