from travel_from_earth import * # Importing class from travel_from_earth file

# Prompting the user for their preferred destination
print("Ready to travel at the speed of light? Choose your destination. \n")
for destination, distance in TRAVEL_TIME.items():
    print(f"Destination: {destination} / Distance: {distance} Miles")
   
user_input = input("\nWhere would you like to go?: ").title()
traveler_destination = LightTravel(user_input, TRAVEL_TIME[user_input])

# Simulating "Travel" time
traveler_destination.travel_to()


