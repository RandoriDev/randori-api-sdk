VERSION ?= $(shell cat ./VERSION)

build:
	docker run --rm -u $(id -u):$(id -g) \
	-v "${PWD}:/local" \
	docker.io/openapitools/openapi-generator-cli:v5.4.0 generate \
	-i /local/randori-api.json \
	-o /local \
	-g python \
	-t /local/templates \
	--git-user-id RandoriDev \
	--git-repo-id randori-api-sdk \
	--global-property=modelTests=false,apiTests=false \
	--additional-properties=packageName=randori_api_sdk,packageUrl=https://github.com/RandoriDev/randori-api-sdk,projectName=randori-api-sdk,packageVersion=$(VERSION)

COPYRIGHT_SKIPPED_EXPRESSIONS := --skip-expressions '.*/vendor/.*'
COPYRIGHT_MAJ_VERSION := v2
COPYRIGHT_IMAGE := us-central1-docker.pkg.dev/randori-inf/us-central1-container/copyrighter:$(COPYRIGHT_MAJ_VERSION)
COPYRIGHT := docker run --pull always -v $$(pwd):/code --rm $(COPYRIGHT_IMAGE)
COPYRIGHT_OPTIONS := -t /code --name Randori --tob 2023-10-01 --website https://randori.com $(COPYRIGHT_SKIPPED_EXPRESSIONS)

copyright:
	$(COPYRIGHT) apply $(COPYRIGHT_OPTIONS)

copyright-check:
	$(COPYRIGHT) check $(COPYRIGHT_OPTIONS)
