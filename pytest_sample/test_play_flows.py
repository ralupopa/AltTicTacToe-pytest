from alttester import AltDriver
from page.helpermethods import HelperMethods

class TestPlay:

    altdriver = AltDriver()

    def setup_method(self):
        self.helper_methods = HelperMethods(self.altdriver)

    def test_player_X_wins(self):
        self.altdriver.load_scene("StartScene",True)

        play = self.helper_methods.play_button
        assert play is not None
        play.click()

        flow = ["1", "5", "9", "3", "7", "8", "4"]
        self.helper_methods.flow_slots_played(flow)