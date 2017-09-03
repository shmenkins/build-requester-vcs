# Targets here are named and act similar to maven build phases
#
# Use current directory name as project name
project_name := $(shell basename $(shell pwd))
# Use same python version as in AWS Lambda
python_interpreter := python3.6

vars_file := Makefile.vars
include $(vars_file)

# Configures this project
Makefile.vars:
	cp $(vars_file).template $(vars_file) && \
		${EDITOR} $(vars_file)

# Initializes the project
init:
	virtualenv venv -p $(python_interpreter) && \
		source venv/bin/activate && \
		pip install -r requirements.txt \
		--force-reinstall \
		--upgrade \
		--find-links ~/.cache/shmenkins

# Removes build artifacts, cleans caches, ...
clean:
	rm -rf build dist .cache .tox

# Runs unit tests (makes no network calls, maximum mocking)
# Need to run pytest as a module and from src so the src is added to the PYTHONPATH
test: clean
	source venv/bin/activate && \
		cd src && \
		python -m pytest ../tests

# Runs integration tests (makes network calls, no mocking)
# Need to run pytest as a module and from src so the src is added to the PYTHONPATH
test-integration: clean
	source venv/bin/activate && \
		cd src && \
		python -m pytest ../tests-integration

# Creates build artifact(s)
package: test
	rm -rf tmp && \
		mkdir tmp && \
		cp -r src/** tmp && \
		cp -r venv/lib/$(python_interpreter)/site-packages/shmenkins tmp && \
		cd tmp && \
		zip -r $(project_name).zip '.' --include '*.py' && \
		mv $(project_name).zip ../ && \
		cd .. && \
		rm -rf tmp

# Runs more tests
verify: package
	tox

# Deploys build artifact(s)
deploy: verify Makefile.vars
	aws s3 cp $(project_name).zip s3://$(bucket)/artifacts/$(project_name).zip

