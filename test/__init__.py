import voicemeeter

DELAY = 0.001
MAX_POLLS = 5

tests = voicemeeter.remote('banana', delay=DELAY, max_polls=MAX_POLLS)

def setup_package():
    tests.login()

def teardown_package():
    tests.logout()
