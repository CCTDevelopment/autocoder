from flask import Blueprint, request, jsonify
from .task_manager import handle_task  # Absolute import

main_blueprint = Blueprint("main", __name__)

@main_blueprint.route("/generate_program", methods=["POST"])
def generate_program():
    data = request.get_json()
    prompt = data.get("prompt")
    
    if not prompt:
        return jsonify({"error": "No prompt provided"}), 400

    response = handle_task(prompt)
    return jsonify(response), 200
