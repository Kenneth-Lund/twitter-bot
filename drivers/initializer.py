from networking.networking import login
from networking.networking import submit_post
from selenium.webdriver.chrome.options import Options
from models.models import Parameters
from selenium import webdriver
import time

def start():

    # 1 initialize bot parameters
    parameters = Parameters()

    #TO DO Fetch top 5 trending #'s

    #TO DO fetch reddit post based on parameters and download media

    # 2 initialize webdriver
    webdriver = initialize_webdriver(parameters)

    # webdriver was not initialized correctly
    if webdriver == None:
        return

    # 3 login twitter user
    user = login(webdriver, parameters)

    time.sleep(3)

    # 4 Submit post
    post = submit_post(webdriver, user)

    print("Scuccess: " + str(post.time_posted))

    return


# Initiliazes and returns a Webdriver object
def initialize_webdriver(parameters):

    try:
        print("Initializing webdriver...")

        opts = Options()

        opts.add_argument('--disable-blink-features=AutomationControlled')
        opts.add_argument("start-maximized")
        driver = webdriver.Chrome(executable_path=parameters.chromedriver_path, options=opts)

        driver.execute_cdp_cmd('Network.setUserAgentOverride', {
            "userAgent": 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:77.0) Gecko/20190101 Firefox/77.0'})

        driver.execute_cdp_cmd('Network.setUserAgentOverride', {
            "userAgent": 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:77.0) Gecko/20190101 Firefox/77.0'})
        time.sleep(2)
        return driver
    except Exception as e:
        print("Issue initializing webdriver: " + e)
        return None


if __name__ == "__main__":
    start()