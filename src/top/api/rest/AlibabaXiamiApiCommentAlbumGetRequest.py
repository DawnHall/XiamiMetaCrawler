'''
Created by auto_sdk on 2015.03.18
'''
from top.api.base import RestApi
class AlibabaXiamiApiCommentAlbumGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.id = None
		self.limit = None
		self.page = None

	def getapiname(self):
		return 'alibaba.xiami.api.comment.album.get'
