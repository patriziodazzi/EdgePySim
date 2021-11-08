import logging

logs = logging
logs.basicConfig(filename='example.log', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
