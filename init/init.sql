CREATE TABLE `user` (
  `email` VARCHAR(255)  PRIMARY KEY,
  `password` VARCHAR(255) NOT NULL,
  `nickname` VARCHAR(255) NOT NULL,
  `status` BOOLEAN,
  `creation_date` DATETIME NOT NULL,
  `last_login` DATETIME,
  `last_acces_page` VARCHAR(255) NOT NULL
)