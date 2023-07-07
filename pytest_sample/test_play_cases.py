from alttester import AltDriver, By

class TestPlay:
    altdriver = AltDriver()

    def test_player_X_wins(self):
        self.altdriver.load_scene("StartScene",True)
        self.altdriver.load_scene("PlayScene",True)
        TextTMP = self.altdriver.wait_for_object(By.PATH,"/Canvas/MainContainer/Board/Slots/Slot1/Text (TMP)",enabled=False)
        self.altdriver.click(TextTMP.get_screen_position())
        TextTMP2 = self.altdriver.wait_for_object(By.PATH,"/Canvas/MainContainer/Board/Slots/Slot5/Text (TMP)",enabled=False)
        self.altdriver.click(TextTMP2.get_screen_position())
        TextTMP3 = self.altdriver.wait_for_object(By.PATH,"/Canvas/MainContainer/Board/Slots/Slot9/Text (TMP)",enabled=False)
        self.altdriver.click(TextTMP3.get_screen_position())
        TextTMP4 = self.altdriver.wait_for_object(By.PATH,"/Canvas/MainContainer/Board/Slots/Slot3/Text (TMP)",enabled=False)
        self.altdriver.click(TextTMP4.get_screen_position())
        TextTMP5 = self.altdriver.wait_for_object(By.PATH,"/Canvas/MainContainer/Board/Slots/Slot7/Text (TMP)",enabled=False)
        self.altdriver.click(TextTMP5.get_screen_position())
        TextTMP6 = self.altdriver.wait_for_object(By.PATH,"/Canvas/MainContainer/Board/Slots/Slot8/Text (TMP)",enabled=False)
        self.altdriver.click(TextTMP6.get_screen_position())
        TextTMP7 = self.altdriver.wait_for_object(By.PATH,"/Canvas/MainContainer/Board/Slots/Slot4/Text (TMP)",enabled=False)
        self.altdriver.click(TextTMP7.get_screen_position())