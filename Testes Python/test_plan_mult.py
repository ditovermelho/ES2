"""
Codigo de teste da propia bliblioteca disponivel em https://testplan.readthedocs.io/en/latest/


pip install testplan

"""

import sys

import mult
from testplan import test_plan
from testplan.testing.multitest import MultiTest, testcase, testsuite


@testsuite
class BasicSuite(object):

    @testcase
    def basic_multiply(self, env, result):
        result.equal(mult.multiply(2, 3), 6, description='Passing assertion')
        result.equal(mult.multiply(2, 2), 5, description='Failing assertion')


@test_plan(name='Multiply')
def main(plan):
    test = MultiTest(name='MultiplyTest',
                     suites=[BasicSuite()])
    plan.add(test)


if __name__ == '__main__':
    sys.exit(not main())
