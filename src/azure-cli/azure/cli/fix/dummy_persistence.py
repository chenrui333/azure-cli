import json
import sys

from knack.log import get_logger
from azure.cli.core.decorators import retry

logger = get_logger(__name__)

# Files extensions for encrypted and plaintext persistence
file_extensions = {True: '.bin', False: '.json'}

print('import dummy persistance')

class Dummy:
    def __int__(self):
        print('in dummy persistence')


for i in ['FilePersistenceWithDataProtection', 'KeychainPersistence', 'LibsecretPersistence',
          'FilePersistence', 'PersistedTokenCache', 'CrossPlatLock', 'PersistenceNotFound']:
    globals()[i] = Dummy


class FilePersistenceWithDataProtection:
    pass


def load_persisted_token_cache(location, encrypt):
    pass


def load_secret_store(location, encrypt):
    pass


def build_persistence(location, encrypt):
    """Build a suitable persistence instance based your current OS"""
    pass


class SecretStore:
    def __init__(self, persistence):
        self._lock_file = persistence.get_location() + ".lockfile"
        self._persistence = persistence

    def save(self, content):
        pass

    @retry()
    def load(self):
        pass


def dummy():
    print('dummy')