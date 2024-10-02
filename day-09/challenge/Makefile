.PHONY: test clean

test:
	# Definir o PYTHONPATH para incluir o diretório src e executar os testes
	PYTHONPATH=$(PYTHONPATH):./src python3 -m unittest discover -s tests -p 'test_*.py'

clean:
	find . -type f -name '*.pyc' -delete
	find . -type d -name '__pycache__' -exec rm -r {} +
