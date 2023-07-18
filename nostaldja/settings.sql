-- settings.sql
CREATE DATABASE Nostaldja;
CREATE USER NostaldjaUser WITH PASSWORD 'nostaldja';
GRANT ALL PRIVILEGES ON DATABASE Nostaldja TO NostaldjaUser;