from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class BMICalculatorE2ETest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_calculate_bmi(self):
        # User goes to the homepage
        self.browser.get(self.live_server_url)

        # User sees the input fields and enters their height and weight
        height_input = self.browser.find_element_by_id('height')
        weight_input = self.browser.find_element_by_id('weight')
        height_input.send_keys('180')
        weight_input.send_keys('80')

        # User submits the form
        submit_button = self.browser.find_element_by_css_selector('input[type="submit"]')
        submit_button.click()

        # User sees the result page with their BMI and category
        bmi_result = self.browser.find_element_by_id('bmi-result')
        category_result = self.browser.find_element_by_id('category-result')

        self.assertIn('24.69', bmi_result.text)
        self.assertIn('Normal Weight', category_result.text)
