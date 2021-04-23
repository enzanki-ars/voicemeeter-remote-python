from test import tests
from nose.tools import assert_equal, nottest

#@nottest
class TestMacroButtons:
    """ Tests for state mode (run mb scripts as well) """
    def test_it_sets_macrobutton0_state_on(self):
        tests.button_setstatus(0, 1, 1)
        assert_equal(tests.button_getstatus(0, 1), 1)

    def test_it_sets_macrobutton0_state_off(self):
        tests.button_setstatus(0, 0, 1)
        assert_equal(tests.button_getstatus(0, 1), 0)

    def test_it_sets_macrobutton1_state_on(self):
        tests.button_setstatus(1, 1, 1)
        assert_equal(tests.button_getstatus(1, 1), 1)

    def test_it_sets_macrobutton1_state_off(self):
        tests.button_setstatus(1, 0, 1)
        assert_equal(tests.button_getstatus(1, 1), 0)

    def test_it_sets_macrobutton2_state_on(self):
        tests.button_setstatus(2, 1, 1)
        assert_equal(tests.button_getstatus(2, 1), 1)

    def test_it_sets_macrobutton2_state_off(self):
        tests.button_setstatus(2, 0, 1)
        assert_equal(tests.button_getstatus(2, 1), 0)

    """ Tests for state only mode (don't run mb scripts) """
    def test_it_sets_macrobutton0_stateonly_on(self):
        tests.button_setstatus(0, 1, 2)
        assert_equal(tests.button_getstatus(0, 2), 1)

    def test_it_sets_macrobutton0_stateonly_off(self):
        tests.button_setstatus(0, 0, 2)
        assert_equal(tests.button_getstatus(0, 2), 0)
  
    def test_it_sets_macrobutton1_stateonly_on(self):
        tests.button_setstatus(1, 1, 2)
        assert_equal(tests.button_getstatus(1, 2), 1)

    def test_it_sets_macrobutton1_stateonly_off(self):
        tests.button_setstatus(1, 0, 2)
        assert_equal(tests.button_getstatus(1, 2), 0)
 
    def test_it_sets_macrobutton2_stateonly_on(self):
        tests.button_setstatus(2, 1, 2)
        assert_equal(tests.button_getstatus(2, 2), 1)

    def test_it_sets_macrobutton2_stateonly_off(self):
        tests.button_setstatus(2, 0, 2)
        assert_equal(tests.button_getstatus(2, 2), 0)

    """ Tests for trigger mode """
    def test_it_sets_macrobutton0_trigger_on(self):
        tests.button_setstatus(0, 1, 3)
        assert_equal(tests.button_getstatus(0, 3), 1)

    def test_it_sets_macrobutton0_trigger_off(self):
        tests.button_setstatus(0, 0, 3)
        assert_equal(tests.button_getstatus(0, 3), 0)

    def test_it_sets_macrobutton1_trigger_on(self):
        tests.button_setstatus(1, 1, 3)
        assert_equal(tests.button_getstatus(1, 3), 1)

    def test_it_sets_macrobutton1_trigger_off(self):
        tests.button_setstatus(1, 0, 3)
        assert_equal(tests.button_getstatus(1, 3), 0)

    def test_it_sets_macrobutton2_trigger_on(self):
        tests.button_setstatus(2, 1, 3)
        assert_equal(tests.button_getstatus(2, 3), 1)

    def test_it_sets_macrobutton2_trigger_off(self):
        tests.button_setstatus(2, 0, 3)
        assert_equal(tests.button_getstatus(2, 3), 0)

#@nottest
class TestMacroButtonsWithAlias:
    """ Test alias functions """
    def test_it_sets_macrobutton0_state_on_with_alias(self):
        tests.button[0].state = True
        assert_equal(tests.button[0].state, True)  

    def test_it_sets_macrobutton0_stateonly_on_with_alias(self):
        tests.button[0].stateonly
        assert_equal(tests.button[0].stateonly, True)

    def test_it_sets_macrobutton0_trigger_on_with_alias(self):
        tests.button[0].trigger = True
        assert_equal(tests.button[0].trigger, True)

    def test_it_sets_macrobutton0_state_off_with_alias(self):
        tests.button[0].state = False
        assert_equal(tests.button[0].state, False) 

    def test_it_sets_macrobutton0_stateonly_off_with_alias(self):
        tests.button[0].stateonly = False
        assert_equal(tests.button[0].stateonly, False)   

    def test_it_sets_macrobutton0_trigger_off_with_alias(self):
        tests.button[0].trigger = False
        assert_equal(tests.button[0].trigger, False)
