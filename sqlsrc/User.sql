Create database IF NOT EXISTS Users;
CREATE USER 'luss'@'localhost' IDENTIFIED BY 'luss';
GRANT SELECT, INSERT, UPDATE, DELETE ON Users.* TO 'luss'@'localhost' IDENTIFIED BY 'luss';

CREATE TABLE IF NOT EXISTS Users.User(
    id bigint(20) unsigned NOT NULL AUTO_INCREMENT,
    fid varchar(200),
    wid varchar(200),
    lname varchar(200),
    fname varchar(200),
    email varchar(20),
    time_created datetime NOT NULL,
    time_modified datetime,
    PRIMARY KEY(`id`)
)

