import requests
from plotly.graph_objs import Bar
from plotly import offline

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
# apparently request using api of this edition
headers = {'Accept': 'application/vnd.github.v3+json'}
# use request to call api
r = requests.get(url, headers = headers)
print(f"Status code: {r.status_code}")
# Assign api respond to 'respond_dict'
respond_dict = r.json()
# print(respond_dict.keys())
repo_dicts = respond_dict['items']
# print(f"Total returned: {len(repo_dicts)}")

repo_links, stars, labels = [], [], []
for repo_dict in repo_dicts:
    repo_name = repo_dict['name']
    repo_url = repo_dict['html_url']
    repo_link = f"<a herf='{repo_url}'>{repo_name}</a>"
    repo_links.append(repo_link)
    stars.append(repo_dict['stargazers_count'])

    owner = repo_dict['owner']['login']
    description = repo_dict['description']
    label = f"{owner}<br />{description}"
    labels.append(label)

# visualization
data = [{
    'type': 'bar',
    'x': repo_links,
    'y': stars,
    'hovertext': labels,
    'marker': {
        'color': 'rgb(60, 150, 150)',
        'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'}
    },
    'opacity': 0.6
}]

my_layout = {
    'title': 'Most welcomed python project in Github',
    'titlefont': {'size': 28},
    'xaxis': {
        'title': 'Repository',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14}
    },
    'yaxis': {
        'title': 'Stars',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14}
    },

}

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename = 'python_repos.html')