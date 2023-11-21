score = 5

def on_forever():
    global score
    if input.pin_is_pressed(TouchPin.P0):
        score += -1
        music.play(music.tone_playable(262, music.beat(BeatFraction.WHOLE)),
            music.PlaybackMode.UNTIL_DONE)
        basic.pause(200)
basic.forever(on_forever)

def on_forever2():
    if score > 0:
        basic.show_number(score)
    else:
        music.play(music.string_playable("F F E E D E C C ", 231),
            music.PlaybackMode.UNTIL_DONE)
        basic.show_string("You dead. L-BOZO")
basic.forever(on_forever2)
