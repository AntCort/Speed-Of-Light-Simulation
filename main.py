import time
from distance import *

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
    current_location = input(
        "Earth | Sun | Moon | Mercury | Venus | Mars | Jupiter | Saturn | Uranus | Neptune| Pluto \nEnter your current location: "
    ).title()
    print("Here are your options on where to travel: ")
    for key, value in distance_from_objects[current_location].items():
        print(f"Destination: {key} / Distance: {'{:,.0f}'.format(value)} Miles")

    new_destination = input("Which would you like to travel to? ").title()

    travel(current_location, new_destination)


main()
