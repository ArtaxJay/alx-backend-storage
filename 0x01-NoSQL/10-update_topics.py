#!/usr/bin/env python3
"""Pymongo: changes all topics of a school doc based on the name"""

import pymongo


def update_topics(mongo_collection, name, topics):
    """
    func changes all topics of a school doc based on the name
    Return:
        name
        or topics
    """
    return mongo_collection.update_many({
            "name": name
        },
        {
            "$set": {
                "topics": topics
            }
        })
