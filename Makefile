# Makefile for the 2cc train set

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

REPO_DIRS = $(dir $(BUNDLE_FILES))

# Targets:
# all, test, tar, install, bundle

# Target for all:
all : grf

# Print the output for a number of variables which define this newgrf.
test : 
	@echo "Call of nforenum:             $(NFORENUM) $(NFORENUM_FLAGS)"
	@echo "Call of grfcodec:             $(GRFCODEC) $(GRFCODEC_FLAGS)"
	@echo "Local installation directory: $(INSTALLDIR)"
	@echo "Repository revision:          r$(GRF_REVISION)"
	@echo "GRF title:                    $(GRF_TITLE)"
	@echo "Bundled files:				 $(FILES_BUNDLE)"
	@echo "Bundle filenames:             Tar=$(TAR_FILENAME) Zip=$(ZIP_FILENAME) Bz2=$(BZIP_FILENAME)"
	@echo "Language files:               $(LANG_FILES)"
	@echo "NFO files:                    $(OTHER_FILES) $(SUB_FILES)"
	@echo "Header and footer:            $(NFODIR)/$(HEADER) $(NFODIR)/$(FOOTER)"
	@echo "Repo-Dirs:                    $(REPO_DIRS)"

# Compile GRF
grf : $(GRF_FILENAME) $(SUB_FILES) $(LANG_FILES) $(OTHER_FILES) $(HEADER_FILE) $(FOOTER_FILE)

$(GRF_FILENAME): $(NFO_FILENAME)
	# pipe all nfo files through grfcodec and produce the grf(s)
	@echo "Compiling GRF:"
	$(GRFCODEC) ${GRFCODEC_FLAGS} $(notdir ${NFO_FILENAME})
	@echo
	
# NFORENUM process copy of the NFO
$(NFO_FILENAME) : $(PNFO_FILENAME)
	# take the combined pnfo file and replace place holders for the name and version by the actual string and create
	# the nfo file for renumbering and grfcodec.
	@echo "Setting title to $(GRF_TITLE)"
	@sed s/{{GRF_TITLE}}/'$(GRF_TITLE)'/ $(PNFO_FILENAME) > $(NFO_FILENAME)
	@echo	
	@echo "NFORENUM processing:"
	-$(NFORENUM) ${NFORENUM_FLAGS} $(NFO_FILENAME)
	@echo
	
# Prepare the nfo file	
# $(PNFO_FILENAME) : $(SUB_FILES) $(LANG_FILES) $(OTHER_FILES) $(HEADER_FILE) $(FOOTER_FILE)
$(PNFO_FILENAME) : $(OTHER_FILES) $(HEADER_FILE)
	# This rule defines how to create a joint pnfo file from the single source files
	# E.g. copy here all relevant files into on file for further processing.
	@echo
	@echo "Generating the nfo:"
	# The header file has to go first, the footer file has to go last. The others may in principle
	# be juggled in between as seen fit.
	@-rm $(PNFO_FILENAME)
	@echo "Header..."
	@cat $(HEADER_FILE) > $(PNFO_FILENAME)
	@echo "...other stuff..."
	@cat $(OTHER_FILES) >> $(PNFO_FILENAME)
# rest commented out till needed as not needed yet
#	@echo "...engines by region..."
#	@cat $(SUB_FILES) >> $(PNFO_FILENAME)
	@echo "...languages..."
	@cat $(LANG_FILES) >> $(PNFO_FILENAME)
#	@echo "... and footer."
#	@cat $(NFODIR)/$(FOOTER) >> $(PNFO_FILENAME)

# Fallback rule: Just update the file's time and be done
%.$(PNFO_SUFFIX):
			
# Clean the source tree
clean:
	@echo "Cleaning source tree:"
	@echo "Remove backups:"
	-rm -rf *.orig *.pre *.bak *~ $(FILENAME)* $(SPRITEDIR)/$(FILENAME).*
	
$(DIR_NAME): $(BUNDLE_FILES)
	@echo "Creating dir $(DIR_NAME)."
	@-mkdir $@ 2>/dev/null
	@-for i in $(REPO_DIRS); do [ ! -e $@/$$i ] && mkdir $@/$$i 2>/dev/null; done
	@echo "Copying files: $(BUNDLE_FILES)"
	@-for i in $(BUNDLE_FILES); do cp $$i $(DIR_NAME)/$$i; done	

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
install: tar
	@echo "Installing grf to $(INSTALLDIR)"
	-cp $(TAR_FILENAME) $(INSTALLDIR)/$(TAR_FILENAME)
	@echo

bundle: grf tar bzip zip
	@echo creating bundle for grf	
	
remake: clean all
