# -*- coding: utf-8 -*-
import os
import time
import unittest

import suds
import sys

from src.test.data_xml.methonSelf import get_current_function_name
from src.test.public.Log import logger
from src.test.public.url import url_query


class Init(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		cls.url = url_query()
		cls.OrderCode = '0'
		cls.SeatCode = '0'
		cls.PrintNo = '0'
		cls.VerifyCode = '0'
		cls.ServiceFee = '0'
		cls.plan_list = []
		cls.SeatCode = '0'
		cls.SessionPlanCode = '0'
