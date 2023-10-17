#!/usr/bin/env python3
"""Insert_school module"""


def insert_school(mongo_collection, **kwargs):
    """
    A function that inserts a new document in a collection based on kwargs
    """
    inserted_id = mongo_collection.insert_one(kwargs).inserted_id
    return inserted_id
