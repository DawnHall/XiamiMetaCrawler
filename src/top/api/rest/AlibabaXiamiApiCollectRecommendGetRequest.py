'''
Created by auto_sdk on 2014.06.30
'''
from top.api.base import RestApi
class AlibabaXiamiApiCollectRecommendGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.description = None
		self.limit = None
		self.page = None
		self.type = None

	def getapiname(self):
		return 'alibaba.xiami.api.collect.recommend.get'
