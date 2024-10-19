import logging 
import employee

'''
[Logging Levels]

DEBUG    : Details information, typically of interrest only when diagnosing properly
INFO     : Confimation that things are working as expected
WARNING  : An indication thst adomthing unexpected as happened, or indicative of some problem in the near future.
          (e.g disk space low, ) The software is sill working as expected.
ERROR    : Due to more serious problem, the software has not been able to perform some function.
CRITICAL : A serious error, indicating that the program itself may be unable to continue running. 

LogRecord Attributes : https://python.readthedocs.io/en/latest/library/logging.html#logrecord-attributes
'''


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(message)s')

file_handler = logging.FileHandler('test.log')
file_handler.setLevel(logging.ERROR)
file_handler.setFormatter(formatter)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)

# basic configiration of logging
# logging.basicConfig(filename='test.log', level=logging.DEBUG, format='%(asctime)s:%(levelname)s:%(message)s')


def add(x, y):
    """ Addition Function """
    return x + y

def subtract(x, y):
    """ Subtraction Function"""
    return x - y 

def divide(x,y):
    """Division Function"""

    try:
        result = x / y
    except ZeroDivisionError:
        logger.exception("Tried to divide by Zero")
    else:
        return result 



num1 = 20 
num2 = 10

add_result = add(num1, num2)
logger.debug(f' Add : {num1} + {num2} = {add_result}')

sub_result = subtract(num1, num2)
logger.debug(f' Sub : {num1} - {num2} = {add_result}')

sub_result = divide(num1, num2)
logger.debug(f' Div : {num1} / {num2} = {add_result}')