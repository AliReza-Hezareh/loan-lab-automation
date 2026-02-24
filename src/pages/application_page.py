from playwright.sync_api import Page


class ApplicationPage:
    def __init__(self, page: Page):
        self.page = page
        
    def fylla_i_personuppgifter(self, förnamn: str, efternamn: str, personnummer: str, email: str, phone: str, address: str, postcode: str, city: str):
        self.page.get_by_label("Personnummer").fill(personnummer)
        self.page.get_by_label("Förnamn").fill(förnamn)
        self.page.get_by_label("Efternamn").fill(efternamn)
        self.page.get_by_label("E-post").fill(email)
        self.page.get_by_label("Telefonnummer").fill(phone)
        self.page.get_by_label("Adress").fill(address)
        self.page.get_by_label("Postnummer").fill(postcode)
        self.page.get_by_label("Stad").fill(city)
        
    def click_next(self):
        self.page.locator("button:has-text('Nästa')").click()
        