#!/usr/bin/env python3
"""Update_topics module"""


def update_topics(mongo_collection, name, topics):
    """
    A function that changes all topics of a school document based on the name
    """

    docs = {"name": name}
    updated = {"$set": {"topics": topics}}

    result = mongo_collection.update_many(docs, updated)
    return result
