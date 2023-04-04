CREATE TABLE IF NOT EXISTS users (
  id INTEGER AUTO_INCREMENT,
  email varchar(64) NOT NULL,
  username varchar(64) NOT NULL,
  password_hash varchar(64) NOT NULL,
  PRIMARY KEY (id)
);
