# pact-pythonissue

## Steps for setting up env
1. From root of the project run python -m venv contract_venv
2. On windows run contract_venv/scripts/activate
3. If on Linux, run source contract_venv/bin/activate
4. run pip install -r ./src/requirements.txt``


## Running the tests
1. cd ./src
2. python ./main_rest_service.py 
3. run consumer_tests --> python -m unittest discover
4. run provider tests --> python ./contract_tess/provider_example.py


