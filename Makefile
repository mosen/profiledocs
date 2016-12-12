# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line.
SPHINXOPTS    =
SPHINXBUILD   = sphinx-build
SPHINXPROJ    = MacAdminsProfileReference
SOURCEDIR     = source
BUILDDIR      = build
AC2MANIFESTDIR = /Applications/Apple\ Configurator\ 2.app/Contents/Frameworks/ConfigurationProfile.framework/Versions/A/Resources

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile

manifests: Makefile
	cp $(AC2MANIFESTDIR)/*manifest.plist "$(SOURCEDIR)/payloads/manifests/ac2"

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
