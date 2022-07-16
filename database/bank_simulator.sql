CREATE TABLE IF NOT EXISTS bank_admin(
    id INTEGER PRIMARY KEY,
    username VARCHAR(15) NOT NULL,
    e_mail VARCHAR(75) NOT NULL UNIQUE,
    user_password VARCHAR(75) NOT NULL
);

CREATE TABLE IF NOT EXISTS user(
    id INTEGER PRIMARY KEY,
    first_name VARCHAR(15) NOT NULL,
    last_name VARCHAR(15) NOT NULL,
    age  INTEGER NOT NULL,
    e_mail VARCHAR(75) NOT NULL UNIQUE,
    nif INTEGER NOT NULL UNIQUE,
    code INTEGER NOT NULL,
    user_password VARCHAR(75) NOT NULL,
    balance DECIMAL(10,4) DEFAULT 0,
    account_number INTEGER NOT NULL UNIQUE, 
    user_type VARCHAR(10) NOT NULL,
    account_state BOOLEAN NOT NULL
);


CREATE TABLE IF NOT EXISTS money_transfer(
    id INTEGER PRIMARY KEY,
    id_sender INTEGER NOT NULL,
    id_receiver INTEGER NOT NULL,
    amount DECIMAL(10,4) NOT NULL,
    transfer_date DATE NOT NUll,
    transfer_code VARCHAR(75) NOT NULL UNIQUE,
    FOREIGN KEY (id_sender) REFERENCES user (id),
    FOREIGN KEY (id_receiver) REFERENCES user (id)
);


INSERT INTO bank_admin (username, e_mail, user_password) 
VALUES ("admin", "admin@bank.cv", "1234"); 
