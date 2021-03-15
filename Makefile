clean:
	@find . -name "*.pyc" -delete
	@rm -rf dist docs/build build statadict.egg-info

test:
	python3 setup.py test

install:
	python3 -m pip install .

.PHONY : dist
dist:
	python3 setup.py sdist bdist_wheel

.PHONY : docs
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
