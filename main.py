import time
from distance import distance_from_objects
from spaceships import spaceships


# Function will get the current destination, new destination
# and chosen space ship to calculate the amount of time
def travel(current_destination, new_destination, space_ship):
    # Assuming distance_from_objects and spaceships are correctly imported and structured
    distance = distance_from_objects[current_destination][
        new_destination
    ]  # Access the distance
    speed_of_light_mps = 186000  # Speed of light in miles per second
    spaceship_speed = (
        spaceships[space_ship]["Speed"] * speed_of_light_mps
    )  # Calculate spaceship speed

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

    destinations = list(distance_from_objects.keys())
    # Display available destinations
    for i, destination in enumerate(destinations, start=1):
        print(f"{i}. {destination}")

    # Get the user's current location by number
    location_choice = int(input("\nPlease enter the number of your current location: "))
    current_location = destinations[location_choice - 1]

    print("\nHere are the available destinations:\n")

    # Display available destinations and their distances from the current location
    for i, (key, value) in enumerate(
        distance_from_objects[current_location].items(), start=1
    ):
        formatted_distance = "{:,.0f}".format(value)
        print(f"{i}. Destination: {key} / Distance: {formatted_distance} Miles")

    # Get the user's desired destination by number
    destination_choice = int(
        input("\nWhich destination would you like to travel to? Enter the number: ")
    )
    new_destination_keys = list(distance_from_objects[current_location].keys())
    new_destination = new_destination_keys[destination_choice - 1]

    print(" ")

    # Display available spaceships and their speeds
    print(
        "\nHere is a list of spaceships and their speeds (as multiples of the speed of light):"
    )
    spaceships_list = list(spaceships.keys())
    for i, spaceship in enumerate(spaceships_list, start=1):
        print(
            f"{i}. {spaceship}: {spaceships[spaceship]['Speed']} times the speed of light"
        )

    # Get the user's chosen spaceship by number
    spaceship_choice_number = int(
        input("\nWhich ship would you like to travel in? Enter the number: ")
    )
    spaceship_choice = spaceships_list[spaceship_choice_number - 1]

    # No need to check if spaceship_choice is valid because the input is controlled by the enumerated list

    # Call the travel function with the user's inputs
    travel(current_location, new_destination, spaceship_choice)


if __name__ == "__main__":
    main()
