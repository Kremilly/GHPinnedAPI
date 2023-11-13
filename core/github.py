import requests

class GitHub:
    
    @classmethod
    def get_pinned_repositories(self, username, token):
        url = "https://api.github.com/graphql"
        
        headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
        }

        query = f"""
        query {{
        user(login: "{username}") {{
            pinnedItems(first: 10, types: REPOSITORY) {{
            nodes {{
                ... on Repository {{
                name
                description
                url
                languages(first: 5) {{
                    nodes {{
                    name
                    }}
                }}
                }}
            }}
            }}
            organizations(first: 10) {{
            nodes {{
                repositories(first: 10, ownerAffiliations: [OWNER]) {{
                nodes {{
                    ... on Repository {{
                    name
                    description
                    url
                    languages(first: 5) {{
                        nodes {{
                        name
                        }}
                    }}
                    }}
                }}
                }}
            }}
            }}
        }}
        }}
        """

        response = requests.post(url, json={"query": query}, headers=headers)

        if response.status_code == 200:
            pinned_repos = response.json()["data"]["user"]["pinnedItems"]["nodes"]
            org_repos = [repo["node"] for org in response.json()["data"]["user"]["organizations"]["nodes"] for repo in org["repositories"]["nodes"]]
            return pinned_repos + org_repos
        else:
            print(f"Error retrieving pinned repositories: {response.text}")
            return None
    
    @classmethod
    def get_repository_info(self, user, token):
        respos_pinned = self.get_pinned_repositories(user, token)

        if respos_pinned:
            result = []

            for repo in respos_pinned:
                linguagens = [lang["name"] for lang in repo["languages"]["nodes"]]

                repo_info = {
                    "name": repo["name"],
                    "description": repo["description"],
                    "url": repo["url"],
                    "languages": linguagens if linguagens else None
                }

                result.append(repo_info)
            return result
        else:
            return None
