##
# @file main.py
# @author Vojtech Obrusnik <xobrus00@stud.fit.vutbr.cz>
# @date 2016-04-11
# @brief Preview of presenter containing example of interaction with its view.


from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.widget import Widget
from ..models import matlib


# Load appropriate view
Builder.load_file('calculator/views/main.kv')


##
# Main class of presenter
class MainPresenter(Widget):
	##
	# @var StringProperty result Information displayed in view
	result = StringProperty('')

	##
	# Handles click action of + button from view
	# @param string result
	def click_add(self, result):
		self.result = 'Value "{}" passed from view.\nCalling matlib.add(5, 4) = {}'.format(result, matlib.add(5, 4))
