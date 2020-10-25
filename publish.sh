#!/bin/bash
version=$1
echo "Version $1"
docker push swir/swir-example-pubsub-configurator:$version
docker push swir/swir-example-pubsub-python-processor:$version
docker push swir/swir-example-pubsub-java-processor:$version
docker push swir/swir-example-pubsub-java-source:$version
docker push swir/swir-example-pubsub-python-sink:$version
docker push swir/swir-example-si-configurator:$version
docker push swir/swir-example-si-python-http-server:$version
docker push swir/swir-example-si-python-grpc-client:$version
docker push swir/swir-example-aws-pubsub-configurator:$version
docker push swir/swir-example-aws-si-configurator:$version
