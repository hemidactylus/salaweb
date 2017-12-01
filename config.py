import os

# directories and so on
basedir = os.path.abspath(os.path.dirname(__file__))

# stuff for Flask
WTF_CSRF_ENABLED = True
from sensible_config import SECRET_KEY

from sensible_config import CONTENTS_DESCRIPTOR_DIRECTORY
from sensible_config import SERVABLE_DIRECTORIES_LOCATION

# database location
DB_NAME='salaweb.db'
dbFullName=os.path.join(basedir,'app','database',DB_NAME)
