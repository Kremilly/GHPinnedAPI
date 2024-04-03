import requests, logging

class GitHub:
    
    @staticmethod
    def user_exists(username, token):
        url = f"https://api.github.com/users/{username}"
        headers = {
            "Authorization": f"Bearer {token}",
            "Accept": "application/vnd.github.v3+json"  # Use a versão v3 da API
        }

        try:
            response = requests.get(url, headers=headers)
            
            if response.status_code == 200:
                return True
            elif response.status_code == 404:
                return False
            else:
                logging.error(f"Failed to check if user exists. Status Code: {response.status_code}, Response: {response.text}")
                return False
            
        except requests.RequestException as e:
            logging.error(f"Request Exception: {e}")
            return False

    @staticmethod
    def get_pinned_repositories(username, token):
        if not GitHub.user_exists(username, token):
            logging.error(f"User '{username}' does not exist on GitHub")
            return 404
        
        url = "https://api.github.com/graphql"

        headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
        }

        query = """
        query {
          user(login: "%s") {
            pinnedItems(first: 10, types: REPOSITORY) {
              nodes {
                ... on Repository {
                  name
                  description
                  url
                  homepageUrl
                  languages(first: 5) {
                    nodes {
                      name
                    }
                  }
                  stargazerCount
                  forkCount
                  repositoryTopics(first: 5) {
                    nodes {
                      topic {
                        name
                      }
                    }
                  }
                }
              }
            }
          }
        }
        """ % username

        try:
            response = requests.post(url, json={"query": query}, headers=headers)
            response.raise_for_status()  # Raise HTTPError for bad responses

            if response.status_code == 200:
                data = response.json().get("data", {}).get("user", {})
                return [
                    {
                        "name": repo["name"],
                        "description": repo["description"],
                        "url": repo["url"],
                        "home": repo.get("homepageUrl", ""),
                        "languages": [lang["name"] for lang in repo["languages"]["nodes"]],
                        "stars": repo.get("stargazerCount", 0),
                        "forks": repo.get("forkCount", 0),
                        "tags": [topic.get("topic", {}).get("name", "") for topic in repo.get("repositoryTopics", {}).get("nodes", [])],
                    }
                    
                    for repo in data.get("pinnedItems", {}).get("nodes", [])
                ]
            
            logging.error(
                f"Error retrieving pinned repositories. Status Code: {response.status_code}, Response: {response.text}"
            )
            
            return None

        except requests.RequestException as e:
            logging.error(f"Request Exception: {e}")
            return None

    @classmethod
    def get_repository_info(cls, user, token):
        repos_pinned = cls.get_pinned_repositories(user, token) 
        return repos_pinned
