#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: william wei 
@license: Apache Licence  
@contact: weixiaole@baidu.com
@file: campaign.py 
@time: 21/01/2018 11:44 AM 
"""
from client import Client


class CampaignService(Client):
    def __init__(self):
        Client.__init__(self, 'bydsp', 'v1', 'CampaignService')

    def get_campaigns(self):
        return self._request('getCampaign')

    def get_campaign_ids(self):
        return self._request('getCampaignId')

    def get_campaigns_by_ids(self, ids):
        if not isinstance(ids, list):
            ids = [ids]
        return self._request('getCampaignId', {'campaignIds': ids})

    def add_campaign(self, campaign):
        return self._request('addCampaign', {'groupTypes': [campaign]})

    def update_campaign(self, campaign):
        return self._request('updateCampaign', {'groupType': [campaign]})

    def delete_campaign(self, campaign):
        return self.update_campaign({'campaignId': campaign['campaignId'], 'status': 2})


