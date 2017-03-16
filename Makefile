HG_INFO=bin/hg-info
FILL_TEMPLATE=bin/fill-template

VERSION=$(shell $(HG_INFO) --version)
# temp - legacy way of getting revision which strips chars (nml doesn't like 'r' or 'M'
REPO_REVISION=$(shell hg id -n | cut -d+ -f1)


all: firs.grf docs

docs:
	python src/render_docs.py '${REPO_TITLE}' '${REPO_REVISION}' '${TEST_INDUSTRY}' '${NO_MP}'

custom_tags.txt: custom_tags.template
	$(FILL_TEMPLATE) --template=custom_tags.template --output=custom_tags.txt \
		version=$(VERSION)

generated/firs.nml: custom_tags.txt
	python src/render_nml.py '${REPO_TITLE}' '${REPO_REVISION}' '${TEST_INDUSTRY}' '${NO_MP}'

firs.grf: generated/firs.nml custom_tags.txt
	nmlc -c -l src/lang --grf firs.grf generated/firs.nml

clean::
	$(_V)-rm -r docs
	$(_V)-rm -r .chameleon_cache
	$(_V)-rm -r generated
	$(_V)-rm -r .nmlcache
	$(_V)-rm -r src/__pycache__
	$(_V)-rm -r src/*/__pycache__

