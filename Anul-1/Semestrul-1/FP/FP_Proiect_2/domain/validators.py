from domain.travel_package import get_id, get_arrival_date, get_departure_date


def validate_package(package: list, packages_list: list):
    """
    Validates a travel package for logical consistency and unique ID.
    :param package: The package to validate.
    :param packages_list: The current list of packages to check for duplicate IDs.
    :raises Exception: If ID already exists or dates are logically incorrect.
    :return: True if valid.
    """
    errors = ""
    current_id = get_id(package)

    # Check for duplicate ID
    for p in packages_list:
        if get_id(p) == current_id:
            errors += "ID already exists!\n"
            break

    # Check date logic
    if get_arrival_date(package) > get_departure_date(package):
        errors += "Departure date cannot be earlier than arrival date!\n"

    if errors:
        raise Exception(errors)
    return True