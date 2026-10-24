import data

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from helpers import retrieve_phone_code


class UrbanRoutesPage:
    # Step 1: Route
    from_field = (By.ID, "from")
    to_field = (By.ID, "to")

    # Step 2: Taxi and Comfort tariff
    pedir_un_taxi_field = (
        By.XPATH,
        "//div[@class='workflow']//button[@class='button round']"
    )
    comfort_field = (
        By.XPATH,
        "//div[@class='tariff-cards']//div[text()='Comfort']"
    )
    comfort_active = (
        By.CSS_SELECTOR,
        ".tcard.active .tcard-title"
    )

    # Step 3: Phone verification
    cellphone_field = (
        By.XPATH,
        "//div[@class='form']//div[@class='np-text']"
    )
    frame_cellphone_field = (By.CSS_SELECTOR, "#phone")
    boton_siguiente_after_cellphone = (
        By.XPATH,
        "//div[@class='modal']//button[text()='Siguiente']"
    )
    boton_introduce_codigo = (
        By.CSS_SELECTOR,
        ".number-picker.open #code"
    )
    boton_confirmar_after_code = (
        By.XPATH,
        "//form//button[text()='Confirmar']"
    )

    # Step 4: Payment card
    element_payment = (
        By.XPATH,
        "//div[@class='form']//div[text()='Método de pago']"
    )
    card_option = (
        By.XPATH,
        "//div//div[text()='Agregar tarjeta']"
    )
    card_number = (By.ID, "number")
    code_of_card = (
        By.XPATH,
        "//div[@class='card-wrapper']//input[@id='code']"
    )
    save_card = (
        By.XPATH,
        "//div//button[text()='Agregar']"
    )
    added_card = (
        By.XPATH,
        "//div[contains(@class,'pp-title') and text()='Tarjeta']"
    )
    boton_exit = (
        By.CSS_SELECTOR,
        ".payment-picker .section.active .section-close"
    )

    # Step 5: Driver message
    mensaje_para_el_conductor = (By.ID, "comment")

    # Step 6: Blanket and handkerchiefs
    manta_y_panuelos = (
        By.XPATH,
        "//div[contains(@class,'r-sw-container')]"
        "[.//div[text()='Manta y pañuelos']]"
        "//span[contains(@class,'slider')]"
    )
    manta_checkbox = (
        By.XPATH,
        "//div[contains(@class,'r-sw-container')]"
        "[.//div[text()='Manta y pañuelos']]"
        "//input[@type='checkbox']"
    )

    # Step 7: Ice cream
    cubeta_de_helado = (
        By.XPATH,
        "//div[@class='r r-type-group']"
        "//div[text()='Cubeta de helado']"
    )
    boton_helado = (
        By.XPATH,
        "//div[@class='r r-type-group']//div[text()='+']"
    )
    number_of_ice_creams = (
        By.XPATH,
        "//div[@class='r r-type-group']"
        "//div[@class='counter-value']"
    )

    # Step 8: Order search modal
    boton_pedir_un_taxi = (By.CLASS_NAME, "smart-button-wrapper")
    order_body = (By.CLASS_NAME, "order-body")
    info_order_body = (By.CLASS_NAME, "order-header-title")

    # Step 9: Driver information
    info_conductor = (
        By.XPATH,
        "//div[contains(text(),'El conductor llegará')]"
    )

    def __init__(self, driver):
        self.driver = driver

    def wait_for_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def wait_for_clickable(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )

    # Step 1
    def wait_for_load_home_page(self):
        self.wait_for_clickable(self.from_field)

    def set_from(self, from_address):
        field = self.wait_for_clickable(self.from_field)
        field.clear()
        field.send_keys(from_address)

    def set_to(self, to_address):
        field = self.wait_for_clickable(self.to_field)
        field.clear()
        field.send_keys(to_address)

    def wait_to_set_route(self):
        self.wait_for_clickable(self.pedir_un_taxi_field)

    def set_route(self, from_address, to_address):
        self.wait_for_load_home_page()
        self.set_from(from_address)
        self.set_to(to_address)
        self.wait_to_set_route()

    def get_from(self):
        return self.driver.find_element(
            *self.from_field
        ).get_property("value")

    def get_to(self):
        return self.driver.find_element(
            *self.to_field
        ).get_property("value")

    # Step 2
    def click_on_pedir_un_taxi(self):
        self.wait_for_clickable(self.pedir_un_taxi_field).click()

    def wait_for_comfort(self):
        self.wait_for_clickable(self.comfort_field)

    def click_on_it(self):
        self.wait_for_clickable(self.comfort_field).click()

    def click_on_comfort(self):
        self.click_on_pedir_un_taxi()
        self.wait_for_comfort()
        self.click_on_it()

    def get_the_text_comfort(self):
        return self.wait_for_element(self.comfort_field).text

    def get_active_tariff(self):
        return self.wait_for_element(self.comfort_active).text

    # Step 3
    def click_on_numero_de_telefono(self):
        self.wait_for_clickable(self.cellphone_field).click()

    def wait_for_numero_de_tel(self):
        self.wait_for_clickable(self.frame_cellphone_field)

    def click_on_the_frame_numero_de_telefono(self, phone_number):
        field = self.wait_for_clickable(self.frame_cellphone_field)
        field.clear()
        field.send_keys(phone_number)

    def click_on_siguiente(self):
        self.wait_for_clickable(
            self.boton_siguiente_after_cellphone
        ).click()

    def wait_for_code(self):
        self.wait_for_clickable(self.boton_introduce_codigo)

    def attach_the_phone_code(self):
        code = retrieve_phone_code(self.driver)
        field = self.wait_for_clickable(self.boton_introduce_codigo)
        field.send_keys(code)

    def click_on_confirmar(self):
        self.wait_for_clickable(
            self.boton_confirmar_after_code
        ).click()

    def set_up_phone_number(self, phone_number):
        self.click_on_numero_de_telefono()
        self.wait_for_numero_de_tel()
        self.click_on_the_frame_numero_de_telefono(phone_number)
        self.click_on_siguiente()
        self.wait_for_code()
        self.attach_the_phone_code()
        self.click_on_confirmar()
        self.wait_for_clickable(self.pedir_un_taxi_field)

    def get_the_phone_number(self):
        return self.wait_for_element(self.cellphone_field).text

    # Step 4
    def search_payment(self):
        element = self.wait_for_clickable(self.element_payment)
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            element
        )
        element.click()

    def wait_for_select_payment(self):
        self.wait_for_clickable(self.card_option)

    def select_card(self):
        self.wait_for_clickable(self.card_option).click()

    def wait_for_more_details(self):
        self.wait_for_clickable(self.card_number)

    def add_card(self, card_number, card_code):
        number_field = self.wait_for_clickable(self.card_number)
        number_field.clear()
        number_field.send_keys(card_number)

        code_field = self.wait_for_clickable(self.code_of_card)
        code_field.clear()
        code_field.send_keys(card_code, Keys.TAB)

        self.wait_for_clickable(self.save_card).click()

    def is_card_added(self):
        return self.wait_for_element(self.added_card).is_displayed()

    def exit_the_metodo_de_pago(self):
        self.wait_for_clickable(self.boton_exit).click()

    def add_card_as_a_payment(self, card_number, card_code):
        self.search_payment()
        self.wait_for_select_payment()
        self.select_card()
        self.wait_for_more_details()
        self.add_card(card_number, card_code)

        # Validate the saved card before closing the payment section.
        card_added = self.is_card_added()
        self.exit_the_metodo_de_pago()
        self.wait_for_clickable(self.pedir_un_taxi_field)

        return card_added

    # Step 5
    def send_mensaje_para_conductor(self, mensaje):
        field = self.wait_for_clickable(
            self.mensaje_para_el_conductor
        )
        field.clear()
        field.send_keys(mensaje)

    def get_mensaje_para_el_conductor(self):
        return self.driver.find_element(
            *self.mensaje_para_el_conductor
        ).get_property("value")

    # Step 6
    def click_manta_y_panuelos(self):
        self.wait_for_clickable(self.manta_y_panuelos).click()

    def is_manta_selected(self):
        checkbox = self.wait_for_element(self.manta_checkbox)
        return checkbox.is_selected()

    # Step 7
    def search_cubeta_de_helado(self):
        cubeta = self.wait_for_element(self.cubeta_de_helado)
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            cubeta
        )

    def add_2_helados(self):
        button = self.wait_for_clickable(self.boton_helado)
        button.click()
        button.click()

    def select_2_helados(self):
        self.search_cubeta_de_helado()
        self.add_2_helados()

    def check_number_of_ice_creams(self):
        return self.wait_for_element(
            self.number_of_ice_creams
        ).text

    # Step 8
    def select_a_taxi(self):
        self.wait_for_clickable(self.boton_pedir_un_taxi).click()

    def see_the_order_body(self):
        self.wait_for_element(self.order_body)

    def wait_until_you_see_the_order_body(self):
        self.select_a_taxi()
        self.see_the_order_body()

    def check_the_order_body(self):
        return self.wait_for_element(self.info_order_body).text

    # Step 9
    def check_the_info_of_the_driver(self):
        return self.wait_for_element(
            self.info_conductor,
            timeout=60
        ).text




