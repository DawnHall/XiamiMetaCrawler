'''
Created by auto_sdk on 2014.07.22
'''
from top.api.base import RestApi
class AlibabaXiamiApiAlbumDetailGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.full_des = None
		self.id = None

	def getapiname(self):
		return 'alibaba.xiami.api.album.detail.get'
