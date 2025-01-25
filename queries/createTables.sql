CREATE TABLE agencies(
    agencyid integer GENERATED ALWAYS AS IDENTITY NOT NULL,
    agencyname varchar(255),
    directorid integer,
    ownerfirstname varchar(255),
    ownerlastname varchar(255),
    agencyhiredate date,
    PRIMARY KEY(agencyid),
    CONSTRAINT agencies_directorid_fkey FOREIGN key(directorid) REFERENCES directors(directorid)
);

CREATE TABLE directors(
    directorid integer GENERATED ALWAYS AS IDENTITY NOT NULL,
    directorfirstname varchar(255),
    directorlastname varchar(255),
    directorhiredate date,
    PRIMARY KEY(directorid)
);

CREATE TABLE sales(
    saleid integer GENERATED ALWAYS AS IDENTITY NOT NULL,
    saledate date,
    salesrepresentativeid integer,
    agencyid integer,
    directorid integer,
    contractname varchar(255),
    contractgrossvalue integer,
    PRIMARY KEY(saleid),
    CONSTRAINT sales_salesrepresentativeid_fkey FOREIGN key(salesrepresentativeid) REFERENCES salesrepresentatives(salesrepresentativeid),
    CONSTRAINT sales_agencyid_fkey FOREIGN key(agencyid) REFERENCES agencies(agencyid),
    CONSTRAINT sales_directorid_fkey FOREIGN key(directorid) REFERENCES directors(directorid)
);

CREATE TABLE salesrepresentatives(
    salesrepresentativeid integer GENERATED ALWAYS AS IDENTITY NOT NULL,
    salesrepresentativefirstname varchar(255),
    salesrepresentativelastname varchar(255),
    agencyid integer,
    PRIMARY KEY(salesrepresentativeid),
    CONSTRAINT salesrepresentatives_agencyid_fkey FOREIGN key(agencyid) REFERENCES agencies(agencyid)
);