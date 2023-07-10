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

    @pytest.mark.parametrize("flow",
        [["1", "5", "9", "3", "7", "8", "4"],
        ["8", "2", "1", "5", "7", "9", "4"],
        ["5", "2", "7", "3", "1", "6", "4"],
        ["5", "4", "9", "2", "1"]])
    def test_player_X_wins(self, flow):
        self.helper_methods.flow_slots_played(flow)
        self.helper_methods.assert_win_info("Player X wins!")

    @pytest.mark.parametrize("flow",
        [["8", "5", "9", "7", "3", "6", "4", "1", "2"],
        ["9", "5", "2", "7", "3", "6", "4", "1", "8"],
        ["4", "5", "9", "2", "8", "7", "3", "6", "1"]])
    def test_draw_result(self, flow):
        self.helper_methods.flow_slots_played(flow)
        self.helper_methods.assert_win_info("It's a draw!")

    @pytest.mark.parametrize("flow",
        [["9", "7", "5", "1", "6", "4"],
        ["8", "5", "2", "7", "9", "3"],
        ["8", "1", "5", "2", "9", "3"]])
    def test_player_O_wins(self, flow):
        self.helper_methods.flow_slots_played(flow)
        self.helper_methods.assert_win_info("Player O wins!")