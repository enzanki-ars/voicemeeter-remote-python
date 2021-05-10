from test import tests
from nose.tools import assert_equal, nottest

#@nottest
class TestVbanOutStreamOn:
    def test_it_sets_and_gets_vban_outstream0_on(self):
        tests.vban_out[0].on = True
        assert_equal(tests.vban_out[0].on, True)

    def test_it_sets_and_gets_vban_outstream1_on(self):
        tests.vban_out[1].on = True
        assert_equal(tests.vban_out[1].on, True)

    def test_it_sets_and_gets_vban_outstream2_on(self):
        tests.vban_out[2].on = True
        assert_equal(tests.vban_out[2].on, True)

    def test_it_sets_and_gets_vban_outstream0_off(self):
        tests.vban_out[0].on = False
        assert_equal(tests.vban_out[0].on, False)

    def test_it_sets_and_gets_vban_outstream1_off(self):
        tests.vban_out[1].on = False
        assert_equal(tests.vban_out[1].on, False)

    def test_it_sets_and_gets_vban_outstream2_off(self):
        tests.vban_out[2].on = False
        assert_equal(tests.vban_out[2].on, False)

#@nottest
class TestVbanInStreamOn:
    def test_it_sets_and_gets_vban_instream0_on(self):
        tests.vban_in[0].on = True
        assert_equal(tests.vban_in[0].on, True)

    def test_it_sets_and_gets_vban_instream1_on(self):
        tests.vban_in[1].on = True
        assert_equal(tests.vban_in[1].on, True)

    def test_it_sets_and_gets_vban_instream2_on(self):
        tests.vban_in[2].on = True
        assert_equal(tests.vban_in[2].on, True)

    def test_it_sets_and_gets_vban_instream0_off(self):
        tests.vban_in[0].on = False
        assert_equal(tests.vban_in[0].on, False)

    def test_it_sets_and_gets_vban_instream1_off(self):
        tests.vban_in[1].on = False
        assert_equal(tests.vban_in[1].on, False)

    def test_it_sets_and_gets_vban_instream2_off(self):
        tests.vban_in[2].on = False
        assert_equal(tests.vban_in[2].on, False)

#@nottest
class TestVbanStringParams:
    def test_it_sets_and_gets_vban_instream0_name_test(self):
        tests.vban_in[0].name = 'test'
        assert_equal(tests.vban_in[0].name, 'test')

    def test_it_sets_and_gets_vban_instream0_name_stream1(self):
        tests.vban_in[0].name = 'Stream1'
        assert_equal(tests.vban_in[0].name, 'Stream1')

    def test_it_sets_and_gets_vban_instream1_name_test(self):
        tests.vban_in[1].name = 'test'
        assert_equal(tests.vban_in[1].name, 'test')

    def test_it_sets_and_gets_vban_instream1_name(self):
        tests.vban_in[1].name = 'Stream2'
        assert_equal(tests.vban_in[1].name, 'Stream2')

    def test_it_sets_and_gets_vban_instream2_name_test(self):
        tests.vban_in[2].name = 'test'
        assert_equal(tests.vban_in[2].name, 'test')

    def test_it_sets_and_gets_vban_instream2_name(self):
        tests.vban_in[2].name = 'Stream3'
        assert_equal(tests.vban_in[2].name, 'Stream3')

    def test_it_sets_and_gets_vban_outstream0_name_test(self):
        tests.vban_out[0].name = 'test'
        assert_equal(tests.vban_out[0].name, 'test')

    def test_it_sets_and_gets_vban_outstream0_name_stream1(self):
        tests.vban_out[0].name = 'Stream1'
        assert_equal(tests.vban_out[0].name, 'Stream1')

    def test_it_sets_and_gets_vban_outstream1_name_test(self):
        tests.vban_out[1].name = 'test'
        assert_equal(tests.vban_out[1].name, 'test')

    def test_it_sets_and_gets_vban_outstream1_name(self):
        tests.vban_out[1].name = 'Stream2'
        assert_equal(tests.vban_out[1].name, 'Stream2')

    def test_it_sets_and_gets_vban_outstream2_name_test(self):
        tests.vban_out[2].name = 'test'
        assert_equal(tests.vban_out[2].name, 'test')

    def test_it_sets_and_gets_vban_outstream2_name(self):
        tests.vban_out[2].name = 'Stream3'
        assert_equal(tests.vban_out[2].name, 'Stream3')


    def test_it_sets_and_gets_vban_instream0_ip(self):
        tests.vban_in[0].ip = '0.0.0.0'
        assert_equal(tests.vban_in[0].ip, '0.0.0.0')

    def test_it_sets_and_gets_vban_instream1_ip(self):
        tests.vban_in[1].ip = '127.0.0.1'
        assert_equal(tests.vban_in[1].ip, '127.0.0.1')

#@nottest
class TestVbanIntParams:
    """ 
    sample rate 
    Warning, assumes a default 48000 value since it is readonly for instreams. 
    If this was changed before tests were run they WILL fail.
    """
    def test_it_gets_vban_instream0_sr(self):
        assert_equal(tests.vban_in[0].sr, 48000)

    def test_it_gets_vban_instream1_sr(self):
        assert_equal(tests.vban_in[1].sr, 48000)

    def test_it_gets_vban_instream2_sr(self):
        assert_equal(tests.vban_in[2].sr, 48000)

    def test_it_sets_and_gets_vban_outstream0_sr_44100(self):
        tests.vban_out[0].sr = 44100
        assert_equal(tests.vban_out[0].sr, 44100)

    def test_it_sets_and_gets_vban_outstream0_sr_48000(self):
        tests.vban_out[0].sr = 48000
        assert_equal(tests.vban_out[0].sr, 48000)

    def test_it_sets_and_gets_vban_outstream1_sr_48000(self):
        tests.vban_out[1].sr = 48000
        assert_equal(tests.vban_out[1].sr, 48000)

    def test_it_sets_and_gets_vban_outstream1_sr_16000(self):
        tests.vban_out[1].sr = 16000
        assert_equal(tests.vban_out[1].sr, 16000)

    def test_it_sets_and_gets_vban_outstream2_sr_48000(self):
        tests.vban_out[2].sr = 48000
        assert_equal(tests.vban_out[2].sr, 48000)

    def test_it_sets_and_gets_vban_outstream2_sr_96000(self):
        tests.vban_out[2].sr = 96000
        assert_equal(tests.vban_out[2].sr, 96000)


    """ 
    channel
    Warning, assumes a default 2 value since it is readonly for instreams. 
    If this was changed before tests were run they WILL fail.
    """
    def test_it_gets_vban_instream0_channel(self):
        assert_equal(tests.vban_in[0].channel, 2)

    def test_it_gets_vban_instream1_channel(self):
        assert_equal(tests.vban_in[1].channel, 2)

    def test_it_gets_vban_instream2_channel(self):
        assert_equal(tests.vban_in[2].channel, 2)

    def test_it_sets_and_gets_vban_outstream0_channel(self):
        tests.vban_out[0].channel = 1
        assert_equal(tests.vban_out[0].channel, 1)

    def test_it_sets_and_gets_vban_outstream0_channel(self):
        tests.vban_out[0].channel = 2
        assert_equal(tests.vban_out[0].channel, 2)

    def test_it_sets_and_gets_vban_outstream1_channel(self):
        tests.vban_out[1].channel = 1
        assert_equal(tests.vban_out[1].channel, 1)

    def test_it_sets_and_gets_vban_outstream1_channel(self):
        tests.vban_out[1].channel = 2
        assert_equal(tests.vban_out[1].channel, 2)

    def test_it_sets_and_gets_vban_outstream2_channel(self):
        tests.vban_out[2].channel = 1
        assert_equal(tests.vban_out[2].channel, 1)

    def test_it_sets_and_gets_vban_outstream2_channel(self):
        tests.vban_out[2].channel = 2
        assert_equal(tests.vban_out[2].channel, 2)

    """ 
    bit
    Warning, assumes a default 16 value since it is readonly for instreams. 
    If this was changed before tests were run they WILL fail.
    """
    def test_it_gets_vban_instream0_bit(self):
        assert_equal(tests.vban_in[0].bit, 16)

    def test_it_gets_vban_instream1_bit(self):
        assert_equal(tests.vban_in[1].bit, 16)

    def test_it_gets_vban_instream2_bit(self):
        assert_equal(tests.vban_in[2].bit, 16)

    def test_it_sets_and_gets_vban_outstream0_bit_16(self):
        tests.vban_out[0].bit = 16
        assert_equal(tests.vban_out[0].bit, 16)

    def test_it_sets_and_gets_vban_outstream0_bit_24(self):
        tests.vban_out[0].bit = 24
        assert_equal(tests.vban_out[0].bit, 24)

    def test_it_sets_and_gets_vban_outstream1_bit_16(self):
        tests.vban_out[1].bit = 16
        assert_equal(tests.vban_out[1].bit, 16)

    def test_it_sets_and_gets_vban_outstream1_bit_24(self):
        tests.vban_out[1].bit = 24
        assert_equal(tests.vban_out[1].bit, 24)

    def test_it_sets_and_gets_vban_outstream2_bit_16(self):
        tests.vban_out[2].bit = 16
        assert_equal(tests.vban_out[2].bit, 16)

    def test_it_sets_and_gets_vban_outstream2_bit_24(self):
        tests.vban_out[2].bit = 24
        assert_equal(tests.vban_out[2].bit, 24)


    def test_it_sets_and_gets_vban_instream0_route_0(self):
        tests.vban_in[0].route = 0
        assert_equal(tests.vban_in[0].route, 0)

    def test_it_sets_and_gets_vban_instream0_route_1(self):
        tests.vban_in[0].route = 1
        assert_equal(tests.vban_in[0].route, 1)

    def test_it_sets_and_gets_vban_instream1_route_3(self):
        tests.vban_in[1].route = 3
        assert_equal(tests.vban_in[1].route, 3)

    def test_it_sets_and_gets_vban_instream1_route_5(self):
        tests.vban_in[1].route = 5
        assert_equal(tests.vban_in[1].route, 5)

    def test_it_sets_and_gets_vban_outstream0_route_0(self):
        tests.vban_out[0].route = 0
        assert_equal(tests.vban_out[0].route, 0)

    def test_it_sets_and_gets_vban_outstream0_route_1(self):
        tests.vban_out[0].route = 1
        assert_equal(tests.vban_out[0].route, 1)

    def test_it_sets_and_gets_vban_outstream1_route_2(self):
        tests.vban_out[1].route = 2
        assert_equal(tests.vban_out[1].route, 2)

    def test_it_sets_and_gets_vban_outstream1_route_5(self):
        tests.vban_out[1].route = 5
        assert_equal(tests.vban_out[1].route, 5)
