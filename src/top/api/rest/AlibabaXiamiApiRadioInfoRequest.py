'''
Created by auto_sdk on 2014.06.04
'''
from top.api.base import RestApi
class AlibabaXiamiApiRadioInfoRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)

	def getapiname(self):
		return 'alibaba.xiami.api.radio.info'
