from flask import Flask, request, jsonify, render_template
import requests
from requests.exceptions import RequestException
from datetime import datetime

app = Flask(__name__)

GITHUB_API_BASE = "https://api.github.com"

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/analyze")
def analyze():
    username = request.args.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400

    user_url = f"{GITHUB_API_BASE}/users/{username}"
    repos_url = f"{GITHUB_API_BASE}/users/{username}/repos"

    try:
        # Add headers to identify our application
        headers = {
            'User-Agent': 'GitHub-Resume-Analyzer',
            'Accept': 'application/vnd.github.v3+json'
        }

        # Get user data
        user_resp = requests.get(user_url, headers=headers)
        print(f"User API Response Status: {user_resp.status_code}")
        print(f"User API Response: {user_resp.text}")

        if user_resp.status_code == 403 and 'X-RateLimit-Remaining' in user_resp.headers and user_resp.headers['X-RateLimit-Remaining'] == '0':
            reset_time = int(user_resp.headers.get('X-RateLimit-Reset', 0))
            reset_dt = datetime.utcfromtimestamp(reset_time).strftime('%Y-%m-%d %H:%M:%S UTC')
            return jsonify({"error": "GitHub API rate limit exceeded", "rate_limit_reset": reset_dt}), 429
        
        if user_resp.status_code != 200:
            error_message = f"GitHub API Error: {user_resp.status_code}"
            if user_resp.text:
                try:
                    error_data = user_resp.json()
                    error_message = error_data.get('message', error_message)
                except:
                    pass
            return jsonify({"error": error_message, "status_code": user_resp.status_code}), 404

        user_data = user_resp.json()

        # Get repositories data
        repos_resp = requests.get(repos_url, headers=headers)
        print(f"Repos API Response Status: {repos_resp.status_code}")
        print(f"Repos API Response: {repos_resp.text}")

        if repos_resp.status_code == 403 and 'X-RateLimit-Remaining' in repos_resp.headers and repos_resp.headers['X-RateLimit-Remaining'] == '0':
            reset_time = int(repos_resp.headers.get('X-RateLimit-Reset', 0))
            reset_dt = datetime.utcfromtimestamp(reset_time).strftime('%Y-%m-%d %H:%M:%S UTC')
            return jsonify({"error": "GitHub API rate limit exceeded", "rate_limit_reset": reset_dt}), 429
        
        if repos_resp.status_code != 200:
            error_message = f"Could not fetch repositories: {repos_resp.status_code}"
            if repos_resp.text:
                try:
                    error_data = repos_resp.json()
                    error_message = error_data.get('message', error_message)
                except:
                    pass
            return jsonify({"error": error_message, "status_code": repos_resp.status_code}), 500

        repos = repos_resp.json()

    except RequestException as e:
        return jsonify({"error": "Network error", "details": str(e)}), 500

    total_stars = sum(repo.get("stargazers_count", 0) for repo in repos)
    languages = list(set(repo.get("language") for repo in repos if repo.get("language")))
    last_activity = max((repo.get("updated_at", "") for repo in repos), default="N/A")

    return render_template('result.html',
                         username=username,
                         public_repos=user_data.get("public_repos"),
                         total_stars=total_stars,
                         languages=languages,
                         last_activity=last_activity)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True) 