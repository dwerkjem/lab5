def main():
    total_attendees = 0
    run = True
    while run:
        company_name = input("What is your companies name: ")
        while True:
            try:
                attendees = int(input(f"How many are attending from {company_name}: "))
                if attendees + total_attendees > 125:
                    raise OverflowError(
                        f"There are not enough space available {125 - total_attendees} seats are left please select less than that or enter zero to quit"
                    )
                if attendees == 0:
                    run = False
                total_attendees += attendees
                break
            except ValueError:
                print("Please type a whole number ie.(45)")
            except OverflowError as err:
                print(err)


if __name__ == "__main__":
    main()
