from playwright.sync_api import Page

class inkomstupppgifterPage:
    def __init__(self, page: Page):
        self.page = page
        
    def fylla_i_inkomst(self, inkomst: str):
        self.page.get_by_label("Månadsinkomst").fill(inkomst)
        
    def fyll_i_Anställningsform(self, anställningsform: str):
        self.page.get_by_label("Anställningsform").select_option(anställningsform)
    
    def fylla_inkomst(self, inkomst: str, anställningsform: str, arbetsgivare: str):
        self.fylla_i_inkomst(inkomst)
        self.fyll_i_Anställningsform(anställningsform)
        self.page.get_by_label("Arbetsgivare").fill(arbetsgivare)
        
    def click_next(self):
        self.page.locator("button:has-text('Nästa')").click()