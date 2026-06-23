"""
Name: Derek R. Neilson
Description: Computer Haven Seminar Registration System
"""

import pandas as pd
import src.plotting


def cost_per_attendee_calc(attendees: int) -> int:
    """Calculates the cost per an attendee

    Args:
        attendees (int): number of attendees

    Returns:
        int: the cost per each attendee
    """

    if attendees <= 0:
        cost_per_attendee = 0
    elif attendees < 4:
        cost_per_attendee = 150
    elif 4 <= attendees < 10:
        cost_per_attendee = 100
    elif attendees >= 10:
        cost_per_attendee = 90
    return cost_per_attendee


def main() -> None:
    """main for Computer Haven Seminar Registration System

    Raises:
        OverflowError: when there is too many people in the room to hold the requested amount
    Arguments:
        None
    Returns:
        None
    """
    total_revenue = 0
    largest_company = ""
    largest_company_size = 0
    largest_company_revue = 0
    number_of_companies = 0
    total_attendees = 0
    run = True
    companies = []
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
                    break
                total_attendees += attendees
                break
            except ValueError:
                print("Please type a whole number ie.(45)")
            except OverflowError as err:
                print(err)
        cost_per_attendee = cost_per_attendee_calc(attendees)
        registration_cost = attendees * cost_per_attendee
        if attendees > largest_company_size:
            largest_company_size = attendees
            largest_company = company_name
            largest_company_revue = registration_cost
        # Attendees should be a valid int by now
        total_revenue += registration_cost
        print(f"That will cost {company_name} ${registration_cost:,.2f}")
        number_of_companies += 1
        companies.append(
            {
                "Company Name": company_name,
                "Attendees": attendees,
                "Cost bracket": cost_per_attendee,
                "Cost": registration_cost,
            }
        )
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
    try:
        average = total_revenue / number_of_companies
    except ZeroDivisionError:
        average = 0
    print()
    print(pd.DataFrame(companies))
    print()
    print(f"Companies Registered: {number_of_companies}")
    print(f"Total Attendees: {total_attendees}")
    print(f"Total Revenue: ${total_revenue:,.2f}")
    print(f"Average Revenue Per Attendee: ${average}")
    print(
        f"Largest company was {largest_company} with {largest_company_size} attendees and costed {largest_company_revue}"
    )
    should_plot = input("Do you want a graph?\nYes or No: ").lower()
    if should_plot == "yes":
        src.plotting.seminar_plots(companies)  # pragma: no cover


if __name__ == "__main__":
    main()  # pragma: no cover
