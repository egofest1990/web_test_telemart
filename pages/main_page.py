from .base_page import BasePage
from .locators import RegisterandLoginPageLocators
from .locators import PasswordRecoveryLocators
import time


class RegistrationClassPage(BasePage):
    def popup_sub(self):
        link_inn = self.find_element(RegisterandLoginPageLocators.POPUP)
        time.sleep(1)
        link_inn.click()
        time.sleep(1)
        return link_inn

    def first_name(self, word):
        link_inn = self.find_element(RegisterandLoginPageLocators.FIRST_NAME)
        link_inn.send_keys(word)
        return link_inn

    def last_name(self, word):
        link_inn = self.find_element(RegisterandLoginPageLocators.LAST_NAME)
        link_inn.send_keys(word)
        return link_inn

    def father_name(self, word):
        link_inn = self.find_element(RegisterandLoginPageLocators.FATHER_NAME)
        link_inn.send_keys(word)
        return link_inn

    def phone_number(self, word):
        link_inn = self.find_element(RegisterandLoginPageLocators.PHONE_NUMBER)
        link_inn.send_keys(word)
        return link_inn

    def email_adress_for_reg(self, word):
        link_inn = self.find_element(RegisterandLoginPageLocators.EMAIL)
        link_inn.send_keys(word)
        return link_inn

    def password(self, word):
        link_inn = self.find_element(RegisterandLoginPageLocators.PASSWORD)
        link_inn.send_keys(word)
        return link_inn

    def password_res(self, word):
        link_inn = self.find_element(RegisterandLoginPageLocators.PASSWORD_RES)
        link_inn.send_keys(word)
        return link_inn

    def popup_newreg(self):
        link_inn = self.find_element(RegisterandLoginPageLocators.POPUP_NEWREG)
        link_inn.click()
        time.sleep(1)
        link_inn.click()
        return link_inn

    def submit_button_registration(self):
        link_in = self.find_element(RegisterandLoginPageLocators.BUTTON_SUBMIT)
        link_in.click()
        return link_in

    def registration_assert(self):
        link_in = self.find_element(RegisterandLoginPageLocators.VALIDATION_CODE)
        assert link_in, "Registration Failed"

    def b_ptn_enter(self):
        link_in = self.find_element(RegisterandLoginPageLocators.POPUP_LOGIN)
        link_in.click()
        return link_in

    def entered_email_or_phone(self, word):
        link_in = self.find_element(RegisterandLoginPageLocators.LOGIN_EMAIL_OR_PHONE)
        link_in.send_keys(word)
        return link_in

    def entered_password_for_login(self, word):
        link_in = self.find_element(RegisterandLoginPageLocators.LOGIN_PASSWORD)
        link_in.send_keys(word)
        return link_in

    def submit_for_login(self):
        link_in = self.find_element(RegisterandLoginPageLocators.SUBMIT_LOGIN)
        link_in.click()
        return link_in

    def login_assert_for_pop_up(self):
        link_in = self.find_element(RegisterandLoginPageLocators.ASSERT_PERSONAL_CABINET_IS_PRESENT)
        assert link_in, "Personal cabinet not found"

    def forget_password_form(self):
        link_inn = self.find_element(PasswordRecoveryLocators.FORGET_PASSWORD)
        link_inn.click()
        return link_inn

    def email_or_phone_for_recovery(self, word):
        link_inn = self.find_element(PasswordRecoveryLocators.EMAIL_OR_PHONE_FOR_RECOVERY)
        link_inn.send_keys(word)
        return link_inn

    def submit_recovery(self):
        link_inn = self.find_element(PasswordRecoveryLocators.SUBMIT_RECOVERY)
        link_inn.click()
        return link_inn

    def recovery_assert_message(self):
        link_inn = self.find_element(PasswordRecoveryLocators.ASSERT_RECOVERY_MESSAGE)
        assert link_inn, "Not message"
