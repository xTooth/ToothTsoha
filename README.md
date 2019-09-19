# ToothTsoha
Tietokantasovellus, harjoitustyö syksy 2019

### [Sovellus Herokussa](https://tsohafoorumi.herokuapp.com/)
Sovellukseen käyttäjä: username: asd password: asd

Tässä pikku huomio, toteutin materiaalissa esiintyviä asioita, joten kirjautuminen ja käyttäjän luominen on nyt toteutettu (ilman bcryptiä sillä se heitti jotain outoa erroria johon en löytänyt fixiä, pitää tutkia lisää: ei löydä muuttujaa password vaikka kyseinen toimii moitteetta kun vaan jättää bcryptin hashauksen välistä pois.) kantataulut käyttäjän ja postin välillä myös toteutettu, ja ulkonäköä hieman kohennettu. Tein alustavasti myös crud ominaisuudet, mutta deleteä en saanut vielä toimimaan toivotulla tavalla. poistaa itse postin mutta ei linkkiä käyttäjään, joten tyhjä posti jää edelleen kummittelemaan.

## Foorumi

Eli ajatus on rakentaa "keskustelupalsta/foorumi" jossa olisi seuraavat päätoiminnallisuudet:

[Käyttötapaukset](documentation/UserStories.md)

## Toteutus

Projekti toteutetaan web sovelluksena, palvelin puoli Pythonia, ja selainpuoli HTML + CSS/Bootstrap



## Alustava Tietokantakaavio

![alt text](documentation/images/tsoha.PNG)
