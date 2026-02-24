from playwright.sync_api import Page


class ApplicationPage:
    def __init__(self, page: Page):
        self.page = page
        
    def fylla_i_personuppgifter(self, förnamn: str, efternamn: str, personnummer: str, email: str, phone: str, address: str, postcode: str, city: str):
        self.page.fill("#personalNumber", personnummer)
        self.page.fill("#firstName", förnamn)
        self.page.fill("#lastName", efternamn)
        self.page.fill("#email", email)
        self.page.fill("#phone", phone)
        self.page.fill("#address", address)
        self.page.fill("#postcode", postcode)
        self.page.fill("#city", city)
        