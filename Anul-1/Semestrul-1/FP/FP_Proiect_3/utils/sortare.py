from typing import List, Callable, Any, Optional

def quick_sort(arr: List[Any], cmp: Callable[[Any, Any], int]):
    def _quick_sort(low: int, high: int):
        if low < high:
            pivot_index = partition(low, high)
            _quick_sort(low, pivot_index - 1)
            _quick_sort(pivot_index + 1, high)

    def partition(low: int, high: int) -> int:
        pivot = arr[high]
        i = low - 1

        for j in range(low, high):
            if cmp(arr[j], pivot) < 0:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    arr_copy = arr[:]
    _quick_sort(0, len(arr_copy) - 1)
    return arr_copy



def gnome_sort(arr: List[Any], cmp: Callable[[Any, Any], int]):
    """
    Gnome Sort works by comparing the current element with the previous one.
    If they are in the correct order, it moves to the next element.
    If not, it swaps them and moves back one step.
    This process continues until the entire list is sorted
    """
    index = 0
    while index < len(arr):
        if index == 0 or cmp(arr[index], arr[index - 1]) >= 0:
            index += 1
        else:
            arr[index], arr[index - 1] = arr[index - 1], arr[index]
            index -= 1
    return arr


def generic_sort(data: List[Any], method: str = 'quick', key: Callable[[Any], Any] = lambda x: x, reversed: bool = False) -> List[Any]:
    """
    Simplified generic sorting function supporting Quick Sort and Gnome Sort.
    Parameters:
        data: List[Any] -> list to be sorted
        method: str -> sorting method: 'quick' or 'gnome'
        key: Callable -> function to extract comparison key
        reversed: bool -> if True, sorts in descending order
    """
    def cmp(a, b):
        return (key(a) > key(b)) - (key(a) < key(b))

    if method == 'quick':
        sorted_data = quick_sort(data[:], cmp)
    elif method == 'gnome':
        sorted_data = gnome_sort(data[:], cmp)
    else:
        raise ValueError("Invalid method. Choose 'quick' or 'gnome'.")

    if reversed:
        sorted_data.reverse()
    return sorted_data
