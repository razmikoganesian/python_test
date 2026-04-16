seat_type = input("Enter seat type (sleeper/AC/general/luxury)"  ).lower()


match seat_type:
    case "sleeper":
        print("You choose a cleeper / no AC man")
    case "ac":
        print("Finally AC")
    case "luxury":
        print("Awesome service, nice and sexy stewardess included")
    case "general":
        print("Just general seat with parolon")
    case _:
        print('Something is wrong!')

    

