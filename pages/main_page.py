from .base_page import BasePage
from .locators import RegisterPageLocators
import time


class RegistrationClassPage(BasePage):
    def popup_sub(self):
        link_inn = self.find_element(RegisterPageLocators.POPUP)
        time.sleep(1)
        link_inn.click()
        time.sleep(1)
        return link_inn

    def first_name(self, word):
        link_inn = self.find_element(RegisterPageLocators.FIRST_NAME)
        link_inn.send_keys(word)
        return link_inn

    def last_name(self, word):
        link_inn = self.find_element(RegisterPageLocators.LAST_NAME)
        link_inn.send_keys(word)
        return link_inn

    def father_name(self, word):
        link_inn = self.find_element(RegisterPageLocators.FATHER_NAME)
        link_inn.send_keys(word)
        return link_inn

    def phone_number(self, word):
        link_inn = self.find_element(RegisterPageLocators.PHONE_NUMBER)
        link_inn.send_keys(word)
        return link_inn

    def email_adress_for_reg(self, word):
        link_inn = self.find_element(RegisterPageLocators.EMAIL)
        link_inn.send_keys(word)
        return link_inn

    def password(self, word):
        link_inn = self.find_element(RegisterPageLocators.PASSWORD)
        link_inn.send_keys(word)
        return link_inn

    def password_res(self, word):
        link_inn = self.find_element(RegisterPageLocators.PASSWORD_RES)
        link_inn.send_keys(word)
        return link_inn

    def popup_newreg(self):
        link_inn = self.find_element(RegisterPageLocators.POPUP_NEWREG)
        link_inn.click()
        time.sleep(1)
        link_inn.click()
        return link_inn

    def submit_button_registration(self):
        link_in = self.find_element(RegisterPageLocators.BUTTON_SUBMIT)
        link_in.click()
        return link_in

    def registration_assert(self):
        link_in = self.find_element(RegisterPageLocators.VALIDATION_CODE)
        assert link_in, "Registration Failed"


