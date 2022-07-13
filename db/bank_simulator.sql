DROP DATABASE IF EXISTS bank_simulator;
CREATE DATABASE bank_simulator;
USE bank_simulator;

CREATE TABLE user(
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(15) NOT NULL,
    last_name VARCHAR(15) NOT NULL,
    age  INT NOT NULL,
    e_mail VARCHAR(75) NOT NULL,
    nif INT NOT NULL,
    code INT NOT NULL,
    passworld VARCHAR(75) NOT NULL,
    balance DECIMAL(10,4) DEFAULT 0,
    account_number INT NOT NULL

);

CREATE TABLE user_admin(
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(15) NOT NULL,
    last_name VARCHAR(15) NOT NULL,
    age  INT NOT NULL,
    e_mail VARCHAR(75) NOT NULL,
    nif INT NOT NULL,
    code INT NOT NULL,
    passworld VARCHAR(75) NOT NULL,
    balance DECIMAL(10,4) DEFAULT 0,
    account_number INT NOT NULL

);


CREATE TABLE money_transfer(
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    id_sender INT NOT NULL,
    id_receiver INT NOT NULL,
    amount DECIMAL(10,4) NOT NULL,
    transfer_date DATE NOT NUll,
    transfer_code VARCHAR(75) NOT NULL
);

ALTER TABLE money_transfer ADD FOREIGN KEY fk_id_sender(id_sender)
REFERENCES user(id) ON DELETE restrict ON UPDATE cascade;

ALTER TABLE money_transfer ADD FOREIGN KEY fk_id_receiver(id_receiver)
REFERENCES user(id) ON DELETE restrict ON UPDATE cascade;