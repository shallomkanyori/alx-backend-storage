#!/usr/bin/env python3
""""List all documents

Functions:
    list_all(mongo_collection)
"""


def list_all(mongo_collection):
    """Returns all documents in a collection."""
    return [d for d in mongo_collection.find()]
