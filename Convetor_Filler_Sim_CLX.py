# Conveyor and filler simulator

from collections import deque
import time
import random
from pylogix import PLC

# Initialize the conveyor belt (deque)
conveyor_belt = deque()

# Boolean flags for monitoring
drum_added_flag = False
drum_removed_flag = False

# Function to write to PLC
def write_PLC(drumStatus):
  with PLC() as comm:
    comm.IPAddress = '11.68.114.200'
    comm.Write('Drum_Simulated_Bool', drumStatus) 


# Function to simulate filling a drum
def fill_drum(drum_id):
    print(f"Filling drum {drum_id}...") 
    time.sleep(2)  # Simulate time taken to fill the drum
    print(f"Drum {drum_id} filled and removed from conveyor.")

# Function to add drums to the conveyor
def add_drum(drum_id):
    global drum_added_flag
    conveyor_belt.append(drum_id)  # Add drum to the end
    drum_added_flag = True  # Set flag to True
    print(f"Drum {drum_id} added to the conveyor.")

# Function to remove drums from the conveyor
def remove_drum():
    global drum_removed_flag
    drum_id = conveyor_belt.popleft()  # Remove the first drum for processing
    drum_removed_flag = True  # Set flag to True
    return drum_id

# Main loop to process drums on the conveyor
def conveyor_system():
    global drum_added_flag, drum_removed_flag
    drum_id = 1
    try:
        while True:
            # Reset flags at the start of each loop
            drum_added_flag = False
            drum_removed_flag = False

            # Randomly add new drums to the conveyor
            if random.random() < 0.5:  # 50% chance to add a new drum
                add_drum(drum_id)
                drum_id += 1

            # Process the next drum if the conveyor isn't empty
            if conveyor_belt:
                current_drum = remove_drum()
                fill_drum(current_drum)
            else:
                print("Conveyor is empty. Waiting for drums...")
                time.sleep(1)  # Wait before checking again

            # Print the status of flags to PLC
            print(f"Drum Added Flag: {drum_added_flag}, Drum Removed Flag: {drum_removed_flag}")
            write_PLC(drum_added_flag)

    except KeyboardInterrupt:
        print("\nConveyor system stopped.")

# Run the conveyor system
conveyor_system()
