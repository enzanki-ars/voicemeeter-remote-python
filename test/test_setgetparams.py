from test import tests
from nose.tools import assert_equal, nottest

#@nottest
class TestSetAndGetParamsFloat:
    """ Tests for state mode (run mb scripts as well) """
    def test_it_sets_and_gets_strip0_mute_on(self):
        tests.set('Strip[0].Mute', 1)
        assert_equal(tests.get('Strip[0].Mute'), 1.0)

    def test_it_sets_and_gets_strip1_mute_on(self):
        tests.set('Strip[1].Mute', 1)
        assert_equal(tests.get('Strip[1].Mute'), 1.0)

    def test_it_sets_and_gets_strip2_mute_on(self):
        tests.set('Strip[2].Mute', 1)
        assert_equal(tests.get('Strip[2].Mute'), 1.0)

    def test_it_sets_and_gets_strip0_mute_off(self):
        tests.set('Strip[0].Mute', 0)
        assert_equal(tests.get('Strip[0].Mute'), 0.0)

    def test_it_sets_and_gets_strip1_mute_off(self):
        tests.set('Strip[1].Mute', 0)
        assert_equal(tests.get('Strip[1].Mute'), 0.0)

    def test_it_sets_and_gets_strip2_mute_off(self):
        tests.set('Strip[2].Mute', 0)
        assert_equal(tests.get('Strip[2].Mute'), 0.0)


@nottest
class TestSetAndGetParamsFloatLoop:
    def test_it_gets_strip0_mute_on(self):
        tests.set('Strip[0].Mute', 1)
        for i in range(10):
            assert_equal(tests.get('Strip[0].Mute'), 1.0)

    def test_it_gets_strip0_mute_off(self):
        tests.set('Strip[0].Mute', 0)
        for i in range(10):
            assert_equal(tests.get('Strip[0].Mute'), 0.0)

#@nottest
class TestSetAndGetParamsFloatWithAlias:
    def test_it_sets_and_gets_input0_A1_on(self):
        tests.strip[0].A1 = True
        assert_equal(tests.strip[0].A1, True)

    def test_it_sets_and_gets_input0_A2_on(self):
        tests.strip[0].A2 = True
        assert_equal(tests.strip[0].A2, True)

    def test_it_sets_and_gets_input0_A3_on(self):
        tests.strip[0].A3 = True
        assert_equal(tests.strip[0].A3, True)

    def test_it_sets_and_gets_input1_A1_on(self):
        tests.strip[1].A1 = True
        assert_equal(tests.strip[1].A1, True)

    def test_it_sets_and_gets_input1_A2_on(self):
        tests.strip[1].A2 = True
        assert_equal(tests.strip[1].A2, True)

    def test_it_sets_and_gets_input1_A3_on(self):
        tests.strip[1].A3 = True
        assert_equal(tests.strip[1].A3, True)

    def test_it_sets_and_gets_input2_A1_on(self):
        tests.strip[2].A1 = True
        assert_equal(tests.strip[2].A1, True)

    def test_it_sets_and_gets_input2_A2_on(self):
        tests.strip[2].A2 = True
        assert_equal(tests.strip[2].A2, True)

    def test_it_sets_and_gets_input2_A3_on(self):
        tests.strip[2].A3 = True
        assert_equal(tests.strip[2].A3, True)

    def test_it_sets_and_gets_output1_gain_on(self):
        tests.bus[0].gain = 1.0
        assert_equal(tests.bus[0].gain, 1.0)

    def test_it_sets_and_gets_output2_mono_on(self):
        tests.bus[2].mono = True
        assert_equal(tests.bus[2].mono, True)

    def test_it_sets_and_gets_input0_A1_off(self):
        tests.strip[0].A1 = False
        assert_equal(tests.strip[0].A1, False)

    def test_it_sets_and_gets_input0_A2_off(self):
        tests.strip[0].A2 = False
        assert_equal(tests.strip[0].A2, False)

    def test_it_sets_and_gets_input0_A3_off(self):
        tests.strip[0].A3 = False
        assert_equal(tests.strip[0].A3, False)

    def test_it_sets_and_gets_strip1_A1_off(self):
        tests.strip[1].A1 = False
        assert_equal(tests.strip[1].A1, False)

    def test_it_sets_and_gets_input1_A2_off(self):
        tests.strip[1].A2 = False
        assert_equal(tests.strip[1].A2, False)

    def test_it_sets_and_gets_input1_A3_off(self):
        tests.strip[1].A3 = False
        assert_equal(tests.strip[1].A3, False)

    def test_it_sets_and_gets_input2_A1_off(self):
        tests.strip[2].A1 = False
        assert_equal(tests.strip[2].A1, False)

    def test_it_sets_and_gets_input2_A2_off(self):
        tests.strip[2].A2 = False
        assert_equal(tests.strip[2].A2, False)

    def test_it_sets_and_gets_input2_A3_off(self):
        tests.strip[2].A3 = False
        assert_equal(tests.strip[2].A3, False)


    def test_it_sets_and_gets_output0_mute_on(self):
        tests.bus[0].mute = True
        assert_equal(tests.bus[0].mute, True)

    def test_it_sets_and_gets_output1_mute_on(self):
        tests.bus[1].mute = True
        assert_equal(tests.bus[1].mute, True)

    def test_it_sets_and_gets_output2_mute_on(self):
        tests.bus[2].mute = True
        assert_equal(tests.bus[2].mute, True)

    def test_it_sets_and_gets_output3_mute_on(self):
        tests.bus[3].mute = True
        assert_equal(tests.bus[3].mute, True)

    def test_it_sets_and_gets_output4_mute_on(self):
        tests.bus[4].mute = True
        assert_equal(tests.bus[4].mute, True)

    def test_it_sets_and_gets_output0_mute_off(self):
        tests.bus[0].mute = False
        assert_equal(tests.bus[0].mute, False)

    def test_it_sets_and_gets_output1_mute_off(self):
        tests.bus[1].mute = False
        assert_equal(tests.bus[1].mute, False)

    def test_it_sets_and_gets_output2_mute_off(self):
        tests.bus[2].mute = False
        assert_equal(tests.bus[2].mute, False)

    def test_it_sets_and_gets_output3_mute_off(self):
        tests.bus[3].mute = False
        assert_equal(tests.bus[3].mute, False)

    def test_it_sets_and_gets_output4_mute_off(self):
        tests.bus[4].mute = False
        assert_equal(tests.bus[4].mute, False)

    def test_it_sets_and_gets_output0_mono_on(self):
        tests.bus[0].mono = True
        assert_equal(tests.bus[0].mono, True)

    def test_it_sets_and_gets_output1_mono_on(self):
        tests.bus[1].mono = True
        assert_equal(tests.bus[1].mono, True)

    def test_it_sets_and_gets_output2_mono_on(self):
        tests.bus[2].mono = True
        assert_equal(tests.bus[2].mono, True)

    def test_it_sets_and_gets_output3_mono_on(self):
        tests.bus[3].mono = True
        assert_equal(tests.bus[3].mono, True)

    def test_it_sets_and_gets_output4_mono_on(self):
        tests.bus[4].mono = True
        assert_equal(tests.bus[4].mono, True)

    def test_it_sets_and_gets_output0_mono_off(self):
        tests.bus[0].mono = False
        assert_equal(tests.bus[0].mono, False)

    def test_it_sets_and_gets_output1_mono_off(self):
        tests.bus[1].mono = False
        assert_equal(tests.bus[1].mono, False)

    def test_it_sets_and_gets_output2_mono_off(self):
        tests.bus[2].mono = False
        assert_equal(tests.bus[2].mono, False)

    def test_it_sets_and_gets_output3_mono_off(self):
        tests.bus[3].mono = False
        assert_equal(tests.bus[3].mono, False)

    def test_it_sets_and_gets_output4_mono_off(self):
        tests.bus[4].mono = False
        assert_equal(tests.bus[4].mono, False)


    def test_it_sets_and_gets_output0_eq_on(self):
        tests.bus[0].eq = True
        assert_equal(tests.bus[0].eq, True)

    def test_it_sets_and_gets_output1_eq_on(self):
        tests.bus[1].eq = True
        assert_equal(tests.bus[1].eq, True)

    def test_it_sets_and_gets_output2_eq_on(self):
        tests.bus[2].eq = True
        assert_equal(tests.bus[2].eq, True)

    def test_it_sets_and_gets_output3_eq_on(self):
        tests.bus[3].eq = True
        assert_equal(tests.bus[3].eq, True)

    def test_it_sets_and_gets_output4_eq_on(self):
        tests.bus[4].eq = True
        assert_equal(tests.bus[4].eq, True)

    def test_it_sets_and_gets_output0_eq_off(self):
        tests.bus[0].eq = False
        assert_equal(tests.bus[0].eq, False)

    def test_it_sets_and_gets_output1_eq_off(self):
        tests.bus[1].eq = False
        assert_equal(tests.bus[1].eq, False)

    def test_it_sets_and_gets_output2_eq_off(self):
        tests.bus[2].eq = False
        assert_equal(tests.bus[2].eq, False)

    def test_it_sets_and_gets_output3_eq_off(self):
        tests.bus[3].eq = False
        assert_equal(tests.bus[3].eq, False)

    def test_it_sets_and_gets_output4_eq_off(self):
        tests.bus[4].eq = False
        assert_equal(tests.bus[4].eq, False)


    def test_it_sets_and_gets_output1_gain(self):
        tests.bus[0].gain = 0.0
        assert_equal(tests.bus[0].gain, 0.0)

    def test_it_sets_and_gets_output2_mono_off(self):
        tests.bus[2].mono = False
        assert_equal(tests.bus[2].mono, False)

#@nottest
class TestSetAndGetParamsString:
    """ Tests for state mode (run mb scripts as well) """
    def test_it_sets_and_gets_strip0_label_test0(self):
        tests.set('Strip[0].label', 'test0')
        assert_equal(tests.get('Strip[0].label', string=True), 'test0')

    def test_it_sets_and_gets_strip0_label_test1(self):
        tests.set('Strip[0].label', 'test1')
        assert_equal(tests.get('Strip[0].label', string=True), 'test1')

    def test_it_sets_and_gets_strip0_label_test2(self):
        tests.set('Strip[0].label', 'test2')
        assert_equal(tests.get('Strip[0].label', string=True), 'test2')

    def test_it_sets_and_gets_strip1_label_test0(self):
        tests.set('Strip[1].label', 'test0')
        assert_equal(tests.get('Strip[1].label', string=True), 'test0')

    def test_it_sets_and_gets_strip1_label_test1(self):
        tests.set('Strip[1].label', 'test1')
        assert_equal(tests.get('Strip[1].label', string=True), 'test1')

    def test_it_sets_and_gets_strip1_label_test2(self):
        tests.set('Strip[1].label', 'test2')
        assert_equal(tests.get('Strip[1].label', string=True), 'test2')

    def test_it_sets_and_gets_strip2_label_test0(self):
        tests.set('Strip[2].label', 'test0')
        assert_equal(tests.get('Strip[2].label', string=True), 'test0')

    def test_it_sets_and_gets_strip2_label_test1(self):
        tests.set('Strip[2].label', 'test1')
        assert_equal(tests.get('Strip[2].label', string=True), 'test1')

    def test_it_sets_and_gets_strip2_label_test2(self):
        tests.set('Strip[2].label', 'test2')
        assert_equal(tests.get('Strip[2].label', string=True), 'test2')
