Create database IF NOT EXISTS Users;
CREATE USER 'luss'@'localhost' IDENTIFIED BY 'luss';
GRANT SELECT, INSERT, UPDATE, DELETE ON Users.* TO 'luss@localhost' IDENTIFIED BY 'luss';

