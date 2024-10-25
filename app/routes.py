import logging
from flask import Blueprint, request, jsonify
from .task_manager import handle_task

main_blueprint = Blueprint("main", __name__)

@main_blueprint.route("/generate_program", methods=["POST"])
def generate_program():
    data = request.get_json()
    prompt = data.get("prompt")
    
    if not prompt:
        logging.error("No prompt provided in the request")
        return jsonify({"error": "No prompt provided"}), 400

    logging.info("Processing prompt: %s", prompt)
    try:
        response = handle_task(prompt)
        logging.info("Prompt processed successfully")
        return jsonify(response), 200
    except Exception as e:
        logging.error("Error processing prompt: %s", e)
        return jsonify({"error": "Internal server error"}), 500
