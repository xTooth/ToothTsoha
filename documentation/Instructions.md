# Käyttöohjeet

### Asennus- ja käynnistysohje

Kun repositorio on ladattu, aja seuraavat komennot sovelluksen juuressa.

Linux/mac:

```
python -m venv venv/
source venv/bin/activate
pip install -r requirements.txt
python app.py
```

Windows:

```
python3 -m venv venv/
venv/Scripts/activate
pip install -r requirements.txt
python app.py
```

Sovelluksen etusivu on tämän jälkeen tarjolla osoitteessa: localhost:5000
Sovelluksen saa sammumaan painamalla:

<kbd>CTRL</kbd>+<kbd>C</kbd>


### Käyttöohje

Palvelu on yksinkertainen foorumisovellus.

##### Etusivu
Täällä pääsee tutkimaan puhutuimpia aiheita.

##### Posts
Täällä pääsee selaamaan sovelluksen kaikkia posteja ja kirjautuneet henkilöt voi tehdä uusia posteja. Postia klikkaamalla sen kommentteja pääsee lukemaan, jos on kirjautunut täältä postia voi kommentoida, ja omia kommenteja voi editoida. Postin luoja voi myös editoida postausta.

##### Users
Lista sovelluksen rekisteröityneitsä henkilöistä. täältä pääsee tutkimaan jokaisen käyttäjän profiilia. Tulevaisuudessa täältäkäsin myös seurataan käyttäjiä.

##### Create account
Uuden tilin luominen

##### Sign in
Jo olemassa olevalle tilille kirjautuminen.

##### Sign out
Uloskirjautuminen.

##### "oma nimi"
Täältä pääsee tutkimaan omaa profiilia.
