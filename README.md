# Data Migration Tool

## Yleiskuvaus
Tämä projekti on suunniteltu siirtämään dataa PostgreSQL-tietokannasta MongoDB:hen turvallisesti ja tehokkaasti. Projekti noudattaa Pythonin PEP 8 -ohjelmointiperiaatteita ja sisältää logituksen jokaisessa vaiheessa virheiden ja tapahtumien seuraamista varten. Projektin tavoitteena oli oppia ja toteuttaa tietomigraation perusperiaatteet, mukaan lukien datan generointi, lataus, siirto ja validointi.


## Työkalut ja kirjastot
Seuraavat työkalut ja kirjastot käytettiin projektin toteuttamiseen:

- **Python**: Pääasiallinen ohjelmointikieli.
- **PostgreSQL**: Lähdetietokanta.
- **MongoDB**: Kohdetietokanta.
- **Pandas**: Datan käsittelyyn ja CSV-tiedostojen lukemiseen.
- **SQLAlchemy**: Yhteyden muodostamiseen PostgreSQL-tietokantaan.
- **PyMongo**: Yhteyden muodostamiseen MongoDB:hen.
- **python-dotenv**: Ympäristömuuttujien hallintaan.
- **loguru**: Lokitukseen.
- **ChatGPT**: Projektin suunnitteluun ja toteutukseen.

## Mitä projektissa tehtiin
1. **Testidatan generointi**: Luotiin Python-skripti, joka generoi 1000 riviä testidataa ja tallentaa sen CSV-tiedostoksi.
2. **PostgreSQL-yhteyden luominen**: Määritettiin PostgreSQL-tietokanta ja taulu datan tallentamiseksi.
3. **Datan lataaminen PostgreSQL:hen**: Generoitu data ladattiin PostgreSQL-tietokantaan.
4. **Datan siirto MongoDB:hen**: PostgreSQL:stä haettu data siirrettiin MongoDB:hen.
5. **Datan validointi**: Varmistettiin, että PostgreSQL:stä ja MongoDB:stä löytyvät rivimäärät täsmäävät.

## Skriptien kuvaus

- **`generate_test_data.py`**:
  - Generoi 1000 riviä testidataa ja tallentaa sen CSV-tiedostoksi `2_data/test_data.csv`.
  - Tallentaa lokit tiedostoon `5_logs/generate_test_data.log`.

- **`test_connection.py`**:
  - Testaa PostgreSQL-yhteyden toimivuuden.
  - Tallentaa lokit tiedostoon `5_logs/test_connection.log`.

- **`load_data_to_postgres.py`**:
  - Lataa generoidun datan CSV-tiedostosta PostgreSQL-tauluun.
  - Tallentaa lokit tiedostoon `5_logs/load_data_to_postgres.log`.

- **`migrate_to_mongodb.py`**:
  - Siirtää datan PostgreSQL:stä MongoDB:hen.
  - Tallentaa lokit tiedostoon `5_logs/migrate_to_mongodb.log`.

- **`validate_data.py`**:
  - Varmistaa, että PostgreSQL:n ja MongoDB:n rivimäärät täsmäävät.
  - Tallentaa lokit tiedostoon `5_logs/validate_data.log`.

## Lisenssi
Tämä projekti on lisensoitu MIT-lisenssillä. Voit vapaasti käyttää, muokata ja jakaa sitä, kunhan säilytät alkuperäisen lisenssimerkinnän.
