#! /bin/bash

if [ "$1" == "build" ];
then
docker build -t fizz-buzz . ;
docker tag fizz-buzz registry.heroku.com/rest-fizz-buzz/web ;
docker push registry.heroku.com/rest-fizz-buzz/web ;
fi;

IMAGE_ID=$(docker inspect registry.heroku.com/rest-fizz-buzz/web --format={{.Id}})

curl -n -X PATCH https://api.heroku.com/apps/rest-fizz-buzz/formation \
  -d '{
  "updates": [
    {
      "type": "web",
      "docker_image": "'$IMAGE_ID'"
    }
  ]
}' \
  -H "Content-Type: application/json" \
  -H "Accept: application/vnd.heroku+json; version=3.docker-releases"
