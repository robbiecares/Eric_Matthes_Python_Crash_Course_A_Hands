from operator import itemgetter
import requests
from plotly.graph_objs import Bar
from plotly import offline

def make_call(url):
    r = requests.get(url)
    status_code = r.status_code
    return r, status_code

# Make an API call and store the response.
r, status_code = make_call('https://hacker-news.firebaseio.com/v0/topstories.json')


# Process information about each submission.
submission_ids = r.json()
submission_dicts = []
for submission_id in submission_ids[:10]:
    # Make a separate API call for each submission.
    r, status_code = make_call(f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json")
    response_dict = r.json()

    # Build a dictionary for each article.
    submission_dict = {
        'title': response_dict['title'],
        'hnid': str(submission_id),
        'hn_link': f"http://news.ycombinator.com/item?id={submission_id}",
        'comments': response_dict['descendants'],
    }
    submission_dicts.append(submission_dict)

submission_dicts = sorted(submission_dicts, key=itemgetter('comments'), reverse=True)

comments = [submission_dict['comments'] for submission_dict in submission_dicts]
hnids = [str(submission_dict['hnid']) for submission_dict in submission_dicts]
discussion_links = []
for submission_dict in submission_dicts:
    url = submission_dict['hn_link']
    title = submission_dict['title']
    discussion_link = f"<a href='{url}'>{title}</a>"
    discussion_links.append(discussion_link)

# Make visualization
data = [{
    'type': 'bar',
    'x': discussion_links,
    'y': comments,
'marker': {
'color': 'rgb(60, 100, 150)',
'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'}
},
'opacity': 0.6,
}]

my_layout = {
'title': 'Top Hacker News Discussions',
'titlefont': {'size': 28},
'xaxis': {
    'title': 'HN ID',
    'type': 'category',
    'titlefont': {'size': 24},
    'tickfont': {'size': 14},
    },
'yaxis': {
    'title': 'Comments',
    'titlefont': {'size': 24},
    'tickfont': {'size': 14},
    },
}

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='HN_top_discussions.html')