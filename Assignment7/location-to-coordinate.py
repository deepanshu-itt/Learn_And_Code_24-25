from API import GeoLocation


def location_to_coordinate():
    
    user_input_place = get_user_input()

    latitude, longitude = GeoLocation.get_coordinates(user_input_place)

    check_coordinate_exists(latitude, longitude)


def get_user_input():
    user_input_place = input("Enter a place name: ")
    return user_input_place


def check_coordinate_exists(latitude, longitude):
    
    if latitude is not None and longitude is not None:
        print(f"\nLatitude: {latitude}\nLongitude: {longitude}")
    else:
        print("\nCould not find coordinates for that place.")


def main():
    
    location_to_coordinate()


if __name__ == "__main__":
    main()
