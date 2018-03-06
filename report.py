#!/usr/bin/env python3
from flask import Flask, request, redirect, url_for
from reportdb import get_most_3pop_articles, get_most_pop_authors
from reportdb import get_days_with_more_errors
app = Flask(__name__)


@app.route('/', methods=['GET'])
def main():
    '''Main page of the forum.'''
    html = '''<b>What are the most popular three articles of all time?</b>'''
    result = "".join(
      '<div>%s - %d views</div>' % row for row in get_most_3pop_articles()
    )
    html = html + result
    html = html + '''<br><b>Who are the most popular article authors of all
    time?</b>'''
    result = "".join(
      '<div>%s - %d views</div>' % row for row in get_most_pop_authors()
    )
    html = html + result
    html = html + '''<br><b>On which days did more than 1% of requests lead to
    errors?</b>'''
    result = "".join(
      '<div>%s - %.2f%% errors</div>' % r for r in get_days_with_more_errors()
    )
    html = html + result
    return html


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
