import sqlite3 

db = sqlite3.connect("Testitietokanta.txt")

db.isolation_level = None


"db.execute(Create table AUTOT (rekkari STRING PRIMARY KEY, merkki STRING, malli STRING)"

rekkari = input("Anna auton rekisterinumero: ")
merkki = input("Anna auton merkki: ")
malli = input("Anna auton malli: ")

db.execute("INSERT INTO AUTOT (rekkari, merkki, malli) VALUES (?,?,?)",[rekkari, merkki, malli])