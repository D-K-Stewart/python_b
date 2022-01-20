-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema python_belt
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `python_belt` ;

-- -----------------------------------------------------
-- Schema python_belt
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `python_belt` DEFAULT CHARACTER SET utf8 ;
USE `python_belt` ;

-- -----------------------------------------------------
-- Table `python_belt`.`users`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `python_belt`.`users` ;

CREATE TABLE IF NOT EXISTS `python_belt`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(255) NULL,
  `last_name` VARCHAR(255) NULL,
  `email` VARCHAR(255) NULL,
  `password` VARCHAR(255) NULL,
  `created_at` DATETIME NULL DEFAULT now(),
  `updated_at` DATETIME NULL DEFAULT now() on update now(),
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `python_belt`.`topics`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `python_belt`.`topics` ;

CREATE TABLE IF NOT EXISTS `python_belt`.`topics` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `title` VARCHAR(255) NULL,
  `network` VARCHAR(255) NULL,
  `release_date` DATE NULL,
  `description` VARCHAR(255) NULL,
  `created_at` DATETIME NULL DEFAULT now(),
  `updated_at` DATETIME NULL DEFAULT Now() on update now(),
  `user_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_topics_users_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_topics_users`
    FOREIGN KEY (`user_id`)
    REFERENCES `python_belt`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
