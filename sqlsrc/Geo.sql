CREATE DATABASE IF NOT EXISTS geo;
GRANT SELECT, INSERT, UPDATE, DELETE ON geo.* TO 'luss'@'localhost' IDENTIFIED BY 'luss';
CREATE TABLE IF NOT EXISTS geo.world(
    id bigint(20) NOT NULL AUTO_INCREMENT,
    nation varchar(100) NOT NULL,
    state varchar(100) NOT NULL,
    city varchar(100) NOT NULL,
    PRIMARY KEY (`id`)
    )

