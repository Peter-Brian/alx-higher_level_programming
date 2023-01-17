import requests
import sys

def get_commits(repo, owner):
    url = f"https://api.github.com/repos/{owner}/{repo}/commits"
    response = requests.get(url)
    commits = response.json()
    for commit in commits[:10]:
        sha = commit['sha']
        author = commit['commit']['author']['name']
        print(f"{sha}: {author}")

if __name__ == "__main__":
    repo = sys.argv[1]
    owner = sys.argv[2]
    get_commits(repo, owner)
