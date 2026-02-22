from playwright.sync_api import Page


class ProductPage:
    def __init__(self, page: Page):
        self.page = page
        self.url = "https://souderbroder-loan-lab.lovable.app/product"
        
    def navigate(self):
        self.page.goto(self.url)
        
    def select_produkt(self, product_name: str):
        self.page.get_by_role("heading", name=product_name).click()
        
    def click_next(self):
        self.page.get_by_role("button", name="Nästa").click()