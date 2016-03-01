'''
Created by auto_sdk on 2015.03.14
'''
from top.api.base import RestApi
class AlibabaXiamiApiLibraryCollectAddRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.id = None

	def getapiname(self):
		return 'alibaba.xiami.api.library.collect.add'
