import argparse, time, platform
import rtmidi
from stupidArtnet import StupidArtnet

import atexit

target_ip = '2.0.0.16'		
universe = 0 										
packet_size = 512								


a = StupidArtnet(target_ip, universe, packet_size, 10, True, True)
print(a)
a.start()
