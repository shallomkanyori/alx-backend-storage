#!/usr/bin/env python3
"""List filtered documents

Function:
    schools_by_topic(mongo_collection, topic)
"""


def schools_by_topic(mongo_collection, topic):
    """Returns the list of school documents having a specific topic."""

    return [d for d in mongo_collection.find({'topics': topic})]
