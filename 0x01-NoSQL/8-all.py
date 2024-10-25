#!/usr/bin/env python3
"""Pymongo: list all documents in a collection"""

import pymongo


def list_all(mongo_collection):
    """
    Func to list all docs in a MongoDB collection
    Return:
        if not mongo DB, ret an empty list
        else, ret all documents
    """
    if not mongo_collection:
        return []
    documents = mongo_collection.find()
    return [post for post in documents]
