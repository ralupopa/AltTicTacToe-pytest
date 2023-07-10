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

    def test_player_X_wins(self):
        flow = ["1", "5", "9", "3", "7", "8", "4"]
        self.helper_methods.flow_slots_played(flow)

        self.helper_methods.assert_win_info("Player X wins!")

    def test_draw_result(self):
        flow = ["8", "5", "9", "7", "3", "6", "4", "1", "2"]
        self.helper_methods.flow_slots_played(flow)

        self.helper_methods.assert_win_info("It's a draw!")
    
    def test_player_O_wins(self):
        flow = ["9", "7", "5", "1", "6", "4"]
        self.helper_methods.flow_slots_played(flow)

        self.helper_methods.assert_win_info("Player O wins!")