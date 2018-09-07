# "Database code" for the DB Forum.

import datetime

import psycopg2

conn = psycopg2.connect(dbname(forum)

#POSTS = [("This is the first post.", datetime.datetime.now())]

def get_posts():
  """Return all posts from the 'database', most recent first."""
  cursor = conn.cursor()
  cursor.execute("select * from posts order by time desc")
  POSTS = cursor.fetchall()
  conn.close()
  return POSTS

def add_post(content):
  """Add a post to the 'database' with the current timestamp."""
  cursor = conn.cursor()
  cursor.execute("insert into posts (content) values content")
  conn.commit()
  conn.close()

#POSTS.append((content, datetime.datetime.now()))
