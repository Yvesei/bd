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


### 19 / Affichez l'âge des animaux

```
mysql> SELECT nom, TIMESTAMPDIFF(YEAR, naissance, CURDATE()) AS age FROM animaux;
+----------+------+
| nom      | age  |
+----------+------+
| Fluffy   |   12 |
| Claws    |   11 |
| Buffy    |    5 |
| Fang     |   14 |
| Bowser   |    6 |
| Chirpy   |    6 |
| Whistler |    7 |
| Slim     |    8 |
| Puffball |    6 |
+----------+------+
9 rows in set (0.001 sec)
```


### 20 / Expliquez le résultat de cette commande : SELECT 1 IS NULL, 1 IS NOT NULL;

Cette commande évalue des expressions logiques :

1 IS NULL: Vérifie si la valeur 1 est NULL. Résultat : 0 (Faux), car 1 n'est pas NULL.

1 IS NOT NULL: Vérifie si la valeur 1 n'est pas NULL. Résultat : 1 (Vrai), car 1 n'est pas NULL.

```
mysql> SELECT 1 IS NULL, 1 IS NOT NULL;
+-----------+---------------+
| 1 IS NULL | 1 IS NOT NULL |
+-----------+---------------+
|         0 |             1 |
+-----------+---------------+
1 row in set (0.002 sec)
```
### 21 / Affichez le nom des animaux dont le nom contient un b ou un P avec une expression régulière
```
mysql> SELECT nom FROM animaux WHERE nom REGEXP 'b|P';
+----------+
| nom      |
+----------+
| Buffy    |
| Bowser   |
| Chirpy   |
| Puffball |
+----------+
4 rows in set (0.091 sec)
```
### 22 / Modifiez le mot de passe de votre utilisateur créé au début avec la valeur "mysql"
```
mysql> ALTER USER 'user'@'localhost' IDENTIFIED BY 'mysql';
Query OK, 0 rows affected (0.047 sec)

mysql> FLUSH PRIVILEGES;
Query OK, 0 rows affected, 1 warning (0.017 sec)
```
### 23 / Donnez une requête sur la table animaux affichant les tuples en version hachées (SHA2)
```
mysql> SELECT SHA2(CONCAT(nom, proprietaire, espece, genre, naissance, IFNULL(mort, '')), 256) AS hashed_data FROM animaux;
+------------------------------------------------------------------+
| hashed_data                                                      |
+------------------------------------------------------------------+
| a05f27fd08f9ad45d9b7930df1c50c0ee235da9cf2c597ae08668190d028f59f |
| 6eed096ab3731ba0d6581dd45349783bb3f1634578d757045cf042a1b65dd80f |
| ece029254a77e478892a2f0639e3ef3135f7097e826755d29a08b00c0d57f282 |
| df3ffceae13931475fbb872df04deae52643c593b75a629ddf3bd676111c013e |
| 2bb879a961f7ea53a5216b7167ed75b0e0eb4f990a0a651c5a228e87a0f15abe |
| d8fd2472b973fea1030942209912b68939f35bd7a058d9b83ec0ab31ef670717 |
| NULL                                                             |
| a5b0f7fd0f6deadfbc684a1d8e7277006848c0e0489152e1f233e48aea8e2b9e |
| 04e64f6ebfeef8ba0701352d4c3acc67c1edab4fc037c09634b9420ef032a13c |
+------------------------------------------------------------------+
9 rows in set (0.023 sec)
```
### 24 / Il existe un script fourni avec MySQL et MariaDB permettant de sécuriser une installation fraîche du serveur de base de données, quel est-il et que fait-il ?

Le script fourni est mysql_secure_installation.

Ce qu'il fait :
Configure un mot de passe pour l'utilisateur root.

Supprime les utilisateurs anonymes.

Désactive les connexions root distantes.

Supprime la base de données de test par défaut.

Recharge les tables de privilèges pour appliquer les modifications.

### 25 / Comment feriez-vous pour chiffrer une cellule sensible d'une de vos tables de base de données ?

Pour chiffrer une cellule, on peut   utiliser les fonctions de chiffrement SQL natives comme AES_ENCRYPT :
```
UPDATE animaux
SET proprietaire = AES_ENCRYPT(proprietaire, 'secret_key')
WHERE nom = 'Fluffy';
```
Pour déchiffrer la valeur :
```
SELECT AES_DECRYPT(proprietaire, 'secret_key') AS proprietaire
FROM animaux
WHERE nom = 'Fluffy';
```


### 26 / Faites un dump de votre base de test dans un fichier "dump.sql"
```
❯ mysqldump -u root -p TP_SecuBDD_GHOUDANE_OUCHTA > dump.sql
Enter password:


❯ ls
dump.sql

❯ cat dump.sql
-- MySQL dump 10.13  Distrib 9.3.0, for macos13.7 (x86_64)
--
-- Host: localhost    Database: TP_SecuBDD_GHOUDANE_OUCHTA
-- ------------------------------------------------------
-- Server version	9.2.0

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `animaux`
--

DROP TABLE IF EXISTS `animaux`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `animaux` (
  `nom` varchar(20) DEFAULT NULL,
  `proprietaire` varchar(20) DEFAULT NULL,
  `espece` varchar(20) DEFAULT NULL,
  `genre` char(1) DEFAULT NULL,
  `naissance` date DEFAULT NULL,
  `mort` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `animaux`
--

LOCK TABLES `animaux` WRITE;
/*!40000 ALTER TABLE `animaux` DISABLE KEYS */;
INSERT INTO `animaux` VALUES ('Fluffy','Harold','chat','f','2013-02-04',NULL),('Claws','Gwen','chat','m','2014-03-17',NULL),('Buffy','Harod','chien','f','2019-05-13',NULL),('Fang','Benny','chien','m','2010-08-27',NULL),('Bowser','Diane','chien','m','2018-08-31','2021-07-29'),('Chirpy','Gwen','oiseau','f','2018-09-11',NULL),('Whistler','Gwen','oiseau',NULL,'2017-12-09',NULL),('Slim','Benny','serpent','m','2016-04-29',NULL),('Puffball','Diane','hamster','f','2019-03-30',NULL);
/*!40000 ALTER TABLE `animaux` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `persons`
--

DROP TABLE IF EXISTS `persons`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `persons` (
  `id` smallint unsigned NOT NULL AUTO_INCREMENT,
  `name` char(60) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `persons`
--

LOCK TABLES `persons` WRITE;
/*!40000 ALTER TABLE `persons` DISABLE KEYS */;
INSERT INTO `persons` VALUES (1,'Antonio Paz'),(2,'Lilliana Angelovska');
/*!40000 ALTER TABLE `persons` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `shirts`
--

DROP TABLE IF EXISTS `shirts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `shirts` (
  `id` smallint unsigned NOT NULL AUTO_INCREMENT,
  `style` enum('t-shirt','polo','dress') NOT NULL,
  `color` enum('red','blue','orange','white','black') NOT NULL,
  `owner` smallint unsigned NOT NULL,
  PRIMARY KEY (`id`),
  KEY `owner` (`owner`),
  CONSTRAINT `shirts_ibfk_1` FOREIGN KEY (`owner`) REFERENCES `persons` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `shirts`
--

LOCK TABLES `shirts` WRITE;
/*!40000 ALTER TABLE `shirts` DISABLE KEYS */;
INSERT INTO `shirts` VALUES (1,'polo','blue',1),(2,'dress','white',1),(3,'t-shirt','blue',1),(4,'dress','orange',2),(5,'polo','red',2),(6,'dress','blue',2),(7,'t-shirt','white',2);
/*!40000 ALTER TABLE `shirts` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `shop`
--

DROP TABLE IF EXISTS `shop`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `shop` (
  `article` int(4) unsigned zerofill NOT NULL DEFAULT '0000',
  `dealer` char(20) NOT NULL DEFAULT '',
  `price` double(16,2) NOT NULL DEFAULT '0.00',
  PRIMARY KEY (`article`,`dealer`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `shop`
--

LOCK TABLES `shop` WRITE;
/*!40000 ALTER TABLE `shop` DISABLE KEYS */;
INSERT INTO `shop` VALUES (0001,'A',3.45),(0001,'B',3.99),(0002,'A',10.99),(0003,'B',1.45),(0003,'C',1.69),(0003,'D',1.25),(0004,'D',19.95);
/*!40000 ALTER TABLE `shop` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-04-27  1:42:38

~                                                                                                                  01:42:44
❯
```



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
