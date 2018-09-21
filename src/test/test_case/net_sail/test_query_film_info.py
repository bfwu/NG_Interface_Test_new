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


class QueryFilmInfo(Init):
	'''查询影片信息'''
	def test_001_search_show_plan(self):
		'''获取影片信息_ID_DQueryFilm'''
		#说明：查询电影院在一段时期中上映的影片信息,测试得来的结果还必须是当天有排期，如果没排期，依然不显示，有拷贝也不行
		requestName = get_current_function_name()
		url = url_query()
		client = suds.client.Client(url)
		xml = OnlineTicketingServiceQuery_D.film_info_xml()
		res = client.service['NetSaleWebServicePort'].query(xml)
		print res
		status = repxml.get_status(res)
		self.assertEqual(status, 'Success')
		SessionPlanCode = repxml.get_value("Code", res)[0]
		logger.info(requestName + '--' + repxml.get_keyOfValue("ErrorMessage", res) + "SessionPlanCode" + ':' + SessionPlanCode)