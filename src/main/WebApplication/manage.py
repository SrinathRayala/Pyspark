import docker
client=docker.from_env(environment={'DOCKER_HOST':'tcp://35.232.216.36:3306'})
print(client)
client.info()
#client.containers.list()
    #from_env('tcp://35.232.216.36:3306')
#client.containers.
#clnt=dc.Client.from_env(environment={'DOCKER_HOST':'tcp://35.232.216.36:3306'})
   # from_env(environment={'DOCKER_HOST':'tcp://35.232.216.36:3306'})
#client=docker.from_env(environment={'DOCKER_HOST':'tcp://35.232.216.36:3306'})