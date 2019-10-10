## Käyttötapaukset

- [x] Käyttäjä voi selata käyttäjien profiileja kirjautumatta
<details><summary>Click to view SQL</summary>
<p>
	
    ```
    TODO
    ```

</p>
</details>

- [x] Käyttäjä voi selata lukea posteja ja kommentteja kirjautumatta

<details><summary>Click to view SQL</summary>
<p>
Get all posts:
	
    ```
    SELECT * FROM post ORDER BY time_modified DESC
    ```

Get most commented posts:
    ```
    "SELECT id, content"
                    " FROM post AS p"
                    " INNER JOIN( SELECT post_id, COUNT(*) AS postcount FROM comment"
                    " GROUP BY post_id) AS c"
                    " ON p.id = c.post_id"
                    " ORDER BY c.postcount DESC LIMIT 5"
    ```
Get posts by one user:

    ```
    TODO
    ```

</p>
</details>

- [x] Käyttäjä voi luoda tilin foorumiin, joka luo hänelle oman profiilisivun

- [x] Käyttäjä voi kirjautua ja kirjautua ulos tililtään

- [x] Kirjautunut käyttäjä voi seurata muita käyttäjiä, ja lopettaa seuraamisen

<details><summary>Click to view SQL</summary>
<p>
	
    ```
    TODO
    ```

</p>
</details>

- [x] Kirjautunut käyttäjä voi tehdä yleisiä postauksia, ja poistaa sekä muokata itse tekemiään kirjoituksia

<details><summary>Click to view SQL</summary>
<p>
	
    ```
    TODO
    ```

</p>
</details>

- [x] Kirjautunut käyttäjä voi lukea muiden tekemiä postauksia 


- [x] Kirjautunut käyttäjä voi kommentoida postauksia , ja poistaa tai muokata omia kommenttejaan


- [x] Kirjautunut käyttäjä voi lukea muiden tekemiä kommentteja

<details><summary>Click to view SQL</summary>
<p>
	
    ```
    TODO
    ```

</p>
</details>

- [x] Kirjautunut käyttäjä voi tykätä postauksista ja poistaa tykkäyksensä
