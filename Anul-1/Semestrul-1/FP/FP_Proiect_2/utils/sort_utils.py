from domain.travel_package import get_price


def partition(packages: list, low: int, high: int) -> int:
    """
    Partitioning function for the QuickSort algorithm.
    Uses the price of the last element as a pivot.
    :param packages: List of travel packages.
    :param low: Starting index of the partition.
    :param high: Ending index of the partition.
    :return: The index of the pivot after partitioning.
    """
    pivot = get_price(packages[high])
    i = low - 1

    for j in range(low, high):
        if get_price(packages[j]) <= pivot:
            i += 1
            packages[i], packages[j] = packages[j], packages[i]

    packages[i + 1], packages[high] = packages[high], packages[i + 1]
    return i + 1


def quick_sort_by_price(packages: list, low: int, high: int):
    """
    Sorts a list of packages in ascending order based on price using QuickSort.
    :param packages: List of travel packages to sort.
    :param low: Starting index.
    :param high: Ending index.
    :return: None (sorts in-place).
    """
    if low < high:
        pivot_index = partition(packages, low, high)
        quick_sort_by_price(packages, low, pivot_index - 1)
        quick_sort_by_price(packages, pivot_index + 1, high)