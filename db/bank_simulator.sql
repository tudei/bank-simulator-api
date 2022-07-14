
CREATE TABLE user(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name VARCHAR(15) NOT NULL,
    last_name VARCHAR(15) NOT NULL,
    age  INTEGER NOT NULL,
    e_mail VARCHAR(75) NOT NULL,
    nif INTEGER NOT NULL,
    code INTEGER NOT NULL,
    user_password VARCHAR(75) NOT NULL,
    balance DECIMAL(10,4) DEFAULT 0,
    account_number INTEGER UNIQUE KEY NOT NULL, 
    user_type VARCHAR(10) NOT NULL
);


CREATE TABLE money_transfer(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_sender INTEGER NOT NULL,
    id_receiver INTEGER NOT NULL,
    amount DECIMAL(10,4) NOT NULL,
    transfer_date DATE NOT NUll,
    transfer_code VARCHAR(75) NOT NULL
);


ALTER TABLE money_transfer ADD FOREIGN KEY fk_id_sender(id_sender)
REFERENCES user(id) ON DELETE restrict ON UPDATE cascade;

ALTER TABLE money_transfer ADD FOREIGN KEY fk_id_receiver(id_receiver)
REFERENCES user(id) ON DELETE restrict ON UPDATE cascade;