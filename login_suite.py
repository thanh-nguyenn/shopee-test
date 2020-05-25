# coding: utf-8
from selenium.webdriver import Chrome, Firefox
from common_lib import *
import unittest

class Login_Test(unittest.TestCase):
	#@classmethod
	def setUp(self):
		self.driver = Firefox()
		self.driver.get("http://newtours.demoaut.com/")
		self.driver.maximize_window()

	# @classmethod
	def tearDown(self):
		self.driver.close()
	
	def test_login(self):
		username = "shopeetest"
		password = "Shopee@2020"
		login(self.driver, username, password)
		
if __name__ == "__main__":
	unittest.main()
