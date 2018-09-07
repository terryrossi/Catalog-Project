# "Database code" for the DB Forum.

import datetime

import psycopg2

#POSTS = [("This is the first post.", datetime.datetime.now())]

def get_posts():
  """Return all posts from the 'database', most recent first."""
  conn = psycopg2.connect(database="forum")
  cursor = conn.cursor()
  cursor.execute("select content, time from posts order by time desc")
  POSTS = cursor.fetchall()
  conn.close()
  return POSTS

def add_post(content):
  """Add a post to the 'database' with the current timestamp."""
  conn = psycopg2.connect(database="forum")
  cursor = conn.cursor()
  cursor.execute("insert into posts (content) values ('%s')" % content)
  conn.commit()
  conn.close()
#POSTS.append((content, datetime.datetime.now()))
