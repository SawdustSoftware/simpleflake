SHELL=/bin/bash
SHELLOPTS=errexit:pipefail

.PHONY:	clean

test:
	nosetests --config=nose.ini test.py

clean:
	rm -rf *.pyc
