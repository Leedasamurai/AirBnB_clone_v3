#!/usr/bin/python3
"""index"""

from api.v1.views import app_views
from flask import jsonify
from models import storage

classes = {
        "amenities": Amenity,
        "cities": City,
        "places": Place,
        "reviews": Review,
        "states": State,
        "users": User,
        }

@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """Returns the status of the API"""
    return jsonify({"status": "OK"})

@app_views.route("/stats")
def stats():
    """Retrieve the number of each objects by type"""
    statistics = {}

    for key, value in classes.items():
        statistics[key] = storage.count(value)

    return jsonify(statistics)
