"""
pip install testplan

Codigo de teste da propia bliblioteca disponivel em https://testplan.readthedocs.io/en/latest/

"""

import sys

from testplan import test_plan
from testplan.common.utils.context import context
from testplan.testing.multitest import MultiTest, testcase, testsuite
from testplan.testing.multitest.driver.tcp import TCPClient, TCPServer


@testsuite
class TCPTestsuite(object):
    """Testsuite for server client connection testcases."""

    def setup(self, env):
        env.server.accept_connection()

    @testcase
    def send_and_receive_msg(self, env, result):
        """Basic send and receive hello message testcase."""
        msg = env.client.cfg.name
        result.log('Client is sending his name: {}'.format(msg))
        bytes_sent = env.client.send_text(msg)

        received = env.server.receive_text(size=bytes_sent)
        result.equal(received, msg, 'Server received client name')

        response = 'Hello {}'.format(received)
        result.log('Server is responding: {}'.format(response))
        bytes_sent = env.server.send_text(response)

        received = env.client.receive_text(size=bytes_sent)
        result.equal(received, response, 'Client received response')


@test_plan(name='TCPConnections')
def main(plan):
    test = MultiTest(name='TCPConnectionsTest',
                     suites=[TCPTestsuite()],
                     environment=[
                         TCPServer(name='server'),
                         TCPClient(name='client',
                                   host=context('server', '{{host}}'),
                                   port=context('server', '{{port}}'))])
    plan.add(test)


if __name__ == '__main__':
    sys.exit(not main())
