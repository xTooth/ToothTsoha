## Tables

### User
```
CREATE TABLE account (
        id INTEGER NOT NULL,
        date_created DATETIME,
        date_modified DATETIME,
        name VARCHAR(144) NOT NULL,
        username VARCHAR(144) NOT NULL,
        password VARCHAR(144) NOT NULL,
        PRIMARY KEY (id)
)
```

### Post
```
CREATE TABLE post (
        id INTEGER NOT NULL,
        date_created DATETIME,
        date_modified DATETIME,
        content VARCHAR(144) NOT NULL,
        account_id INTEGER NOT NULL,
        PRIMARY KEY (id),
        FOREIGN KEY(account_id) REFERENCES account (id)
)
```

### Comment
```
CREATE TABLE comment (
        id INTEGER NOT NULL,
        date_created DATETIME,
        date_modified DATETIME,
        content VARCHAR(144) NOT NULL,
        account_id INTEGER NOT NULL,
        post_id INTEGER NOT NULL,
        PRIMARY KEY (id),
        FOREIGN KEY(account_id) REFERENCES account (id),
        FOREIGN KEY(post_id) REFERENCES post (id)
)
```

## Associationtables

### Likes
```
CREATE TABLE likes (
        post_id INTEGER,
        liker_id INTEGER,
        FOREIGN KEY(post_id) REFERENCES post (id),
        FOREIGN KEY(liker_id) REFERENCES account (id)
)
```

### Followers
```
CREATE TABLE followers (
        follower_id INTEGER,
        followed_id INTEGER,
        FOREIGN KEY(follower_id) REFERENCES account (id),
        FOREIGN KEY(followed_id) REFERENCES account (id)
)
```



