'''
Created by auto_sdk on 2014.10.23
'''
from top.api.base import RestApi
class AlibabaXiamiApiCollectDetailGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.full_des = None
		self.id = None
		self.tag = None

	def getapiname(self):
		return 'alibaba.xiami.api.collect.detail.get'
