from models import User
import sqlite3
from sqlite3 import OperationalError

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


class AccountOpen:
    def create_user(self, details: User):

        query = r"""INSERT INTO user (first_name, last_name, password, aadhar, contact, address, email) VALUES("{}", "{}", "{}", "{}", "{}", "{}", "{}")
            """.format(
            details.first_name,
            details.last_name,
            details.password,
            details.aadhar,
            details.contact,
            details.address,
            details.email,
        )
        conn.execute(query)
        conn.commit()

    def check_exist(self):
        cursor = conn.execute(
            f"""SELECT aadhar FROM user WHERE aadhar = {self.details.aadhar}"""
        )

        for row in cursor:
            print(row[0])


if __name__ == "__main__":

    try:
        create_table()
    except OperationalError:
        OperationalError()

    user = User(
        **{
            "first_name": "",
            "last_name": "",
            "password": "",
            "aadhar": "",
            "contact": "",
            "address": "",
            "email": "",
        }
    )
    print(user.address)
    AccountOpen().create_user(user)
