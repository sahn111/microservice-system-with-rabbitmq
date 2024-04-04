from sqlalchemy.ext.automap import automap_base

from .db_config import sqlalchemy_engine

Base = automap_base()

Base.prepare(autoload_with=sqlalchemy_engine)

Device = Base.classes.device
Location = Base.classes.location