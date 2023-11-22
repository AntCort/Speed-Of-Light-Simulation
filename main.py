import time
from distance import distance_from_objects


# Funciton will get the new destination to calculate the amount of time
def travel(current_destination, new_destination):
    remaining_seconds = (
        distance_from_objects[current_destination][new_destination] / 186000
    )
    print(f"Enjoy your trip to: {new_destination}!")

    if remaining_seconds < 0:
        print("No travel time calculated.")
        return

    # While loop to countdown each second during travel
    while remaining_seconds > 0:
        hours, remainder = divmod(int(remaining_seconds), 3600)
        mins, secs = divmod(remainder, 60)
        time_formatted = "{:02d}:{:02d}:{:02d}".format(hours, mins, secs)
        print(f"Time left in journey {time_formatted}.")
        time.sleep(1)
        remaining_seconds -= 1

    # Will print once arrived to destination
    print(f"You have arrived to your destination: {new_destination}!")


def main():
    print(
        "Welcome to the Speed of Light Simulator. Below are your options for travel destinations:\n"
    )
    print("|".join(distance_from_objects.keys()))

    current_location = input("\nPlease enter your current location: ")
    print("\nHere are the available destinations:\n")

    for key, value in distance_from_objects[current_location].items():
        formatted_distance = "{:,.0f}".format(value)
        print(f"Destination: {key} / Distance: {formatted_distance} Miles")

    new_destination = input("\nWhich destination would you like to travel to? ").title()
    print(" ")

    travel(current_location, new_destination)


if __name__ == "__main__":
    main()
