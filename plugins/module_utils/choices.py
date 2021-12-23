# -*- coding: utf-8 -*-
# Copyright: (c) 2021, XLAB Steampunk <steampunk@xlab.si>
#
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type

from . import errors

class ChoicesClient:
    def __init__(self, table_client):
        self.table_client = table_client

    def get_choices(self, table_name, element=None):
        query = {
            "name": table_name,
        }
        if element:
            query["element"] = element

        choices = self.table_client.list_records("sys_choice", query)
        return choices
    
    def group_choices(self, data): 
        result = dict()
        for item in data:
            key = item["element"]
            bucket = result.get(key, [])
            bucket.append((item["value"], item["label"]))
            result[key] = bucket
        return result

    def get_grouped_choices(self, table_name):
        data = self.get_choices(table_name)
        grouped = self.group_choices(data)
        return grouped
