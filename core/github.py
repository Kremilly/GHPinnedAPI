import requests
import json
import logging

class GitHub:

    @classmethod
    def get_pinned_repositories(cls, username, token):
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
            organizations(first: 10) {
              nodes {
                repositories(first: 10, ownerAffiliations: [OWNER]) {
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
          }
        }
        """ % username

        try:
            response = requests.post(url, json={"query": query}, headers=headers)
            response.raise_for_status()  # Raise HTTPError for bad responses

            if response.status_code == 200:
                data = response.json()
                pinned_repos = cls.extract_repos(data["data"]["user"]["pinnedItems"]["nodes"])
                org_repos = [
                    cls.extract_repo(org["repositories"]["nodes"])
                    for org in data["data"]["user"]["organizations"]["nodes"]
                ]
                return pinned_repos + org_repos
            else:
                logging.error(
                    f"Error retrieving pinned repositories. Status Code: {response.status_code}, Response: {response.text}"
                )
                return None

        except requests.RequestException as e:
            logging.error(f"Request Exception: {e}")
            return None

    @staticmethod
    def extract_repos(repos):
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
            for repo in repos
        ]

    @classmethod
    def get_repository_info(cls, user, token):
        repos_pinned = cls.get_pinned_repositories(user, token)

        if repos_pinned:
            return repos_pinned
        else:
            return None
