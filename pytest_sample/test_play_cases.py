from alttester import AltDriver, By
from page.helpermethods import HelperMethods
import time

class TestPlay:

    altdriver = AltDriver()

    def setup_method(self):
        self.helper_methods = HelperMethods(self.altdriver)

    def test_player_X_wins(self):
        self.altdriver.load_scene("StartScene",True)

        play = self.helper_methods.play_button
        assert play is not None
        #self.altdriver.click(play.get_screen_position())
        play.click()

        TextTMP = self.helper_methods.slot_number("1")
        self.altdriver.click(TextTMP.get_screen_position())
        TextTMP2 = self.helper_methods.slot_number("5")
        self.altdriver.click(TextTMP2.get_screen_position())
        TextTMP3 = self.helper_methods.slot_number("9")
        self.altdriver.click(TextTMP3.get_screen_position())
        TextTMP4 = self.helper_methods.slot_number("3")
        self.altdriver.click(TextTMP4.get_screen_position())
        TextTMP5 = self.helper_methods.slot_number("7")
        self.altdriver.click(TextTMP5.get_screen_position())
        TextTMP6 = self.helper_methods.slot_number("8")
        self.altdriver.click(TextTMP6.get_screen_position())
        TextTMP7 = self.helper_methods.slot_number("4")
        self.altdriver.click(TextTMP7.get_screen_position())

        self.helper_methods.assert_win_info("Player X wins!")

    def test_interact_with_alttester_panel(self):
        self.altdriver.load_scene("StartScene",True)

        alttester_logo = self.altdriver.wait_for_object(By.PATH, '//AltDialog/Icon', timeout = 3)
        assert alttester_logo is not None
        alttester_logo.click()
        object_port = self.altdriver.wait_for_object(By.PATH, '//PortInputField/Text', timeout = 3)
        assert object_port is not None
        assert object_port.get_text() == "13000"

        # restart_button = self.altdriver.wait_for_object(By.PATH, '//RestartButton', timeout = 3)
        # restart_button.click()
        # time.sleep(5)