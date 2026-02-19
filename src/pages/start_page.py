from playwright.sync_api import Page


class StartPage:
    def __init__(self, page: Page):
        self.page = page
        self.url = "https://kzmcpfklrqymzazaxlmv.supabase.co/functions/v1/partner-loan-api"
        
        self.loan_amount_input = "#loan-amount"
        self.repayment_dropdown = "#repaymentMonths"
        self.next_button = "text=Next"

    def navigate(self):
        self.page.goto(self.url)
        
    def fill_loan_amount(self, amount):
        self.page.fill(self.loan_amount_input, str(amount))

    def click_apply_now(self):
        self.page.click("text=Apply Now")