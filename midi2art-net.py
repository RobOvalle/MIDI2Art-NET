import argparse, time, platform
import rtmidi
from stupidArtnet import StupidArtnet

import atexit

#Info Artnet
target_ip = '2.0.0.16'		
universe = 0 										
packet_size = 512								


a = StupidArtnet(target_ip, universe, packet_size, 10, True, True)
print(a)
a.start()

def chaopescao(): 
    a.stop()
    del a

def midi_received(data, unused):
    msg, delta_time = data
    print("MIDI message: ", msg) #Debug pa ver la nota
    #a.set_single_value(msg[1],255 - (msg[2] *2))
    a.set_single_value(msg[1],(msg[2] *2))
    
