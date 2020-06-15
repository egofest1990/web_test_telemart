from .pages.main_page import RegistrationClassPage
import random
import allure


@allure.title("Test register")
@allure.story("Open pages")
def test_register_form(browser, record_testsuite_property):
    nmbr = random.randint(2, 100000000000)
    nmbr_phone = random.randint(0000000, 9999999)
    entered_to = RegistrationClassPage(browser)
    entered_to.open()
    entered_to.popup_sub()
    entered_to.popup_newreg()
    entered_to.first_name("Test")
    entered_to.last_name("Test")
    entered_to.father_name("Test")
    entered_to.phone_number(f"063{nmbr_phone}")
    entered_to.email_adress_for_reg(f"igorfesenko25+{nmbr}@gmail.com")
    entered_to.password("qwerty")
    entered_to.password_res("qwerty")
    entered_to.submit_button_registration()
    entered_to.registration_assert()
