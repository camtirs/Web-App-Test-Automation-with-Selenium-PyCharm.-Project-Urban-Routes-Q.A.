import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import data
from pages import UrbanRoutesPage


class TestUrbanRoutes:

    def setup_method(self):
        chrome_options = Options()
        chrome_options.set_capability(
            "goog:loggingPrefs",
            {"performance": "ALL"}
        )

        self.driver = webdriver.Chrome(options=chrome_options)
        self.routes_page = UrbanRoutesPage(self.driver)
        self.driver.get(data.urban_routes_url)

    def teardown_method(self):
        if hasattr(self, "driver") and self.driver:
            self.driver.quit()

    def prepare_route(self):
        self.routes_page.set_route(
            data.address_from,
            data.address_to
        )

    def prepare_comfort(self):
        self.prepare_route()
        self.routes_page.click_on_comfort()
        assert self.routes_page.get_active_tariff() == "Comfort"

    def prepare_order(self):
        """Completes the prerequisites for submitting a taxi order."""
        self.prepare_comfort()

        self.routes_page.set_up_phone_number(data.phone_number)

        assert self.routes_page.add_card_as_a_payment(
            data.card_number,
            data.card_code
        )

        self.routes_page.send_mensaje_para_conductor(
            data.message_for_driver
        )

        self.routes_page.click_manta_y_panuelos()
        assert self.routes_page.is_manta_selected()

        self.routes_page.select_2_helados()
        assert self.routes_page.check_number_of_ice_creams() == "2"

    # Test 1: Route
    def test_set_route(self):
        self.prepare_route()

        assert self.routes_page.get_from() == data.address_from
        assert self.routes_page.get_to() == data.address_to

    # Test 2: Comfort tariff
    def test_select_comfort_tariff(self):
        self.prepare_comfort()

    # Test 3: Phone number
    def test_fill_phone_number(self):
        self.prepare_comfort()

        self.routes_page.set_up_phone_number(data.phone_number)

        assert (
            self.routes_page.get_the_phone_number()
            == data.phone_number
        )

    # Test 4: Payment card
    def test_add_card(self):
        self.prepare_comfort()

        assert self.routes_page.add_card_as_a_payment(
            data.card_number,
            data.card_code
        )

    # Test 5: Driver message
    def test_message_for_driver(self):
        self.prepare_comfort()

        self.routes_page.send_mensaje_para_conductor(
            data.message_for_driver
        )

        assert (
            self.routes_page.get_mensaje_para_el_conductor()
            == data.message_for_driver
        )

    # Test 6: Blanket and handkerchiefs
    def test_order_blanket_and_handkerchiefs(self):
        self.prepare_comfort()

        self.routes_page.click_manta_y_panuelos()

        assert self.routes_page.is_manta_selected()

    # Test 7: Two ice creams
    def test_order_two_ice_creams(self):
        self.prepare_comfort()

        self.routes_page.select_2_helados()

        assert (
            self.routes_page.check_number_of_ice_creams()
            == "2"
        )

    # Test 8: Taxi search modal
    def test_car_search_modal(self):
        self.prepare_order()

        self.routes_page.wait_until_you_see_the_order_body()

        assert (
            self.routes_page.check_the_order_body()
            == "Buscar automóvil"
        )

    # Test 9: Driver information
    def test_driver_info(self):
        self.prepare_order()

        self.routes_page.wait_until_you_see_the_order_body()

        driver_info = self.routes_page.check_the_info_of_the_driver()

        assert "El conductor llegará" in driver_info