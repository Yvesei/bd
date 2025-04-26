## MySQL/MariaDB Exercises

### 1. Connect to your MySQL or MariaDB database manager

### 2. Create the database
```sql
CREATE DATABASE TP_SecuBDD_GHOUDANE_OUCHTA;
```

### 3. List the existing databases
```sql
SHOW DATABASES;
```

### 4. Create a user with access only to the created database
```sql
CREATE USER 'user'@'localhost' IDENTIFIED BY 'pass';
GRANT ALL PRIVILEGES ON TP_SecuBDD_GHOUDANE_OUCHTA.* TO 'user'@'localhost';
```

### 5. Grant the user all privileges on all objects of all databases
```sql
GRANT ALL PRIVILEGES ON *.* TO 'user'@'localhost';
```

### 6. Display the privileges of the connected user
```sql
SHOW GRANTS FOR 'user'@'localhost';
```

### 7. List all system users
```sql
SELECT 
    Host, 
    User, 
    authentication_string AS password 
FROM 
    mysql.user;
```

####  output:
```
+-----------+------------------+------------------------------------------------------------------------+
| Host      | User             | password                                                               |
+-----------+------------------+------------------------------------------------------------------------+
| localhost | mysql.infoschema | $A$005$THISISACOMBINATIONOFINVALIDSALTANDPASSWORDTHATMUSTNEVERBRBEUSED |
| localhost | mysql.session    | $A$005$THISISACOMBINATIONOFINVALIDSALTANDPASSWORDTHATMUSTNEVERBRBEUSED |
| localhost | mysql.sys        | $A$005$THISISACOMBINATIONOFINVALIDSALTANDPASSWORDTHATMUSTNEVERBRBEUSED |
| localhost | root             |                                                                        |
dC%b5xGVsKX09TW1gnr9yhI595aWftxBA2kiWWxlABe/q0 |U3|_@d_
+-----------+------------------+------------------------------------------------------------------------+
5 rows in set (0.00 sec)
```

### 8. Display the structure of the `mysql` user table
```sql
DESC mysql.user;
```

### 9. Display the list of tables in the `mysql` database
```sql
SHOW TABLES FROM mysql;
```

### 10. Display the version and time of the DBMS
```sql
SELECT VERSION(), NOW();
```

### 11. Create a suppliers table and modify it
```sql
CREATE TABLE fournisseurs ( code INT, nom CHAR );
ALTER TABLE fournisseurs ADD prenom CHAR, ADD ref INT;
DROP TABLE fournisseurs;
```

### 12. Display the result of `sin(PI/4)` and `(4+1)*6` on the same line
```sql
SELECT SIN(PI()/4), (4+1)*6;
```

### 13. Create the `shop` table and insert data
```sql
CREATE TABLE shop (
    article INT(4) UNSIGNED ZEROFILL DEFAULT '0000' NOT NULL,
    dealer CHAR(20) DEFAULT '' NOT NULL,
    price DOUBLE(16,2) DEFAULT '0.00' NOT NULL,
    PRIMARY KEY(article, dealer)
);

INSERT INTO shop VALUES
(1,'A',3.45),(1,'B',3.99),(2,'A',10.99),(3,'B',1.45),(3,'C',1.69),
(3,'D',1.25),(4,'D',19.95);
```

### 14. Result of the following query
```sql
SELECT arTIcle FROM SHoP;
```

### 15. Create a `customer` user with read-only rights on `shop`
```sql
CREATE USER 'customer'@'localhost' IDENTIFIED BY 'password';
GRANT SELECT ON shop TO 'customer'@'localhost';
```

#### What error message appears when attempting an insertion?
```sql
INSERT INTO shop VALUES (5,'E',9.99);
```
Reponse:
```
mysql> INSERT INTO shop VALUES (5,'E',9.99);
ERROR 1142 (42000): INSERT command denied to user 'customer'@'localhost' for table 'shop'
```
### 16. Results of the following queries
```sql
SELECT MAX(article) AS article FROM shop;
SELECT article, dealer, price FROM shop WHERE price=(SELECT MAX(price) FROM shop);
SELECT article, MAX(price) AS price FROM shop GROUP BY article;
SELECT article, dealer, price FROM shop s1 WHERE price=(SELECT MAX(s2.price) FROM shop s2 WHERE s1.article = s2.article);
```

### 17. Create tables and insert values
```sql

CREATE TABLE persons (
 id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
 name CHAR(60) NOT NULL,
 PRIMARY KEY (id)
 );

CREATE TABLE shirts (
 id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
 style ENUM('t-shirt', 'polo', 'dress') NOT NULL,
 color ENUM('red', 'blue', 'orange', 'white', 'black') NOT NULL,
 owner SMALLINT UNSIGNED NOT NULL REFERENCES persons,
 PRIMARY KEY (id)
);

INSERT INTO persons VALUES (NULL, 'Antonio Paz');

INSERT INTO shirts VALUES
 (NULL, 'polo', 'blue', LAST_INSERT_ID()),
 (NULL, 'dress', 'white', LAST_INSERT_ID()),
 (NULL, 't-shirt', 'blue', LAST_INSERT_ID());


INSERT INTO persons VALUES (NULL, 'Lilliana Angelovska');
INSERT INTO persons VALUES (1, 'Laurent Marot');

INSERT INTO shirts VALUES
 (NULL, 'dress', 'orange', LAST_INSERT_ID()),
 (NULL, 'polo', 'red', LAST_INSERT_ID()),
 (NULL, 'dress', 'blue', LAST_INSERT_ID()),
 (NULL, 't-shirt', 'white', LAST_INSERT_ID());

SELECT s.* FROM persons p, shirts s
WHERE p.name LIKE 'Lilliana%'
AND s.owner = p.id
AND s.color <> 'white';

CREATE TABLE animaux (nom VARCHAR(20), proprietaire VARCHAR(20), espece VARCHAR(20), genre CHAR(1), naissance DATE, mort DATE);
```

code de retour:

```
mysql> CREATE TABLE persons (
    ->  id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
    ->  name CHAR(60) NOT NULL,
    ->  PRIMARY KEY (id)
    ->  );
Query OK, 0 rows affected (0.02 sec)

mysql>
mysql> CREATE TABLE shirts (
    ->  id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
    ->  style ENUM('t-shirt', 'polo', 'dress') NOT NULL,
    ->  color ENUM('red', 'blue', 'orange', 'white', 'black') NOT NULL,
    ->  owner SMALLINT UNSIGNED NOT NULL REFERENCES persons,
    ->  PRIMARY KEY (id)
    -> );
Query OK, 0 rows affected (0.01 sec)

mysql>
mysql> INSERT INTO persons VALUES (NULL, 'Antonio Paz');
Query OK, 1 row affected (0.01 sec)

mysql>
mysql> INSERT INTO shirts VALUES
    ->  (NULL, 'polo', 'blue', LAST_INSERT_ID()),
    ->  (NULL, 'dress', 'white', LAST_INSERT_ID()),
    ->  (NULL, 't-shirt', 'blue', LAST_INSERT_ID());
Query OK, 3 rows affected (0.00 sec)
Records: 3  Duplicates: 0  Warnings: 0

mysql>
mysql>
mysql> INSERT INTO persons VALUES (NULL, 'Lilliana Angelovska');
Query OK, 1 row affected (0.00 sec)

mysql> INSERT INTO persons VALUES (1, 'Laurent Marot');
ERROR 1062 (23000): Duplicate entry '1' for key 'persons.PRIMARY'
mysql>
mysql> INSERT INTO shirts VALUES
    ->  (NULL, 'dress', 'orange', LAST_INSERT_ID()),
    ->  (NULL, 'polo', 'red', LAST_INSERT_ID()),
    ->  (NULL, 'dress', 'blue', LAST_INSERT_ID()),
    ->  (NULL, 't-shirt', 'white', LAST_INSERT_ID());
Query OK, 4 rows affected (0.00 sec)
Records: 4  Duplicates: 0  Warnings: 0

mysql>
mysql> SELECT s.* FROM persons p, shirts s
    -> WHERE p.name LIKE 'Lilliana%'
    -> AND s.owner = p.id
    -> AND s.color <> 'white';
+----+-------+--------+-------+
| id | style | color  | owner |
+----+-------+--------+-------+
|  4 | dress | orange |     2 |
|  5 | polo  | red    |     2 |
|  6 | dress | blue   |     2 |
+----+-------+--------+-------+
3 rows in set (0.00 sec)

mysql>
mysql> CREATE TABLE animaux (nom VARCHAR(20), proprietaire VARCHAR(20), espece VARCHAR(20), genre CHAR(1), naissance DATE, mort DATE);
Query OK, 0 rows affected (0.01 sec)
```


### 18. Python script `question18.py` to insert data
```python
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",       
    user="user",            
    password="pass",    
    database="TP_SecuBDD_GHOUDANE_OUCHTA" 
)

cursor = conn.cursor()

data = [
    ("Fluffy", "Harold", "chat", "f", "2013-02-04", None),
    ("Claws", "Gwen", "chat", "m", "2014-03-17", None),
    ("Buffy", "Harod", "chien", "f", "2019-05-13", None),
    ("Fang", "Benny", "chien", "m", "2010-08-27", None),
    ("Bowser", "Diane", "chien", "m", "2018-08-31", "2021-07-29"),
    ("Chirpy", "Gwen", "oiseau", "f", "2018-09-11", None),
    ("Whistler", "Gwen", "oiseau", None, "2017-12-09", None),
    ("Slim", "Benny", "serpent", "m", "2016-04-29", None),
    ("Puffball", "Diane", "hamster", "f", "2019-03-30", None)
]

insert_query = """
INSERT INTO animaux (nom, proprietaire, espece, genre, naissance, mort)
VALUES (%s, %s, %s, %s, %s, %s)
"""

try:
    cursor.executemany(insert_query, data)
    conn.commit()
    print(f"{cursor.rowcount} enregistrements ont été insérés.")
except mysql.connector.Error as err:
    print(f"Erreur: {err}")
finally:
    cursor.close()
    conn.close()
```


18 / Créez un script python "question18.py" (vous avez droit à mysql.connector en librairie non standard) pour insérer le listing suivant :

Fluffy	Harold	chat	f	'2013-02-04'	\N
Claws	Gwen 	chat 	m	'2014-03-17'	\N
Buffy	Harod	chien	f	'2019-05-13'	\N
Fang	Benny	chien	m	'2010-08-27'	\N
Bowser	Diane	chien	m	'2018-08-31'	'2021-07-29'
Chirpy	Gwen	oiseau	f	'2018-09-11'	\N
Whistler	Gwen	oiseau	\N	'2017-12-09'	\N
Slim	Benny	serpent	m	'2016-04-29'	\N
Puffball	Diane	hamster	f	'2019-03-30'	\N

19 / Affichez l'âge des animaux
20 / Expliquez le résultat de cette commande : SELECT 1 IS NULL, 1 IS NOT NULL;
21 / Affichez le nom des animaux dont le nom contient un b ou un P avec une expression régulière
22 / Modifiez le mot de passe de votre utilisateur créé au début avec la valeur "mysql"
23 / Donnez une requête sur la table animaux affichant les tuples en version hachées (SHA2)
24 / Il existe un script fourni avec MySQL et MariaDB permettant de sécuriser une installation fraîche du serveur de base de données, quel est-il et que fait-il ?
25 / Comment feriez-vous pour chiffrer une cellule sensible d'une de vos tables de base de données ?
26 / Faites un dump de votre base de test dans un fichier "dump.sql"

27 / On souhaite stocker des informations en base concernant des employés d'une entreprise, entre autre leur Identifiant unique, et leur Salaire. Mais leur salaire doit rester secret et seule une personne autorisée doit pouvoir accéder à cette information, qui doit être protégée contre un attaquant disposant des droits d'administration sur la machine serveur hébergeant la base.
La contrainte est cependant qu'il doit rester possible pour une personne autorisée de comparer les salaires de deux employés, et d'obtenir la somme des salaires ; et ce, sans compromettre le secret (le salaire ne doit pas transiter en clair).

Définissez une base pour cela. Trouvez et utilisez des primitives de chiffrement homomorphe (ne les implémentez pas vous-même) permettant de comparer des entiers chiffrés, et d'additionner des entiers chiffrés.
Indice pour le premier cas : il s'agit de trouver un algorithme préservant la relation d'ordre — aka. Order Revealing Encryption — (afin que les requêtes sur intervalles soient permises).

Donnez l'implémentation en python du middleware et d'une application cliente de cette base illustrant le chiffrement, la récupération, et le déchiffrement des informations de la base.
Votre projet doit présenter entre autre deux scripts client.py et server.py

Le script server.py affiche à son lancement l'ip et le port par lesquels on peut le joindre. Il communique avec le SGBD et est considéré comme faisant partie du périmètre accessible par l'attaquant.
Il permet d'exécuter :
- la comparaison de deux employés sur leur salaire chiffré
- la somme chiffrée des salaires
Il est essentiel d'utiliser les ressources du serveur pour exécuter ces opérations, il est interdit par exemple de retourner la liste des salaires chiffrés au client pour qu'ensuite les salaires soient déchiffrés côté client afin d'en produire la somme.

Le script client.py est hors périmètre de l'attaquant. Lancé avec en paramètres l'ip et le port du serveur, il propose un menu permettant :
- d'ajouter un enregistrement à la base
- d'afficher le contenu de la base
- de comparer deux employés sur leur salaire
- d'obtenir la somme des salaires

Toute la partie chiffrement/déchiffrement doit être transparente pour l'utilisateur, à aucun moment on ne lui demande de comprendre le chiffrement en question ou de gérer des clés (similaire au fait que vous n'avez pas besoin de comprendre HTTPS pour afficher une page web).

28 / Implémentez une attaque statistique permettant à un utilisateur illégitime d'approximer l'information chiffrée. Expliquez votre méthodologie pour créer un jeu de données dont la répartition est publique, puis pour retrouver avec approximation les informations de ce jeu de données à partir de ce modèle de répartition et de la suite ordonnée et chiffrée de ces informations.
Lien utile : https://blog.cryptographyengineering.com/2019/02/11/attack-of-the-week-searchable-encryption-and-the-ever-expanding-leakage-function/




# All commands:
```
❯ mysql --host=localhost --user=root
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 9
Server version: 9.2.0 Homebrew

Copyright (c) 2000, 2025, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> list database
    -> ;
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'list database' at line 1
mysql> show databases
    -> ;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
| sys                |
+--------------------+
4 rows in set (0.00 sec)

mysql> CREATE DATABASE TP_SecuBDD_GHOUDANE_OUCHTA;
Query OK, 1 row affected (0.01 sec)

mysql> show databases;
+----------------------------+
| Database                   |
+----------------------------+
| information_schema         |
| mysql                      |
| performance_schema         |
| sys                        |
| TP_SecuBDD_GHOUDANE_OUCHTA |
+----------------------------+
5 rows in set (0.01 sec)

mysql> CREATE USER 'user'@'localhost' IDENTIFIED BY 'pass';
Query OK, 0 rows affected (0.01 sec)

mysql> GRANT ALL PRIVILEGES ON TP_SecuBDD_GHOUDANE_OUCHTA.* TO 'user'@'localhost';
Query OK, 0 rows affected (0.01 sec)

mysql> GRANT ALL PRIVILEGES ON *.* TO 'user'@'localhost';
Query OK, 0 rows affected (0.01 sec)

mysql> SHOW GRANTS FOR 'user'@'localhost';
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Grants for user@localhost                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| GRANT SELECT, INSERT, UPDATE, DELETE, CREATE, DROP, RELOAD, SHUTDOWN, PROCESS, FILE, REFERENCES, INDEX, ALTER, SHOW DATABASES, SUPER, CREATE TEMPORARY TABLES, LOCK TABLES, EXECUTE, REPLICATION SLAVE, REPLICATION CLIENT, CREATE VIEW, SHOW VIEW, CREATE ROUTINE, ALTER ROUTINE, CREATE USER, EVENT, TRIGGER, CREATE TABLESPACE, CREATE ROLE, DROP ROLE ON *.* TO `user`@`localhost`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| GRANT ALLOW_NONEXISTENT_DEFINER,APPLICATION_PASSWORD_ADMIN,AUDIT_ABORT_EXEMPT,AUDIT_ADMIN,AUTHENTICATION_POLICY_ADMIN,BACKUP_ADMIN,BINLOG_ADMIN,BINLOG_ENCRYPTION_ADMIN,CLONE_ADMIN,CONNECTION_ADMIN,CREATE_SPATIAL_REFERENCE_SYSTEM,ENCRYPTION_KEY_ADMIN,FIREWALL_EXEMPT,FLUSH_OPTIMIZER_COSTS,FLUSH_PRIVILEGES,FLUSH_STATUS,FLUSH_TABLES,FLUSH_USER_RESOURCES,GROUP_REPLICATION_ADMIN,GROUP_REPLICATION_STREAM,INNODB_REDO_LOG_ARCHIVE,INNODB_REDO_LOG_ENABLE,OPTIMIZE_LOCAL_TABLE,PASSWORDLESS_USER_ADMIN,PERSIST_RO_VARIABLES_ADMIN,REPLICATION_APPLIER,REPLICATION_SLAVE_ADMIN,RESOURCE_GROUP_ADMIN,RESOURCE_GROUP_USER,ROLE_ADMIN,SENSITIVE_VARIABLES_OBSERVER,SERVICE_CONNECTION_ADMIN,SESSION_VARIABLES_ADMIN,SET_ANY_DEFINER,SHOW_ROUTINE,SYSTEM_USER,SYSTEM_VARIABLES_ADMIN,TABLE_ENCRYPTION_ADMIN,TELEMETRY_LOG_ADMIN,TRANSACTION_GTID_TAG,XA_RECOVER_ADMIN ON *.* TO `user`@`localhost` |
| GRANT ALL PRIVILEGES ON `tp_secubdd_ghoudane_ouchta`.* TO `user`@`localhost`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
3 rows in set (0.00 sec)

mysql> SHOW GRANTS FOR 'user'@'localhost';
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Grants for user@localhost                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| GRANT SELECT, INSERT, UPDATE, DELETE, CREATE, DROP, RELOAD, SHUTDOWN, PROCESS, FILE, REFERENCES, INDEX, ALTER, SHOW DATABASES, SUPER, CREATE TEMPORARY TABLES, LOCK TABLES, EXECUTE, REPLICATION SLAVE, REPLICATION CLIENT, CREATE VIEW, SHOW VIEW, CREATE ROUTINE, ALTER ROUTINE, CREATE USER, EVENT, TRIGGER, CREATE TABLESPACE, CREATE ROLE, DROP ROLE ON *.* TO `user`@`localhost`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| GRANT ALLOW_NONEXISTENT_DEFINER,APPLICATION_PASSWORD_ADMIN,AUDIT_ABORT_EXEMPT,AUDIT_ADMIN,AUTHENTICATION_POLICY_ADMIN,BACKUP_ADMIN,BINLOG_ADMIN,BINLOG_ENCRYPTION_ADMIN,CLONE_ADMIN,CONNECTION_ADMIN,CREATE_SPATIAL_REFERENCE_SYSTEM,ENCRYPTION_KEY_ADMIN,FIREWALL_EXEMPT,FLUSH_OPTIMIZER_COSTS,FLUSH_PRIVILEGES,FLUSH_STATUS,FLUSH_TABLES,FLUSH_USER_RESOURCES,GROUP_REPLICATION_ADMIN,GROUP_REPLICATION_STREAM,INNODB_REDO_LOG_ARCHIVE,INNODB_REDO_LOG_ENABLE,OPTIMIZE_LOCAL_TABLE,PASSWORDLESS_USER_ADMIN,PERSIST_RO_VARIABLES_ADMIN,REPLICATION_APPLIER,REPLICATION_SLAVE_ADMIN,RESOURCE_GROUP_ADMIN,RESOURCE_GROUP_USER,ROLE_ADMIN,SENSITIVE_VARIABLES_OBSERVER,SERVICE_CONNECTION_ADMIN,SESSION_VARIABLES_ADMIN,SET_ANY_DEFINER,SHOW_ROUTINE,SYSTEM_USER,SYSTEM_VARIABLES_ADMIN,TABLE_ENCRYPTION_ADMIN,TELEMETRY_LOG_ADMIN,TRANSACTION_GTID_TAG,XA_RECOVER_ADMIN ON *.* TO `user`@`localhost` |
| GRANT ALL PRIVILEGES ON `tp_secubdd_ghoudane_ouchta`.* TO `user`@`localhost`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
3 rows in set (0.00 sec)

mysql> SELECT Host, User, Password FROM mysql.user;
ERROR 1054 (42S22): Unknown column 'Password' in 'field list'
mysql> SELECT Host, User, Password FROM mysql.user;
ERROR 1054 (42S22): Unknown column 'Password' in 'field list'
mysql> SELECT Host, User FROM mysql.user
    -> ;
+-----------+------------------+
| Host      | User             |
+-----------+------------------+
| localhost | mysql.infoschema |
| localhost | mysql.session    |
| localhost | mysql.sys        |
| localhost | root             |
| localhost | user             |
+-----------+------------------+
5 rows in set (0.00 sec)

mysql> SELECT * FROM mysql.user;
+-----------+------------------+-------------+-------------+-------------+-------------+-------------+-----------+-------------+---------------+--------------+-----------+------------+-----------------+------------+------------+--------------+------------+-----------------------+------------------+--------------+-----------------+------------------+------------------+----------------+---------------------+--------------------+------------------+------------+--------------+------------------------+----------+------------------------+--------------------------+----------------------------+---------------+-------------+-----------------+----------------------+-----------------------+------------------------------------------------------------------------+------------------+-----------------------+-------------------+----------------+------------------+----------------+------------------------+---------------------+--------------------------+-----------------+
| Host      | User             | Select_priv | Insert_priv | Update_priv | Delete_priv | Create_priv | Drop_priv | Reload_priv | Shutdown_priv | Process_priv | File_priv | Grant_priv | References_priv | Index_priv | Alter_priv | Show_db_priv | Super_priv | Create_tmp_table_priv | Lock_tables_priv | Execute_priv | Repl_slave_priv | Repl_client_priv | Create_view_priv | Show_view_priv | Create_routine_priv | Alter_routine_priv | Create_user_priv | Event_priv | Trigger_priv | Create_tablespace_priv | ssl_type | ssl_cipher             | x509_issuer              | x509_subject               | max_questions | max_updates | max_connections | max_user_connections | plugin                | authentication_string                                                  | password_expired | password_last_changed | password_lifetime | account_locked | Create_role_priv | Drop_role_priv | Password_reuse_history | Password_reuse_time | Password_require_current | User_attributes |
+-----------+------------------+-------------+-------------+-------------+-------------+-------------+-----------+-------------+---------------+--------------+-----------+------------+-----------------+------------+------------+--------------+------------+-----------------------+------------------+--------------+-----------------+------------------+------------------+----------------+---------------------+--------------------+------------------+------------+--------------+------------------------+----------+------------------------+--------------------------+----------------------------+---------------+-------------+-----------------+----------------------+-----------------------+------------------------------------------------------------------------+------------------+-----------------------+-------------------+----------------+------------------+----------------+------------------------+---------------------+--------------------------+-----------------+
| localhost | mysql.infoschema | Y           | N           | N           | N           | N           | N         | N           | N             | N            | N         | N          | N               | N          | N          | N            | N          | N                     | N                | N            | N               | N                | N                | N              | N                   | N                  | N                | N          | N            | N                      |          | 0x                     | 0x                       | 0x                         |             0 |           0 |               0 |                    0 | caching_sha2_password | $A$005$THISISACOMBINATIONOFINVALIDSALTANDPASSWORDTHATMUSTNEVERBRBEUSED | N                | 2025-01-29 12:33:25   |              NULL | Y              | N                | N              |                   NULL |                NULL | NULL                     | NULL            |
| localhost | mysql.session    | N           | N           | N           | N           | N           | N         | N           | Y             | N            | N         | N          | N               | N          | N          | N            | Y          | N                     | N                | N            | N               | N                | N                | N              | N                   | N                  | N                | N          | N            | N                      |          | 0x                     | 0x                       | 0x                         |             0 |           0 |               0 |                    0 | caching_sha2_password | $A$005$THISISACOMBINATIONOFINVALIDSALTANDPASSWORDTHATMUSTNEVERBRBEUSED | N                | 2025-01-29 12:33:25   |              NULL | Y              | N                | N              |                   NULL |                NULL | NULL                     | NULL            |
| localhost | mysql.sys        | N           | N           | N           | N           | N           | N         | N           | N             | N            | N         | N          | N               | N          | N          | N            | N          | N                     | N                | N            | N               | N                | N                | N              | N                   | N                  | N                | N          | N            | N                      |          | 0x                     | 0x                       | 0x                         |             0 |           0 |               0 |                    0 | caching_sha2_password | $A$005$THISISACOMBINATIONOFINVALIDSALTANDPASSWORDTHATMUSTNEVERBRBEUSED | N                | 2025-01-29 12:33:25   |              NULL | Y              | N                | N              |                   NULL |                NULL | NULL                     | NULL            |
| localhost | root             | Y           | Y           | Y           | Y           | Y           | Y         | Y           | Y             | Y            | Y         | Y          | Y               | Y          | Y          | Y            | Y          | Y                     | Y                | Y            | Y               | Y                | Y                | Y              | Y                   | Y                  | Y                | Y          | Y            | Y                      |          | 0x                     | 0x                       | 0x                         |             0 |           0 |               0 |                    0 | caching_sha2_password |                                                                        | N                | 2025-01-29 12:33:24   |              NULL | N              | Y                | Y              |                   NULL |                NULL | NULL                     | NULL            |
| localhost | user             | Y           | Y           | Y           | Y           | Y           | Y         | Y           | Y             | Y            | Y         | N          | Y               | Y          | Y          | Y            | Y          | Y                     | Y                | Y            | Y               | Y                | Y                | Y              | Y                   | Y                  | Y                | Y          | Y            | Y                      |          | 0x                     | 0x                       | 0x                         |             0 |           0 | dC%b5xGVsKX09TW1gnr9yhI595aWftxBA2kiWWxlABe/q0 | N                | 2025-04-08 11:49:09   |              NULL | N              | Y                | Y              |                   NULL |                NULL | NULL                     | NULL            |
+-----------+------------------+-------------+-------------+-------------+-------------+-------------+-----------+-------------+---------------+--------------+-----------+------------+-----------------+------------+------------+--------------+------------+-----------------------+------------------+--------------+-----------------+------------------+------------------+----------------+---------------------+--------------------+------------------+------------+--------------+------------------------+----------+------------------------+--------------------------+----------------------------+---------------+-------------+-----------------+----------------------+-----------------------+------------------------------------------------------------------------+------------------+-----------------------+-------------------+----------------+------------------+----------------+------------------------+---------------------+--------------------------+-----------------+
5 rows in set (0.00 sec)

mysql> SELECT Host, User, authentication_string FROM mysql.user;
+-----------+------------------+------------------------------------------------------------------------+
| Host      | User             | authentication_string                                                  |
+-----------+------------------+------------------------------------------------------------------------+
| localhost | mysql.infoschema | $A$005$THISISACOMBINATIONOFINVALIDSALTANDPASSWORDTHATMUSTNEVERBRBEUSED |
| localhost | mysql.session    | $A$005$THISISACOMBINATIONOFINVALIDSALTANDPASSWORDTHATMUSTNEVERBRBEUSED |
| localhost | mysql.sys        | $A$005$THISISACOMBINATIONOFINVALIDSALTANDPASSWORDTHATMUSTNEVERBRBEUSED |
| localhost | root             |                                                                        |
dC%b5xGVsKX09TW1gnr9yhI595aWftxBA2kiWWxlABe/q0 |U3|_@d_
+-----------+------------------+------------------------------------------------------------------------+
5 rows in set (0.00 sec)

mysql> SELECT
    ->     Host,
    ->     User,
    ->     authentication_string AS password
    -> FROM
    ->     mysql.user;
+-----------+------------------+------------------------------------------------------------------------+
| Host      | User             | password                                                               |
+-----------+------------------+------------------------------------------------------------------------+
| localhost | mysql.infoschema | $A$005$THISISACOMBINATIONOFINVALIDSALTANDPASSWORDTHATMUSTNEVERBRBEUSED |
| localhost | mysql.session    | $A$005$THISISACOMBINATIONOFINVALIDSALTANDPASSWORDTHATMUSTNEVERBRBEUSED |
| localhost | mysql.sys        | $A$005$THISISACOMBINATIONOFINVALIDSALTANDPASSWORDTHATMUSTNEVERBRBEUSED |
| localhost | root             |                                                                        |
dC%b5xGVsKX09TW1gnr9yhI595aWftxBA2kiWWxlABe/q0 |U3|_@d_
+-----------+------------------+------------------------------------------------------------------------+
5 rows in set (0.00 sec)

mysql> DESC mysql.user;
+--------------------------+-----------------------------------+------+-----+-----------------------+-------+
| Field                    | Type                              | Null | Key | Default               | Extra |
+--------------------------+-----------------------------------+------+-----+-----------------------+-------+
| Host                     | char(255)                         | NO   | PRI |                       |       |
| User                     | char(32)                          | NO   | PRI |                       |       |
| Select_priv              | enum('N','Y')                     | NO   |     | N                     |       |
| Insert_priv              | enum('N','Y')                     | NO   |     | N                     |       |
| Update_priv              | enum('N','Y')                     | NO   |     | N                     |       |
| Delete_priv              | enum('N','Y')                     | NO   |     | N                     |       |
| Create_priv              | enum('N','Y')                     | NO   |     | N                     |       |
| Drop_priv                | enum('N','Y')                     | NO   |     | N                     |       |
| Reload_priv              | enum('N','Y')                     | NO   |     | N                     |       |
| Shutdown_priv            | enum('N','Y')                     | NO   |     | N                     |       |
| Process_priv             | enum('N','Y')                     | NO   |     | N                     |       |
| File_priv                | enum('N','Y')                     | NO   |     | N                     |       |
| Grant_priv               | enum('N','Y')                     | NO   |     | N                     |       |
| References_priv          | enum('N','Y')                     | NO   |     | N                     |       |
| Index_priv               | enum('N','Y')                     | NO   |     | N                     |       |
| Alter_priv               | enum('N','Y')                     | NO   |     | N                     |       |
| Show_db_priv             | enum('N','Y')                     | NO   |     | N                     |       |
| Super_priv               | enum('N','Y')                     | NO   |     | N                     |       |
| Create_tmp_table_priv    | enum('N','Y')                     | NO   |     | N                     |       |
| Lock_tables_priv         | enum('N','Y')                     | NO   |     | N                     |       |
| Execute_priv             | enum('N','Y')                     | NO   |     | N                     |       |
| Repl_slave_priv          | enum('N','Y')                     | NO   |     | N                     |       |
| Repl_client_priv         | enum('N','Y')                     | NO   |     | N                     |       |
| Create_view_priv         | enum('N','Y')                     | NO   |     | N                     |       |
| Show_view_priv           | enum('N','Y')                     | NO   |     | N                     |       |
| Create_routine_priv      | enum('N','Y')                     | NO   |     | N                     |       |
| Alter_routine_priv       | enum('N','Y')                     | NO   |     | N                     |       |
| Create_user_priv         | enum('N','Y')                     | NO   |     | N                     |       |
| Event_priv               | enum('N','Y')                     | NO   |     | N                     |       |
| Trigger_priv             | enum('N','Y')                     | NO   |     | N                     |       |
| Create_tablespace_priv   | enum('N','Y')                     | NO   |     | N                     |       |
| ssl_type                 | enum('','ANY','X509','SPECIFIED') | NO   |     |                       |       |
| ssl_cipher               | blob                              | NO   |     | NULL                  |       |
| x509_issuer              | blob                              | NO   |     | NULL                  |       |
| x509_subject             | blob                              | NO   |     | NULL                  |       |
| max_questions            | int unsigned                      | NO   |     | 0                     |       |
| max_updates              | int unsigned                      | NO   |     | 0                     |       |
| max_connections          | int unsigned                      | NO   |     | 0                     |       |
| max_user_connections     | int unsigned                      | NO   |     | 0                     |       |
| plugin                   | char(64)                          | NO   |     | caching_sha2_password |       |
| authentication_string    | text                              | YES  |     | NULL                  |       |
| password_expired         | enum('N','Y')                     | NO   |     | N                     |       |
| password_last_changed    | timestamp                         | YES  |     | NULL                  |       |
| password_lifetime        | smallint unsigned                 | YES  |     | NULL                  |       |
| account_locked           | enum('N','Y')                     | NO   |     | N                     |       |
| Create_role_priv         | enum('N','Y')                     | NO   |     | N                     |       |
| Drop_role_priv           | enum('N','Y')                     | NO   |     | N                     |       |
| Password_reuse_history   | smallint unsigned                 | YES  |     | NULL                  |       |
| Password_reuse_time      | smallint unsigned                 | YES  |     | NULL                  |       |
| Password_require_current | enum('N','Y')                     | YES  |     | NULL                  |       |
| User_attributes          | json                              | YES  |     | NULL                  |       |
+--------------------------+-----------------------------------+------+-----+-----------------------+-------+
51 rows in set (0.12 sec)

mysql> SHOW TABLES FROM mysql;
+------------------------------------------------------+
| Tables_in_mysql                                      |
+------------------------------------------------------+
| columns_priv                                         |
| component                                            |
| db                                                   |
| default_roles                                        |
| engine_cost                                          |
| func                                                 |
| general_log                                          |
| global_grants                                        |
| gtid_executed                                        |
| help_category                                        |
| help_keyword                                         |
| help_relation                                        |
| help_topic                                           |
| innodb_index_stats                                   |
| innodb_table_stats                                   |
| ndb_binlog_index                                     |
| password_history                                     |
| plugin                                               |
| procs_priv                                           |
| proxies_priv                                         |
| replication_asynchronous_connection_failover         |
| replication_asynchronous_connection_failover_managed |
| replication_group_configuration_version              |
| replication_group_member_actions                     |
| role_edges                                           |
| server_cost                                          |
| servers                                              |
| slave_master_info                                    |
| slave_relay_log_info                                 |
| slave_worker_info                                    |
| slow_log                                             |
| tables_priv                                          |
| time_zone                                            |
| time_zone_leap_second                                |
| time_zone_name                                       |
| time_zone_transition                                 |
| time_zone_transition_type                            |
| user                                                 |
+------------------------------------------------------+
38 rows in set (0.01 sec)

mysql> SELECT VERSION(), NOW();
+-----------+---------------------+
| VERSION() | NOW()               |
+-----------+---------------------+
| 9.2.0     | 2025-04-08 12:04:28 |
+-----------+---------------------+
1 row in set (0.00 sec)

mysql> CREATE TABLE fournisseurs ( code INT, nom CHAR );
ERROR 1046 (3D000): No database selected
mysql> ALTER TABLE fournisseurs ADD prenom CHAR, ADD ref INT;
ERROR 1046 (3D000): No database selected
mysql> DROP TABLE fournisseurs;
ERROR 1046 (3D000): No database selected
mysql>
mysql>
mysql>
mysql>
mysql>
mysql> select database TP_SecuBDD_GHOUDANE_OUCHTA
    -> ;
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'TP_SecuBDD_GHOUDANE_OUCHTA' at line 1
mysql>
mysql>
mysql> show databases
    -> ;
+----------------------------+
| Database                   |
+----------------------------+
| information_schema         |
| mysql                      |
| performance_schema         |
| sys                        |
| TP_SecuBDD_GHOUDANE_OUCHTA |
+----------------------------+
5 rows in set (0.01 sec)

mysql> select TP_SecuBDD_GHOUDANE_OUCHTA;
ERROR 1054 (42S22): Unknown column 'TP_SecuBDD_GHOUDANE_OUCHTA' in 'field list'
mysql> use TP_SecuBDD_GHOUDANE_OUCHTA;
Database changed
mysql> CREATE TABLE fournisseurs ( code INT, nom CHAR );
Query OK, 0 rows affected (0.03 sec)

mysql> ALTER TABLE fournisseurs ADD prenom CHAR, ADD ref INT;
Query OK, 0 rows affected (0.04 sec)
Records: 0  Duplicates: 0  Warnings: 0

mysql> DROP TABLE fournisseurs;
Query OK, 0 rows affected (0.01 sec)

mysql> SELECT SIN(PI()/4), (4+1)*6;
+--------------------+---------+
| SIN(PI()/4)        | (4+1)*6 |
+--------------------+---------+
| 0.7071067811865475 |      30 |
+--------------------+---------+
1 row in set (0.00 sec)

mysql> CREATE TABLE shop (
    ->     article INT(4) UNSIGNED ZEROFILL DEFAULT '0000' NOT NULL,
    ->     dealer CHAR(20) DEFAULT '' NOT NULL,
    ->     price DOUBLE(16,2) DEFAULT '0.00' NOT NULL,
    ->     PRIMARY KEY(article, dealer)
    -> );
Query OK, 0 rows affected, 3 warnings (0.01 sec)

mysql> INSERT INTO shop VALUES
    -> (1,'A',3.45),(1,'B',3.99),(2,'A',10.99),(3,'B',1.45),(3,'C',1.69),
    -> (3,'D',1.25),(4,'D',19.95);
Query OK, 7 rows affected (0.01 sec)
Records: 7  Duplicates: 0  Warnings: 0

mysql> SELECT arTIcle FROM SHoP;
+---------+
| arTIcle |
+---------+
|    0001 |
|    0001 |
|    0002 |
|    0003 |
|    0003 |
|    0003 |
|    0004 |
+---------+
7 rows in set (0.00 sec)

mysql> CREATE USER 'customer'@'localhost' IDENTIFIED BY 'password';
Query OK, 0 rows affected (0.03 sec)

mysql> GRANT SELECT ON shop TO 'customer'@'localhost';
Query OK, 0 rows affected (0.00 sec)

mysql> INSERT INTO shop VALUES (5,'E',9.99);
Query OK, 1 row affected (0.00 sec)

mysql> delete from shop where article=5;
Query OK, 1 row affected (0.00 sec)

mysql> =mysql>
mysql>
mysql> SELECT MAX(article) AS article FROM shop;
+---------+
| article |
+---------+
|       4 |
+---------+
1 row in set (0.01 sec)

mysql> SELECT article, dealer, price FROM shop WHERE price=(SELECT MAX(price) FROM shop);
+---------+--------+-------+
| article | dealer | price |
+---------+--------+-------+
|    0004 | D      | 19.95 |
+---------+--------+-------+
1 row in set (0.01 sec)

mysql> SELECT article, MAX(price) AS price FROM shop GROUP BY article;
+---------+-------+
| article | price |
+---------+-------+
|    0001 |  3.99 |
|    0002 | 10.99 |
|    0003 |  1.69 |
|    0004 | 19.95 |
+---------+-------+
4 rows in set (0.00 sec)

mysql> SELECT article, dealer, price FROM shop s1 WHERE price=(SELECT MAX(s2.price) FROM shop s2 WHERE s1.article = s2.article);
+---------+--------+-------+
| article | dealer | price |
+---------+--------+-------+
|    0001 | B      |  3.99 |
|    0002 | A      | 10.99 |
|    0003 | C      |  1.69 |
|    0004 | D      | 19.95 |
+---------+--------+-------+
4 rows in set (0.00 sec)

mysql> CREATE TABLE persons (
    ->  id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
    ->  name CHAR(60) NOT NULL,
    ->  PRIMARY KEY (id)
    ->  );
Query OK, 0 rows affected (0.02 sec)

mysql>
mysql> CREATE TABLE shirts (
    ->  id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
    ->  style ENUM('t-shirt', 'polo', 'dress') NOT NULL,
    ->  color ENUM('red', 'blue', 'orange', 'white', 'black') NOT NULL,
    ->  owner SMALLINT UNSIGNED NOT NULL REFERENCES persons,
    ->  PRIMARY KEY (id)
    -> );
Query OK, 0 rows affected (0.01 sec)

mysql>
mysql> INSERT INTO persons VALUES (NULL, 'Antonio Paz');
Query OK, 1 row affected (0.01 sec)

mysql>
mysql> INSERT INTO shirts VALUES
    ->  (NULL, 'polo', 'blue', LAST_INSERT_ID()),
    ->  (NULL, 'dress', 'white', LAST_INSERT_ID()),
    ->  (NULL, 't-shirt', 'blue', LAST_INSERT_ID());
Query OK, 3 rows affected (0.00 sec)
Records: 3  Duplicates: 0  Warnings: 0

mysql>
mysql>
mysql> INSERT INTO persons VALUES (NULL, 'Lilliana Angelovska');
Query OK, 1 row affected (0.00 sec)

mysql> INSERT INTO persons VALUES (1, 'Laurent Marot');
ERROR 1062 (23000): Duplicate entry '1' for key 'persons.PRIMARY'
mysql>
mysql> INSERT INTO shirts VALUES
    ->  (NULL, 'dress', 'orange', LAST_INSERT_ID()),
    ->  (NULL, 'polo', 'red', LAST_INSERT_ID()),
    ->  (NULL, 'dress', 'blue', LAST_INSERT_ID()),
    ->  (NULL, 't-shirt', 'white', LAST_INSERT_ID());
Query OK, 4 rows affected (0.00 sec)
Records: 4  Duplicates: 0  Warnings: 0

mysql>
mysql> SELECT s.* FROM persons p, shirts s
    -> WHERE p.name LIKE 'Lilliana%'
    -> AND s.owner = p.id
    -> AND s.color <> 'white';
+----+-------+--------+-------+
| id | style | color  | owner |
+----+-------+--------+-------+
|  4 | dress | orange |     2 |
|  5 | polo  | red    |     2 |
|  6 | dress | blue   |     2 |
+----+-------+--------+-------+
3 rows in set (0.00 sec)

mysql>
mysql> CREATE TABLE animaux (nom VARCHAR(20), proprietaire VARCHAR(20), espece VARCHAR(20), genre CHAR(1), naissance DATE, mort DATE);
Query OK, 0 rows affected (0.01 sec)

```
