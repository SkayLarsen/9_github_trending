import requests
from datetime import date, timedelta


def get_trending_repositories(top_size=20, days=7):
    url = "https://api.github.com/search/repositories"
    start_date = date.today() - timedelta(days)
    params = {'q': 'created:>%s' % start_date, 'sort': 'stars', 'per_page': top_size}
    response = requests.get(url, params)
    return response.json()["items"]


if __name__ == '__main__':
    trending_repositories = get_trending_repositories()
    print("Список интересных репозиториев:")
    for rep in trending_repositories:
        print("Репозиторий {}  имеет {} звёзд, {} открытых задач, и доступен по ссылке: {}".format(
              rep['name'], rep['stargazers_count'], rep['open_issues'], rep['html_url']))