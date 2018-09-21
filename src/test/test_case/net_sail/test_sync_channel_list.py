# -*- coding: utf-8 -*-
import os
import time
import unittest

import suds
import sys

from src.test.data_xml import OnlineTicketingServiceQuery_D
from src.test.data_xml.methonSelf import get_current_function_name
from src.test.init import Init
from src.test.public import repxml
from src.test.public.Log import logger
from src.test.public.url import url_query


class SyncChannelList(Init):
	def test_001_sync_channel_lsit(self):
		'''同步排期_ID_SyncChannelList'''
		global SessionPlanCode
		requestName = get_current_function_name()
		client = suds.client.Client(self.url)
		xml = OnlineTicketingServiceQuery_D.sync_channel_list()
		res = client.service['NetSaleWebServicePort'].query(xml)
		print res
		status = repxml.get_status(res)
		self.assertEqual(status, 'Success')
		logger.info(
			requestName + '--' + repxml.get_keyOfValue("ErrorMessage", res))
