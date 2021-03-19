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
  `Date` date NOT NULL,
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

INSERT INTO `department` (`ID`, `Name`) VALUES
(1,	'Кадровый отдел'),
(3,	'Бухгалтерский отдел'),
(4,	'Бюро пропусков'),
(5,	'Отдел развития перспективных технологий'),
(6,	'Технический отдел'),
(7,	'Отдел снабжения'),
(8,	'Административно-хозяйственный отдел'),
(9,	'Юридический отдел'),
(10,	'Отдел аналитики'),
(11,	'Отдел главного управления');

DROP TABLE IF EXISTS `employee`;
CREATE TABLE `employee` (
  `ID_code` bigint NOT NULL AUTO_INCREMENT,
  `Last_Name` tinytext NOT NULL,
  `First_Name` tinytext NOT NULL,
  `Otchestvo` tinytext NOT NULL,
  `Staffing_Table` bigint NOT NULL,
  `BirthDay` date NOT NULL,
  `Premium` float DEFAULT NULL,
  PRIMARY KEY (`ID_code`),
  KEY `Staffing_Table` (`Staffing_Table`),
  CONSTRAINT `employee_ibfk_1` FOREIGN KEY (`Staffing_Table`) REFERENCES `staffing_table` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO `employee` (`ID_code`, `Last_Name`, `First_Name`, `Otchestvo`, `Staffing_Table`, `BirthDay`, `Premium`) VALUES
(1,	'Филиппов',	'Филипп',	'Петрович',	1,	'1966-03-19',	0),
(3,	'Петров',	'Петр',	'Петрович',	2,	'1989-03-19',	0),
(4,	'Бурков',	'Алексей',	'Семенович',	3,	'1990-03-19',	NULL),
(5,	'Жаднов',	'Максим',	'Максимович',	4,	'1990-11-19',	NULL),
(6,	'Петрушкенкевич',	'Павел',	'Валерьевич',	5,	'1990-06-19',	NULL),
(7,	'Вавкин',	'Никита',	'Дмитриевич',	6,	'1999-10-25',	NULL),
(8,	'Баранов',	'Ашан',	'Михайлович',	7,	'1995-10-25',	NULL),
(9,	'Яковлев',	'Виктор',	'Викторович',	8,	'1976-03-19',	NULL),
(10,	'Бутусова',	'Антонина',	'Ильишна',	9,	'1987-01-27',	NULL),
(11,	'Сиянина',	'Пелагея',	'Афанасьевна',	10,	'1991-04-01',	NULL),
(12,	'Чужинов',	'Геннадий',	'Всеволодович',	11,	'1983-02-16',	NULL),
(13,	'Мещеряков',	'Николай',	'Афанасьевич',	12,	'1980-11-07',	NULL),
(14,	'Жиренкова',	'Настасья',	'Федоровна',	13,	'1977-11-03',	NULL),
(15,	'Пыхтин',	'Антон',	'Петрович',	14,	'1966-10-01',	NULL),
(16,	'Меншиков',	'Павел',	'Кириллович',	15,	'1994-06-18',	NULL),
(17,	'Балдагуев',	'Егор',	'Иннокентиевич',	16,	'1974-04-02',	NULL),
(18,	'Веденина',	'Таисия',	'Прокопьевна',	17,	'1987-05-20',	NULL),
(19,	'Харьков',	'Федор',	'Никитьевич',	18,	'1986-05-11',	NULL),
(20,	'Ядренникова',	'Юлия',	'Тимофеевна',	19,	'1970-06-21',	NULL),
(21,	'Балаев',	'Василий',	'Трофимович',	20,	'1973-09-15',	NULL),
(22,	'Урбановская',	'Лидия',	'Михаиловна',	21,	'1976-04-03',	NULL),
(23,	'Батрутдинова',	'Анна',	'Николаевна',	22,	'1989-04-16',	NULL),
(24,	'Ёлкин',	'Афанасий',	'Аркадьевич',	23,	'1971-09-04',	NULL),
(25,	'Машукова',	'Галина',	'Данииловна',	24,	'1971-10-20',	NULL),
(26,	'Петухов',	'Тимофей',	'Филиппович',	25,	'1969-12-10',	NULL),
(27,	'Чудова',	'Лариса',	'Семеновна',	26,	'1982-03-25',	NULL),
(28,	'Травин',	'Константин',	'Григорьевич',	27,	'1972-03-27',	NULL),
(29,	'Яфраков',	'Арсений',	'Ильич',	28,	'1980-08-15',	NULL),
(30,	'Юхтриц',	'Арсений',	'Аркадьевич',	29,	'1964-12-23',	NULL),
(31,	'Лобан',	'Леонтий',	'Лукьевич',	30,	'1994-05-09',	NULL),
(32,	'Тимирязев',	'Серафим',	'Максимович',	30,	'1992-12-20',	NULL),
(33,	'Пахомов',	'Филипп',	'Климентович',	30,	'1986-10-21',	NULL);

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
  CONSTRAINT `passport_ibfk_2` FOREIGN KEY (`Employee`) REFERENCES `employee` (`ID_code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO `passport` (`ID`, `Number`, `Issue_Date`, `Institution`, `Employee`) VALUES
(1,	'4 286 688 611',	'2017-01-20',	'ОВД России по г. Златоуст',	1),
(2,	'4 850 107 025',	'2009-10-20',	'Отделом УФМС России по г. Брянск',	3),
(3,	'4 860 448 885',	'2010-02-20',	'Отделом внутренних дел России по г. Жуковский',	4),
(4,	'4 557 640 710',	'2010-02-20',	'Отделом УФМС России по г. Салават',	5),
(5,	'4 946 336 648',	'2010-02-20',	'ОВД России по г. Подольск',	6),
(6,	'4 493 530 389',	'2010-04-20',	'Отделением УФМС России по г. Новороссийск',	7),
(7,	'4 812 935 119',	'2015-06-20',	'Управление внутренних дел по г. Улан-Удэ',	8),
(8,	'4 765 493 685',	'2021-02-20',	'Отделом внутренних дел России по г. Ростов-на-Дону',	9),
(9,	'4 389 127 421',	'2007-02-20',	'Отделением УФМС России по г. Невинномысск',	10),
(10,	'4 034 620 239',	'2011-06-20',	'Отделением УФМС России по г. Калуга',	11),
(11,	'4 740 483 196',	'2003-01-20',	'Отделом УФМС России по г. Нижний Тагил',	12),
(12,	'4 117 136 723',	'2000-12-20',	'ОУФМС России по г. Владикавказ',	13),
(13,	'4 710 485 094',	'1997-08-20',	'Отделом внутренних дел России по г. Омск',	14),
(14,	'4 647 273 253',	'2011-01-20',	'Отделением УФМС России по г. Таганрог',	15),
(15,	'4 084 771 129',	'2014-08-20',	'Управление внутренних дел по г. Рубцовск',	16),
(16,	'4 196 536 534',	'2019-08-20',	'Отделением УФМС России по г. Магнитогорск',	17),
(17,	'4 490 514 278',	'2007-02-20',	'ОУФМС России по г. Евпатория',	18),
(18,	'4 971 551 987',	'2006-05-20',	'Отделом внутренних дел России по г. Набережные Челны',	19),
(19,	'4 419 913 817',	'2020-04-20',	'Отделом УФМС России по г. Курск',	20),
(20,	'4 046 862 375',	'2018-01-20',	'ОУФМС России по г. Старый Оскол',	21),
(21,	'4 298 402 399',	'2021-11-20',	'Отделом УФМС России по г. Железногорск',	22),
(22,	'4 893 256 225',	'2009-08-20',	'Отделом УФМС России по г. Саратов',	23),
(23,	'4 041 550 579',	'2016-01-20',	'Отделом УФМС России по г. Абакан',	24),
(24,	'4 345 721 146',	'2016-02-20',	'Отделением УФМС России по г. Дзержинск',	25),
(25,	'4 583 317 787',	'2014-07-20',	'Отделом УФМС России по г. Кемерово',	26),
(26,	'4 361 799 851',	'2002-05-20',	'Отделом внутренних дел России по г. Комсомольск-на-Амуре',	27),
(27,	'4 522 601 676',	'2016-09-20',	'Отделом УФМС России по г. Элиста',	28),
(28,	'4 331 148 387',	'2020-11-20',	'Отделением УФМС России по г. Липецк',	29),
(29,	'4 141 226 906',	'2009-07-20',	'ОВД России по г. Нижнекамск',	30),
(30,	'4 079 456 544',	'2014-10-20',	'Отделением УФМС России по г. Копейск',	31),
(31,	'4 364 666 805',	'2012-10-20',	'ОУФМС России по г. Серпухов',	32),
(32,	'4 424 290 001',	'2006-03-20',	'Отделением УФМС России по г. Волжский',	33);

DROP TABLE IF EXISTS `position`;
CREATE TABLE `position` (
  `ID` bigint NOT NULL AUTO_INCREMENT,
  `Name` tinytext NOT NULL,
  `Grade` tinyint NOT NULL,
  `Salary` float NOT NULL,
  `Coeff` double NOT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO `position` (`ID`, `Name`, `Grade`, `Salary`, `Coeff`) VALUES
(1,	'Генеральный директор',	18,	0,	4.5),
(3,	'Главный инженер',	17,	0,	3.51),
(4,	'Заместитель по кадрам и быту',	17,	0,	3.51),
(6,	'Заместитель по экономике',	17,	0,	3.51),
(7,	'Заместитель по снабжению',	17,	0,	3.51),
(8,	'Начальник отдела',	11,	0,	2.242),
(9,	'Работник отдела',	5,	0,	1.268),
(10,	'Младший работник отдела',	1,	0,	1),
(11,	'Охрана',	5,	0,	1.268);

DROP TABLE IF EXISTS `private_information`;
CREATE TABLE `private_information` (
  `ID` bigint NOT NULL AUTO_INCREMENT,
  `Marital_Status` tinytext NOT NULL,
  `Count_Family` tinyint NOT NULL,
  `Adress` text NOT NULL,
  PRIMARY KEY (`ID`),
  CONSTRAINT `private_information_ibfk_1` FOREIGN KEY (`ID`) REFERENCES `employee` (`ID_code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO `private_information` (`ID`, `Marital_Status`, `Count_Family`, `Adress`) VALUES
(1,	'Холост',	0,	'Россия, г. Рубцовск, Гагарина ул., д. 16 кв.103'),
(3,	'В браке',	3,	'Россия, г. Каспийск, Солнечная ул., д. 17 кв.23'),
(4,	'В браке',	1,	'Россия, г. Долгопрудный, Зеленая ул., д. 3 кв.197'),
(5,	'В браке',	1,	'Россия, г. Нефтеюганск, Мичурина ул., д. 21 кв.189'),
(6,	'В браке',	3,	'Россия, г. Волгоград, Мичурина ул., д. 23 кв.162'),
(7,	'В браке',	1,	'Россия, г. Салават, Речной пер., д. 6 кв.194'),
(8,	'В браке',	1,	'Россия, г. Нефтекамск, Центральный пер., д. 23 кв.184'),
(9,	'В браке',	1,	'Россия, г. Старый Оскол, Новая ул., д. 11 кв.165'),
(10,	'Не замужем',	0,	'Россия, г. Псков, Ленинская ул., д. 20 кв.9'),
(11,	'В браке',	3,	'Россия, г. Копейск, Восточная ул., д. 25 кв.198'),
(12,	'В браке',	1,	'Россия, г. Петрозаводск, Садовая ул., д. 18 кв.82'),
(13,	'Холост',	0,	'Россия, г. Златоуст, Новоселов ул., д. 12 кв.94'),
(14,	'В браке',	3,	'Россия, г. Нефтекамск, Колхозная ул., д. 6 кв.63'),
(15,	'В браке',	1,	'Россия, г. Нижневартовск, Радужная ул., д. 8 кв.57'),
(16,	'В браке',	1,	'Россия, г. Нальчик, Мирная ул., д. 20 кв.30'),
(17,	'В браке',	2,	'Россия, г. Воронеж, Речная ул., д. 6 кв.104'),
(18,	'В браке',	1,	'Россия, г. Новокузнецк, 17 Сентября ул., д. 15 кв.137'),
(19,	'Холост',	0,	'Россия, г. Евпатория, Калинина ул., д. 15 кв.93'),
(20,	'В браке',	2,	'Россия, г. Якутск, Колхозный пер., д. 2 кв.210'),
(21,	'В браке',	1,	'Россия, г. Раменское, Первомайская ул., д. 23 кв.19'),
(22,	'В браке',	2,	'Россия, г. Псков, Дружбы ул., д. 2 кв.199'),
(23,	'Не замужем',	0,	'Россия, г. Салават, Дачная ул., д. 8 кв.138'),
(24,	'В браке',	1,	'Россия, г. Ногинск, Цветочная ул., д. 6 кв.174'),
(25,	'В браке',	1,	'Россия, г. Кострома, Парковая ул., д. 4 кв.6'),
(26,	'Холост',	0,	'Россия, г. Химки, Мирная ул., д. 23 кв.110'),
(27,	'Не замужем',	0,	'Россия, г. Коломна, Садовая ул., д. 7 кв.86'),
(28,	'В браке',	2,	'Россия, г. Уссурийск, Западная ул., д. 13 кв.203'),
(29,	'Холост',	0,	'Россия, г. Северск, Лесная ул., д. 23 кв.174'),
(30,	'В браке',	3,	'Россия, г. Ставрополь, Шоссейная ул., д. 14 кв.3'),
(31,	'В браке',	3,	'Россия, г. Арзамас, Партизанская ул., д. 24 кв.87'),
(32,	'В браке',	1,	'Россия, г. Евпатория, Полесская ул., д. 15 кв.162'),
(33,	'В браке',	3,	'Россия, г. Балаково, Трудовая ул., д. 1 кв.39');

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

INSERT INTO `staffing_table` (`ID`, `Position`, `Count`, `Employed`, `Dept`) VALUES
(1,	1,	1,	1,	11),
(2,	3,	1,	1,	11),
(3,	4,	1,	1,	11),
(4,	6,	1,	1,	11),
(5,	7,	1,	1,	11),
(6,	10,	3,	1,	1),
(7,	9,	3,	1,	1),
(8,	8,	1,	1,	1),
(9,	10,	3,	1,	3),
(10,	9,	3,	1,	3),
(11,	8,	1,	1,	3),
(12,	10,	3,	1,	5),
(13,	9,	3,	1,	5),
(14,	8,	1,	1,	5),
(15,	10,	3,	1,	6),
(16,	9,	3,	1,	6),
(17,	8,	1,	1,	6),
(18,	10,	3,	1,	7),
(19,	9,	3,	1,	7),
(20,	8,	1,	1,	7),
(21,	10,	3,	1,	8),
(22,	9,	3,	1,	8),
(23,	8,	1,	1,	8),
(24,	10,	3,	1,	9),
(25,	9,	3,	1,	9),
(26,	8,	1,	1,	9),
(27,	10,	3,	1,	10),
(28,	9,	3,	1,	10),
(29,	8,	1,	1,	10),
(30,	11,	3,	3,	4);

-- 2021-03-19 16:59:58