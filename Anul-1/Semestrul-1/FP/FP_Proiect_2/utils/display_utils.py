from domain.travel_package import get_id, get_arrival_date, get_departure_date, get_location, get_price


def display_all_packages(packages: list):
    """
    Prints a formatted list of all travel packages or a message if empty.
    :param packages: List of travel packages to display.
    """
    print("\n--- TRAVEL PACKAGES LIST ---")
    if not packages or not isinstance(packages, list):
        print("No packages available to display.")
        return

    # Table Header
    print(f"{'ID':<4} | {'Arrival':<12} | {'Departure':<12} | {'Location':<15} | {'Price':<10}")
    print("-" * 65)

    for p in packages:
        pkg_id = get_id(p)
        arrival = get_arrival_date(p).strftime("%d.%m.%Y")
        departure = get_departure_date(p).strftime("%d.%m.%Y")
        location = get_location(p).capitalize()
        price = get_price(p)

        print(f"{pkg_id:<4} | {arrival:<12} | {departure:<12} | {location:<15} | {price:<10.2f} RON")