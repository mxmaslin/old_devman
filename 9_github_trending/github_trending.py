import datetime
import requests


def get_trending_repositories(top_size):
    now = datetime.datetime.now()
    week = datetime.timedelta(weeks=1)
    last_week_start = now - week
    last_week_start = str(last_week_start.date())
    url = 'http://api.github.com/search/repositories'
    created = 'created:>={}'.format(last_week_start)
    payload = {'q': created, 'sort': 'stars', 'per_page': top_size}
    request = requests.get(url, params=payload)
    return request.json()['items']


def get_open_issues_amount(repo_owner, repo_name):
    url = 'http://api.github.com/repos/{}/{}/issues'
    request = requests.get(url.format(repo_owner, repo_name))
    return len([x for x in request.json() if x['state'] == 'open'])


if __name__ == '__main__':
    top_size = 20
    trending_repositories = get_trending_repositories(top_size)
    for repository in trending_repositories:
        repo_owner = repository['owner']['login']
        repo_name = repository['name']
        repository_issues_amount = get_open_issues_amount(repo_owner, repo_name)
        repo_url = repository['url']
        print('{} has {} issue(s)'.format(repo_url, repository_issues_amount))
