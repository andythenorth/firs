# Makefile for the newgrf sample makefile

# Name of the Makefile which contains all the settings which describe
# how to make this newgrf. It defines all the paths, the grf name,
# the files for a bundle etc.
MAKEFILECONFIG=Makefile.config

# Name of the Makefile which contains the local settings. It overrides
# the global settings in Makefile.config.
MAKEFILELOCAL=Makefile.local

shell = /bin/sh
 	
# We want to disable the default rules. It's not c/c++ anyway
.SUFFIXES:

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
PCX_FILES  = $(shell cat $(PNFO_FILES) | grep '$(PCX_SUFFIX)' | awk '{ print $$2 }' | grep '$(PCX_SUFFIX)' | sort | uniq)

# Targets:
# all, test, bundle, install, dev, remake

.PHONY: clean all bundle bundle_tar bundle_zip bundle_bzip install release release_zip remake test

# Target for all:
all : grf

# Print the output for a number of variables which define this newgrf.
test : 
	$(_E) "Call of nforenum:             $(NFORENUM) $(NFORENUM_FLAGS)"
	$(_E) "Call of grfcodec:             $(GRFCODEC) $(GRFCODEC_FLAGS)"
	$(_E) "Local installation directory: $(shell [ -n "$(INSTALLDIR)" ] && echo "$(INSTALLDIR)" || echo "Not defined!")"
	$(_E) "Repository revision:          r$(GRF_REVISION)"
	$(_E) "GRF title:                    $(GRF_TITLE)"
	$(_E) "Bundled files:                $(BUNDLE_FILES)"
	$(_E) "Bundle filenames:             Tar=$(TAR_FILENAME) Zip=$(ZIP_FILENAME) Bz2=$(BZIP_FILENAME)"
	$(_E) "PNFO files:                   $(PNFO_FILES)"
	$(_E) "PCX files:                    $(PCX_FILES)"
	$(_E) "Dirs (nightly/release/base):  $(DIR_NIGHTLY) / $(DIR_RELEASE) / $(DIR_BASE)"
ifeq ($(OSTYPE),Linux)
	$(_E) "Host type:                    $(OSTYPE) (Linux)"
else 
ifeq ($(OSTYPE),Darwin)
	$(_E) "Host type:                    $(OSTYPE) (Mac)"
else
ifeq ($(shell echo "$(OSTYPE)" | cut -d_ -f1),MINGW32)
	$(_E) "Host type:                    $(OSTYPE) (Win)"
else
	$(_E) "Host type:                    unknown (win?)"
endif
endif
endif

# Compile GRF
grf : $(GRF_FILENAME)

%.$(GRF_SUFFIX): $(SPRITEDIR)/%.$(NFO_SUFFIX)
# pipe all nfo files through grfcodec and produce the grf(s)
	$(_E) "[GRFCODEC] $@"
	$(_V) $(GRFCODEC) ${GRFCODEC_FLAGS} $(notdir $@)
	$(_E)
	
# NFORENUM process copy of the NFO
.INTERMEDIATE: %.$(NFO_SUFFIX)
.PRECIOUS: %.$(NFO_SUFFIX)
%.$(NFO_SUFFIX): $(PCX_FILES) $(PNFO_FILES) $(REV_FILENAME)
# replace the place holders for version and name by the respective variables:
	$(_E) "[Generating] $(@:.$(NFO_SUFFIX)=.$(CPNFO_SUFFIX))"
	$(_V) if [ -f $(@:.$(NFO_SUFFIX)=.$(CPNFO_SUFFIX)) ]; then rm $(@:.$(NFO_SUFFIX)=.$(CPNFO_SUFFIX)) ; fi
	$(_V) for i in $(PNFO_FILES); do echo "#include \"$$i\"" >> $(@:.$(NFO_SUFFIX)=.$(CPNFO_SUFFIX)); done
	$(_E) "[Generating] $@"
	$(_V) $(CC) $(CC_FLAGS) $(@:.$(NFO_SUFFIX)=.$(CPNFO_SUFFIX)) | sed -e "s/$(GRF_ID_DUMMY)/$(GRF_ID)/" -e "s/$(GRF_TITLE_DUMMY)/$(GRF_TITLE)/" | grep -v '#' > $@ 
	$(_E) 
	$(_E) "[NFORENUM] $@"
	$(_V)-$(NFORENUM) ${NFORENUM_FLAGS} $@ 
	$(_E)
	
# Rules for making the appropriate files: no rule. Just check for them
%.$(PCX_SUFFIX):
	$(_E) "Checking $@"
%.$(PNFO_SUFFIX):
	$(_E) "Checking $@"
	
$(REV_FILENAME):
	$(_V) if [ -e *.$(REV_SUFFIX) ]; then rm *.$(REV_SUFFIX) ; fi
	$(_V) echo "$(BUILDFILENAME)" > $(REV_FILENAME)
			
# Clean the source tree
clean:
	$(_E) "[CLEANING]"
	$(_V)-rm -rf *.orig *.new *.pre *.bak *~ $(FILENAME)* $(SPRITEDIR)/$(FILENAME).* *.$(REV_SUFFIX) $(BANANAS_FILENAME)
mrproper: clean
	$(_V)-rm -rf $(DIR_NIGHTLY)* $(DIR_RELEASE)* $(DIR_RELEASE_SRC)
	
$(DIR_NIGHTLY) $(DIR_RELEASE) : $(BUNDLE_FILES)
	$(_E) "[BUNDLE]"
	$(_E) "[Generating] $@."
	$(_V) if [ -e $@ ]; then rm -rf $@; fi
	$(_V) mkdir $@
	$(_V) -for i in $(BUNDLE_FILES); do cp $$i $@; done	
	$(_V) -cat $(READMEFILE) | sed -e "s/$(GRF_TITLE_DUMMY)/$(GRF_TITLE)/" \
		| sed -e "s/{{GRF_MD5}}/`$(MD5SUM) $(GRF_FILENAME)`/" \
		| sed -e "s/{{GRF_REVISION}}/$(GRF_REVISION)/" \
		| sed -e "s/{{GRF_ID}}/$(GRF_ID)/" \
		> $@/$(notdir $(READMEFILE))
bundle: $(DIR_NIGHTLY)

%.$(TAR_SUFFIX): % $(BUNDLE_FILES)
# Create the release bundle with all files in one tar
	$(_E) "[Generating] $@"
	$(_V) $(TAR) $(TAR_FLAGS) $@ $(basename $@)
	$(_E) echo
bundle_tar: $(TAR_FILENAME)

bundle_zip: $(ZIP_FILENAME)
$(ZIP_FILENAME): $(DIR_NIGHTLY)
	$(_E) "[Generating] $@"
	$(_V) $(ZIP) $(ZIP_FLAGS) $(ZIP_FILENAME) $(DIR_NIGHTLY)

bundle_bzip: $(BZIP_FILENAME)
$(BZIP_FILENAME): $(TAR_FILENAME)
	$(_E) "[Generating] $<.$(BZIP2_SUFFIX)"
	$(_V) $(BZIP) $(BZIP_FLAGS) $(TAR_FILENAME)

# Installation process
install: $(TAR_FILENAME) $(INSTALLDIR)
	$(_E) "[INSTALL] to $(INSTALLDIR)"
	$(_V)-cp $(TAR_FILENAME) $(INSTALLDIR)
	$(_E)
	
release: $(DIR_RELEASE) $(DIR_RELEASE).$(TAR_SUFFIX)
	$(_E) "[RELEASE] to $(DIR_RELEASE)"
release-install: release
	$(_E) "[INSTALL] to $(INSTALLDIR)"
	$(_V)-cp $(DIR_RELEASE).$(TAR_SUFFIX) $(INSTALLDIR)
	$(_E)
release_zip: $(DIR_RELEASE)
	$(_E) "[Generating] $(ZIP_FILENAME)"
	$(_V) $(ZIP) $(ZIP_FLAGS) $(ZIP_FILENAME) $<
release_source:
	$(_V) rm -rf $(DIR_RELEASE_SRC)
	$(_V) mkdir -p $(DIR_RELEASE_SRC)
	$(_V) cp -R $(SPRITEDIR) $(DOCDIR) Makefile Makefile.config $(DIR_RELEASE_SRC)
	$(_V) cp Makefile.local.sample $(DIR_RELEASE_SRC)/Makefile.local
	$(_V) echo 'GRF_REVISION = $(GRF_REVISION)' >> $(DIR_RELEASE_SRC)/Makefile.local
	$(_V) echo 'GRF_MODIFIED = $(GRF_MODIFIED)' >> $(DIR_RELEASE_SRC)/Makefile.local
	$(_V) echo 'REPO_TAGS    = $(REPO_TAGS)'    >> $(DIR_RELEASE_SRC)/Makefile.local
	$(_V) $(MAKE) -C $(DIR_RELEASE_SRC) mrproper
	$(_V) $(TAR) --gzip -cf $(DIR_RELEASE_SRC).tar.gz $(DIR_RELEASE_SRC)
	$(_V) rm -rf $(DIR_RELEASE_SRC)
	
$(INSTALLDIR):
	$(_E) "$(error Installation dir does not exist. Check your makefile.local)"
	
bananas: $(BANANAS_FILENAME) 
$(BANANAS_FILENAME): $(GRF_FILENAME) $(READMEFILE)
	$(_E) "[Bananas] to $@"
	$(_V) if [ -f $(BANANAS_FILENAME) ]; then rm $(BANANAS_FILENAME) ; fi
	$(_V)$(TAR) $(TAR_FLAGS) $(BANANAS_FILENAME) $(GRF_FILENAME) -C $(DOCDIR) $(notdir $(READMEFILE) $(LICENSEFILE))
	
remake: clean all
