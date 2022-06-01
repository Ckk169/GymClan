PRAGMA FOREIGN_KEY = ON;

DROP TABLE bookings;
DROP TABLE members;
DROP TABLE classes;

CREATE TABLE members(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name VARCHAR NOT NULL,
    last_name VARCHAR NOT NULL
);

CREATE TABLE classes(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR,
    size INTEGER,
    time DATETIME 
);

CREATE TABLE bookings(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    member_id INTEGER,
    class_id INTEGER,
    FOREIGN KEY (member_id)
        REFERENCES members(id) ON DELETE CASCADE,
    FOREIGN KEY (class_id)
        REFERENCES classes(id) on DELETE CASCADE

);

