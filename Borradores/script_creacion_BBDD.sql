-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema base_datos_empleados
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema base_datos_empleados
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `base_datos_empleados` DEFAULT CHARACTER SET utf8 ;
USE `base_datos_empleados` ;

-- -----------------------------------------------------
-- Table `base_datos_empleados`.`rotacion`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `base_datos_empleados`.`rotacion` (
  `id_empleado` INT NOT NULL AUTO_INCREMENT,
  `employeenumber` INT NULL,
  `attrition` VARCHAR(45) NULL,
  PRIMARY KEY (`id_empleado`),
  UNIQUE INDEX `id_empleado_UNIQUE` (`id_empleado` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `base_datos_empleados`.`datos_personales`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `base_datos_empleados`.`datos_personales` (
  `id_empleado` INT NOT NULL AUTO_INCREMENT,
  `year_birth` INT NULL,
  `age` INT NULL,
  `distance_from_home` VARCHAR(45) NULL,
  `gender` VARCHAR(45) NULL,
  `education` VARCHAR(45) NULL,
  `education_field` VARCHAR(45) NULL,
  `num_companies_worked` INT NULL,
  `total_working_years` FLOAT NULL,
  `marital_status` VARCHAR(45) NULL,
  `year_with_current_manager` INT NULL,
  `years_since_last_promotion` INT NULL,
  `years_at_company` INT NULL,
  PRIMARY KEY (`id_empleado`),
  UNIQUE INDEX `id_empleado_UNIQUE` (`id_empleado` ASC) VISIBLE,
  CONSTRAINT `fk_datos_personales_rotacion1`
    FOREIGN KEY (`id_empleado`)
    REFERENCES `base_datos_empleados`.`rotacion` (`id_empleado`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `base_datos_empleados`.`datos_contrato`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `base_datos_empleados`.`datos_contrato` (
  `id_empleado` INT NOT NULL AUTO_INCREMENT,
  `department` VARCHAR(45) NULL,
  `business_travel` VARCHAR(45) NULL,
  `job_level` VARCHAR(45) NULL,
  `job_role` VARCHAR(45) NULL,
  `stock_option_level` VARCHAR(45) NULL,
  `training_times_last_year` INT NULL,
  `remote_work` VARCHAR(45) NULL,
  PRIMARY KEY (`id_empleado`),
  UNIQUE INDEX `id_empleado_UNIQUE` (`id_empleado` ASC) VISIBLE,
  CONSTRAINT `fk_datos_contrato_rotacion1`
    FOREIGN KEY (`id_empleado`)
    REFERENCES `base_datos_empleados`.`rotacion` (`id_empleado`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `base_datos_empleados`.`datos_salario`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `base_datos_empleados`.`datos_salario` (
  `id_empleado` INT NOT NULL AUTO_INCREMENT,
  `overtime` VARCHAR(45) NULL,
  `montly_income` VARCHAR(45) NULL,
  `monthly_rate` INT NULL,
  `percent_salary_hike` INT NULL,
  `hourly_rate` VARCHAR(45) NULL COMMENT 'Hay que repasar esta columna en el jupy de limpieza porque salen cosas raras',
  `salary` VARCHAR(45) NULL COMMENT 'Falta crearla y calcularla en python.',
  PRIMARY KEY (`id_empleado`),
  UNIQUE INDEX `id_empleado_UNIQUE` (`id_empleado` ASC) VISIBLE,
  CONSTRAINT `fk_datos_salario_rotacion`
    FOREIGN KEY (`id_empleado`)
    REFERENCES `base_datos_empleados`.`rotacion` (`id_empleado`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `base_datos_empleados`.`empleado_encuesta`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `base_datos_empleados`.`empleado_encuesta` (
  `id_empleado` INT NOT NULL,
  `id_encuesta` INT NOT NULL,
  PRIMARY KEY (`id_encuesta`),
  INDEX `fk_empleado_encuesta_rotacion1_idx` (`id_empleado` ASC) VISIBLE,
  CONSTRAINT `fk_empleado_encuesta_rotacion1`
    FOREIGN KEY (`id_empleado`)
    REFERENCES `base_datos_empleados`.`rotacion` (`id_empleado`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `base_datos_empleados`.`datos_encuestas_empleado`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `base_datos_empleados`.`datos_encuestas_empleado` (
  `id_encuesta` INT NOT NULL AUTO_INCREMENT,
  `enviroment_satisfaction` INT NULL,
  `job_satisfaction` VARCHAR(45) NULL,
  `relationship_satisfaction` VARCHAR(45) NULL,
  `worklife_balance` FLOAT NULL,
  `job_involvment` INT NULL,
  PRIMARY KEY (`id_encuesta`),
  UNIQUE INDEX `id_encuesta_UNIQUE` (`id_encuesta` ASC) VISIBLE,
  CONSTRAINT `fk_datos_encuestas_empleado_empleado_encuesta1`
    FOREIGN KEY (`id_encuesta`)
    REFERENCES `base_datos_empleados`.`empleado_encuesta` (`id_encuesta`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `base_datos_empleados`.`datos_encuestas_manager`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `base_datos_empleados`.`datos_encuestas_manager` (
  `id_encuesta` INT NOT NULL,
  `performance_rating` VARCHAR(45) NULL,
  PRIMARY KEY (`id_encuesta`),
  CONSTRAINT `fk_datos_encuestas_manager_empleado_encuesta1`
    FOREIGN KEY (`id_encuesta`)
    REFERENCES `base_datos_empleados`.`empleado_encuesta` (`id_encuesta`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
