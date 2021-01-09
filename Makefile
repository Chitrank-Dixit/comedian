.git/hooks/pre-commit:  # Install git pre-commit hook
	pip install pre-commit
	pre-commit install

up:
	vagrant up

halt:
	vagrant halt

destroy:
	vagrant destroy

activate-venv:
	./.tox/dev/bin/activate