#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: william wei 
@license: Apache Licence  
@contact: weixiaole@baidu.com
@file: group.py 
@time: 22/01/2018 2:27 PM 
"""

from client import Client


class GroupService(Client):
    def __init__(self):
        Client.__init__(self, 'bydsp', 'v1', 'GroupService')

    def get_groups_by_campaign_id(self, campaign_id):
        return self._request('getGroupByCampaignId', {'campaignId': campaign_id})

    def get_group_ids_by_campaign_id(self, campaign_id):
        return self._request('getGroupIdByCampaignId', {'campaignId': campaign_id})

    def get_groups_by_ids(self, ids):
        if not isinstance(ids, list):
            ids = [ids]
        return self._request('getGroupByGroupId', {'groupIds': ids})

    def add_group(self, group):
        return self._request('addGroup', {'groupTypes': [group]})

    def update_group(self, group):
        return self._request('updateGroup', {'groupTypes': [group]})

    def delete_group(self, group):
        return self.update_group({'groupId': group['groupId'], 'status': 2})
