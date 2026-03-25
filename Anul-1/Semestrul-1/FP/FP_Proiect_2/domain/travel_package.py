def create_package(package_id: int, arrival_date, departure_date, location: str, price: float):
    """
    Creates a travel package entity.
    :param package_id: The unique identifier of the package.
    :param arrival_date: Datetime object representing the arrival date.
    :param departure_date: Datetime object representing the departure date.
    :param location: String representing the destination.
    :param price: Positive number representing the trip price.
    :return: A list representing the travel package.
    """
    return [package_id, arrival_date, departure_date, location, price]


def get_id(package: list) -> int:
    """
    Returns the ID of the package.
    :param package: The travel package.
    :return: The package ID.
    """
    return package[0]


def get_arrival_date(package: list):
    """
    Returns the arrival date of the package.
    :param package: The travel package.
    :return: Arrival date as a datetime object.
    """
    return package[1]


def get_departure_date(package: list):
    """
    Returns the departure date of the package.
    :param package: The travel package.
    :return: Departure date as a datetime object.
    """
    return package[2]


def get_location(package: list) -> str:
    """
    Returns the location of the package.
    :param package: The travel package.
    :return: The location string.
    """
    return package[3]


def get_price(package: list) -> float:
    """
    Returns the price of the package.
    :param package: The travel package.
    :return: The price value.
    """
    return package[4]


def modify_package(package: list, arrival_date, departure_date, location: str, price: float) -> list:
    """
    Updates the details of an existing package.
    :param package: The package to be modified.
    :param arrival_date: New arrival date.
    :param departure_date: New departure date.
    :param location: New location.
    :param price: New price.
    :return: The updated package.
    """
    package[1] = arrival_date
    package[2] = departure_date
    package[3] = location
    package[4] = price
    return package
