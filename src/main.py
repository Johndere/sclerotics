##
# @file main.py
# @author Vojtech Obrusnik <xobrus00@stud.fit.vutbr.cz>
# @date 2016-04-11
# @brief Application start point.


import kivy
kivy.require('1.9.1')

from kivy.app import App
from calculator.presenters.main import MainPresenter


##
# Main application class
class CalculatorApp(App):

	##
	# Initialization of base application widget
	def build(self):
		# Set window title
		self.title = 'Calculator'
		return MainPresenter()


if __name__ == '__main__':
	CalculatorApp().run()
