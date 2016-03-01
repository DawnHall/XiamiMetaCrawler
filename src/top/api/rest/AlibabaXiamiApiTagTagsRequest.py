'''
Created by auto_sdk on 2014.10.23
'''
from top.api.base import RestApi
class AlibabaXiamiApiTagTagsRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.object_id = None
		self.object_type = None

	def getapiname(self):
		return 'alibaba.xiami.api.tag.tags'
