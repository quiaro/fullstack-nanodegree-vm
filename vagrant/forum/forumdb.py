#
# Database access functions for the web forum.
#

import time
import psycopg2
import psycopg2.extras

## Database connection
DB = []

## Get posts from database.
def GetAllPosts():
    '''Get all the posts from the database, sorted with the newest first.

    Returns:
      A list of dictionaries, where each dictionary has a 'content' key
      pointing to the post content, and 'time' key pointing to the time
      it was posted.
    '''
    db = psycopg2.connect("dbname=forum")
    c = db.cursor(cursor_factory=psycopg2.extras.DictCursor)
    c.execute("""
        select content, time from posts order by time desc;
    """)
    rows = c.fetchall()
    db.close()
    return rows

    # posts = [{'content': str(row[1]), 'time': str(row[0])} for row in DB]
    # posts.sort(key=lambda row: row['time'], reverse=True)
    # return posts

## Add a post to the database.
def AddPost(content):
    '''Add a new post to the database.

    Args:
      content: The text content of the new post.
    '''
    db = psycopg2.connect("dbname=forum")
    c = db.cursor()
    c.execute("""
        insert into posts (content) values (%s);
    """, (content,))
    db.commit()
    db.close()

    # DB.append((t, content))
