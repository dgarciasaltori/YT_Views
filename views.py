from time import sleep
from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy, ProxyType

proxy_address = "PROXY_IP_ADDRESS:PROXY_PORT"
username = "PROXY_USERNAME"
password = "PROXY_PASSWORD"

proxy = Proxy({
    'proxyType': ProxyType.MANUAL,
    'httpProxy': proxy_address,
    'ftpProxy': proxy_address,
    'sslProxy': proxy_address,
    'noProxy': ''
})

capabilities = webdriver.DesiredCapabilities.CHROME.copy()
proxy.add_to_capabilities(capabilities)

options = webdriver.ChromeOptions()
options.add_argument('--proxy-server={0}'.format(proxy_address))
options.add_argument('--proxy-auth={0}:{1}'.format(username, password))

driver1 = webdriver.Chrome(options=options, desired_capabilities=capabilities)
driver2 = webdriver.Chrome(options=options, desired_capabilities=capabilities)
driver3 = webdriver.Chrome(options=options, desired_capabilities=capabilities)
driver4 = webdriver.Chrome(options=options, desired_capabilities=capabilities)

driver1.get('https://www.youtube.com/watch?v=XqbvYgaZF0k')
driver2.get('https://www.youtube.com/watch?v=XqbvYgaZF0k')
driver3.get('https://www.youtube.com/watch?v=XqbvYgaZF0k')
driver4.get('https://www.youtube.com/watch?v=XqbvYgaZF0k')

while True:
    sleep(85)
    driver1.refresh()
    driver2.refresh()
    driver3.refresh()
    driver4.refresh()

