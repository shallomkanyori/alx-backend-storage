#!/usr/bin/env python3
"""Log stats

Displays some stats about Nginx logs stored in MongoDB.
"""
from pymongo import MongoClient


if __name__ == '__main__':
    client = MongoClient('mongodb://127.0.0.1:27017')
    log_coll = client.logs.nginx

    print('{} logs'.format(log_coll.count_documents({})))

    print('Methods:')
    method_list = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
    for m in method_list:
        method_count = log_coll.count_documents({'method': m})
        print('\tmethod {}: {}'.format(m, method_count))

    status_check_count = log_coll.count_documents({'method': 'GET',
                                                   'path': '/status'})
    print('{} status check'.format(status_check_count))
