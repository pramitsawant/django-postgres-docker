# Userful Docker Comands

### Running Management commands inside a docker container

#### Locate The Container

```sh
docker ps
```

#### Logging Into The Container

```sh
docker exec -it {container_id} bash
```

#### Running the command

```sh
cd folder
python manage.py makemigration
```
