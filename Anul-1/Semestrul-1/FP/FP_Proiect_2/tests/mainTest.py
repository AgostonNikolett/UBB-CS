from Tests.domainTest import test_all_domain
from Tests.serviceTest import test_all_services
from Tests.utilityTest import test_all_utility


def main_test():
    """
    Functia de legatura a tuturor testelor
    :param a: lista cu elementele de testat
    :return:
    """
    # Repositories tests
    test_all_domain()
    test_all_services()
    test_all_utility()