-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost:8889
-- Generation Time: Mar 29, 2023 at 06:18 AM
-- Server version: 5.7.34
-- PHP Version: 8.0.8

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `PoolPal`
--

-- --------------------------------------------------------

--
-- Table structure for table `carpeople`
--

CREATE TABLE `carpeople` (
  `CPID` int(11) NOT NULL,
  `DID` int(11) NOT NULL,
  `PID` int(11) NOT NULL,
  `PEmail` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `carpooling`
--

CREATE TABLE `carpooling` (
  `CPID` int(11) NOT NULL,
  `DID` int(11) NOT NULL,
  `DateTime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `CPStartLocation` varchar(64) NOT NULL,
  `CPStartLatitude` float NOT NULL,
  `CPStartLongitude` float NOT NULL,
  `CPEndLocation` varchar(64) NOT NULL,
  `CPEndLatitude` float NOT NULL,
  `CPEndLongitude` float NOT NULL,
  `Status` varchar(64) NOT NULL,
  `Capacity_remaining` int(11) NOT NULL,
  `CarpoolPrice` decimal(10,2) NOT NULL,
  `PassengerPrice` decimal(10,2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `carpooling`
--

INSERT INTO `carpooling` (`CPID`, `DID`, `DateTime`, `CPStartLocation`, `CPStartLatitude`, `CPStartLongitude`, `CPEndLocation`, `CPEndLatitude`, `CPEndLongitude`, `Status`, `Capacity_remaining`, `CarpoolPrice`, `PassengerPrice`) VALUES
(1, 1, '2023-03-25 00:00:00', 'Punggol MRT', 1.40286, 103.906, 'Sengkang MRT', 1.39166, 103.896, 'Active', 3, '0.00', '0.00'),
(2, 2, '2023-03-26 00:00:00', 'Hougang MRT', 1.37336, 103.886, 'Serangoon MRT', 1.34904, 103.874, 'Active', 2, '0.00', '0.00'),
(3, 3, '2023-03-25 00:00:00', 'Tampines MRT', 1.35483, 103.944, 'Pasir Ris MRT', 1.37396, 103.949, 'Active', 0, '0.00', '0.00'),
(4, 4, '2023-03-27 00:00:00', 'Jurong East MRT', 1.33447, 103.743, 'Clementi MRT', 1.31526, 103.766, 'Active', 1, '0.00', '0.00'),
(5, 5, '2023-03-28 00:00:00', 'Bedok MRT', 1.32402, 103.933, 'Changi Business Park', 1.33337, 103.967, 'Active', 2, '0.00', '0.00');

-- --------------------------------------------------------

--
-- Table structure for table `driver`
--

CREATE TABLE `driver` (
  `DID` int(11) NOT NULL,
  `DName` varchar(64) NOT NULL,
  `DGender` char(1) NOT NULL,
  `DEmail` varchar(64) NOT NULL,
  `DPasswordHash` varchar(64) NOT NULL,
  `DVehicleNo` varchar(64) NOT NULL,
  `DLicenseNo` varchar(64) NOT NULL,
  `DLicenseExpiration` datetime DEFAULT NULL,
  `DPhoneNo` int(11) NOT NULL,
  `DCar` varchar(100) NOT NULL,
  `DCapacity` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `driver`
--

INSERT INTO `driver` (`DID`, `DName`, `DGender`, `DEmail`,`DPasswordHash`,`DVehicleNo`, `DLicenseNo`, `DLicenseExpiration`, `DPhoneNo`, `DCar`, `DCapacity`) VALUES
(1, 'Chirag Nagpal', 'M', 'chiragwork02@gmail.com', "b'$2b$12$y0EzUA9Oec4ilB15U02vaOA5y31RlkPA4TqaMCtihQ.kA6yasI4XS'", 'SG12344', '12340', '2030-10-12 00:00:00', 83606092, 'Innova', 5),
(2, 'Bryan Adams', 'M', 'bryan@gmail.com', "b'$2b$12$y0EzUA9Oec4ilB15U02vaOA5y31RlkPA4TqaMCtihQ.kA6yasI4XS'", 'SG16657', '12341', '2023-10-12 00:00:00', 12345678, 'Tesla Model X', 7),
(3, 'Dame Lillard', 'M', 'Dame@gmail.com', "b'$2b$12$y0EzUA9Oec4ilB15U02vaOA5y31RlkPA4TqaMCtihQ.kA6yasI4XS'", 'SG123657', '12342', '2045-10-23 00:00:00', 87654321, 'Celantra', 13),
(4, 'dswda', 'F', 'dsdsd@gmail.com', "b'$2b$12$y0EzUA9Oec4ilB15U02vaOA5y31RlkPA4TqaMCtihQ.kA6yasI4XS'", 'SG12343657', '12343', '2045-10-23 00:00:00', 87654341, 'Celantra', 13),
(5, 'Beauty', 'F', 'beauty@gmail.com', "b'$2b$12$y0EzUA9Oec4ilB15U02vaOA5y31RlkPA4TqaMCtihQ.kA6yasI4XS'", 'SG3657', '12344', '2094-10-23 00:00:00', 87654344, 'Celantra XYZ', 65),
(6, 'r2', 'F', 'bryan@gmai.com', "b'$2b$12$y0EzUA9Oec4ilB15U02vaOA5y31RlkPA4TqaMCtihQ.kA6yasI4XS'", '1234234G', '123143', '2023-03-09 00:00:00', 22222222, 'Tesla Model X', 2),
(7, 'Timmus', 'M', 't@gmail.com', "b'$2b$12$y0EzUA9Oec4ilB15U02vaOA5y31RlkPA4TqaMCtihQ.kA6yasI4XS'", '3421343', '2341234', '2023-12-09 00:00:00', 12344344, 'Innova', 9),
(8, 'Timmus', 'M', 'timmus@gmail.com', "b'$2b$12$y0EzUA9Oec4ilB15U02vaOA5y31RlkPA4TqaMCtihQ.kA6yasI4XS'", '1234', 'G123455', '2023-03-29 00:00:00', 12345678, 'Tesla Model X', 123),
(9, 'William', 'M', 'wl@gmai.com', "b'$2b$12$y0EzUA9Oec4ilB15U02vaOA5y31RlkPA4TqaMCtihQ.kA6yasI4XS'", '1234234G', '123143', '2023-03-25 00:00:00', 22222222, 'Tesla Model X', 1234);

-- --------------------------------------------------------

--
-- Table structure for table `passengers`
--

CREATE TABLE `passengers` (
  `PID` int(11) NOT NULL,
  `PName` varchar(200) NOT NULL,
  `PUserName` varchar(200) NOT NULL,
  `PAge` int(11) NOT NULL,
  `PGender` char(1) NOT NULL,
  `PEmail` varchar(200) NOT NULL,
  `PPasswordHash` varchar(200) NOT NULL,
  `PAddress` varchar(400) NOT NULL,
  `PPhone` int(11) NOT NULL,
  `PAccount_Created_At` datetime DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `passengers`
--

INSERT INTO `passengers` (`PID`, `PName`, `PUserName`, `PAge`, `PGender`, `PEmail`, `PPasswordHash`, `PAddress`, `PPhone`, `PAccount_Created_At`) VALUES
(1, 'Adama Traore', 'Adamamu', 21, 'M', 'adam@gmail.com',"b'$2b$12$y0EzUA9Oec4ilB15U02vaOA5y31RlkPA4TqaMCtihQ.kA6yasI4XS'",'180 Bencoolen Street, 189646', 83606092, '2023-03-22 10:39:11');

-- --------------------------------------------------------

--
-- Table structure for table `review`
--

CREATE TABLE `review` (
  `CPID` int(11) NOT NULL,
  `DID` int(11) NOT NULL,
  `PID` int(11) NOT NULL,
  `PRating` int(11) DEFAULT NULL,
  `DRating` int(11) DEFAULT NULL,
  `PDescription` varchar(100) DEFAULT NULL,
  `DDescription` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `staff`
--

CREATE TABLE `staff` (
  `SID` int(11) NOT NULL,
  `SName` varchar(100) NOT NULL,
  `SEmail` varchar(100) NOT NULL,
  `SPasswordHash` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `User`
--

CREATE TABLE `User` (
  `Email` varchar(200) NOT NULL,
  `Role` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
INSERT INTO `User` (`Email`,`Role`) VALUES ('adam@gmail.com','Passenger');

-- --------------------------------------------------------

--
-- Table structure for table `users for videos`
--

CREATE TABLE IF NOT EXISTS dispute (
  id INTEGER AUTO_INCREMENT,
  email varchar(64) NOT NULL,
  username varchar(64) NOT NULL,
  password_hash varchar(64) NOT NULL,
  PRIMARY KEY (id)
);


--
-- Indexes for dumped tables
--

--
-- Indexes for table `carpeople`
--
ALTER TABLE `carpeople`
  ADD PRIMARY KEY (`CPID`,`DID`,`PID`);

--
-- Indexes for table `carpooling`
--
ALTER TABLE `carpooling`
  ADD PRIMARY KEY (`CPID`,`DID`),
  ADD KEY `DID` (`DID`);

--
-- Indexes for table `driver`
--
ALTER TABLE `driver`
  ADD PRIMARY KEY (`DID`,`DEmail`);

--
-- Indexes for table `passengers`
--
ALTER TABLE `passengers`
  ADD PRIMARY KEY (`PID`,`PEmail`),
  ADD UNIQUE KEY `PUserName` (`PUserName`);

--
-- Indexes for table `review`
--
ALTER TABLE `review`
  ADD PRIMARY KEY (`CPID`,`DID`,`PID`),
  ADD KEY `PID` (`PID`);

--
-- Indexes for table `staff`
--
ALTER TABLE `staff`
  ADD PRIMARY KEY (`SID`);

--
-- Indexes for table `User`
--
ALTER TABLE `User`
  ADD PRIMARY KEY (`Email`,`Role`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `driver`
--
ALTER TABLE `driver`
  MODIFY `DID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `passengers`
--
ALTER TABLE `passengers`
  MODIFY `PID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `staff`
--
ALTER TABLE `staff`
  MODIFY `SID` int(11) NOT NULL AUTO_INCREMENT;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `carpooling`
--
ALTER TABLE `carpooling`
  ADD CONSTRAINT `carpooling_ibfk_1` FOREIGN KEY (`DID`) REFERENCES `driver` (`DID`);

--
-- Constraints for table `review`
--
ALTER TABLE `review`
  ADD CONSTRAINT `review_ibfk_1` FOREIGN KEY (`CPID`) REFERENCES `carpooling` (`CPID`),
  ADD CONSTRAINT `review_ibfk_2` FOREIGN KEY (`PID`) REFERENCES `passengers` (`PID`);
/*COMMIT; */;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
