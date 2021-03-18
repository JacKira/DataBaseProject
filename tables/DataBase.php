-- Adminer 4.7.8 MySQL dump

SET NAMES utf8;
SET time_zone = '+00:00';
SET foreign_key_checks = 0;
SET sql_mode = 'NO_AUTO_VALUE_ON_ZERO';

SET NAMES utf8mb4;

DROP TABLE IF EXISTS `business_trips`;
CREATE TABLE `business_trips` (
  `ID` bigint NOT NULL AUTO_INCREMENT,
  `Employee` bigint NOT NULL,
  `City` tinytext NOT NULL,
  `Target` text NOT NULL,
  `Start_Date` date NOT NULL,
  `End_Date` date NOT NULL,
  `Prepaid_Expense` float NOT NULL,
  PRIMARY KEY (`ID`),
  KEY `Employee` (`Employee`),
  CONSTRAINT `business_trips_ibfk_1` FOREIGN KEY (`Employee`) REFERENCES `employee` (`ID_code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


DROP TABLE IF EXISTS `business_trips_report`;
CREATE TABLE `business_trips_report` (
  `ID` bigint NOT NULL AUTO_INCREMENT,
  `Purpose_Payment` text NOT NULL,
  `Value` float NOT NULL,
  `Businnes_Trips` bigint NOT NULL,
  PRIMARY KEY (`ID`),
  KEY `Businnes_Trips` (`Businnes_Trips`),
  CONSTRAINT `business_trips_report_ibfk_1` FOREIGN KEY (`Businnes_Trips`) REFERENCES `business_trips` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


DROP TABLE IF EXISTS `department`;
CREATE TABLE `department` (
  `ID` bigint NOT NULL AUTO_INCREMENT,
  `Name` text NOT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


DROP TABLE IF EXISTS `employee`;
CREATE TABLE `employee` (
  `ID_code` bigint NOT NULL AUTO_INCREMENT,
  `Last_Name` tinytext NOT NULL,
  `First_Name` tinytext NOT NULL,
  `Otchestvo` tinytext NOT NULL,
  `Staffing_Table` bigint NOT NULL,
  `BirthDay` date NOT NULL,
  `Premium` float NOT NULL,
  PRIMARY KEY (`ID_code`),
  KEY `Staffing_Table` (`Staffing_Table`),
  CONSTRAINT `employee_ibfk_1` FOREIGN KEY (`Staffing_Table`) REFERENCES `staffing_table` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


DROP TABLE IF EXISTS `employee_transfers`;
CREATE TABLE `employee_transfers` (
  `ID` bigint NOT NULL AUTO_INCREMENT,
  `Justification` text NOT NULL,
  `Order_Number` text NOT NULL,
  `Order_Date` date NOT NULL,
  `Employee` bigint NOT NULL,
  `Stuffing_Table` bigint NOT NULL,
  PRIMARY KEY (`ID`),
  KEY `Stuffing_Table` (`Stuffing_Table`),
  KEY `Employee` (`Employee`),
  CONSTRAINT `employee_transfers_ibfk_1` FOREIGN KEY (`Stuffing_Table`) REFERENCES `staffing_table` (`ID`),
  CONSTRAINT `employee_transfers_ibfk_2` FOREIGN KEY (`Employee`) REFERENCES `employee` (`ID_code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


DROP TABLE IF EXISTS `passport`;
CREATE TABLE `passport` (
  `ID` bigint NOT NULL AUTO_INCREMENT,
  `Number` tinytext NOT NULL,
  `Issue_Date` date NOT NULL,
  `Institution` text NOT NULL,
  `Employee` bigint NOT NULL,
  PRIMARY KEY (`ID`),
  KEY `Employee` (`Employee`),
  CONSTRAINT `passport_ibfk_1` FOREIGN KEY (`Employee`) REFERENCES `employee` (`ID_code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


DROP TABLE IF EXISTS `position`;
CREATE TABLE `position` (
  `ID` bigint NOT NULL AUTO_INCREMENT,
  `Name` tinytext NOT NULL,
  `Grade` tinyint NOT NULL,
  `Salary` float NOT NULL,
  `Coeff` double NOT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


DROP TABLE IF EXISTS `private_information`;
CREATE TABLE `private_information` (
  `ID` bigint NOT NULL AUTO_INCREMENT,
  `Marital_Status` tinytext NOT NULL,
  `Count_Family` tinyint NOT NULL,
  `Adress` text NOT NULL,
  PRIMARY KEY (`ID`),
  CONSTRAINT `private_information_ibfk_3` FOREIGN KEY (`ID`) REFERENCES `employee` (`ID_code`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


DROP TABLE IF EXISTS `project_employee`;
CREATE TABLE `project_employee` (
  `ID` bigint NOT NULL AUTO_INCREMENT,
  `Project` bigint NOT NULL,
  `Employee` bigint NOT NULL,
  `Salary` float NOT NULL,
  PRIMARY KEY (`ID`),
  KEY `Employee` (`Employee`),
  KEY `Project` (`Project`),
  CONSTRAINT `project_employee_ibfk_1` FOREIGN KEY (`Employee`) REFERENCES `employee` (`ID_code`),
  CONSTRAINT `project_employee_ibfk_2` FOREIGN KEY (`Project`) REFERENCES `projects` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


DROP TABLE IF EXISTS `projects`;
CREATE TABLE `projects` (
  `ID` bigint NOT NULL AUTO_INCREMENT,
  `Name` tinytext NOT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


DROP TABLE IF EXISTS `staffing_table`;
CREATE TABLE `staffing_table` (
  `ID` bigint NOT NULL AUTO_INCREMENT,
  `Position` bigint NOT NULL,
  `Count` tinyint NOT NULL,
  `Employed` tinyint NOT NULL,
  `Dept` bigint NOT NULL,
  PRIMARY KEY (`ID`),
  KEY `Position` (`Position`),
  KEY `Dept` (`Dept`),
  CONSTRAINT `staffing_table_ibfk_1` FOREIGN KEY (`Position`) REFERENCES `position` (`ID`),
  CONSTRAINT `staffing_table_ibfk_2` FOREIGN KEY (`Dept`) REFERENCES `department` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


-- 2021-03-18 17:03:13