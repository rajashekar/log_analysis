import psycopg2
import sys

DBNAME = "news"


def connect(database_name):
    """Connect to the database.  Returns a database connection."""
    try:
        db = psycopg2.connect(database=database_name)
        return db
    except psycopg2.Error as e:
        print("Unable to connect to database")
        sys.exit(1)


def get_most_3pop_articles():
    """What are the most popular three articles of all time?"""
    conn = connect(DBNAME)
    cur = conn.cursor()
    cur.execute("""SELECT a.title,b.viewcount
                FROM articles a,
                 (SELECT path, COUNT(*) AS viewcount
                    FROM log
                    WHERE path LIKE '/article/%'
                    GROUP BY path
                    ORDER BY viewcount DESC
                    LIMIT 3) b
                WHERE '/article/'||a.slug = b.path
                ORDER BY b.viewcount DESC;""")
    results = cur.fetchall()
    conn.close()
    return results


def get_most_pop_authors():
    """Who are the most popular article authors of all time?"""
    conn = connect(DBNAME)
    cur = conn.cursor()
    cur.execute("""SELECT c.name, sum(b.viewcount) AS totalviews
                    FROM
                        articles a,
                        (SELECT path, COUNT(*) AS viewcount
                         FROM log
                         WHERE path LIKE '/article/%'
                         GROUP BY path
                         ORDER BY viewcount DESC) b,
                        authors c
                    WHERE '/article/'||a.slug = b.path
                    AND a.author = c.id
                    GROUP BY c.name
                    ORDER BY totalviews DESC;
                """)
    results = cur.fetchall()
    conn.close()
    return results


def get_days_with_more_errors():
    """On which days did more than 1% of requests lead to errors?"""
    conn = connect(DBNAME)
    cur = conn.cursor()
    cur.execute("""SELECT to_char(b.time, 'Mon DD, YYYY') AS date,
                    round(
                        CAST(
                            float8 (100*b.errorcount::FLOAT/a.totalcount::FLOAT
                        ) AS numeric), 2
                    ) AS errorpercent
                   FROM
                    (SELECT
                      TIME::DATE, COUNT(*) AS totalcount
                      FROM log GROUP BY TIME::DATE) a ,
                    (SELECT
                      TIME::DATE, COUNT(*) AS errorcount
                      FROM log WHERE status != '200 OK' GROUP BY TIME::DATE) b
                   WHERE a.time = b.time
                    AND round(
                          CAST(
                            float8 (100*b.errorcount::FLOAT/a.totalcount::FLOAT
                          ) AS numeric), 2
                        ) > 1.0
                """)
    results = cur.fetchall()
    conn.close()
    return results
