import unittest
from messages.hello.greetings import greetings

class TestHello(unittest.TestCase):
    def test_greetings(self):
        self.assertEqual(greetings('Look'), 'Hello, Look!')