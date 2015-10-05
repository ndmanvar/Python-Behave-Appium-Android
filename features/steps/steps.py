import os
from appium import webdriver

username = os.environ.get('SAUCE_USERNAME')
access_key = os.environ.get('SAUCE_ACCESS_KEY')

@given('we are on a "{device_name}" device')
def step_impl(context, device_name):

  desired_caps = {
    "name": context.name,
    "app": "http://saucelabs.com/example_files/ContactManager.apk",
    "platformName": "Android",
    "deviceName": device_name,
    "browserName": "",
    "platformVersion": "4.4",
    "appiumVersion": "1.4.11",
    "deviceOrientation": "portrait"
  }

  url = 'http://%s:%s@ondemand.saucelabs.com:80/wd/hub' % (username, access_key)

  context.driver = webdriver.Remote(url, desired_caps)

@given('I click on the add contact button')
def step_impl(context):
  button_one = context.driver.find_element_by_name("Add Contact")
  button_one.click()

@when('I enter a name and email')
def step_impl(context):
  text_fields = context.driver.find_elements_by_class_name("android.widget.EditText")
  text_fields[0].send_keys("Some Name")
  text_fields[2].send_keys("Some@example.com")

@then('I click the Save button')
def step_impl(context):
  save_button = context.driver.find_element_by_name("Save").click()
