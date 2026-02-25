from playwright.sync_api import Page

class inkomstupppgifterPage:
    def __init__(self, page: Page):
        self.page = page
        
    def fylla_i_inkomst(self, inkomst: str):
        self.page.wait_for_selector("#monthlyIncome")
        self.page.locator("#monthlyIncome").fill(inkomst)
        
    def fyll_i_Anställningsform(self, anställningsform: str):
        self.page.wait_for_selector("#employmentType")
        self.page.locator("#employmentType").click()
        self.page.get_by_text(anställningsform).click()
        
            
    def fyll_i_arbetsgivare(self, arbetsgivare: str):
        self.page.wait_for_selector("#employer")
        self.page.locator("#employer").fill(arbetsgivare)
    
    def fyll_i_Sidoinkomst(self, sidoinkomst: str):
        self.page.wait_for_selector("#sideIncome")
        self.page.locator("#sideIncome").fill(sidoinkomst)
    
    def fylla_inkomst(self, inkomst: str, anställningsform: str, arbetsgivare: str, sidoinkomst: str = "0"):
        self.page.get_by_role("heading", name="Inkomstuppgifter").wait_for()
        self.fylla_i_inkomst(inkomst)
        self.fyll_i_Anställningsform(anställningsform)
        self.fyll_i_arbetsgivare(arbetsgivare)
        self.fyll_i_Sidoinkomst(sidoinkomst)
        
    def click_next(self):
        self.page.locator("button:has-text('Nästa')").click()