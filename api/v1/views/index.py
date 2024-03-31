#!/usr/bin/python3
"""index"""

from api.v1.views import app_views
from flask import jsonify
from models import storage

@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """Returns the status of the API"""
    return jsonify({"status": "OK"})

@app_views.route('/status', methods=['GET'])
def count():
    """ returns number of each objects by type """
    total = {}
    classes = {"Amenity": "amenities",
            "City": "cities",
            "Place": "places",
            "Review": "reviews",
            "State": "states",
            "User": "users"}
    for cls in classes:
        count = storage.count(cls)
        total[classes.get(cls)] = count
    return jsonify(total)
