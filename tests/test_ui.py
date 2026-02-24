from src.pages.product_page import ProductPage
from src.pages.application_page import ApplicationPage
from faker import Faker
fake = Faker()

def test_select_product(page):
    product_page = ProductPage(page)
    application_page = ApplicationPage(page)
    
    
    product_page.navigate()
    product_page.select_produkt("Bil")
    product_page.click_next()
    
    application_page.fylla_i_personuppgifter(
        personnummer="19900101-1234",
        förnamn=fake.first_name(),
        efternamn=fake.last_name(),
        email=fake.email(),
        phone=fake.phone_number(),
        address=fake.street_address(),
        postcode=fake.postcode(),
        city=fake.city()
    )
    application_page.click_next()