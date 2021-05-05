from test import tests
from nose.tools import assert_equal, nottest

#@nottest
class TestVbanOutStream:
    def test_it_sets_and_gets_vban_outstream0_on(self):
        tests.vban_out[0].enable = True
        assert_equal(tests.vban_out[0].enable, True)

    def test_it_sets_and_gets_vban_outstream1_on(self):
        tests.vban_out[1].enable = True
        assert_equal(tests.vban_out[1].enable, True)

    def test_it_sets_and_gets_vban_outstream2_on(self):
        tests.vban_out[2].enable = True
        assert_equal(tests.vban_out[2].enable, True)

    def test_it_sets_and_gets_vban_outstream0_off(self):
        tests.vban_out[0].enable = False
        assert_equal(tests.vban_out[0].enable, False)

    def test_it_sets_and_gets_vban_outstream1_off(self):
        tests.vban_out[1].enable = False
        assert_equal(tests.vban_out[1].enable, False)

    def test_it_sets_and_gets_vban_outstream2_off(self):
        tests.vban_out[2].enable = False
        assert_equal(tests.vban_out[2].enable, False)

#@nottest
class TestVbanInStream:
    def test_it_sets_and_gets_vban_instream0_on(self):
        tests.vban_in[0].enable = True
        assert_equal(tests.vban_in[0].enable, True)

    def test_it_sets_and_gets_vban_instream1_on(self):
        tests.vban_in[1].enable = True
        assert_equal(tests.vban_in[1].enable, True)

    def test_it_sets_and_gets_vban_instream2_on(self):
        tests.vban_in[2].enable = True
        assert_equal(tests.vban_in[2].enable, True)

    def test_it_sets_and_gets_vban_instream0_off(self):
        tests.vban_in[0].enable = False
        assert_equal(tests.vban_in[0].enable, False)

    def test_it_sets_and_gets_vban_instream1_off(self):
        tests.vban_in[1].enable = False
        assert_equal(tests.vban_in[1].enable, False)

    def test_it_sets_and_gets_vban_instream2_off(self):
        tests.vban_in[2].enable = False
        assert_equal(tests.vban_in[2].enable, False)