CREATE DATABASE IF NOT EXISTS `test`;


USE `test`;

CREATE TABLE `user` (
    `id` INT AUTO_INCREMENT PRIMARY KEY,
    `name` VARCHAR(255) NOT NULL
);

INSERT INTO `user` (name) VALUES ('Long');
INSERT INTO `user` (name) VALUES ('Vu Anh');

SELECT * FROM `user`;
