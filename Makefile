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

# this is a macOS-specifc install location; the pre-2017 Makefile handled multiple platforms, that could be restored if needed
install: firs.grf
	cp firs.grf ~/Documents/OpenTTD/newgrf/

clean:
	for f in .chameleon_cache .nmlcache src/__pycache__ src/*/__pycache__ docs generated \
	$(GRF_FILE) $(TAR_FILE) $(ZIP_FILE) $(MD5_FILE) $(BUNDLE_DIR) $(SOURCE_NAME).tar;\
	do if test -e $$f;\
	   then rm -r $$f;\
	   fi;\
	done
