# Density transmitter simulator

import time
import random
from pylogix import PLC


# Function to write to PLC
def write_PLC(value):
  with PLC() as comm:
    comm.IPAddress = '11.68.114.200'
    comm.Write('Gravity', value) 



# Main loop to process drums on the conveyor
def densityTransmitter():
    global drum_added_flag, drum_removed_flag
    drum_id = 1
    try:
        while True:
            

            # Generate the random gravity
            gravity = random.random() * 8.8
            if 8 <= gravity <=8.8:
                # Print the gravity to PLC
                print(f"Current Gravity Value: {gravity}")
                # write the gravity to the PLC           
                write_PLC(gravity)
                time.sleep(0.5)   
    except KeyboardInterrupt:
        print("\nDensity instrumentStoped")

# Run the Density Transmitter
densityTransmitter()
