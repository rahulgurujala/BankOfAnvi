import sqlite3

conn = sqlite3.connect("db.sqlite3")


def create_table():
    query = """
        CREATE TABLE `User` (
        `first_name` VARCHAR NOT NULL,
        `last_name` VARCHAR NOT NULL,
        `password` VARCHAR NOT NULL,
        `aadhar` VARCHAR NOT NULL,
        `contact` VARCHAR NOT NULL,
        `address` VARCHAR NOT NULL,
        `email` VARCHAR NOT NULL
    )
    """
    conn.execute(query)
