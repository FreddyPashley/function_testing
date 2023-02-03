Function Testing
===============
This is a package for Python 3 to test function outputs, and time the execution of functions.

Installing
============

    pip install function_testing

Usage
=====

    >>> from function_testing import Test
    >>> tester = Test()
    >>> result = tester.test(function, locals(), ...)
    >>> result.all()