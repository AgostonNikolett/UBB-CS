from domain.travel_package import get_arrival_date, get_departure_date, get_location, get_price
from utils.undo_utils import add_to_undo

def search_packages_in_interval(packages: list, start_date, end_date):
    """
    Finds packages that are fully contained within a given time interval.
    :param packages: List of packages.
    :param start_date: Interval start date.
    :param end_date: Interval end date.
    :return: List of matching packages.
    """
    results = []
    for p in packages:
        # Check if the package stay is within the user-provided bounds
        if start_date <= get_arrival_date(p) and get_departure_date(p) <= end_date:
            results.append(p)
    return results

def get_average_price_by_destination(packages: list, destination: str) -> float:
    """
    Calculates the arithmetic mean price for a specific location.
    :param packages: List of packages.
    :param destination: The target location.
    :return: Average price (float).
    """
    filtered_prices = [get_price(p) for p in packages if get_location(p) == destination]
    if not filtered_prices:
        return 0.0
    return sum(filtered_prices) / len(filtered_prices)

def filter_by_price_and_location(packages: list, destination: str, max_price: float, undo_list=None):
    """
    Removes packages that do NOT match the destination and exceed a certain price.
    :param max_price:
    :param destination:
    :param packages: List of packages.
    :param undo_list: Undo history list.
    :return: Number of deleted packages.
    """
    add_to_undo(packages, undo_list)
    initial_count = len(packages)
    # Keep packages that either match the destination OR are cheaper than the threshold
    packages[:] = [p for p in packages if get_location(p) == destination or get_price(p) <= max_price]
    return initial_count - len(packages)

def perform_undo(packages: list, undo_list: list):
    """
    Reverts the package list to its state before the last destructive operation.
    :param packages: The current package list.
    :param undo_list: The stack of previous states.
    :return: The restored list of packages.
    """
    if not undo_list:
        raise Exception("Nothing to undo!")
    return undo_list.pop()