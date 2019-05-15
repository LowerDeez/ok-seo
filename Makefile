coverage:
	coverage erase
	coverage run -m django test --settings=seo.tests.settings {posargs}
	coverage report
	coveralls
