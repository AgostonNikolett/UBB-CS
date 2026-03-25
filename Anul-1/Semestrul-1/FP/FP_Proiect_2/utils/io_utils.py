import datetime
import os

def clear_screen():
    """
    Clears the terminal screen based on the operating system.
    :return: None
    """
    os.system('clear' if os.name == 'posix' else 'cls')

def read_number(prompt: str, converter_function, error_msg: str):
    """
    Reads an input from the user and converts it using the provided function.
    Validates that the number is positive.
    :param prompt: Message to display to the user.
    :param converter_function: Function used to convert the input (e.g., int, float).
    :param error_msg: Message to display in case of a conversion error or non-positive value.
    :return: The converted positive number.
    """
    while True:
        try:
            value = converter_function(input(prompt))
            if value > 0:
                return value
            raise ValueError
        except ValueError:
            print(error_msg)

def read_date(date_format: str, error_msg: str, prompt="Enter date (day month year): "):
    """
    Reads a string from the user and converts it into a datetime object.
    :param date_format: The expected format of the date string.
    :param error_msg: Message to display if the format is incorrect.
    :param prompt: Message to display for the input.
    :return: A datetime object.
    """
    while True:
        try:
            return datetime.datetime.strptime(input(prompt), date_format)
        except ValueError:
            print(error_msg)