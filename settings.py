from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
BASE_LOG_DIR = BASE_DIR / 'logs'


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'data': {
            'format': 'DATA:  %(asctime)s | %(message)s'
        },
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(asctime)s %(module)s -> %(message)s'
        },
    },
    'handlers': {
        'app': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': BASE_LOG_DIR/'app.log',
            'formatter': 'data'
        },
        'fastapi': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': BASE_LOG_DIR / 'fastapi.log',
            'formatter': 'simple'
        }
    },
    'loggers': {
        'app': {
            'handlers': ['app'],
            'level': 'INFO',
            'propagate': False,
        },
        'fastapi': {
            'handlers': ['fastapi'],
            'level': 'INFO',
            'propagate': False,
        }
    }
}


MONGODB_URL = "mongodb://mongo:27017/"
REDIS_URL = "redis://redis:6379/0"
REDIS_HOST = "redis"
DATABASE_NAME = "AdsCtr"
APP_COL = 'ads'
INIT_FILE_PATH = 'task-23-dataset.csv'

