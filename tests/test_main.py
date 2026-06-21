from src import main as computer_haven


def test_cost_per_attendee_calc_under_one() -> None:
    list_of_negative_integers = range(-1, -1000, -1)
    for number in list_of_negative_integers:
        assert computer_haven.cost_per_attendee_calc(number) == 0


def test_cost_per_attendee_calc_between_zero_and_three() -> None:
    list_of_integers_between_zero_and_three = range(1, 3)
    for number in list_of_integers_between_zero_and_three:
        assert computer_haven.cost_per_attendee_calc(number) == 150


def test_cost_per_attendee_calc_between_four_and_nine() -> None:
    list_of_integers_between_three_and_nine = range(4, 9)
    for number in list_of_integers_between_three_and_nine:
        assert computer_haven.cost_per_attendee_calc(number) == 100


def test_cost_per_attendee_calc_over_nine() -> None:
    list_of_integers_between_over_nine = range(10, 1000)
    for number in list_of_integers_between_over_nine:
        assert computer_haven.cost_per_attendee_calc(number) == 90


main = computer_haven.main


def run_main_with_inputs(monkeypatch, capsys, inputs):
    """
    Helper function to fake user input and capture printed output.
    """
    input_iter = iter(inputs)

    monkeypatch.setattr("builtins.input", lambda prompt="": next(input_iter))

    main()

    return capsys.readouterr().out


def test_main_registers_one_company(monkeypatch, capsys):
    output = run_main_with_inputs(
        monkeypatch,
        capsys,
        [
            "Acme",  # company name
            "3",  # attendees
            "N",  # no more companies
            "No",
        ],
    )

    assert "That will cost Acme $450.00" in output
    assert "Companies Registered: 1" in output
    assert "Total Attendees: 3" in output
    assert "Total Revenue: $450.00" in output
    assert "Largest company was Acme with 3 attendees" in output


def test_main_registers_multiple_companies(monkeypatch, capsys):
    output = run_main_with_inputs(
        monkeypatch, capsys, ["Acme", "3", "Y", "Beta Corp", "10", "N", "No"]
    )

    assert "That will cost Acme $450.00" in output
    assert "That will cost Beta Corp $900.00" in output
    assert "Companies Registered: 2" in output
    assert "Total Attendees: 13" in output
    assert "Total Revenue: $1,350.00" in output
    assert "Largest company was Beta Corp with 10 attendees" in output


def test_main_rejects_non_integer_attendees(monkeypatch, capsys):
    output = run_main_with_inputs(
        monkeypatch,
        capsys,
        [
            "Acme",
            "abc",  # invalid
            "2",  # valid retry
            "N",
            "No",
        ],
    )

    assert "Please type a whole number" in output
    assert "Companies Registered: 1" in output
    assert "Total Attendees: 2" in output
    assert "Total Revenue: $300.00" in output


def test_main_rejects_over_capacity(monkeypatch, capsys):
    output = run_main_with_inputs(
        monkeypatch,
        capsys,
        [
            "Huge Corp",
            "126",  # too many
            "125",  # valid retry
            "N",
            "No",
        ],
    )

    assert "There are not enough space available" in output
    assert "Companies Registered: 1" in output
    assert "Total Attendees: 125" in output
    assert "Total Revenue: $11,250.00" in output


def test_main_done_immediately_does_not_crash(monkeypatch, capsys):
    output = run_main_with_inputs(monkeypatch, capsys, ["done", "NO"])

    assert "Companies Registered: 0" in output
    assert "Total Attendees: 0" in output
    assert "Total Revenue: $0.00" in output


def test_main_invalid_Y_or_N(monkeypatch, capsys):
    output = run_main_with_inputs(
        monkeypatch,
        capsys,
        [
            "Acme",
            "1",
            "No",  # Invalid input
            "n",  # Valid Retry
            "No",
        ],
    )

    assert "That will cost Acme $150.00" in output
    assert "Companies Registered: 1" in output
    assert "Total Attendees: 1" in output
    assert "Total Revenue: $150.00" in output


def test_main_zero_attendees_quits(monkeypatch, capsys):
    output = run_main_with_inputs(
        monkeypatch,
        capsys,
        ["Acme", "0", "N", "NO"],
    )

    assert "That will cost Acme $0.00" in output
    assert "Companies Registered: 1" in output
    assert "Total Attendees: 0" in output
    assert "Total Revenue: $0.00" in output
