# Pseudocode for lab 5 Computer Haven

```txt
total_attendees = 0

while True:
    company_name = input 
    attendees = input
    if attendees + total_attendees > 125:
        invalid input

    if attendees is between 1 and 3 inclusive:
        cost_per_attendee = 150
    if attendees is between 4 and 9 inclusive:
        cost_per_attendee = 100
    if attendees is above 10 inclusive:
        cost_per_attendee = 90

    total_registration_cost = cost_per_attendee * attendees
    another_company = input
    if another_company == y:
        another_company = False
    if another_company == n:
        another_company = True
    else:
        ask again another_company again

    if another_company:
        break
```