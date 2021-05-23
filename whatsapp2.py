from selenium import webdriver

driver = webdriver.Chrome('C:\\Users\\Aviv\\Downloads\\chromedriver_win32\\chromedriver.exe')
driver.implicitly_wait(15)
driver.get('https://web.whatsapp.com')

# loop forever
while True:
    try:
        driver.find_element_by_css_selector("span[title='" + input("Enter name to spam: ") + "']").click()
        inputString = input("Enter message to send: ")
        for i in range(0, int(input("how many msgs to send?"))):
            driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(inputString)
            driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button').click()
    except Exception:
        print("cant do the thing")
    finally:
        print("lets do it again!:")
