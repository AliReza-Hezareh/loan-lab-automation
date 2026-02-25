from playwright.sync_api import Page

class loan_amountPage:
    def __init__(self, page: Page):
         self.page = page
         
    def fylla_i_lånebelopp(self, lånebelopp: str):
        self.page.get_by_role("heading", name="Lånebelopp och återbetalningstid").wait_for()
        self.page.locator("input[type='number']").fill(lånebelopp)

    def klicka_beräkna(self):
        self.page.get_by_text("Beräkna månadskostnad").click()

    def click_next(self):
        self.page.locator("button:has-text('Nästa')").click()