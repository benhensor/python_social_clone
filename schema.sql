-- Drop the "posts" table if it already exists
DROP TABLE IF EXISTS posts;

-- Create the "posts" table
CREATE TABLE posts (
    -- The "id" column is an integer primary key with auto-incrementing values
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    -- The "name" column is a text field and cannot be null
    name TEXT NOT NULL,
    -- The "content" column is a text field and cannot be null
    content TEXT NOT NULL
);
