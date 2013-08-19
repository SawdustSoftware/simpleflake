SHELL=/bin/bash
SHELLOPTS=errexit:pipefail

.PHONY:	clean

test:
	nosetests --config=nose.ini tests/test.py

clean:
	rm -rf */*.pyc build dist docs/_build/
