query_creacion_bbdd='''CREATE SCHEMA IF NOT EXISTS `base_datos_empleados_ETL` DEFAULT CHARACTER SET utf8 ;;
'''

query_creacion_tabla_rotacion='''
                                CREATE TABLE IF NOT EXISTS `base_datos_empleados_ETL`.`rotacion` (
                                `id_empleado` INT NOT NULL ,
                                `employeenumber` VARCHAR(45) NULL,
                                `attrition` VARCHAR(45) NULL,
                                PRIMARY KEY (`id_empleado`),
                                UNIQUE INDEX `id_empleado_UNIQUE` (`id_empleado` ASC) VISIBLE)
                                ENGINE = InnoDB;'''

query_creacion_tabla_datos_personales='''CREATE TABLE IF NOT EXISTS `base_datos_empleados_ETL`.`datos_personales` (
                                        `id_empleado` INT NOT NULL,
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
                                            REFERENCES `base_datos_empleados_ETL`.`rotacion` (`id_empleado`)
                                            ON DELETE NO ACTION
                                            ON UPDATE NO ACTION)
                                        ENGINE = InnoDB;'''

query_creacion_tabla_datos_contrato='''CREATE TABLE IF NOT EXISTS `base_datos_empleados_ETL`.`datos_contrato` (
                                        `id_empleado` INT NOT NULL ,
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
                                            REFERENCES `base_datos_empleados_ETL`.`rotacion` (`id_empleado`)
                                            ON DELETE NO ACTION
                                            ON UPDATE NO ACTION)
                                        ENGINE = InnoDB;'''

query_creacion_tabla_datos_salario='''CREATE TABLE IF NOT EXISTS `base_datos_empleados_ETL`.`datos_salario` (
                                        `id_empleado` INT NOT NULL ,
                                        `overtime` VARCHAR(45) NULL,
                                        `montly_income` VARCHAR(45) NULL,
                                        `monthly_rate` INT NULL,
                                        `percent_salary_hike` INT NULL,
                                        `hourly_rate` VARCHAR(45) NULL COMMENT 'Hay que repasar esta columna en el jupy de limpieza porque salen cosas raras',
                                        PRIMARY KEY (`id_empleado`),
                                        UNIQUE INDEX `id_empleado_UNIQUE` (`id_empleado` ASC) VISIBLE,
                                        CONSTRAINT `fk_datos_salario_rotacion`
                                            FOREIGN KEY (`id_empleado`)
                                            REFERENCES `base_datos_empleados_ETL`.`rotacion` (`id_empleado`)
                                            ON DELETE NO ACTION
                                            ON UPDATE NO ACTION)
                                        ENGINE = InnoDB;'''
query_creacion_tabla_empleado_encuesta='''CREATE TABLE IF NOT EXISTS `base_datos_empleados_etl`.`empleado_encuesta` (
                                        `id_empleado` INT NOT NULL,
                                        `id_encuesta_empleado` INT NOT NULL,
                                        `id_encuesta_manager` INT NOT NULL,
                                        PRIMARY KEY (`id_empleado`),
                                        INDEX `fk_empleado_encuesta_rotacion1_idx` (`id_empleado` ASC) VISIBLE,
                                        UNIQUE INDEX `id_encuesta_empleado_UNIQUE` (`id_encuesta_empleado` ASC) VISIBLE,
                                        UNIQUE INDEX `id_encuesta_manager_UNIQUE` (`id_encuesta_manager` ASC) VISIBLE,
                                        CONSTRAINT `fk_empleado_encuesta_rotacion1`
                                            FOREIGN KEY (`id_empleado`)
                                            REFERENCES `base_datos_empleados_etl`.`rotacion` (`id_empleado`))'''

query_creacion_tabla_datos_encuesta_empleado='''CREATE TABLE IF NOT EXISTS `base_datos_empleados_etl`.`datos_encuestas_empleado` (
                                                `id_encuesta` INT NOT NULL ,
                                                `enviroment_satisfaction` INT NULL DEFAULT NULL,
                                                `job_satisfaction` VARCHAR(45) NULL DEFAULT NULL,
                                                `relationship_satisfaction` VARCHAR(45) NULL DEFAULT NULL,
                                                `worklife_balance` FLOAT NULL DEFAULT NULL,
                                                `job_involvment` INT NULL DEFAULT NULL,
                                                PRIMARY KEY (`id_encuesta`),
                                                UNIQUE INDEX `id_encuesta_UNIQUE` (`id_encuesta` ASC) VISIBLE,
                                                CONSTRAINT `fk_datos_encuestas_empleado_empleado_encuesta1`
                                                    FOREIGN KEY (`id_encuesta`)
                                                    REFERENCES `base_datos_empleados_etl`.`empleado_encuesta` (`id_encuesta_empleado`))
                                                ENGINE = InnoDB
                                                DEFAULT CHARACTER SET = utf8mb3;'''

query_creacion_tabla_datos_encuesta_manager='''CREATE TABLE IF NOT EXISTS `base_datos_empleados_etl`.`datos_encuestas_manager` (
                                                `id_encuesta` INT NOT NULL,
                                                `performance_rating` VARCHAR(45) NULL DEFAULT NULL,
                                                UNIQUE INDEX `id_encuesta_UNIQUE` (`id_encuesta` ASC),
                                                CONSTRAINT `fk_datos_encuestas_manager_empleado_encuesta1`
                                                    FOREIGN KEY (`id_encuesta`)
                                                    REFERENCES `base_datos_empleados_etl`.`empleado_encuesta` (`id_encuesta_manager`)
                                                    ON DELETE NO ACTION
                                                    ON UPDATE NO ACTION)
                                                ENGINE = InnoDB
                                                DEFAULT CHARACTER SET = utf8mb3;'''

query_insertar_rotacion='INSERT INTO rotacion (id_empleado,employeenumber, attrition) VALUES (%s,%s, %s)'
query_insertar_datos_personales=' INSERT INTO datos_personales (id_empleado, year_birth, age, distance_from_home, gender, education, education_field, num_companies_worked, total_working_years, marital_status, year_with_current_manager, years_since_last_promotion, years_at_company) VALUES (%s,%s, %s, %s, %s, %s,%s, %s, %s, %s, %s,%s,%s)'
query_insertar_datos_contrato='INSERT INTO datos_contrato (id_empleado, department, business_travel, job_level, job_role, stock_option_level, training_times_last_year, remote_work) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)'
query_insertar_datos_salario='INSERT INTO datos_salario (id_empleado, overtime, montly_income, monthly_rate, percent_salary_hike, hourly_rate) VALUES (%s, %s, %s, %s, %s, %s)'
query_insertar_empleado_encuesta='INSERT INTO empleado_encuesta (id_empleado, id_encuesta_empleado, id_encuesta_manager) VALUES (%s, %s, %s)'
query_insertar_datos_encuesta_empleado='INSERT INTO datos_encuestas_empleado (id_encuesta, enviroment_satisfaction, job_satisfaction, relationship_satisfaction, worklife_balance, job_involvment) VALUES (%s, %s, %s, %s, %s, %s)'
query_insertar_datos_encuesta_manager='INSERT INTO datos_encuestas_manager (id_encuesta, performance_rating) VALUES (%s, %s)'


