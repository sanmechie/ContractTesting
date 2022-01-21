from pact.verifier import Verifier


def test_provider():
    verifier = Verifier(provider="CountryService", provider_base_url='http://localhost:9011')
    o, logs = verifier.verify_pacts('consumer-provider.json', log_dir='./', log_level='DEBUG')
    print('logs', logs)
    print('output', o)

test_provider()

# import requests
# import pdb; pdb.set_trace()
# r = requests.post('http://localhost:9011/countries', headers={"Content-type": "application/json"}, json={"name": "Germany", "capital": "Berlin", "area": 50000})
#
# print(r.json())
