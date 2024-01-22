#!/usr/bin/env python3
"""Change school topics

Functions:
    update_topics(mongo_collection, name, topics)
"""


def update_topics(mongo_collection, name, topics):
    """Updates topics attribute of school document based on name.

    Args:
        mongo_collection: pymongo collection object.
        name (str): The school name to update.
        topics (list of str): The list of topics.
    """

    mongo_collection.update_many({'name': name}, {'$set': {'topics': topics}})
