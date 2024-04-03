import os

from flask import Flask, render_template

from core.github_endpoints import GitHubEndpoints

app = Flask(__name__)

@app.route("/")
def index():
    return render_template(
        'index.html', 
        header='GH Pinned API',
        title='GH Pinned API - Home', 
    )

@app.route('/api', methods=['GET'])
def get_pinneds():
    return GitHubEndpoints.repos_pinned()

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
