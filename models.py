import sqlite3
# import os.path as path because we want to use the path module
from os import path

# ROOT is defined as the directory where the file is located
ROOT = path.dirname(path.relpath((__file__)))

# define the create_post function
def create_post(name, content):
  # connect to the database
  con = sqlite3.connect(path.join(ROOT, 'database.db'))
  # create a cursor object
  cur = con.cursor()
  # execute the query to insert the name and content into the posts table
  cur.execute('insert into posts (name, content) values(?, ?)', (name, content))
  # commit the changes to the database
  con.commit()
  # close the connection to the database
  con.close()


# define the get_posts function
def get_posts():
  # connect to the database
  con = sqlite3.connect(path.join(ROOT, 'database.db'))
  # create a cursor object
  cur = con.cursor()
  # execute the query to select all the posts from the posts table
  cur.execute('select * from posts')
  # fetch all the posts from the database
  posts = cur.fetchall()
  # close the connection to the database
  return posts
