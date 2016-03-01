'''
Created by auto_sdk on 2015.04.14
'''
from top.api.base import RestApi
class AlibabaXiamiApiSearchCollectsGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.key = None
		self.limit = None
		self.order = None
		self.page = None
		self.tag = None

	def getapiname(self):
		return 'alibaba.xiami.api.search.collects.get'
