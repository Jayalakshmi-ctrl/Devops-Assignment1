from flask import Blueprint, jsonify, abort
from models import PROGRAMS, METRICS

api = Blueprint('api', __name__)

# Service Endpoint 1: Fetch overall gym and infrastructure baseline metrics
@api.route('/api/metrics', methods=['GET'])
def get_gym_metrics():
    return jsonify(METRICS), 200

# Service Endpoint 2: List all available fitness tracks
@api.route('/api/programs', methods=['GET'])
def list_programs():
    # Returns the list of program names to match choice inputs
    return jsonify(list(PROGRAMS.keys())), 200

# Service Endpoint 3: Fetch custom workout and nutrition plans matching a track name
@api.route('/api/programs/<string:program_name>', methods=['GET'])
def get_program_details(program_name):
    # Safe match lookup matching your desktop UI state drop-down selections
    if program_name not in PROGRAMS:
        return jsonify({"error": f"Program '{program_name}' does not exist"}), 404
        
    return jsonify(PROGRAMS[program_name]), 200
