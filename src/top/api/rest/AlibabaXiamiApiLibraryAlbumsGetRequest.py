'''
Created by auto_sdk on 2014.09.11
'''
from top.api.base import RestApi
class AlibabaXiamiApiLibraryAlbumsGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.limit = None
		self.page = None

	def getapiname(self):
		return 'alibaba.xiami.api.library.albums.get'
