from alttester import AltDriver, By

class HelperMethods:

    def __init__(self, altdriver):
        self.altdriver = altdriver

    @property
    def play_button(self):
        return self.altdriver.wait_for_object(By.PATH, '//PlayButton', timeout = 3)

    def slot_number(self, number):
        return self.altdriver.wait_for_object(By.PATH, "/Canvas/MainContainer/Board/Slots/Slot" + number + "/Text (TMP)")