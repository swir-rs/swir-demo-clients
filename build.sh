#!/bin/bash
version=$1
grpc_dir=$2
echo "Version $1 $2"
root_dir=$(pwd)

cd swir-pubsub-python-processor
printf "\n**********************\n"
printf "\nSwir Pubsub python processor  \n"
cp $grpc_dir/grpc_api/*.proto .
docker build --tag swir/swir-example-pubsub-python-processor:$version .
rm *.proto
printf "\nSwir Pubsub python processor  done"
printf "\n**********************\n"
cd ../swir-pubsub-java-processor
printf "\n**********************\n"
printf "\nJava processor  \n"
docker build --tag swir/swir-example-pubsub-java-processor:$version .
printf "\nJava processor  done"
printf "\n**********************\n"
cd ../swir-pubsub-java-source
printf "\n**********************\n"
printf "\nJava GRPC source  \n"
cp -r $grpc_dir/grpc_api/ .
docker build --tag swir/swir-example-pubsub-java-source:$version .
rm -rf grpc_api
printf "\nJava GRPC source...done"
printf "\n**********************\n"
cd ../swir-pubsub-python-sink
printf "\n**********************\n"
printf "\nPython GRPC sink  \n"
cp $grpc_dir/grpc_api/*.proto .
docker build --tag swir/swir-example-pubsub-python-sink:$version .
rm *.proto
printf "Python GRPC sink... done  \n"
printf "\n**********************\n"

cd ../swir-si-http-server
printf "\n**********************\n"
printf "\nPython HTTP server  \n"
docker build --tag swir/swir-example-si-python-http-server:$version .
printf "\nPython HTTP server  done"
printf "\n**********************\n"

cd ../swir-si-grpc-client
printf "\n**********************\n"
printf "\nPython GRPC client  \n"
cp $grpc_dir/grpc_api/*.proto .
docker build --tag swir/swir-example-si-python-grpc-client:$version .
rm *.proto
printf "\nPython GRPC client ... done \n"
printf "\n**********************\n"


cd ../swir-pubsub-configurator
printf "\n**********************\n"
printf "\nConfigurator \n"
docker build --tag swir/swir-example-pubsub-configurator:$version .
printf "\nConfigurator... done"
printf "\n**********************\n"

cd ../swir-si-configurator
printf "\n**********************\n"
printf "\nConfigurator \n"
docker build --tag swir/swir-example-si-configurator:$version .
docker build --tag swir/swir-example-si-aws-configurator:$version .

cd ../swir-pubsub-aws-configurator
printf "\n**********************\n"
printf "\nConfigurator \n"
docker build --tag swir/swir-example-pubsub-aws-configurator:$version .
printf "\nConfigurator... done"
printf "\n**********************\n"

cd $root_dir

images=$(docker image list swir/swir-*$version | grep swir | wc -l)
if [[ $images -eq 10 ]]; then
    printf "All good. Expected 10 images... got $images\n"
else
    printf "Something went wrong. Expected 10 images... got $images\n"    
fi    

