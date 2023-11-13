import os
from dotenv import load_dotenv
from core.github import GitHub
from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template(
        'index.html', 
        header='GH Pinned API',
        title='GH Pinned API - Home', 
    )

@app.route('/api', methods=['GET'])
def repos_pinned():
    load_dotenv()

    user = request.args.get('user')
    token = os.environ.get('GH_TOKEN')

    if not user:
        return jsonify({"error": "Parameter 'user' not provided"}), 400

    repos_info = GitHub.get_repository_info(user, token)

    if repos_info:
        return jsonify(repos_info)
    else:
        return jsonify({"error": "Error fetching pinned repositories"}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
