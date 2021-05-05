from test import tests
from nose.tools import assert_equal, nottest

#@nottest
class TestRecorderOutChannel:
    def test_it_sets_and_gets_recorder_A1_on(self):
        tests.recorder.A1 = True
        assert_equal(tests.recorder.A1, True)

    def test_it_sets_and_gets_recorder_A2_on(self):
        tests.recorder.A2 = True
        assert_equal(tests.recorder.A2, True)

    def test_it_sets_and_gets_recorder_A3_on(self):
        tests.recorder.A3 = True
        assert_equal(tests.recorder.A3, True)

    def test_it_sets_and_gets_recorder_A1_off(self):
        tests.recorder.A1 = False
        assert_equal(tests.recorder.A1, False)

    def test_it_sets_and_gets_recorder_A2_off(self):
        tests.recorder.A2 = False
        assert_equal(tests.recorder.A2, False)

    def test_it_sets_and_gets_recorder_A3_off(self):
        tests.recorder.A3 = False
        assert_equal(tests.recorder.A3, False)

    def test_it_sets_and_gets_recorder_B1_on(self):
        tests.recorder.B1 = True
        assert_equal(tests.recorder.B1, True)

    def test_it_sets_and_gets_recorder_B2_on(self):
        tests.recorder.B2 = True
        assert_equal(tests.recorder.B2, True)

    def test_it_sets_and_gets_recorder_B1_off(self):
        tests.recorder.B1 = False
        assert_equal(tests.recorder.B1, False)

    def test_it_sets_and_gets_recorder_B2_off(self):
        tests.recorder.B2 = False
        assert_equal(tests.recorder.B2, False)
