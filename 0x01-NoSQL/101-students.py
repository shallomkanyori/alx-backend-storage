#!/usr/bin/env python3
"""Top students

Functions:
    top_students(mongo_collection)
"""


def top_students(mongo_collection):
    """Returns a lists of all students sorted by average score."""
    res = mongo_collection.aggregate([{'$addFields': {
                                            'averageScore': {
                                                '$avg': '$topics.score'}}},
                                      {'$sort': {'averageScore': -1}}])

    return res
