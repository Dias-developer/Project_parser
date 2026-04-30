from playwright.sync_api import sync_playwright
from auth import login_and_save_cookie
from parser import get_datas

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)

        context = browser.new_context()
        login_and_save_cookie(context)

        context = browser.new_context(
            storage_state="state.json",
        )

        page = context.new_page()

        page.goto('https://quotes.toscrape.com')

        all_datas = []

        while True:
            data = get_datas(page)
            all_datas.extend(data)

            next_btn = page.query_selector('.next a')

            if not next_btn:
                break

            next_url = next_btn.get_attribute('href')
            page.goto('https://quotes.toscrape.com' + next_url)
        print(all_datas)
        browser.close()

if "__main__" == __name__:
    main()