# -*- coding: utf-8 -*-
"""
Linked list is just like a set of nested dict
@author: danid
"""

head = {
        "value":2,
        "next": {
            "value":4,
            "next":{
                "value":6,
                "next":None}
            }
    }
    

print(head['next']['next']['value'])