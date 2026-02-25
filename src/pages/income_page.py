from playwright.sync_api import Page

class inkomstupppgifterPage:
    def __init__(self, page: Page):
        self.page = page
        
    def fylla_i_inkomst(self, inkomst: str):
        self.page.get_by_label("Månadsinkomst (SEK) *").fill(inkomst)
        
    def fyll_i_Anställningsform(self, anställningsform: str):
        self.page.get_by_label("Anställningsform *").select_option(anställningsform)
    
    def fyll_i_arbetsgivare(self, arbetsgivare: str):
        self.page.get_by_label("Arbetsgivare *").fill(arbetsgivare)
    
    def fyll_i_Sidoinkomst(self, sidoinkomst: str):
        self.page.get_by_label("Sidoinkomst (SEK/månad)").fill(sidoinkomst)
    
    def fylla_inkomst(self, inkomst: str, anställningsform: str, arbetsgivare: str, sidoinkomst: str = "0"):
        self.fylla_i_inkomst(inkomst)
        self.fyll_i_Anställningsform(anställningsform)
        self.fyll_i_arbetsgivare(arbetsgivare)
        self.fyll_i_Sidoinkomst(sidoinkomst)
        
    def click_next(self):
        self.page.locator("button:has-text('Nästa')").click()