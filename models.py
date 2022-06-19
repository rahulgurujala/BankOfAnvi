from dataclasses import dataclass
from locale import setlocale, currency, LC_ALL

setlocale(LC_ALL, "en_IN.UTF-8")


@dataclass
class User:
    first_name: str
    last_name: str
    password: str
    aadhar: str
    contact: str
    address: str
    email: str


@dataclass
class Loan:
    """Loan Class for loan functionality.

    :param principal: Principal amount
    :type principal: float
    :param rate_of_interest: Interest rate per annum
    :type rate_of_interest: float
    :param loan_tenure: Tenure of loan in months
    :type loan_tenure: int

    Example
    -------

        >>> loan = Loan(5000, 6.5, 12)
        >>> loan
        <Loan(emi_per_month='₹ 430.33', total_interest='₹ 163.99', total_amount='₹ 5,163.99')>
    """

    principal: float
    rate_of_interest: float
    loan_tenure: int

    def emi(self):
        rate = self.rate_of_interest / 12 / 100
        return (
            self.principal
            * rate
            * ((1 + rate) ** self.loan_tenure)
            / ((1 + rate) ** self.loan_tenure - 1)
        )

    def interest_amount(self):
        return self.emi() * self.loan_tenure - self.principal

    def total_payment(self):
        return self.principal + self.interest_amount()

    def __str__(self):
        emi_per_month = currency(self.emi(), grouping=True)
        total_interest = currency(self.interest_amount(), grouping=True)
        total_amount = currency(self.total_payment(), grouping=True)
        return f"<Loan({emi_per_month=}, {total_interest=}, {total_amount=})>"


@dataclass
class Account:
    user: User
    balance: float
    loan: Loan
    active: bool = True


if __name__ == "__main__":
    loan = Loan(5000, 6.0, 12)
    print(loan)
