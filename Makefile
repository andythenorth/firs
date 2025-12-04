# Various needed programs
GIT = git
PYTHON3 = home/reinier/venvttd/bin/python3
SED = sed
ZIP = zip

NMLC = home/reinier/venvttd/bin/nmlc
GRFID = grfid

GIT_INFO = $(PYTHON3) src/polar_fox/git_info.py
FILL_TEMPLATE = bin/fill-template
FIND_FILES = bin/find-files
MK_ARCHIVE = bin/mk-archive

# Project details
PROJECT_NAME = firs

NML_LANG_DIR = generated/lang
NML_FILE = generated/firs.nml
NML_FLAGS =-c -l $(NML_LANG_DIR) --verbosity=4 --no-optimisation-warning --list-unused-strings
GS_DIR = generated/gs

-include Makefile.local

EXPORTED = no
ifeq ($(strip $(EXPORTED)),no)
  # Not exported source, therefore regular checkout
  REPO_INFO = $(shell $(GIT_INFO))
  REPO_REVISION = $(word 1,$(REPO_INFO))
  REPO_VERSION = $(word 2,$(REPO_INFO))
else
  # Exported version, lines below should get modified in 'bundle_src' target
  REPO_REVISION = ${exported_revision}
  REPO_VERSION = ${exported_version}
endif

PROJECT_VERSIONED_NAME = $(PROJECT_NAME)-$(REPO_VERSION)
ARGS = '${TEST_INDUSTRY}' '${NO_MP}'

GRF_FILE = generated/$(PROJECT_NAME).grf
TAR_FILE = $(PROJECT_VERSIONED_NAME).tar
ZIP_FILE = $(PROJECT_VERSIONED_NAME).zip
MD5_FILE = $(PROJECT_NAME).check.md5

HTML_DOCS = docs

SOURCE_NAME = $(PROJECT_VERSIONED_NAME)-source
BUNDLE_DIR = bundle_dir

# graphviz tools
GVPR ?= $(shell which gvpr)
DOT  ?= $(shell which dot)

# Build rules
.PHONY: default graphics lang nml grf tar bundle_tar bundle_zip bundle_src clean
default: html_docs grf gs
# bundle needs to clean first to ensure we don't use outdated/cached version info
bundle_tar: clean tar
bundle_zip: $(ZIP_FILE)
release: bundle_tar copy_docs_to_grf_farm
install: install_grf install_gs
lang: $(NML_LANG_DIR)
nml: $(NML_FILE)
grf: $(GRF_FILE)
tar: $(TAR_FILE)
html_docs: $(HTML_DOCS)
gs: $(GS_DIR)

# remove the @ for more verbose output (@ suppresses command output)
_V ?= 

$(NML_LANG_DIR): $(shell $(FIND_FILES) --ext=.py --ext=.pynml --ext=.pylng --ext=.toml src)
	$(_V) $(PYTHON3) src/render_lang.py $(ARGS) "grf"

$(HTML_DOCS): $(shell $(FIND_FILES) --ext=.py --ext=.pynml --ext=.pt --ext=.lng src)
	$(_V) $(PYTHON3) src/render_docs.py $(ARGS)
# Insane trick to check whether both DOT and GVPR are not empty.
ifeq ($(DOT)$(GVPR),$(GVPR)$(DOT))
	echo "[HTML DOCS] graphviz not found, skipping cargo flow graphs"
else
	mkdir docs/html/static/img/cargoflow
	$(GVPR) 'BEG_G { fname = sprintf("docs/html/%s.dot", $$G.name); writeG($$G, fname) }' docs/cargoflow.dotall
	cd docs/html; $(DOT) -Tsvg -O *.dot
endif

$(NML_FILE): $(shell $(FIND_FILES) --ext=.py --ext=.pynml src)
	$(_V) $(PYTHON3) src/render_nml.py $(ARGS)
	# this is a temporary hack to call render_graphics which is only used for book-keeping as of Oct 2022
	$(_V) $(PYTHON3) src/render_graphics.py $(ARGS)

$(GRF_FILE): $(shell $(FIND_FILES) --ext=.py --ext=.png src) $(NML_LANG_DIR) $(NML_FILE) $(HTML_DOCS)
	$(NMLC) $(NML_FLAGS) --grf=$(GRF_FILE) $(NML_FILE)

$(TAR_FILE): $(GRF_FILE) $(HTML_DOCS)
# the goal here is a sparse tar for distribution
	# create an intermediate dir, and copy in what we need
	mkdir $(PROJECT_VERSIONED_NAME)
	cp docs/readme.txt $(PROJECT_VERSIONED_NAME)
	cp docs/changelog.txt $(PROJECT_VERSIONED_NAME)
	cp docs/license.txt $(PROJECT_VERSIONED_NAME)
	cp $(GRF_FILE) $(PROJECT_VERSIONED_NAME)
	$(MK_ARCHIVE) --tar --output=$(TAR_FILE) $(PROJECT_VERSIONED_NAME)
	# delete the intermediate dir
	rm -r $(PROJECT_VERSIONED_NAME)

$(ZIP_FILE): $(TAR_FILE)
	$(ZIP) -9rq $(ZIP_FILE) $(TAR_FILE) >/dev/null

$(MD5_FILE): $(GRF_FILE)
	$(GRFID) -m $(GRF_FILE) > $(MD5_FILE)

bundle_src: $(MD5_FILE)
	if test -d $(BUNDLE_DIR); then rm -r $(BUNDLE_DIR); fi
	mkdir $(BUNDLE_DIR)
	$(GIT) archive -t files $(BUNDLE_DIR)/src
	$(FILL_TEMPLATE) --template=Makefile \
		--output=$(BUNDLE_DIR)/src/Makefile \
		"exported_revision=$(REPO_REVISION)" \
		"exported_version=$(REPO_VERSION)"
	$(SED) -i -e 's/^EXPORTED = no/EXPORTED = yes/' $(BUNDLE_DIR)/src/Makefile
	$(MK_ARCHIVE) --tar --output=$(SOURCE_NAME).tar --base=$(SOURCE_NAME) \
		`$(FIND_FILES) $(BUNDLE_DIR)/src` $(MD5_FILE)

$(GS_DIR): $(shell $(FIND_FILES) --ext=.py --ext=.pynut --ext=.pt --ext=.txt --ext=.pytxt --ext=.toml src)
	$(_V) $(PYTHON3) src/render_gs.py $(ARGS)
	$(_V) $(PYTHON3) src/render_lang.py $(ARGS) "gs"

# this expects to find a '../../grf.farm' path relative to the project, and will fail otherwise
copy_docs_to_grf_farm:
	$(_V) $(PYTHON3) src/polar_fox/grf_farm.py $(PROJECT_NAME)

# this is a macOS-specific install location; the pre-2017 Makefile handled multiple platforms, that could be restored if needed
install_grf: $(GRF_FILE)
    # remove first, OpenTTD does not like having the _contents_ of the current file change under it, but will handle a removed-and-replaced file correctly
	rm ~/Documents/OpenTTD/newgrf/$(PROJECT_NAME).grf
	cp $(GRF_FILE) ~/Documents/OpenTTD/newgrf/

# this is a macOS-specific install location; the pre-2017 Makefile handled multiple platforms, that could be restored if needed
install_gs: $(GS_DIR)
    # remove first, OpenTTD does not like having the _contents_ of the current file change under it, but will handle a removed-and-replaced file correctly
	rm -r ~/Documents/OpenTTD/game/$(PROJECT_NAME)-gs
	cp -r $(GS_DIR) ~/Documents/OpenTTD/game/$(PROJECT_NAME)-gs

clean:
	$(_V) echo "[CLEANING]"
	$(_V) for f in .chameleon_cache .nmlcache src/__pycache__ src/*/__pycache__ docs generated \
	$(GRF_FILE) $(TAR_FILE) $(ZIP_FILE) $(MD5_FILE) $(BUNDLE_DIR) $(SOURCE_NAME).tar;\
	do if test -e $$f;\
	   then rm -r $$f;\
	   fi;\
	done
	$(_V) echo "[DONE]"
