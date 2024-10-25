#!/usr/bin/env python3
"""Pymongo: inserts a new doc in a collection based on kwargs"""

import pymongo


def insert_school(mongo_collection, **kwargs):
    """
    Insert a doc into a mongo DB collection
    Return:
        ID of the inserted doc
    """
    data = mongo_collection.insert_one(kwargs)
    return data.inserted_id
