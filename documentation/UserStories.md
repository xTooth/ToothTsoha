## Käyttötapaukset

- [x] Käyttäjä voi selata käyttäjien profiileja kirjautumatta
<details><summary>SQL</summary>
<p>List users:

```SQL
    SELECT account_id, name FROM account
```
Get specific user:
    
```SQL
    SELECT * FROM account WHERE account_id = ?
```
</p>
</details>

- [x] Käyttäjä voi selata lukea posteja ja kommentteja kirjautumatta
<details><summary>SQL</summary>
<p>Get all posts:
	
```SQL
    SELECT * FROM post ORDER BY time_modified DESC
```

Get most commented posts:
    
```SQL
    SELECT id, content
                    FROM post AS p
                    INNER JOIN( SELECT post_id, COUNT(*) AS postcount FROM comment
                    GROUP BY post_id) AS c
                    ON p.id = c.post_id
                    ORDER BY c.postcount DESC LIMIT 5
```

Get most liked posts:

```SQL
    SELECT id, content
                    FROM post AS p
                    INNER JOIN( SELECT post_id, COUNT(*) AS likecount FROM likes
                    GROUP BY post_id) AS l
                    ON p.id = l.post_id
                    ORDER BY l.likecount DESC LIMIT 5
```

Get posts by one user:

```SQL
    SELECT * FROM post WHERE account_id = ? ORDER BY time_modified DESC
```

Get comments for a post:

```SQL
    SELECT * FROM comment WHERE post_id = ? ORDER BY time_modified DESC
```
</p>
</details>

- [x] Käyttäjä voi luoda tilin foorumiin, joka luo hänelle oman profiilisivun
<details><summary>SQL</summary>
<p>
Create new user:

```SQL
    INSERT INTO account (date_created, date_modified, name, username, password)
    VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, ?, ?, ?, ?)	
```
    
</p>
</details>

- [x] Käyttäjä voi kirjautua ja kirjautua ulos tililtään

- [x] Kirjautunut käyttäjä voi seurata muita käyttäjiä, ja lopettaa seuraamisen
<details><summary>SQL</summary>
<p>
Get posts by followed users:

```SQL
    SELECT post.id AS post_id, post.date_created AS post_date_created, post.date_modified AS post_date_modified, post.content AS post_content, post.account_id AS post_account_id
    FROM post JOIN followers ON followers.followed_id = post.account_id
    WHERE followers.follower_id = ? ORDER BY post.date_modified DESC
```

Follow a user:

```SQL
    INSERT INTO followers (followed_id, follower_id) VALUES (?, ?)
```

Unfollow a user

```SQL
    DELETE FROM followers WHERE followers.follower_id = ? 
              AND followers.followed_id = ?
```
</p>
</details>

- [x] Kirjautunut käyttäjä voi tehdä yleisiä postauksia, ja poistaa sekä muokata itse tekemiään kirjoituksia
<details><summary>SQL</summary>
<p>
Create Post:
    
```SQL
    INSERT INTO post (date_created, date_modified, content, account_id)
    VALUES(CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, ?,?)
```


Edit Post:

```SQL
    UPDATE post SET date_modified=CURRENT_TIMESTAMP, content = ? 
    WHERE post_id = ?
```

Delete Post:

```SQL
    DELETE post WHERE post_id = ?
```
    
</p>
</details>

- [x] Kirjautunut käyttäjä voi lukea muiden tekemiä postauksia 

- [x] Kirjautunut käyttäjä voi kommentoida postauksia , ja poistaa tai muokata omia kommenttejaan
<details><summary>SQL</summary>
<p>
Create Comment:

```SQL
    INSERT INTO comment (date_created, date_modified, content, account_id, post_id)
    VALUES(CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, ?,?,?)
```
Edit Comment:

```SQL
    UPDATE commment SET date_modified=CURRENT_TIMESTAMP, content = ?
    WHERE comment_id = ?
```
    

Delete Comment:

```SQL
    DELETE comment WHERE comment_id = ?
```
    
</p>
</details>

- [x] Kirjautunut käyttäjä voi lukea muiden tekemiä kommentteja

- [x] Kirjautunut käyttäjä voi tykätä postauksista ja poistaa tykkäyksensä
<details><summary>SQL</summary>
<p>
Like:

```SQL
    INSERT INTO like (account_id, post_id) VALUES ( ?, ?)

```
    
Remove Like:

```SQL
    DELETE FROM like WHERE account_id = ? AND post_id = ?
```

</p>
</details>