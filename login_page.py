# coding: utf-8
from selenium.webdriver.common.keys import Keys
from time import sleep

class LoginPage(object):
	def __init__(self, driver):
		self.driver = driver

	def get_textbox_username(self):
		return self.driver.find_element_by_xpath("//input[@name='userName']")
		
	def get_textbox_password(self):
		return self.driver.find_element_by_xpath("//input[@name='password']")

	def get_btn_login(self):
		return self.driver.find_element_by_xpath("//input[@name='login']")

	def login(self, username, password):
		self.get_textbox_username().send_keys(username)
		self.get_textbox_password().send_keys(password)
		self.get_btn_login().click()
		sleep(3)