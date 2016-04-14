##
# @file test_matlib.py
# @author Vojtech Obrusnik <xobrus00@stud.fit.vutbr.cz>
# @date 2016-04-14
# @brief Test suite for mathematical library

import unittest
import sys
# Append relative link to /src directory to be able to do import
sys.path.append(sys.path[0] + '/..')
from calculator.models import matlib


class TestMatlib(unittest.TestCase):

	def test_add(self):
		add = matlib.add

		self.assertEqual(add(1, 2), 3)
		self.assertEqual(add(-1, 2), 1)
