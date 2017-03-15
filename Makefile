HG_INFO=bin/hg-info
FILL_TEMPLATE=bin/fill-template

VERSION=$(shell $(HG_INFO) --version)

all: firs.grf

custom_tags.txt: custom_tags.template
	$(FILL_TEMPLATE) --template=custom_tags.template --output=custom_tags.txt \
		version=$(VERSION)

generated/firs.nml: custom_tags.txt
	python src/render_nml.py

firs.grf: generated/firs.nml custom_tags.txt
	nmlc -c -l src/lang --grf firs.grf generated/firs.nml
