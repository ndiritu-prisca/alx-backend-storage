#!/usr/bin/env python3
"""A schools_by_topic module"""


def schools_by_topic(mongo_collection, topic):
    """
    A function that returns the list of school having a specific topic
    """
    results = mongo_collection.find({"topics": topic})
    return list(results)
