'''
Created by auto_sdk on 2014.08.08
'''
from top.api.base import RestApi
class AlibabaXiamiApiSongSongsByTagGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.limit = None
		self.page = None
		self.tag = None

	def getapiname(self):
		return 'alibaba.xiami.api.song.songsByTag.get'
