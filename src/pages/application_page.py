from playwright.sync_api import Page


class applicationPage:
    def __init__(self, page: Page):
        self.page = page
        self.url = "https://souderbroder-loan-lab.lovable.app"
        
        self.first_name_input = "#firstName"
        self.last_name_input = "#lastName"
        self.personal_number_input = "#personalNumber"
        self.email_input = "#email"
        self.address_input = "#address"
        self.postcode_input = "#postcode"
        self.city_input = "#city"
        self.phone_input = "#phone"
        self.employment_type_dropdown = "#employmentType"
        self.employer_input = "#employer"
        self.income_input = "#income"
        self.submit_button = "text=Submit"