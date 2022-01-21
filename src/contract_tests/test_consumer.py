import atexit
import unittest

import requests
from pact import Consumer, Provider


pact = Consumer('Consumer').has_pact_with(Provider('Provider'))
pact.start_service()
atexit.register(pact.stop_service)


class GetUserInfoContract(unittest.TestCase):
    def test_get_user(self):
        expected = {"name":"Germany", "capital": "Berlin", "area": 50000}

        (pact
         .given('Service is Up')
         .upon_receiving('a request for UserA')
         .with_request('POST', '/countries', body=expected)
         .will_respond_with(201, body=expected))

        with pact:
            result = requests.post(pact.uri + '/countries', json=expected)

        self.assertEqual(result.json(), expected)