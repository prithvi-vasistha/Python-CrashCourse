import pytest
from employee import My_Employee

@pytest.fixture
def John():
    John = My_Employee("John","Doe", int(10000))
    return John

def test_give_std_raise(John):
    prev_salary = John.salary
    John.give_raise()
    assert John.salary == prev_salary+5000

def test_give_custom_raise(John):
    prev_salary = John.salary
    raise_amount = 12000
    John.give_raise(raise_amount)
    assert John.salary == prev_salary+raise_amount


