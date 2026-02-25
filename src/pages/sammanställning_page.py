from playwright.sync_api import Page

class sammanställningPage:
    def __init__(self, page: Page):
        self.page = page
        
    def verify_page_loaded(self):
        self.page.get_by_role("heading", name="sammanställning").wait_for()
    
    def verify_loan_amount_visible(self, amount : str):
        self.page.get_by_text(amount).wait_for()
        
        
    def click_next(self):
        self.page.locator("button:has-text('Nästa')").click()