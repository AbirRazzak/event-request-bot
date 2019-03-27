from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

USER_NAME = ''
PASSWORD = ''

EVENT_NAME = 'Fake Event'
EVENT_DESC = 'This is a totally testable description'
START_DATE = '01 Apr 2019'
START_TIME = '01:15 PM'
# END_DATE = '01 Apr 2019'
END_TIME = '02:15 PM'
EVENT_LOCATION = 'Drexel Park'
EST_ATTENDANCE = '20'
SAFAC_ACC_NUM = '170178'
EST_COST = '$0'
PHONE_NUMBER = '2672748265'

browser = webdriver.Firefox(executable_path='D:\\GitRepositories\\event-request-bot\\assets\\geckodriver.exe')
browser.implicitly_wait(10)  # this thing runs too fast, increase for slower internet
browser.get('https://dragonlink.drexel.edu/')
browser.find_element_by_class_name('css-lnzkvj').click()  # log-in button
browser.find_element_by_id('username').send_keys(USER_NAME)
browser.find_element_by_id('password').send_keys(PASSWORD)
browser.find_element_by_class_name('btn-success').click()

# browser.get('https://dragonlink.drexel.edu/actioncenter/organization/fisdu/events')
# browser.find_element_by_class_name('button-text').click()
browser.get('https://dragonlink.drexel.edu/submitter/organization/FISDU/eventsubmission/create')

# page 1
browser.find_element_by_id('Name').send_keys(EVENT_NAME)
Select(browser.find_element_by_id('Theme')).select_by_value('Cultural')
browser.find_element_by_id('Description_ifr').send_keys(EVENT_DESC)
# Date and Times
browser.find_element_by_id('Instances[0]_StartDate').send_keys(Keys.BACKSPACE*11)
browser.find_element_by_id('Instances[0]_StartDate').send_keys(START_DATE)
browser.find_element_by_id('Instances[0]_StartDate').send_keys(Keys.ENTER)

browser.find_element_by_id('Instances[0]_StartTime').send_keys(Keys.BACKSPACE*11)
browser.find_element_by_id('Instances[0]_StartTime').send_keys(START_TIME)
browser.find_element_by_id('Instances[0]_StartTime').send_keys(Keys.ENTER)

# browser.find_element_by_id('Instances[0]_EndDate').send_keys(Keys.BACKSPACE*11)
# browser.find_element_by_id('Instances[0]_EndDate').send_keys(END_DATE)
# browser.find_element_by_id('Instances[0]_EndDate').send_keys(Keys.ENTER)

browser.find_element_by_id('Instances[0]_EndTime').send_keys(Keys.BACKSPACE*11)
browser.find_element_by_id('Instances[0]_EndTime').send_keys(END_TIME)
browser.find_element_by_id('Instances[0]_EndTime').send_keys(Keys.ENTER)

# Location
browser.find_element_by_class_name('instance-location-button').click()
browser.find_element_by_class_name('btn-hide-map').click()
browser.find_element_by_id('Instances[0].ExternalLocation').send_keys(EVENT_LOCATION)
browser.find_elements_by_class_name('ui-button-text')[1].click()  # save button

browser.find_elements_by_class_name('mdl-button')[1].click()  # next button

# page 2
# For now, skip uploading an event banner photo
browser.find_elements_by_class_name('mdl-button')[1].click()  # skip button

# page 3
browser.find_element_by_css_selector("input[type='radio'][value='33452529']").click()  # level 0 event
browser.find_elements_by_class_name('mdl-button')[1].click()  # next button

# page 4
Select(browser.find_element_by_id('dropDown-7693942')).select_by_value('33945649')  # see below for selection by text
# Select(browser.find_element_by_id('dropDown-7693942'))
# .select_by_visible_text('Identity Based- CE Contact is Maurice Cottman')
browser.find_element_by_css_selector("input[type='radio'][value='33457723'").click()  # org is not new

# TODO: ADD LOGIC TO CHOOSE OPEN OR CLOSED EVENT
browser.find_element_by_css_selector("input[type='radio'][value='33457724'").click()  # if open event
browser.find_element_by_css_selector("input[type='radio'][value='33457725'").click()  # if closed event

browser.find_element_by_id('answerTextBox-33457726-free').send_keys(EST_ATTENDANCE)  # estimated attendance
browser.find_element_by_css_selector("input[type='radio'][value='33457727'").click()  # on campus event

# TODO: ADD LOGIC TO CHOOSE YES OR NO FOOD
browser.find_element_by_css_selector("input[type='radio'][value='33457730'").click()  # if providing food
browser.find_element_by_css_selector("input[type='radio'][value='33457731'").click()  # if no food

browser.find_element_by_css_selector("input[type='radio'][value='33457732'").click()  # using SAFAC funds
browser.find_element_by_id('answerTextBox-33457732-free').send_keys(SAFAC_ACC_NUM)
browser.find_element_by_id('answerTextBox-33457738-free').send_keys(EST_COST)
browser.find_element_by_id('answerTextBox-33457739-free').send_keys(PHONE_NUMBER)
browser.find_elements_by_class_name('mdl-button')[1].click()  # next button

# page 5
# TODO: ADD LOGIC TO CHOOSE YES OR NO EQUIPMENT
browser.find_element_by_css_selector("input[type='radio'][value='33845560'").click()  # if need to reserve equipment
browser.find_element_by_css_selector("input[type='radio'][value='33845561'").click()  # if no
browser.find_element_by_css_selector("input[type='radio'][value='31993464'").click()  # yes, need to reserve space

# can probably manually do the rest by myself
# TODO: WRITE A COMMAND LINE OR UI TO INPUT VALUES TO RUN THIS CODE
