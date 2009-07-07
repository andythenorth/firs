# Makefile for the FIRS industry set

# Name of the Makefile which contains all the settings which describe
# how to make this newgrf. It defines all the paths, the grf name,
# the files for a bundle etc.
MAKEFILECONFIG=Makefile.config

# Name of the Makefile which contains the local settings. It overrides
# the global settings in Makefile.config.
MAKEFILELOCAL=Makefile.local

shell = /bin/sh

# Add some OS detection and guess an install path (use the system's default)
OSTYPE=$(shell uname -s)
ifeq ($(OSTYPE),Linux)
INSTALLDIR=$(HOME)/.openttd/data
else 
ifeq ($(OSTYPE),Darwin)
INSTALLDIR=$(HOME)/Documents/OpenTTD/data
else
ifeq ($(shell echo "$(OSTYPE)" | cut -d_ -f1),MINGW32)
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
# PCX_FILES  = $(shell cat $(PNFO_FILENAME) | sed "s/^[ \t]*//" | grep '$(PCX_SUFFIX)')
PCX_FILES  = $(shell cat $(PNFO_FILES) | grep '$(PCX_SUFFIX)' | awk '{ print $$2 }' | grep 'pcx' | sort | uniq)

# Targets:
# all, test, bundle, install, dev, remake

.PHONY: clean all bundle bundle_tar bundle_zip bundle_bzip install release release_zip remake test

# Target for all:
all : grf

# Print the output for a number of variables which define this newgrf.
test : 
	$(V) echo "Call of nforenum:             $(NFORENUM) $(NFORENUM_FLAGS)"
	$(V) echo "Call of grfcodec:             $(GRFCODEC) $(GRFCODEC_FLAGS)"
	$(V) echo "Local installation directory: $(shell [ -n "$(INSTALLDIR)" ] && echo "$(INSTALLDIR)" || echo "Not defined!")"
	$(V) echo "Repository revision:          r$(GRF_REVISION)"
	$(V) echo "GRF title:                    $(GRF_TITLE)"
	$(V) echo "Bundled files:                $(BUNDLE_FILES)"
	$(V) echo "Bundle filenames:             Tar=$(TAR_FILENAME) Zip=$(ZIP_FILENAME) Bz2=$(BZIP_FILENAME)"
	$(V) echo "PNFO files:                   $(PNFO_FILES)"
	$(V) echo "PCX files:                    $(PCX_FILES)"
	$(V) echo "Dirs (nightly/release/base):  $(DIR_NIGHTLY) / $(DIR_RELEASE) / $(DIR_BASE)"
ifeq ($(OSTYPE),Linux)
	$(V) echo "Host type:                    $(OSTYPE) (Linux)"
else 
ifeq ($(OSTYPE),Darwin)
	$(V) echo "Host type:                    $(OSTYPE) (Mac)"
else
ifeq ($(shell echo "$(OSTYPE)" | cut -d_ -f1),MINGW32)
	$(V) echo "Host type:                    $(OSTYPE) (Win)"
else
	$(V) echo "Host type:                    unknown (win?)"
endif
endif
endif

# Compile GRF
grf : $(GRF_FILENAME)

$(GRF_FILENAME): $(NFO_FILENAME)
	# pipe all nfo files through grfcodec and produce the grf(s)
	$(V) echo "Compiling GRF:"
	$(V) $(GRFCODEC) ${GRFCODEC_FLAGS} $(notdir ${GRF_FILENAME})
	$(V) echo
	
# NFORENUM process copy of the NFO
$(NFO_FILENAME): $(PCX_FILES) $(PNFO_FILES) $(REV_FILENAME)
	$(V) # replace the place holders for version and name by the respective variables:
	$(V) -rm $(CPNFO_FILENAME)
	$(V) for i in $(PNFO_FILES); do echo "#include \"$$i\"" >> $(CPNFO_FILENAME); done
	$(V) echo "Setting title to $(GRF_TITLE)..."
	$(V) $(CC) $(CC_FLAGS) $(CPNFO_FILENAME) | sed -e "s/$(GRF_ID_DUMMY)/$(GRF_ID)/" -e "s/$(GRF_TITLE_DUMMY)/$(GRF_TITLE)/" | grep -v '#' > $@
	$(V) echo	
	$(V) echo "NFORENUM processing:"
	$(V)-$(NFORENUM) ${NFORENUM_FLAGS} $@ 
	$(V) echo
	
# Rules for making the appropriate files: no rule. Just check for them
%.$(PCX_SUFFIX):
	$(V) echo "Checking $@"
%.$(PNFO_SUFFIX):
	$(V) echo "Checking $@"
	
$(REV_FILENAME):
	$(V) -rm *.$(REV_SUFFIX)
	$(V) echo "$(BUILDFILENAME)" > $(REV_FILENAME)
			
# Clean the source tree
clean:
	$(V) echo "Cleaning source tree:"
	$(V) echo "Remove backups:"
	-rm -rf *.orig *.pre *.bak *~ $(FILENAME)* $(SPRITEDIR)/$(FILENAME).* *.$(REV_SUFFIX)
	
$(DIR_NIGHTLY) $(DIR_RELEASE) : $(BUNDLE_FILES)
	$(V) echo "Creating dir $@."
	$(V) -mkdir $@ 2>/dev/null
	$(V) -rm $@/* 2>/dev/null
	$(V) echo "Copying files: $(BUNDLE_FILES)"
	$(V) -for i in $(BUNDLE_FILES); do cp $$i $@; done	
	$(V) -cat $(READMEFILE) | sed -e "s/$(GRF_TITLE_DUMMY)/$(GRF_TITLE)/" \
		| sed -e "s/{{GRF_MD5}}/`$(MD5SUM) $(GRF_FILENAME)`/" \
		| sed -e "s/{{GRF_REVISION}}/$(GRF_REVISION)/" \
		| sed -e "s/{{GRF_ID}}/$(GRF_ID)/" \
		> $@/$(notdir $(READMEFILE))
bundle: $(DIR_NIGHTLY)

%.$(TAR_SUFFIX): % $(BUNDLE_FILES)
	# Create the release bundle with all files in one tar
	$(V) echo "Basename: $(basename $@) (and $(DIR_NIGHTLY) and $(DIR_RELEASE))"
	$(V) $(TAR) $(TAR_FLAGS) $@ $(basename $@)
	$(V) echo "Creating tar for publication"
	$(V) echo
bundle_tar: $(TAR_FILENAME)

bundle_zip: $(ZIP_FILENAME)
$(ZIP_FILENAME): $(DIR_NIGHTLY)
	$(V) echo "creating zip archive"
	$(V) $(ZIP) $(ZIP_FLAGS) $(ZIP_FILENAME) $(DIR_NIGHTLY)

bundle_bzip: $(BZIP_FILENAME)
$(BZIP_FILENAME): $(TAR_FILENAME)
	$(V) echo "creating bzip2'ed tar archive"
	$(V) $(BZIP) $(BZIP_FLAGS) $(TAR_FILENAME)

# Installation process
install: $(TAR_FILENAME) $(INSTALLDIR)
	$(V) echo "Installing grf to $(INSTALLDIR)"
	$(V)-cp $(TAR_FILENAME) $(INSTALLDIR)
	$(V) echo
	
release: $(DIR_RELEASE) $(DIR_RELEASE).$(TAR_SUFFIX)
	$(V) echo "Creating release bundle $(DIR_RELEASE) and tar"
release-install: release
	$(V) echo "Installing $(DIR_RELEASE) to $(INSTALLDIR)"
	$(V)-cp $(DIR_RELEASE).$(TAR_SUFFIX) $(INSTALLDIR)
	$(V) echo
release_zip: $(DIR_RELEASE)
	$(V) $(ZIP) $(ZIP_FLAGS) $(ZIP_FILENAME) $@
	
$(INSTALLDIR):
	$(V) echo "$(error Installation dir does not exist. Check your makefile.local)"
	
remake: clean all
