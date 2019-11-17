from selenium.webdriver import Chrome

def before_all(context):
    path = "C:\\Users\\dell\\Downloads\\chromedriver_win32 (8)\\chromedriver.exe"
    context.driver = Chrome(executable_path=path)
    context.driver.maximize_window()

def after_all(context):
    context.driver.close()