import os
from dotenv import load_dotenv

from flask import jsonify, request

from core.github import GitHub

class GitHubEndpoints(GitHub):

    @classmethod
    def repos_pinned(cls):
        load_dotenv()

        if not request.args and 'user' in request.args:
            return jsonify({"error": "Parameter 'user' not provided"}), 400
        
        user = request.args['user']
        token = os.environ.get('GH_TOKEN')

        callback = cls.get_pinned_repositories(user, token)
        
        if not callback:
            return jsonify({"message": f"User '{user}' does not have any pinned repositories"}), 200
        elif callback == 404:
            return jsonify({"error": f"User '{user}' does not exist on GitHub"}), 404
        elif callback:
            return jsonify(callback), 200
        else:
            return jsonify({"error": "Error fetching pinned repositories"}), 500
