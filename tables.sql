CREATE TABLE IF NOT EXISTS passengers (
    PID INTEGER AUTO_INCREMENT,
    PName VARCHAR(200) NOT NULL,
    PUserName VARCHAR(200) NOT NULL UNIQUE,
    PAge INTEGER NOT NULL,
    PGender CHAR(1) NOT NULL,
    PEmail VARCHAR(200)NOT NULL,
    PAddress VARCHAR(400) NOT NULL,
    PPhone INTEGER NOT NULL,
    PAccount_Created_At DATETIME DEFAULT NOW(),
    PRIMARY KEY(PID, PEmail)
);


CREATE TABLE IF NOT EXISTS carpooling (
    CPID INTEGER AUTO_INCREMENT,
    DID INTEGER NOT NULL,
    DriverFee FLOAT(2) DEFAULT 0,
    DateTime DATETIME DEFAULT CURRENT_TIMESTAMP NOT NULL,
    CPStartLocation VARCHAR(64) NOT NULL,
    CPStartCoordinates FLOAT(10) NOT NULL,
    CPendLocation VARCHAR(64) NOT NULL,
    CPEndCoordinates FLOAT(10) NOT NULL, 
    Status VARCHAR(64) NOT NULL,
    Capacity_remaining INTEGER NOT NULL,
    FOREIGN KEY (DID) REFERENCES driver(DID),
    PRIMARY KEY(CPID, DID)
);


CREATE TABLE IF NOT EXISTS `driver` (
 `DID` int(11) NOT NULL,
 `DName` varchar(64) NOT NULL,
 `DGender` char(1) NOT NULL,
 `DEmail` varchar(64) NOT NULL,
 `DVehicleNo` varchar(64) NOT NULL,
 `DLicenseNo` varchar(64) NOT NULL,
 `DLicenseExpiration` datetime DEFAULT NULL,
 `DPhoneNo` int(11) NOT NULL,
 `DCar` varchar(100) NOT NULL,
 `DCapacity` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
