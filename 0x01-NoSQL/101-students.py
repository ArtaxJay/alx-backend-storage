#!/usr/bin/env python3
"""
Pymongo: func returns all students sorted by average score
"""


def top_students(mongo_collection):
    """ sort students by avg. score and return the sorted list """
    return mongo_collection.aggregate([
        {
            "$project":
                {
                    "name": "$name",
                    "averageScore": {"$avg": "$topics.score"}
                }
        },
        {
            "$sort":
                {
                    "averageScore": -1
                }
        }
    ])
