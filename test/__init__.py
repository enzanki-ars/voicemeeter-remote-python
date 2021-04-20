import voicemeeter

DELAY = 0.001
MDELAY = 0.005
MAX_POLLS = 9

tests = voicemeeter.remote('banana', delay=DELAY, mdelay=MDELAY, max_polls=MAX_POLLS)

def setup_package():
    tests._login()

def teardown_package():
    tests._logout()
