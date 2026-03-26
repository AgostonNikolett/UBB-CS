from typing import List, Callable, Any


def generic_sort(data: List[Any], method: str = 'quick', key: Callable = lambda x: x, reverse: bool = False) -> List[
    Any]:
    """
    Simplified generic sorting function supporting Quick Sort and Gnome Sort.
    :param data: The list to be sorted.
    :param method: Sorting method: 'quick' or 'gnome'[cite: 27, 29].
    :param key: Function to extract comparison key[cite: 25].
    :param reverse: If True, sorts in descending order.
    :return: A new sorted list.
    """

    def compare(a, b):
        # Returns -1, 0, or 1 based on comparison
        return (key(a) > key(b)) - (key(a) < key(b))

    sorted_data = data[:]  # Work on a copy to keep the original list intact

    if method == 'quick':
        sorted_data = _quick_sort(sorted_data, compare)
    elif method == 'gnome':
        sorted_data = _gnome_sort(sorted_data, compare)
    else:
        raise ValueError("Invalid sorting method. Choose 'quick' or 'gnome'.")

    if reverse:
        sorted_data.reverse()
    return sorted_data


def _quick_sort(arr: List[Any], cmp: Callable) -> List[Any]:
    """Quick Sort implementation with in-place partitioning[cite: 25]."""

    def _recursive_inner(low, high):
        if low < high:
            pivot_idx = _partition(low, high)
            _recursive_inner(low, pivot_idx - 1)
            _recursive_inner(pivot_idx + 1, high)

    def _partition(low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if cmp(arr[j], pivot) < 0:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    _recursive_inner(0, len(arr) - 1)
    return arr


def _gnome_sort(arr: List[Any], cmp: Callable) -> List[Any]:
    """Gnome Sort implementation. Complexity: O(n) to O(n^2)."""
    index = 0
    while index < len(arr):
        if index == 0 or cmp(arr[index], arr[index - 1]) >= 0:
            index += 1
        else:
            arr[index], arr[index - 1] = arr[index - 1], arr[index]
            index -= 1
    return arr