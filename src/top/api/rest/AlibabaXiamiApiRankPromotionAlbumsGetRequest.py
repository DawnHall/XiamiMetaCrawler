'''
Created by auto_sdk on 2015.03.19
'''
from top.api.base import RestApi
class AlibabaXiamiApiRankPromotionAlbumsGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.limit = None
		self.page = None
		self.type = None

	def getapiname(self):
		return 'alibaba.xiami.api.rank.promotion.albums.get'
