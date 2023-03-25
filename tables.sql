  CREATE TABLE IF NOT EXISTS passengers (
      PID INTEGER AUTO_INCREMENT,
      PName VARCHAR(200) NOT NULL,
      PUserName VARCHAR(200) NOT NULL UNIQUE,
      PPasswordHash VARCHAR(400) NOT NULL,
      PAge INTEGER NOT NULL,
      PGender CHAR(1) NOT NULL,
      PEmail VARCHAR(200)NOT NULL,
      PAddress VARCHAR(400) NOT NULL,
      PPhone INTEGER NOT NULL,
      PAccount_Created_At DATETIME DEFAULT NOW(),
      PRIMARY KEY(PID, PEmail)
  );


  CREATE TABLE carpooling (
      CPID INTEGER NOT NULL,
      DID INTEGER NOT NULL,
      DriverFee NUMERIC(10, 2) NOT NULL,
      DateTime TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
      CPStartLocation VARCHAR(64) NOT NULL,
      CPStartLatitude FLOAT(10) NOT NULL,
      CPStartLongitude FLOAT(10) NOT NULL,
      CPEndLocation VARCHAR(64) NOT NULL,
      CPEndLatitude FLOAT(10) NOT NULL,
      CPEndLongitude FLOAT(10) NOT NULL,
      Status VARCHAR(64) NOT NULL,
      Capacity_remaining INTEGER NOT NULL,
      PRIMARY KEY (CPID, DID),
      FOREIGN KEY (DID) REFERENCES driver(DID)
  );


  CREATE TABLE IF NOT EXISTS review (
    CPID INTEGER NOT NULL,
    DID INTEGER NOT NULL,
    PID INTEGER NOT NULL,
    PRating INTEGER,
    DRating INTEGER,
    PDescription VARCHAR(100),
    DDescription VARCHAR(100),
    FOREIGN KEY (CPID) REFERENCES carpooling(CPID),
    FOREIGN KEY (PID) REFERENCES passengers(PID), 
    PRIMARY KEY (CPID,DID,PID)
  );

  CREATE TABLE IF NOT EXISTS staff (
    SID INTEGER AUTO_INCREMENT,
    SName varchar(100) NOT NULL,
    Gender varchar(1) NOT NULL,
    PRIMARY KEY (SID)
  );

  CREATE TABLE IF NOT EXISTS `driver` (
  `DID` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `DName` varchar(64) NOT NULL,
  `DGender` char(1) NOT NULL,
  `DEmail` varchar(64) NOT NULL UNIQUE,
  `DPasswordHash` varchar(400) NOT NULL,
  `DVehicleNo` varchar(64) NOT NULL,
  `DLicenseNo` varchar(64) NOT NULL,
  `DLicenseExpiration` datetime DEFAULT NULL,
  `DPhoneNo` int(11) NOT NULL,
  `DCar` varchar(100) NOT NULL,
  `DCapacity` int(11) NOT NULL
  ) ENGINE=InnoDB DEFAULT CHARSET=utf8;


  CREATE TABLE carpeople (
      CPID INTEGER NOT NULL,
      DID INTEGER NOT NULL,
      PID INTEGER NOT NULL,
      PEmail VARCHAR(100) NOT NULL,
      PRIMARY KEY (CPID, DID, PID)
  );

CREATE TABLE User (
    Email VARCHAR(200) NOT NULL,
    Role VARCHAR(10) NOT NULL,
    PRIMARY KEY (Email, Role)
);


