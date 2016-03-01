'''
Created by auto_sdk on 2014.06.30
'''
from top.api.base import RestApi
class AlibabaXiamiApiRadioGuessGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.limit = None

	def getapiname(self):
		return 'alibaba.xiami.api.radio.guess.get'
