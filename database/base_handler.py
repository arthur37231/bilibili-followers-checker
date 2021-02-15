from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .schema import Base


class BaseHandler(object):

    _Session = None

    @staticmethod
    def _make_connection_url(**kwargs):
        host = kwargs.get('host')
        port = kwargs.get('port')
        user = kwargs.get('user')
        dbname = kwargs.get('db_name')
        password = kwargs.get('db_password')

        return f'postgresql://{user}:{password}@{host}:{port}/{dbname}'

    @staticmethod
    def create_connection(conf):
        _engine = create_engine(BaseHandler._make_connection_url(**conf))
        BaseHandler._Session = sessionmaker(bind=_engine)

        # Define table
        Base.metadata.create_all(bind=_engine)

    def __init__(self, *args, **kwargs):
        self._session = None

    def update_obj(self, obj):
        self._session.add(obj)

    def __enter__(self):
        self.connect()

    def __exit__(self, exception_type, exception_value, traceback):
        self.disconnect()

    def connect(self):
        self._session = BaseHandler._Session()

    def disconnect(self, is_error=False):
        if self._session is not None:
            if not is_error:
                self._session.commit()
            self._session.close()
            self._session = None

    def commit(self):
        self._session.commit()
