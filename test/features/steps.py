from nose.tools import *
import sys
from freshen import *
sys.path.append("/home/roman/dev/freshen/test")
import calculator


def before():
    global calc
    global result
    calc = calculator.Calculator()
    result = None

@Given("I have entered (\d+) into the calculator")
def enter(num):
    calc.push(int(num))

@When("I press (\w+)")
def press(button):
    global result
    op = getattr(calc, button)
    result = op()

@Then("the result should be (.*) on the screen")
def check_result(value):
    assert_equal(str(result), value)

