from selenium import webdriver

browser = webdriver.Firefox()

browser.get('http://127.0.0.1:5000')

assert "Hello, World!" in browser.page_source

print "Test passed!"
browser.quit()