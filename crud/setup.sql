-- CREATE table "data_type"
CREATE TABLE data_type (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(45),
    summary VARCHAR(512),
    description TEXT
);

--INSERT 3 records

INSERT INTO data_type (
    name,
    summary,
    description
) VALUES (
    "Integer",
    "Integer values",
    "A data type that stores integer types"
);

INSERT INTO data_type (
    name,
    summary,
    description
) VALUES (
    "Float",
    "Floating point values",
    "A data type that allows us to store multiple values after the decimal point"
);

INSERT INTO data_type (
    name,
    summary,
    description
) VALUES (
    "Boolean",
    "True or False values",
    "Named after George Boole (Boolean algebra); These can take True or False as their default values"
);