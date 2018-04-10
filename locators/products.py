"""
Locators for Products Page are placed here
"""
from selenium.webdriver.common.by import By
from .base import BasePageLocators


# pylint: disable=too-few-public-methods
class ProductsPageLocators(BasePageLocators):
    """
    Locators for Products Page are placed here
    """
    MAC_PRODUCT_IMAGE = (By.XPATH, '//*[@id="content"]/div[2]/div/div/div[1]/a/img')

    @staticmethod
    def find_product_link(product_name):
        """
        Wrapper for product name locator.
        """
        link = (By.XPATH, '//a[text()="{}"]'.format(product_name))
        return link
