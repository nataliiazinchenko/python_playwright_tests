from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto('http://google.com/')
    page.screenshot(path="demo.png")
    browser.close()