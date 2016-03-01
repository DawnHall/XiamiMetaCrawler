'''
Created by auto_sdk on 2014.09.05
'''
from top.api.base import RestApi
class AlibabaXiamiApiLibraryAlbumRemoveRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.id = None

	def getapiname(self):
		return 'alibaba.xiami.api.library.album.remove'
