films = {
    "Blade Runner": [13, 5],
    "Matrix": [8, 5],
    "Guardians of the Galaxy": [5, 5],
    "A.I. Artificial Intelligence": [12, 5]
    # dictionary of scifi films
    # #age is the first element in that list
    # number of seats is the second in the list
}

while True:

    choice = input("Name the film: ").strip().title()

    if choice in films:
        age = int(input("How old are you?: ").strip())
        # casting the string into an int

        # check user age
        if age >= films[choice][0]:

            # check enough seats/tickets
            num_seats = films[choice][1]

            if num_seats > 0:
                print("Enjoy the film!")
                films[choice][1] = films[choice][1] - 1
                # subtract one from the #s of tickets left
            else:
                print("Sorry, we are sold out!")
        else:
            print("You are too young to see that film!")
    else:
        print("We don't have that film...")
