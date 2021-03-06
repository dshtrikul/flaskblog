CREATE DATABASE IF NOT EXISTS blog_db;

CREATE TABLE user (
id INTEGER NOT NULL AUTO_INCREMENT,
username VARCHAR(20) NOT NULL,
email VARCHAR(120) NOT NULL,
image_file VARCHAR(20) NOT NULL,
password VARCHAR(60) NOT NULL,
aboutme VARCHAR(1000),
last_seen DATETIME,
PRIMARY KEY (id),
UNIQUE (username),
UNIQUE (email)
);

CREATE TABLE post (
id INTEGER NOT NULL AUTO_INCREMENT,
title VARCHAR(120) NOT NULL,
date_posted DATETIME NOT NULL,
content TEXT NOT NULL,
user_id INTEGER NOT NULL,
PRIMARY KEY (id),
FOREIGN KEY(user_id)
REFERENCES user (id)
);
