# -*- coding: utf-8 -*-
import os
import time
import unittest

import suds
import sys

from src.test.init import Init

print sys.path
from src.test.public.Log import logger
from src.test.public.url import url_query
from src.test.data_xml import OnlineTicketingServiceQuery_D
from src.test.data_xml.methonSelf import *


class QueryTicketType(Init):
	'''查询票价类型'''
	def test_001_search_show_plan(self):
		'''查询放映计划_ID_DQuerySession'''
		global SessionPlanCode
		requestName = get_current_function_name()
		client = suds.client.Client(self.url)
		xml = OnlineTicketingServiceQuery_D.film_plan_xml()
		res = client.service['NetSaleWebServicePort'].query(xml)
		status = repxml.get_status(res)
		self.assertEqual(status, 'Success')
		SessionPlanCode = repxml.get_value("Code", res)[0]
		logger.info(
		requestName + '--' + repxml.get_keyOfValue("ErrorMessage", res) + "SessionPlanCode" + ':' + SessionPlanCode)
		
	def test_002_query_ticket_type(self):
		'''查询票价类型_ID_QueryTicketTyp'''
		global SessionPlanCode
		requestName = get_current_function_name()
		client = suds.client.Client(self.url)
		xml = OnlineTicketingServiceQuery_D.film_plan_xml()
		res = client.service['NetSaleWebServicePort'].query(xml)
		print res
		status = repxml.get_status(res)
		self.assertEqual(status, 'Success')
		SessionPlanCode = repxml.get_value("Code", res)[0]
		logger.info(
		requestName + '--' + repxml.get_keyOfValue("ErrorMessage",res) + "SessionPlanCode" + ':' + SessionPlanCode)
	

