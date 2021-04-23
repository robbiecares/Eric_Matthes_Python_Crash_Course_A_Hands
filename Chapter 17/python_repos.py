import requests

def make_call(url, headers=''):
    if headers:
        r = requests.get(url, headers)
    else:
        r = requests.get(url)
    status_code = r.status_code

    return r, status_code

# Make an API call and store the response.
r, status_code = make_call('https://api.github.com/search/repositories?q=language:python&sort=stars',headers={'Accept': 'application/vnd.github.v3+json'})
print(f"Status code: {r.status_code}")

# Store API response in a variable.
response_dict = r.json()
print(f"Total repositories: {response_dict['total_count']}")

# Explore information about the repositories.
repo_dicts = response_dict['items']
print(f"Repositories returned: {len(repo_dicts)}")

# Summarize details of each repository
print("\nSelected information about each repository:\n")
for repo_dict in repo_dicts:
    print(f"Name: {repo_dict['name']}")
    print(f"Owner: {repo_dict['owner']['login']}")
    print(f"Stars: {repo_dict['stargazers_count']}")
    print(f"Repository: {repo_dict['html_url']}")
    print(f"Created: {repo_dict['created_at']}")
    print(f"Updated: {repo_dict['updated_at']}")
    print(f"Description: {repo_dict['description']}\n")