from playwright.sync_api import Playwright, sync_playwright, ViewportSize
from fake_useragent import UserAgent
viewport: ViewportSize = {'height':800, 'width':1000}
def get_datas(playwright: Playwright):
    browser = playwright.chromium.launch(headless=True)
    content = browser.new_context(
        viewport=viewport,
        user_agent=UserAgent().random,
    )

    page = content.new_page()

    page.goto('https://quotes.toscrape.com/')

    data = []

    quotes = page.query_selector_all('.quote')

    for q in quotes:
        author = q.query_selector('.author')
        quote = q.query_selector('.text')

        if author and quote:
            data.append({
                'author': author.inner_text().strip(),
                'quote': quote.inner_text().strip(),
            })
    print(data)