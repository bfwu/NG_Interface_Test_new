# -*- coding: utf-8 -*-

import time
import unittest

import suds

from src.test.data_xml import OnlineTicketingServiceQuery_D
from src.test.data_xml import *
from src.test.data_xml.methonSelf import get_current_function_name, getAvilableSaleSeat
from src.test.init import Init
from src.test.public import repxml
from src.test.public.Log import logger
from src.test.public.url import url_query


class SearchHallSeat(Init):
	'''查询影厅座位'''
	def test_001_search_show_plan(self):
		'''查询放映计划_ID_DQuerySession'''
		global SessionPlanCode
		requestName = get_current_function_name()
		client = suds.client.Client(self.url)
		xml = OnlineTicketingServiceQuery_D.film_plan_xml()
		res = client.service['NetSaleWebServicePort'].query(xml)
		
		self.assertEqual(repxml.get_status(res), 'Success')
		SessionPlanCode = repxml.get_value("Code", res)[0]
		logger.info(
			requestName + '--' + repxml.get_keyOfValue("ErrorMessage", res) + "SessionPlanCode" + ':' + SessionPlanCode)
	
	def test_002_plan_seat_xml(self):
		'''查询放映计划可用座位_ID_DQuerySessionSeat'''
		requestName = get_current_function_name()
		global SeatCode
		client = suds.client.Client(self.url)
		xml = OnlineTicketingServiceQuery_D.plan_seat_xml(SessionPlanCode)
		res = client.service['NetSaleWebServicePort'].query(xml)
		
		self.assertEqual(repxml.get_status(res), 'Success')
		SeatCode = getAvilableSaleSeat(res)
		logger.info(requestName + '--' + repxml.get_keyOfValue("ErrorMessage", res) + "SeatCode" + ':' + SeatCode)
	