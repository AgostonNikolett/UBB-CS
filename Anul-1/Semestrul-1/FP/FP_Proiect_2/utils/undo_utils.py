def add_to_undo(packages: list, undo_list: list):
    """
    Saves a copy of the current packages list to the undo stack.
    :param packages: The current list of packages.
    :param undo_list: The list acting as a stack for previous states.
    :return: None
    """
    if undo_list is not None:
        # We store a shallow copy of the list to preserve the state of elements
        undo_list.append(packages[:])