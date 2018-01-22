#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: william wei 
@license: Apache Licence  
@contact: weixiaole@baidu.com
@file: advertisement.py 
@time: 22/01/2018 2:38 PM 
"""

from client import Client


class AdvertisementService(Client):
    def __init__(self):
        Client.__init__(self, 'bydsp', 'v1', 'AdService')

    def get_ad_by_id(self, ids):
        if not isinstance(ids, list):
            ids = [ids]
        return self._request('getAdByAdId', {'adIds': ids})

    def get_ads_by_group_id(self, group_id):
        return self._request('getAdByGroupId', {'groupId': group_id})

    def get_ad_ids_by_group_id(self, group_id):
        return self._request('getAdIdByGroupId', {'groupId': group_id})

    def add_ad(self, ad):
        return self._request('addAd', {'adTypes': [ad]})

    def update_ad(self, ad):
        return self._request('updateAd', {'adTypes': [ad]})

    def copy_ad(self, group_ids, ad_ids):
        return self._request('copyAd', {'groupIds': group_ids, 'adIds': ad_ids})

    def delete_ads(self, ids):
        if not isinstance(ids, list):
            ids = [ids]
        return self._request('deleteAd', {'adIds': ids})
