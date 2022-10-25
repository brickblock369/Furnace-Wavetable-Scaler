looper = 0
while looper < 1:

    looper2 = 0
    while looper2 < 1:
        number_set = input("Enter your values here: ")
        numbers = number_set.split()
        for num in range(len(numbers)):
            try:
                numbers[num] = int(numbers[num])
                looper2 = 1
            except ValueError:
                looper2 = 0
                print("Enter only numbers please!\n")
                break

    looper4 = 0
    while looper4 < 1:
        original_height = input("Enter the wavetable's original height: ")
        try:
            original_height = int(original_height)
            looper4 = 1
        except ValueError:
            print("Enter only a number please!\n")

    looper3 = 0
    while looper3 < 1:
        new_height = input("Enter a new height value for the wavetable: ")
        try:
            new_height = int(new_height)
            looper3 = 1
        except ValueError:
            print("Enter only a number please!\n")

    scaled_numbers = ""

    for num in numbers:
        scaled_numbers += (str(round((((1 * (num / original_height) + num)) * ((new_height + 1) / (original_height + 1)) - 1 * (num / original_height)))) + " ")
    print("\nHere are the set of numbers scaled by what you entered:\n" + scaled_numbers + "\n")