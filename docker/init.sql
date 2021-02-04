BEGIN;

CREATE SCHEMA datascience;

DROP TABLE IF EXISTS datascience.badges;

CREATE TABLE datascience.badges (
    id                  	integer,
    user_id             	integer,
    name                	varchar(50),
    date                	timestamp,
    class               	smallint,
    tag_based           	boolean,
    PRIMARY KEY (id)
);

COPY datascience.badges(id, user_id, name, date, class, tag_based)
FROM '/docker-entrypoint-initdb.d/data/badges.csv'
WITH (
  FORMAT CSV,
  DELIMITER ',',
  NULL '',
  HEADER,
  FORCE_NULL(user_id, name, date, class, tag_based)
);

COMMIT;

DROP TABLE IF EXISTS datascience.comments;

CREATE TABLE datascience.comments (
    id                  	integer,
    post_id             	integer,
    score               	integer,
    text                	varchar(600),
    creation_date       	timestamp,
    user_id             	integer,
    content_license     	varchar(12),
    user_display_name   	varchar(40),
    PRIMARY KEY (id)
);

COPY datascience.comments(id, post_id, score, text, creation_date, user_id, content_license, user_display_name)
FROM '/docker-entrypoint-initdb.d/data/comments.csv'
WITH (
  FORMAT CSV,
  DELIMITER ',',
  NULL '',
  HEADER,
  FORCE_NULL(post_id, score, text, creation_date, user_id, content_license, user_display_name)
);

COMMIT;

DROP TABLE IF EXISTS datascience.post_history;

CREATE TABLE datascience.post_history (
    id                  	integer,
    post_history_type_id	smallint,
    post_id             	integer,
    revision_guid       	uuid,
    creation_date       	timestamp,
    user_id             	integer,
    text                	varchar,
    content_license     	varchar(12),
    comment             	varchar(400),
    user_display_name   	varchar(40),
    PRIMARY KEY (id)
);

COPY datascience.post_history(id, post_history_type_id, post_id, revision_guid, creation_date, user_id, text, content_license, comment, user_display_name)
FROM '/docker-entrypoint-initdb.d/data/post_history.csv'
WITH (
  FORMAT CSV,
  DELIMITER ',',
  NULL '',
  HEADER,
  FORCE_NULL(post_history_type_id, post_id, revision_guid, creation_date, user_id, text, content_license, comment, user_display_name)
);

COMMIT;

DROP TABLE IF EXISTS datascience.post_links;

CREATE TABLE datascience.post_links (
    id                  	integer,
    creation_date       	timestamp,
    post_id             	integer,
    related_post_id     	integer,
    link_type_id        	smallint,
    PRIMARY KEY (id)
);

COPY datascience.post_links(id, creation_date, post_id, related_post_id, link_type_id)
FROM '/docker-entrypoint-initdb.d/data/post_links.csv'
WITH (
  FORMAT CSV,
  DELIMITER ',',
  NULL '',
  HEADER,
  FORCE_NULL(creation_date, post_id, related_post_id, link_type_id)
);

COMMIT;

DROP TABLE IF EXISTS datascience.posts;

CREATE TABLE datascience.posts (
    id                  	integer,
    post_type_id        	smallint,
    creation_date       	timestamp,
    score               	integer,
    view_count          	integer,
    body                	varchar,
    owner_user_id       	integer,
    last_activity_date  	timestamp,
    title               	varchar(250),
    tags                	varchar(250),
    answer_count        	integer,
    comment_count       	integer,
    favorite_count      	integer,
    closed_date         	timestamp,
    content_license     	varchar(12),
    accepted_answer_id  	integer,
    last_editor_user_id 	integer,
    last_edit_date      	timestamp,
    parent_id           	integer,
    owner_display_name  	varchar(40),
    community_owned_date	timestamp,
    last_editor_display_name	varchar(40),
    PRIMARY KEY (id)
);

COPY datascience.posts(id, post_type_id, creation_date, score, view_count, body, owner_user_id, last_activity_date, title, tags, answer_count, comment_count, favorite_count, closed_date, content_license, accepted_answer_id, last_editor_user_id, last_edit_date, parent_id, owner_display_name, community_owned_date, last_editor_display_name)
FROM '/docker-entrypoint-initdb.d/data/posts.csv'
WITH (
  FORMAT CSV,
  DELIMITER ',',
  NULL '',
  HEADER,
  FORCE_NULL(post_type_id, creation_date, score, view_count, body, owner_user_id, last_activity_date, title, tags, answer_count, comment_count, favorite_count, closed_date, content_license, accepted_answer_id, last_editor_user_id, last_edit_date, parent_id, owner_display_name, community_owned_date, last_editor_display_name)
);

COMMIT;

DROP TABLE IF EXISTS datascience.tags;

CREATE TABLE datascience.tags (
    id                  	integer,
    tag_name            	varchar(35),
    count               	integer,
    excerpt_post_id     	integer,
    wiki_post_id        	integer,
    PRIMARY KEY (id)
);

COPY datascience.tags(id, tag_name, count, excerpt_post_id, wiki_post_id)
FROM '/docker-entrypoint-initdb.d/data/tags.csv'
WITH (
  FORMAT CSV,
  DELIMITER ',',
  NULL '',
  HEADER,
  FORCE_NULL(tag_name, count, excerpt_post_id, wiki_post_id)
);

COMMIT;

DROP TABLE IF EXISTS datascience.users;

CREATE TABLE datascience.users (
    id                  	integer,
    reputation          	integer,
    creation_date       	timestamp,
    display_name        	varchar(40),
    last_access_date    	timestamp,
    website_url         	varchar(200),
    location            	varchar(100),
    about_me            	varchar,
    views               	integer,
    up_votes            	integer,
    down_votes          	integer,
    account_id          	integer,
    profile_image_url   	varchar(200),
    PRIMARY KEY (id)
);

COPY datascience.users(id, reputation, creation_date, display_name, last_access_date, website_url, location, about_me, views, up_votes, down_votes, account_id, profile_image_url)
FROM '/docker-entrypoint-initdb.d/data/users.csv'
WITH (
  FORMAT CSV,
  DELIMITER ',',
  NULL '',
  HEADER,
  FORCE_NULL(reputation, creation_date, display_name, last_access_date, website_url, location, about_me, views, up_votes, down_votes, account_id, profile_image_url)
);

COMMIT;

DROP TABLE IF EXISTS datascience.votes;

CREATE TABLE datascience.votes (
    id                  	integer,
    post_id             	integer,
    vote_type_id        	smallint,
    creation_date       	timestamp,
    user_id             	integer,
    bounty_amount       	integer,
    PRIMARY KEY (id)
);

COPY datascience.votes(id, post_id, vote_type_id, creation_date, user_id, bounty_amount)
FROM '/docker-entrypoint-initdb.d/data/votes.csv'
WITH (
  FORMAT CSV,
  DELIMITER ',',
  NULL '',
  HEADER,
  FORCE_NULL(post_id, vote_type_id, creation_date, user_id, bounty_amount)
);

COMMIT;
