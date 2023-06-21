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
    print("MIDI message: ", msg)
    #a.set_single_value(msg[1],255 - (msg[2] *2))
    #multiplies the 128 midi value to fit the 255 dmx/artnet value
    a.set_single_value(msg[1],(msg[2] *2))
    
    
   
if __name__ == "__main__":
    atexit.register(chaopescao)
    parser = argparse.ArgumentParser()
    parser.add_argument("--midi", type=str, default = "MIDIArtnet", help = "Keyword identifying the MIDI input device (default: %(default)s).")
    args = parser.parse_args()

    #check the current ports (from rtmidi examples)
    midi_in = rtmidi.MidiIn()
    for idx, name in enumerate(midi_in.get_ports()):
        if args.midi in name:
            print("Found preferred MIDI input device %d: %s" % (idx, name))
            midi_in.open_port(idx)
            midi_in.set_callback(midi_received)
            break
        else:
            print("Ignoring unselected MIDI device: ", name)

    if not midi_in.is_port_open():
        if platform.system() == 'Windows':
            print("Virtual MIDI inputs are not currently supported on Windows, see python-rtmidi documentation.")
        else:
            print("Creating virtual MIDI input.")
            midi_in.open_virtual_port(args.midi)
    
    if not midi_in.is_port_open():
        print("No MIDI device opened, exiting.")

    else:
        print("Waiting for input.")
        while True:
            time.sleep(1)
