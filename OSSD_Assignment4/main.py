from selenium import webdriver
driver=webdriver.Chrome()
driver.get("https://lms.umt.edu.pk/login/index.php")
driver.find_element_by_id("username").send_keys("f2019105054")
driver.find_element_by_id("password").send_keys("bTDT11@H")
driver.find_element_by_id("loginbtn").click
button=driver.find_element_by_tag_name("button").click()
x=driver.find_elements_by_tag_name("a")
for i in range(17,26):
    print(i,x[i].text)