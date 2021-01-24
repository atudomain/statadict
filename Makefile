all: clean test package
.PHONY: clean test package install dist docs release-major release-minor release-patch upload

clean:
	@find . -name "*.pyc" -delete
	@rm -rf dist docs/build build statadict.egg-info

test:
	cd statadict/tests && python3 -m unittest discover -t ../..

install:
	python3 -m pip install .

dist:
	python3 setup.py sdist bdist_wheel

docs:
	python3 setup.py build_sphinx

package: dist docs

release-patch:
	bumpversion patch
	git push origin main --follow-tags

release-minor:
	bumpversion minor
	git push origin main --follow-tags

release-major:
	bumpversion major
	git push origin main --follow-tags

upload:
	rm -f dist/*
	python3 setup.py sdist bdist_wheel
	twine upload dist/*
