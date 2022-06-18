"""foo"""

from packages.logger import project_logger
from packages.classifier import ClassifierClient as classifier_client_python
from packages.testlink import get_link_to_test_without_validate
from packages.project_selenium import setup_selenium_driver

logger = project_logger("Test1")

if __name__ == '__main__':
    site_to_test = get_link_to_test_without_validate()
    #site_to_test = "https://www.modern-academy.edu.eg/university/student/login.aspx"
    driver = setup_selenium_driver()

    classifier = classifier_client_python(driver)
    driver.get(site_to_test)

    newaccount = classifier.find_button_matching_label(
        'Create New Account')

    newaccount.click()

    sinup = classifier.find_button_matching_label('sign up')

    sinup.click()

    firstname = classifier.find_text_field_matching_label(
        'first name')

    print(firstname.get_attribute("aria-required") == "true")

    # email = classifier.find_elements_matching_label('email')
    # password = classifier.find_elements_matching_label('password')
    # log_in = classifier.find_elements_matching_label('log in')

    # email.send_keys("asdasd@gmail.com")
    # password.send_keys("huwidy87dw")
    # log_in.click()

    #assert password[0].get_attribute("value") == ""
