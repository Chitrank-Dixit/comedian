Sideeffect (sefct)
===
command list
---
- `sefct --help` (list all available flags)
- `sefct --dry-run "touch abc.txt"` (dry run command on shell)
- `sefct --commit "touch abc.txt"` (run command on shell)

build docker
---
`docker build -t sideeffect .`
 
run docker
--- 
`docker run -it sideeffect sefct ls`

`docker run sideeffect black --check --diff .`

`docker run sideeffect flake8 .`

Tox create an environment
`tox --devenv venv-py36 -e py36`
`source venv-py36/bin/activate`

Run tox for specific environment
`tox -e dev` # for dev virtual env
`source ./.tox/dev/bin/activate`

`tox -e release` # for release virtual env
`source ./.tox/release/bin/activate`
