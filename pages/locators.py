from selenium.webdriver.common.by import By


class RegisterPageLocators:
    POPUP = (By.CSS_SELECTOR, "a.b-link-enter")
    POPUP_NEWREG = (By.CSS_SELECTOR, "a.b-ptn-newreg")
    LAST_NAME = (By.ID, "popupInputRegSName")
    FIRST_NAME = (By.ID, "popupInputRegFName")
    FATHER_NAME = (By.ID, "popupInputRegMName")
    PHONE_NUMBER = (By.ID, "popupInputRegPhone")
    EMAIL = (By.ID, "popupInputRegMail")
    PASSWORD = (By.ID, "popupInputRegPasw")
    PASSWORD_RES = (By.ID, "popupInputRegPaswRes")
    BUTTON_SUBMIT = (By.CSS_SELECTOR, "button.b-btn.b-btn-newreg")
    VALIDATION_CODE =(By.ID, "popupInputValidationCode")