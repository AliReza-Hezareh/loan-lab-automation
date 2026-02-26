from playwright.sync_api import Page
from src.config import GUI_BASE_URL


class ProductPage:
    def __init__(self, page: Page):
        self.page = page
        
    def navigate(self):
        self.page.goto(GUI_BASE_URL)
        
    def select_produkt(self, product_name: str):
        self.page.get_by_role("heading", name=product_name).click()
        
    def click_next(self):
        self.page.get_by_role("button", name="Nästa").click()
        
    def fyll_i_personuppgifter(self, first_name, last_name, personal_number, email):
        self.page.fill("#personalNumber", personal_number)
        self.page.fill("#firstName", first_name)
        self.page.fill("#lastName", last_name)
        self.page.fill("#email", email)