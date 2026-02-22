from playwright.sync_api import Page


class StartPage:
    def __init__(self, page: Page):
        self.page = page
        self.url = "https://souderbroder-loan-lab.lovable.app"
        
        self.loan_amount_input = "#loan-amount"
        self.repayment_dropdown = "#repaymentMonths"
        self.next_button = "text=Next"

    def navigate(self):
        self.page.goto(self.url)
        
    def fill_loan_amount(self, amount): 
        self.page.fill(self.loan_amount_input, str(amount))

    def select_repayment_months(self, months):
        self.page.select_option(self.repayment_dropdown, str(months))
    def click_next(self):
        self.page.click(self.next_button)
        
    def apply_for_loan(self, amount, months):
        self.fill_loan_amount(amount)
        self.select_repayment_months(months)
        self.click_next()