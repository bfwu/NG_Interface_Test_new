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


class QueryOrderSuccess(Init):
	'''查询订单信息'''
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
	
	def test_002_plan_seat_xml(self):
		'''查询放映计划可用座位_ID_DQuerySessionSeat'''
		global SeatCode
		requestName = get_current_function_name()
		client = suds.client.Client(self.url)
		xml = OnlineTicketingServiceQuery_D.plan_seat_xml(SessionPlanCode)
		res = client.service['NetSaleWebServicePort'].query(xml)
		status = repxml.get_status(res)
		self.assertEqual(status, 'Success')
		SeatCode = getAvilableSaleSeat(res)
		logger.info(requestName + '--' + repxml.get_keyOfValue("ErrorMessage", res) + "SeatCode" + ':' + SeatCode)
	
	def test_003_lock_seat_xml(self):
		'''锁定座位_ID_DLockSeat'''
		global OrderCode
		requestName = get_current_function_name()
		client = suds.client.Client(self.url)
		xml = OnlineTicketingServiceQuery_D.lock_seat_xml(SessionPlanCode, SeatCode)
		res = client.service['NetSaleWebServicePort'].query(xml)
		status = repxml.get_status(res)
		OrderCode = repxml.get_keyOfValue("OrderCode", res)
		self.assertEqual(status, 'Success')
		logger.info(requestName + '--' + repxml.get_keyOfValue("ErrorMessage", res) + "OrderCode" + ':' + OrderCode)
	
	def test_004_confirm_SCTS_order(self):
		'''确认SCTS订单交易接口_ID_SubmitOrder'''
		global PrintNo, VerifyCode
		requestName = get_current_function_name()
		client = suds.client.Client(self.url)
		xml = OnlineTicketingServiceQuery_D.order_sure_xml(OrderCode, SessionPlanCode, SeatCode, '50', '40', '10', '3')
		res = client.service['NetSaleWebServicePort'].query(xml)
		print res
		status = repxml.get_status(res)
		PrintNo = repxml.get_keyOfValue("PrintNo", res)
		VerifyCode = repxml.get_keyOfValue("VerifyCode", res)
		logger.info(requestName + '--' + repxml.get_keyOfValue("ErrorMessage",
															   res) + "PrintNo" + ':' + PrintNo + "VerifyCode" + ':' + VerifyCode)
		self.assertEqual(status, 'Success')
	
	def test_005_query_order_info(self):
		'''查询订单信息_ID_DQueryOrder'''
		requestName = get_current_function_name()
		client = suds.client.Client(self.url)
		xml = OnlineTicketingServiceQuery_D.query_order_info(OrderCode)
		res = client.service['NetSaleWebServicePort'].query(xml)
		
		logger.info(requestName + '--' + repxml.get_keyOfValue("ErrorMessage", res))
		status = repxml.get_status(res)
		self.assertEqual(status, 'Success')
	