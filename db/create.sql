## This file will create the necessary database schema and user for the application 
#--create the database if not exist
CREATE DATABASE IF NOT EXISTS map_traveller;
#--create the database if not exist
CREATE DATABASE IF NOT EXISTS map_traveller_test;

#--create the user by explicit GRANT statements
GRANT ALL ON map_traveller.* TO 'map_traveller_rw'@'localhost' IDENTIFIED BY PASSWORD '*7ACD3D16F14CC6994BBB3E0D445EF1972109F0FF';
GRANT ALL ON map_traveller.* TO 'map_traveller_rw'@'%' IDENTIFIED BY PASSWORD '*7ACD3D16F14CC6994BBB3E0D445EF1972109F0FF';
FLUSH PRIVILEGES;

#--create the user by explicit GRANT statements
GRANT ALL ON map_traveller_test.* TO 'map_traveller_rw'@'localhost' IDENTIFIED BY PASSWORD '*7ACD3D16F14CC6994BBB3E0D445EF1972109F0FF';
GRANT ALL ON map_traveller_test.* TO 'map_traveller_rw'@'%' IDENTIFIED BY PASSWORD '*7ACD3D16F14CC6994BBB3E0D445EF1972109F0FF';
FLUSH PRIVILEGES;