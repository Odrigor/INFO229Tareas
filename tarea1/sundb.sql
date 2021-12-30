CREATE DATABASE IF NOT EXISTS sun;
USE sun;
CREATE TABLE news (
		id_news INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
		url TEXT,
		title TEXT, 
		date TEXT,
		media_outlet VARCHAR(50),
		category VARCHAR(100));
INSERT INTO news (url,title,date,media_outlet,category) VALUES
    ('https://www.thesun.co.uk/sport/17172941/chelsea-1-brighton-1-lukaku-james-welbeck/
','GOOD LUK, BAD LUCK Chelsea 1 Brighton 1: Dramatic Welbeck equaliser cancels out Lukaku opener as Reece James goes off injured in huge blow 
','2021-12-29','The Sun','football'),
    ('https://www.thesun.co.uk/money/17166481/supermarkets-slash-price-xmas-treats-heroes-lindt/
','CHOC OUT Supermarkets including Tesco and Iceland slash price of Xmas treats like Heroes and Lindt by up to 50%
','2021-12-29','The Sun','money'),
    ('https://www.thesun.co.uk/news/17096917/ghislaine-maxwell-guilty-of-grooming-girls/
','EVIL PREDATOR Ghislaine Maxwell GUILTY of grooming girls for paedo Jeffrey Epstein to abuse in sex-trafficking trial
','2021-12-29','The Sun','crime');
