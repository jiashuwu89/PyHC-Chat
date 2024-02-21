# pyhc_bots.py
from .helper_bot import HelperBot

class PyspedasBot(HelperBot):
    REPO_NAME = "pyspedas"
    REPO_URL = "https://github.com/spedas/pyspedas.git"
    SUFFIXES = [".py", ".md"]
    def __init__(self, use_local_vector_store=True):
        super().__init__(PyspedasBot.REPO_NAME, PyspedasBot.REPO_URL, PyspedasBot.SUFFIXES, use_local_vector_store)


class PyspedasExampleBot(HelperBot):
    REPO_NAME = "pyspedas_examples"
    REPO_URL = "https://github.com/spedas/pyspedas_examples.git"
    SUFFIXES = [".py", ".md", ".ipynb"]
    def __init__(self, use_local_vector_store=True):
        super().__init__(PyspedasExampleBot.REPO_NAME, PyspedasExampleBot.REPO_URL, PyspedasExampleBot.SUFFIXES, use_local_vector_store)


class THEMISExampleBot(HelperBot):
    REPO_NAME = "themis-examples"
    REPO_URL = "https://github.com/spedas/themis-examples.git"
    SUFFIXES = [".py", ".md", ".ipynb"]
    def __init__(self, use_local_vector_store=True):
        super().__init__(THEMISExampleBot.REPO_NAME, THEMISExampleBot.REPO_URL, THEMISExampleBot.SUFFIXES, use_local_vector_store)


class MMSExampleBot(HelperBot):
    REPO_NAME = "mms-examples"
    REPO_URL = "https://github.com/spedas/mms-examples.git"
    SUFFIXES = [".py", ".md", ".ipynb"]
    def __init__(self, use_local_vector_store=True):
        super().__init__(MMSExampleBot.REPO_NAME, MMSExampleBot.REPO_URL, MMSExampleBot.SUFFIXES, use_local_vector_store)
