-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema conditioner
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema conditioner
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `conditioner` DEFAULT CHARACTER SET utf8 ;
USE `conditioner` ;

-- -----------------------------------------------------
-- Table `conditioner`.`state`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `conditioner`.`state` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `humidity` VARCHAR(45) NOT NULL,
  `temp` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
