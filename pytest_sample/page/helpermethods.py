from alttester import By

class HelperMethods:

    def __init__(self, altdriver):
        self.altdriver = altdriver

    @property
    def play_button(self):
        return self.altdriver.wait_for_object(By.PATH, '//PlayButton', timeout = 3)
    
    def win_info(self):
        return self.altdriver.wait_for_object(By.PATH, '//WinInfo', timeout = 3)

    def slot_number(self, number):
        return self.altdriver.wait_for_object(By.PATH, "/Canvas/MainContainer/Board/Slots/Slot" + number + "/Text (TMP)")
    
    def flow_slots_played(self, slots):
        for slot in slots:
            place = self.slot_number(slot)
            assert place is not None
            self.altdriver.click(place.get_screen_position())
            #place.click()

    def assert_win_info(self, msg_result):
        assert self.win_info() is not None
        assert self.win_info().get_text() == msg_result
