import time

SPEED_OF_LIGHT = 186000 # 186000 Miles per second
TRAVEL_TIME = { # Dictionary containing Key: Destination and Value: Miles from Earth
    "Sun": 92955807,
    "Moon": 238900,
    "Mercury": 36200000,
    "Venus": 67200000,
    "Mars": 141600000,
    "Jupiter": 483800000,
    "Saturn": 889700000,
    "Uranus": 1780000000,
    "Neptune": 2800000000
}
class LightTravel: 
    def __init__(self, astro_object, distance): # Initialization
        self.astro_object = astro_object
        self.distance = distance
        
    # Function to simulate travel of the speed of light to prompted destination     
    def travel_to(self): 
        remaining_seconds = self.distance / SPEED_OF_LIGHT
        print(f"Enjoy your trip to: {self.astro_object}!")
        
        if remaining_seconds < 0:
            print("No travel time calculated.")
            return
        
        # While loop to countdown each second during travel
        while remaining_seconds > 0:
                hours, remainder = divmod(int(remaining_seconds), 3600)
                mins, secs = divmod(remainder, 60)
                time_formatted = '{:02d}:{:02d}:{:02d}'.format(hours, mins, secs)
                print(f"Time left in journey {time_formatted}.")
                time.sleep(1)
                remaining_seconds -= 1
                
        # Will print once arrived to destination        
        print(f"You have arrived to your destination: {self.astro_object}!")
                