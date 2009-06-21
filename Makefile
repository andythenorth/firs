# Makefile for the FIRS industry set

# Name of the Makefile which contains all the settings which describe
# how to make this newgrf. It defines all the paths, the grf name,
# the files for a bundle etc.
MAKEFILECONFIG=Makefile.config

# Name of the Makefile which contains the local settings. It overrides
# the global settings in Makefile.config.
MAKEFILELOCAL=Makefile.local

SHELL = /bin/sh

# Add some OS detection and guess an install path (use the system's default)
OSTYPE=$(shell uname -s)
ifeq ($(OSTYPE),Linux)
INSTALLDIR=$(HOME)/.openttd/data
else 
ifeq ($(OSTYPE),Darwin)
INSTALLDIR=$(HOME)/Documents/OpenTTD/data
else
ifeq ($(OSTYPE),MINGW32_NT-5.1)
INSTALLDIR=C:\Documents and Settings\$(USERNAME)\My Documents\OpenTTD\data
else
INSTALLDIR=
endif
endif
endif

# Get the Repository revision, tags and the modified status
GRF_REVISION = $(shell hg parent --template="{rev}")
GRF_MODIFIED = $(shell [ -n "`hg status \"." | grep -v '^?'`" ] && echo "M" || echo "")
# " \" (syntax highlighting line
REPO_TAGS    = $(shell hg parent --template="{tags}" | grep -v "tip" | cut -d\  -f1)

# Include the global configuration file
include ${MAKEFILECONFIG}

# this overrides definitions from above by individual settings:
-include ${MAKEFILELOCAL}

REPO_DIRS    = $(dir $(BUNDLE_FILES))
# read the main source file and get a list of all (p)nfo files which comprise the newgrf. We depend on them.
PNFO_FILES = $(shell cat $(PNFO_FILENAME) | sed "s/^[ \t]*//" | grep '$(PNFO_SUFFIX)')
PCX_FILES  = $(shell cat $(PNFO_FILENAME) | sed "s/^[ \t]*//" | grep '$(PCX_SUFFIX)')

# Targets:
# all, test, bundle, install, dev, remake

.PHONY: clean all tar zip bzip install dev bundle remake test

# Target for all:
all : grf

# Print the output for a number of variables which define this newgrf.
test : 
	@echo "Call of nforenum:             $(NFORENUM) $(NFORENUM_FLAGS)"
	@echo "Call of grfcodec:             $(GRFCODEC) $(GRFCODEC_FLAGS)"
	@echo "Local installation directory: $(shell [ -n "$(INSTALLDIR)" ] && echo "$(INSTALLDIR)" || echo "Not defined!")"
	@echo "Repository revision:          r$(GRF_REVISION)"
	@echo "GRF title:                    $(GRF_TITLE)"
	@echo "Bundled files:				 $(BUNDLE_FILES)"
	@echo "Bundle filenames:             Tar=$(TAR_FILENAME) Zip=$(ZIP_FILENAME) Bz2=$(BZIP_FILENAME)"
	@echo "PNFO files:                   $(PNFO_FILES)"
	@echo "PCX files:                    $(PCX_FILES)"
	@echo "DEV_FILENAME:                 $(DEV_FILENAME)"
ifeq ($(OSTYPE),Linux)
	@echo "Host type:                    $(OSTYPE) (Linux)"
else 
ifeq ($(OSTYPE),Darwin)
	@echo "Host type:                    $(OSTYPE) (Mac)"
else
ifeq ($(OSTYPE),MINGW32_NT-5.1)
	@echo "Host type:                    $(OSTYPE) (Win)"
else
	@echo "Host type unknown (win?)"
endif
endif
endif

# Compile GRF
grf : $(GRF_FILENAME)

$(GRF_FILENAME): $(NFO_FILENAME)
	# pipe all nfo files through grfcodec and produce the grf(s)
	@echo "Compiling GRF:"
	$(GRFCODEC) ${GRFCODEC_FLAGS} $(notdir ${GRF_FILENAME})
	@echo
	
# NFORENUM process copy of the NFO
$(NFO_FILENAME): $(PCX_FILES) $(PNFO_FILES)
	@# replace the place holders for version and name by the respective variables:
	@-rm $(CPNFO_FILENAME)
	@for i in $(PNFO_FILES); do echo "#include \"$$i\"" >> $(CPNFO_FILENAME); done
	@echo "Setting title to $(GRF_TITLE)..."
	@$(CC) $(CC_FLAGS) $(CPNFO_FILENAME) | sed -e "s/$(GRF_ID_DUMMY)/$(GRF_ID)/" -e "s/$(GRF_TITLE_DUMMY)/$(GRF_TITLE)/" | grep -v '#' > $@
	@echo	
	@echo "NFORENUM processing:"
	-$(NFORENUM) ${NFORENUM_FLAGS} $@
	@echo
	
# Rules for making the appropriate files: no rule. Just check for them
%.$(PCX_SUFFIX):
	@echo "Checking $@"
%.$(PNFO_SUFFIX):
	@echo "Checking $@"
			
# Clean the source tree
clean:
	@echo "Cleaning source tree:"
	@echo "Remove backups:"
	-rm -rf *.orig *.pre *.bak *~ $(FILENAME)* $(SPRITEDIR)/$(FILENAME).*
	
$(DIR_NAME): $(BUNDLE_FILES)
	@echo "Creating dir $(DIR_NAME)."
	@-mkdir $@ 2>/dev/null
	@-rm $@/* 2>/dev/null
	@echo "Copying files: $(BUNDLE_FILES)"
	@-for i in $(BUNDLE_FILES); do cp $$i $(DIR_NAME); done	
	@-cat $(READMEFILE) | sed -e "s/$(GRF_TITLE_DUMMY)/$(GRF_TITLE)/" > $@/$(notdir $(READMEFILE))

$(TAR_FILENAME): $(DIR_NAME) $(BUNDLE_FILES)
	# Create the release bundle with all files in one tar
	$(TAR) $(TAR_FLAGS) $(TAR_FILENAME) $(DIR_NAME)
	@echo "Creating tar for publication"
	@echo
tar: $(TAR_FILENAME)

zip: $(ZIP_FILENAME)
$(ZIP_FILENAME): $(DIR_NAME)
	@echo "creating zip'ed tar archive"
	$(ZIP) $(ZIP_FLAGS) $(ZIP_FILENAME) $(DIR_NAME)

bzip: $(BZIP_FILENAME)
$(BZIP_FILENAME): $(TAR_FILENAME)
	@echo "creating bzip2'ed tar archive"
	$(BZIP) $(BZIP_FLAGS) $(TAR_FILENAME)

# Installation process
install: $(TAR_FILENAME) $(INSTALLDIR)
	@echo "Installing grf to $(INSTALLDIR)"
	-cp $(TAR_FILENAME) $(INSTALLDIR)
	@echo

bundle: grf tar bzip zip

$(DEV_FILENAME): $(INSTALLDIR) $(BUNDLE_FILES)
	@-mkdir $@ 2>/dev/null
	@-rm $@/* 2>/dev/null
	@echo "Copying files: $(BUNDLE_FILES)"
	@-for i in $(BUNDLE_FILES); do cp $$i $(DEV_FILENAME); done
	@-cat $(READMEFILE) | sed -e "s/$(GRF_TITLE_DUMMY)/$(GRF_TITLE)/" > $@/$(notdir $(READMEFILE))
	$(TAR) $(TAR_FLAGS) $(DEV_FILENAME).$(TAR_SUFFIX) $(DEV_FILENAME)
	@-cp $(DEV_FILENAME).$(TAR_SUFFIX) $(INSTALLDIR)
	
$(INSTALLDIR):
	@echo "$(error Installation dir does not exist. Check your makefile.local)"

dev: grf $(DEV_FILENAME)
	
remake: clean all
