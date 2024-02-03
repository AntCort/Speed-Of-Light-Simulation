import time
from distance import distance_from_objects
from spaceships import spaceships


# Function will get the current destination, new destination 
# and chosen space ship to calculate the amount of time
def travel(current_destination, new_destination, space_ship):
    # Assuming distance_from_objects and spaceships are correctly imported and structured
    distance = distance_from_objects[current_destination][new_destination]  # Access the distance
    speed_of_light_mps = 186000  # Speed of light in miles per second
    spaceship_speed = spaceships[space_ship]["Speed"] * speed_of_light_mps  # Calculate spaceship speed
    
    remaining_seconds = distance / spaceship_speed  # Calculate travel time
    
    print(f"Preparing for warp speed to: {new_destination}!")
    
    # Warp speed countdown
    warp_countdown = 5  # 5 seconds to warp speed
    while warp_countdown > 0:
        print(f"Warp speed in {warp_countdown} seconds...")
        time.sleep(1)  # Simulate countdown
        warp_countdown -= 1
    
    print("Initiating warp speed now!")
    
    # Main travel countdown
    if remaining_seconds < 0:
        print("No travel time calculated.")
        return
    
    while remaining_seconds > 0:
        hours, remainder = divmod(int(remaining_seconds), 3600)
        mins, secs = divmod(remainder, 60)
        time_formatted = "{:02d}:{:02d}:{:02d}".format(hours, mins, secs)
        print(f"Time left in journey {time_formatted}.")
        time.sleep(1)  # Simulate real-time countdown
        remaining_seconds -= 1
    
    # Arrival notification
    print(f"You have arrived at your destination: {new_destination}!")



# Define the main function to run the Speed of Light Simulator
def main():
    print(
        "Welcome to the Speed of Light Simulator. Below are your options for travel destinations:\n"
    )

    # Display available destinations
    print("|".join(distance_from_objects.keys()))

    # Get the user's current location
    current_location = input("\nPlease enter your current location: ").title()

    print("\nHere are the available destinations:\n")

    # Display available destinations and their distances
    for key, value in distance_from_objects[current_location].items():
        formatted_distance = "{:,.0f}".format(value)
        print(f"Destination: {key} / Distance: {formatted_distance} Miles")

    # Get the user's desired destination
    new_destination = input("\nWhich destination would you like to travel to? ").title()
    print(" ")

    # Display available spaceships
    print("\nHere is a list of spaceships: ")
    print("|".join(spaceships.keys()))

    # Get the user's chosen spaceship
    spaceship_choice = input("\nWhich ship would you like to travel in?: ").title()

    # Call the travel function with the user's inputs
    travel(current_location, new_destination, spaceship_choice)


if __name__ == "__main__":
    main()
