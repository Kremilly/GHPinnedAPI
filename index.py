import os

from flask_caching import Cache
from flask import Flask, render_template

from core.github_endpoints import GitHubEndpoints

app = Flask(__name__)
app.config.from_mapping({
    "DEBUG": True,
    "CACHE_TYPE": "SimpleCache",
    "CACHE_DEFAULT_TIMEOUT": 300
})

cache = Cache(app)

@app.route("/")
def index():
    return render_template(
        'index.html', 
        header='GH Pinned API',
        title='GH Pinned API - Home', 
    )

@app.route('/api', methods=['GET'])
@cache.cached(timeout=180)
def get_pinneds():
    return GitHubEndpoints.repos_pinned()

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
