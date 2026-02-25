import pytest 
from playwright.sync_api import Page, expect
from src.pages.product_page import ProductPage
from src.pages.application_page import ApplicationPage
from src.pages.income_page import inkomstupppgifterPage
from src.pages.loan_belopp_page import loan_amountPage
from src.pages.sammanställning_page import sammanställningPage
from faker import Faker

fake = Faker()

@pytest.fixture
def till_personuppgifter(page: Page) -> Page:
    product_page = ProductPage(page)
    product_page.navigate()
    product_page.select_produkt("Bil")
    product_page.click_next()
    expect(page.get_by_role("heading", name="Personuppgifter")).to_be_visible()
    return page
    

def select_product(page):
    product_page = ProductPage(page)
    
    
    product_page.navigate()
    product_page.select_produkt("Bil")
    product_page.click_next()
    
    expect(page.get_by_role("heading", name="Personuppgifter")).to_be_visible()
    
def fylla_i_personuppgifter(till_personuppgifter: Page):
    application_page = ApplicationPage(till_personuppgifter)
    
    application_page.fylla_i_personuppgifter(
        personnummer="2601072396",
        förnamn=fake.first_name(),
        efternamn=fake.last_name(),
        email=fake.email(),
        phone=fake.phone_number(),
        address=fake.street_address(),
        postcode=fake.postcode(),
        city=fake.city()
    )
    expect(till_personuppgifter.get_by_label("Personnummer")).to_have_value("2601072396")
    


def test_fill_income_information(page):
    product_page = ProductPage(page)
    application_page = ApplicationPage(page)
    income_page = inkomstupppgifterPage(page)
    loan_page = loan_amountPage(page)
    samman_page = sammanställningPage(page)

    product_page.navigate()
    product_page.select_produkt("Bil")
    product_page.click_next()

    application_page.fylla_i_personuppgifter(
        personnummer="2601072396",
        förnamn=fake.first_name(),
        efternamn=fake.last_name(),
        email=fake.email(),
        phone=fake.phone_number(),
        address=fake.street_address(),
        postcode=fake.postcode(),
        city=fake.city()
    )
    application_page.click_next()

    income_page.fylla_inkomst(
        inkomst="30000",
        anställningsform="Visstidsanställd",
        arbetsgivare="Test AB",
        sidoinkomst="5000"
    )

    income_page.click_next()

    page.get_by_role("heading", name="Lånebelopp").wait_for()
    assert page.get_by_role("heading", name="Lånebelopp").is_visible()
    

    loan_page.fylla_i_lånebelopp("150000")
    slider = page.locator("input[type='range']")
    slider.fill("24")
    loan_page.klicka_beräkna()
    loan_page.click_next()

    page.get_by_role("heading", name="Sammanställning").wait_for()
    assert page.get_by_role("heading", name="Sammanställning").is_visible()
    

    samman_page.verify_page_loaded()
    samman_page.verify_loan_amount_visible("150000")

    samman_page.click_next()

    page.get_by_role("heading", name="Bekräftelse").wait_for()
    assert page.get_by_role("heading", name="Bekräftelse").is_visible()