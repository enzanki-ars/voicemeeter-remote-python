import voicemeeter

DELAY = 0.005
MAX_POLLS = 8

kind = 'banana'

voicemeeter.launch(kind)

tests = voicemeeter.remote(kind, delay=DELAY, max_polls=MAX_POLLS)

def setup_package():
    tests.login()

def teardown_package():
    tests.logout()
