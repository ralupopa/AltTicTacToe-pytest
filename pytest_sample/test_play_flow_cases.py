from alttester import AltDriver
from page.helpermethods import HelperMethods
import pytest

class TestPlay:

    altdriver = AltDriver()

    def setup_method(self):
        self.helper_methods = HelperMethods(self.altdriver)

    @pytest.fixture(autouse=True)
    def before_and_after_test(self):
        self.altdriver.load_scene("StartScene",True)

        play = self.helper_methods.play_button
        assert play is not None
        play.click()

    @pytest.mark.parametrize("flow, msg",
        [(["1", "5", "9", "3", "7", "8", "4"], "Player X wins!"),
        (["8", "5", "9", "7", "3", "6", "4", "1", "2"], "It's a draw!"),
        (["9", "7", "5", "1", "6", "4"], "Player O wins!")])
    def test_flow_cases(self, flow, msg):
        self.helper_methods.flow_slots_played(flow)

        self.helper_methods.assert_win_info(msg)