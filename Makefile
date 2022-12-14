.PHONY: coherent build

MODULES = furuta_plot

coherent:
	$(eval VERSION := $(shell grep '^__version__ = ".*"$$' setup.py))
	@if [ -z '$(VERSION)' ]; then \
	  echo "Missing version. Check the setup.py file."; \
	  exit 1; \
	 fi
	echo '$(VERSION)'

	sed -i 's|^__version__ = ".*"$$|$(VERSION)|g' $(foreach mod, $(MODULES), $(mod)/__init__.py)

build: coherent
	rm -rf dist
	python3 setup.py sdist


# Testing rules

CONDA_ACTIVATE = source $$(conda info --base)/etc/profile.d/conda.sh ; conda activate ; conda activate
CONDA_ENV = _furuta_test_
CONDA_PACKAGES = python=3.10.* matplotlib=3.5.* numpy=1.23.*

dbg_reset:
	$(CONDA_ACTIVATE) base \
	&& conda env remove -n $(CONDA_ENV) \
	&& conda create -y -n $(CONDA_ENV) $(CONDA_PACKAGES)
