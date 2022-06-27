from models import User
from utils import create_table, conn
from sqlite3 import OperationalError
from hashlib import sha256


class AccountOpen:
    def __init__(self, details: User) -> None:
        self.details = details

    def create_user(self):

        query = r"""INSERT INTO user (first_name, last_name, password, aadhar, contact, address, email) VALUES("{}", "{}", "{}", "{}", "{}", "{}", "{}")
            """.format(
            self.details.first_name,
            self.details.last_name,
            sha256(self.details.password.encode("utf-8")).hexdigest(),
            self.details.aadhar,
            self.details.contact,
            self.details.address,
            self.details.email,
        )
        conn.execute(query)
        conn.commit()

    def check_exist(self):
        cursor = conn.execute(
            f"""SELECT * FROM User WHERE aadhar = '{self.details.aadhar}'"""
        )

        for row in cursor:
            print(row)


# Below lines are just for testing purpose
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
    ras = AccountOpen(user)
    ras.create_user()
    ras.check_exist()
