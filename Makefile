HG_INFO=bin/hg-info
FILL_TEMPLATE=bin/fill-template

VERSION=$(shell $(HG_INFO) --version)

all: firs.grf docs

docs:
	python src/render_docs.py

custom_tags.txt: custom_tags.template
	$(FILL_TEMPLATE) --template=custom_tags.template --output=custom_tags.txt \
		version=$(VERSION)

generated/firs.nml: custom_tags.txt
	python src/render_nml.py

firs.grf: generated/firs.nml custom_tags.txt
	nmlc -c -l src/lang --grf firs.grf generated/firs.nml

clean::
	$(_V)-rm -r docs
	$(_V)-rm -r .chameleon_cache
	$(_V)-rm -r generated
	$(_V)-rm -r .nmlcache
	$(_V)-rm -r src/__pycache__
	$(_V)-rm -r src/*/__pycache__

