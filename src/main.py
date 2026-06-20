"""
Name: Derek R. Neilson
Description: Computer Haven Seminar Registration System
"""


def main() -> None:
    """main for Computer Haven Seminar Registration System

    Raises:
        OverflowError: when there is too many people in the room to hold the requested amount
    Arguments:
        None
    Returns:
        None
    """

    number_of_companies = 0
    total_attendees = 0
    run = True
    while run:
        company_name = input("What is your companies name?\nEnter 'done' to quit: ")
        if company_name.lower() == "done":
            break
        while True:
            try:
                attendees = int(
                    input(
                        f"How many are attending from {company_name}?\nenter zero to quit: "
                    )
                )
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

        # Attendees should be a valid int by now
        cost_per_attendee = cost_per_attendee_calc(attendees)
        registration_cost = attendees * cost_per_attendee
        print(f"That will cost {company_name} ${registration_cost:,.2f}")
        number_of_companies += 1
        if run:
            another_company = input(
                "Should another company be entered?\nY or N: "
            ).upper()
            while run and (another_company != "Y" and another_company != "N"):
                another_company = input(
                    "Should another company be entered?\nY or N only please: "
                ).upper()
            if another_company == "N":
                run = False
                break


def cost_per_attendee_calc(attendees: int) -> int:
    """Calculates the cost per an attendee

    Args:
        attendees (int): number of attendees

    Returns:
        int: the cost per each attendee
    """

    if attendees == 0:
        cost_per_attendee = 0
    elif attendees < 4:
        cost_per_attendee = 150
    elif 4 <= attendees < 10:
        cost_per_attendee = 100
    elif attendees >= 10:
        cost_per_attendee = 90
    return cost_per_attendee


if __name__ == "__main__":
    main()
