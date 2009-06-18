# Makefile for the FIRS industry set

# Name of the Makefile which contains all the settings which describe
# how to make this newgrf. It defines all the paths, the grf name,
# the files for a bundle etc.
MAKEFILECONFIG=Makefile.config

# Name of the Makefile which contains the local settings. It overrides
# the global settings in Makefile.config.
MAKEFILELOCAL=Makefile.local

SHELL = /bin/sh

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
# Targets:
# all, test, tar, install

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
	@echo "Language files:               $(LANG_FILES)"
	@echo "NFO files:                    $(HEADER_FILE) $(OTHER_FILES) $(NFO_SUBFILES) $(FOOTER_FILE)"
	@echo "PCX files:                    $(PCX_FILES)"
	@echo "Sub dirs:                     $(foreach dir,$(NFO_SUBDIRS),$(NFODIR)/$(dir))"
#	@echo "Files in sub dirs:            $(NFO_SUBFILES)"
#	@echo "Sub files:                    $(foreach dir,$(NFO_SUBDIRS),$(wildcard $(NFODIR)/$(dir)/*.$(PNFO_SUFFIX)))"

# Compile GRF
grf : $(GRF_FILENAME)

$(GRF_FILENAME): $(NFO_FILENAME)
	# pipe all nfo files through grfcodec and produce the grf(s)
	@echo "Compiling GRF:"
	$(GRFCODEC) ${GRFCODEC_FLAGS} $(notdir ${GRF_FILENAME})
	@echo
	
# NFORENUM process copy of the NFO
$(NFO_FILENAME) : $(CPNFO_FILENAME)
	@# replace the place holders for version and name by the respective variables:
	@echo "Setting title to $(GRF_TITLE)..."
	@sed s/{{GRF_TITLE}}/'$(GRF_TITLE)'/ $(CPNFO_FILENAME) > $(NFO_FILENAME)
	@echo	
	@echo "NFORENUM processing:"
	-$(NFORENUM) ${NFORENUM_FLAGS} $(NFO_FILENAME)
	@echo
	
# Prepare the nfo file	
$(CPNFO_FILENAME) : $(NFO_SUBFILES) $(PCX_FILES) $(LANG_FILES) $(OTHER_FILES) $(HEADER_FILE) $(FOOTER_FILE)
	@echo
	@echo "Generating the $(CPNFO_FILENAME)..."
	@# The header file has to go first, the footer file has to go last. The others may in principle
	@# be juggled in between as seen fit.
	@cat $(HEADER_FILE) $(OTHER_FILES) $(NFO_SUBFILES) $(LANG_FILES) $(FOOTER_FILE) > $(CPNFO_FILENAME)
	
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

$(TAR_FILENAME): $(DIR_NAME) $(BUNDLE_FILES)
	# Create the release bundle with all files in one tar
	$(TAR) $(TAR_FLAGS) $(TAR_FILENAME) $(DIR_NAME)
	@echo "Creating tar for publication"
	@echo
tar: $(TAR_FILENAME)

zip : $(ZIP_FILENAME)
$(ZIP_FILENAME): $(DIR_NAME)
	@echo "creating zip'ed tar archive"
	$(ZIP) $(ZIP_FLAGS) $(ZIP_FILENAME) $(DIR_NAME)

bzip: tar $(BZIP_FILENAME)
$(BZIP_FILENAME):
	@echo "creating bzip2'ed tar archive"
	$(BZIP) $(BZIP_FLAGS) $(TAR_FILENAME)

# Installation process
install: $(TAR_FILENAME)
	@echo "Installing grf to $(INSTALLDIR)"
	-cp $(TAR_FILENAME) $(INSTALLDIR)/$(TAR_FILENAME)
	@echo

bundle: grf tar bzip zip
	@echo creating bundle for grf	
	
remake: clean all

