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
