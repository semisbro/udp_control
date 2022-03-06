import vlc
vlcInstance = vlc.Instance()
player = vlcInstance.media_player_new()
player.set_mrl("rtsp://URL_PATH")
player.play()