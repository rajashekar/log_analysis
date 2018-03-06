#!/usr/bin/env python3
from reportdb import get_most_3pop_articles, get_most_pop_authors
from reportdb import get_days_with_more_errors


def main():
    '''Main page of the forum.'''
    f = open('sample_output.txt', 'w')
    f.write('What are the most popular three articles of all time?')
    result = "".join(
      '\n%s - %d views' % row for row in get_most_3pop_articles()
    )
    f.write(result)
    f.write('\n\nWho are the most popular article authors of all time?')
    result = "".join(
      '\n%s - %d views' % row for row in get_most_pop_authors()
    )
    f.write(result)
    f.write('\n\nOn which days did more than 1% of requests lead to errors?')
    result = "".join(
      '\n%s - %.2f%% errors' % r for r in get_days_with_more_errors()
    )
    f.write(result)
    f.close()


main()
