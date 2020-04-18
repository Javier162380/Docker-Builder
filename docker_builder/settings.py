from .cli import cli
from .db import StorageFactory

params = cli()

db_object = StorageFactory.load_stro