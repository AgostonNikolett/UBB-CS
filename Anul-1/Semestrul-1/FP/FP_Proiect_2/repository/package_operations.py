from domain.travel_package import create_package, get_id, modify_package, get_location, get_price
from domain.validators import validate_package
from utils.undo_utils import add_to_undo


def add_package_to_list(packages: list, arrival_date, departure_date, location: str, price: float, undo_list=None):
    """
    Adds a new travel package to the list.
    :param packages: Current list of travel packages.
    :param arrival_date: Datetime object for arrival.
    :param departure_date: Datetime object for departure.
    :param location: Destination string.
    :param price: Package price.
    :param undo_list: List for storing state for undo operations.
    :return: None
    """
    # Auto-generate ID based on the last element
    package_id = get_id(packages[-1]) + 1 if packages else 1

    new_package = create_package(package_id, arrival_date, departure_date, location, price)

    try:
        validate_package(new_package, packages)
        add_to_undo(packages, undo_list)
        packages.append(new_package)
    except Exception as e:
        # Business logic: instead of printing, we re-raise or handle quietly
        raise e


def get_package_by_id(packages: list, package_id: int):
    """
    Retrieves a package from the list by its unique ID.
    :param packages: List of travel packages.
    :param package_id: The ID to search for.
    :raises Exception: If ID is not found.
    :return: The found package object.
    """
    for p in packages:
        if get_id(p) == package_id:
            return p
    raise Exception(f"Package with ID {package_id} does not exist!")


def update_package_service(packages: list, package_id: int, arrival_date, departure_date, location: str, price: float,
                           undo_list=None):
    """
    Modifies an existing package's details.
    :param price:
    :param location:
    :param departure_date:
    :param arrival_date:
    :param packages: List of travel packages.
    :param package_id: ID of the package to update.
    :param undo_list: Undo history list.
    :return: None
    """
    target_package = get_package_by_id(packages, package_id)
    add_to_undo(packages, undo_list)
    modify_package(target_package, arrival_date, departure_date, location, price)


def delete_package_by_id(packages: list, package_id: int):
    """
    Removes a package from the list by its unique ID.
    :param packages: The list of travel packages.
    :param package_id: The ID of the package to be removed.
    :raises Exception: If the ID does not exist in the list.
    :return: None (modifies the list in-place).
    """
    initial_length = len(packages)

    # We use a list comprehension for an "in-place" update of the list content
    packages[:] = [p for p in packages if get_id(p) != package_id]

    if len(packages) == initial_length:
        raise Exception(f"Delete failed: No package found with ID {package_id}.")


def delete_packages_by_destination(packages: list, destination: str, undo_list=None):
    """
    Deletes all packages matching a specific destination.
    :param packages: List of travel packages.
    :param destination: The location to filter for deletion.
    :param undo_list: Undo history list.
    """
    add_to_undo(packages, undo_list)
    # Using list comprehension to filter in-place replacement
    packages[:] = [p for p in packages if get_location(p) != destination]


def delete_packages_by_price(packages: list, max_price: float, undo_list=None):
    """
    Removes packages that exceed a certain price.
    :param packages: List of travel packages.
    :param max_price: The price threshold.
    :param undo_list: Undo history list.
    """
    add_to_undo(packages, undo_list)
    packages[:] = [p for p in packages if get_price(p) <= max_price]