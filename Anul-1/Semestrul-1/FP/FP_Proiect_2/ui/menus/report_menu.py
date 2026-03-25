from service.package_service import get_average_price_by_destination
from utils.sort_utils import quick_sort_by_price
from utils.display_utils import display_all_packages

def package_reports_menu(packages: list):
    while True:
        print("\n--- Reports Menu ---")
        print("1. Average price for a destination")
        print("2. Sort all packages by price (Ascending)")
        print("B. Back")

        option = input("Select option: ").strip().lower()
        if option == '1':
            dest = input("Destination: ").strip().lower()
            avg = get_average_price_by_destination(packages, dest)
            print(f">>> The average price for {dest.capitalize()} is: {avg:.2f} RON")
        elif option == '2':
            # We sort a copy to avoid changing the original list permanently if not intended
            sorted_list = packages[:]
            if sorted_list:
                quick_sort_by_price(sorted_list, 0, len(sorted_list) - 1)
                display_all_packages(sorted_list)
            else:
                print("List is empty.")
        elif option == 'b':
            break