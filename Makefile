help:
	@echo "Usage: make <target>"
	@echo "    check         run pre-commit and tests"
	@echo "    doc           run documentation build process"
	@echo "    help          show summary of available commands"
	@echo "    l10n          update .pot and .po files"
	@echo "    package       build package distribution"
	@echo "    pre-commit    run pre-commit against all files"
	@echo "    setup         setup development environment"
	@echo "    test          run tests (in parallel)"
	@echo "    tox           run tox (in parallel)"

check:
	make l10n
	make pre-commit
	make doc
	make test

clean:
	@for ext in mo pot pyc; do \
		find . -type f -name "*.$$ext" -delete; \
	done
	@rm -rf .mypy_cache .pytest_cache dist .tox

doc:
	mkdocs build

l10n:
	find . -type f -name "*.pot" -delete
	scripts/l10n/generate_po_files.py >/dev/null 2>&1
	scripts/l10n/generate_mo_files.py

package:
	scripts/l10n/generate_mo_files.py
	python -m build

pre-commit:
	pre-commit run --all-files

release-notes:
	@scripts/generate_release_notes.py

sbom:
	@python -m cyclonedx_py requirements requirements/runtime.txt

setup:
	pip install --upgrade pip
	pip install --requirement requirements/dev.txt
	pip install --requirement requirements/docs.txt
	pip install --requirement requirements/runtime.txt
	pip install --requirement requirements/tests.txt
	pre-commit install --hook-type pre-commit
	pre-commit install --hook-type pre-push
	make l10n
	make package

snapshot:
	scripts/l10n/generate_mo_files.py
	scripts/generate_snapshots.py

test:
	scripts/l10n/generate_mo_files.py
	pytest --cov=. --cov-config=pyproject.toml --cov-report term-missing --cov-report xml --durations 10 --durations-min=0.75 --dist loadscope --no-cov-on-fail --numprocesses auto

tox:
	tox --parallel auto
