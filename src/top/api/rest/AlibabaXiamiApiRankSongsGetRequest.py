'''
Created by auto_sdk on 2014.08.26
'''
from top.api.base import RestApi
class AlibabaXiamiApiRankSongsGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.type = None

	def getapiname(self):
		return 'alibaba.xiami.api.rank.songs.get'
