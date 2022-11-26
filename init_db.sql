# SELECT SECTION
SELECT * FROM PLANES;
SELECT * FROM FLIGHT;
SELECT * FROM PASSENGER;
SELECT CURRENT_DATE();
SHOW TABLES;
SELECT * FROM EMPLOYEE;
SELECT * FROM TICKET;


# CREATE SECTION
CREATE DATABASE PROJECT_DBMS;
CREATE TABLE PLANES (
    REG_NUMBER VARCHAR(6) PRIMARY KEY,
    PLANE_NAME CHAR(4) NOT NULL,
    NUMBER_OF_SEAT INT NOT NULL,
    QUANTITY_SEAT_TYPE1 INT,
    QUANTITY_SEAT_TYPE2 INT,
    MANUFACTURER VARCHAR(20)
);

CREATE TABLE FLIGHT (
    FLIGHTID VARCHAR(10) PRIMARY KEY,
    PLANEID VARCHAR(6),
    DEPARTURE_DATE DATE NOT NULL,
    ARRIVAL_DATE DATE NOT NULL ,
    DESTINATION VARCHAR(10) NOT NULL ,
    ORIGIN VARCHAR(10) NOT NULL ,
    QUANTITY_SEAT1 INT,
    QUANTITY_SEAT2 INT,
    FOREIGN KEY (PLANEID) REFERENCES PLANES(REG_NUMBER)
);

CREATE TABLE PASSENGER(
    PASSID VARCHAR(10) PRIMARY KEY,
    PASSNAME VARCHAR(100),
    PASSPHONENUMBER NUMERIC(10),
    PASSADDRESS VARCHAR(100),
    PASSIDNO NUMERIC(12)
);

CREATE TABLE EMPLOYEE(
    EMPID VARCHAR(10) PRIMARY KEY,
    EMPNAME VARCHAR(30),
    EMPADD VARCHAR(30),
    EMPPHONENUM VARCHAR(30),
    EMPPOSITION VARCHAR(30)
);

CREATE TABLE TICKET(
    TICKETID VARCHAR(10),
    EMPID VARCHAR(10),
    PASSID VARCHAR(10),
    FLIGHTID VARCHAR(10),
    SEATTYPE INT,
    TOTALCOST NUMERIC(20),
    PRIMARY KEY (TICKETID),
    FOREIGN KEY (EMPID) REFERENCES EMPLOYEE(EMPID),
    FOREIGN KEY (PASSID) REFERENCES PASSENGER(PASSID),
    FOREIGN KEY (FLIGHTID) REFERENCES FLIGHT(FLIGHTID),
    CONSTRAINT CK_SEAT_TYPE CHECK (SEATTYPE >= 1 AND SEATTYPE <=2)
);

# PROCEDURE SECTION
CREATE PROCEDURE FILL_AVAILABLE_SEAT(PLANEID_INP VARCHAR(6))
BEGIN
    DECLARE AVLB_TYPE1 INT DEFAULT 0;
    DECLARE AVLB_TYPE2 INT DEFAULT 0;
    SELECT TYPE1SEAT INTO AVLB_TYPE1 FROM PLANES WHERE PLANES.PLANEID=PLANEID_INP;
    SELECT TYPE2SEAT INTO AVLB_TYPE2 FROM PLANES WHERE PLANES.PLANEID=PLANEID_INP;
    UPDATE FLIGHT
        SET QUANTITY_SEAT1=AVLB_TYPE1, QUANTITY_SEAT2=AVLB_TYPE2
        WHERE FLIGHT.PLANEID LIKE PLANEID_INP;
END;

# EXECUTE PROCEDURE SECTION
CALL FILL_AVAILABLE_SEAT("ck101");

# ALTER SECTION
ALTER TABLE FLIGHT ADD COLUMN NOTE VARCHAR(255);

ALTER TABLE PLANES RENAME COLUMN REG_NUMBER TO PLANEID;
ALTER TABLE PLANES RENAME COLUMN PLANE_NAME TO PLANENAME;
ALTER TABLE PLANES RENAME COLUMN NUMBER_OF_SEAT TO TOTALSEAT;
ALTER TABLE PLANES RENAME COLUMN QUANTITY_SEAT_TYPE1 TO TYPE1SEAT;
ALTER TABLE PLANES RENAME COLUMN QUANTITY_SEAT_TYPE2 TO TYPE2SEAT;

ALTER TABLE TICKET MODIFY COLUMN TICKETID VARCHAR(20);

# DROP SECTION
DROP PROCEDURE FILL_AVAILABLE_SEAT;

# TRUNCATE SECTION
TRUNCATE FLIGHT;


