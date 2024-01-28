# CTR Backend

CTR Backend with Fastapi

Serve Estimated CTRs of Machine Learning model

use redis and celery for caching system. mongodb for database

# Instalation
```bash
docker compose build
docker compose up -d
```

## Usage
fisrt server start init_mongo.py for create schema of mongodb database

then start test.py for pass unit test

then start init.sh script bash for run project 

when fastapi project run celery app start beat and worker for update cache system every 1 minute in redis and in /predict endpoint first check redis for find data if not exist in cache check mongodb and get data

app use middleware for prepare /stats endpoint data
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
