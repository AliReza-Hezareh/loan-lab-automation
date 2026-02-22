from src.pages.product_page import ProductPage

def test_select_product(page):
    product_page = ProductPage(page)
    product_page.navigate()
    
    product_page.select_produkt("Bil")
    product_page.click_next()