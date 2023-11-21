let score = 5
basic.forever(function () {
    if (input.pinIsPressed(TouchPin.P0)) {
        score += -1
        music.play(music.tonePlayable(262, music.beat(BeatFraction.Whole)), music.PlaybackMode.UntilDone)
        basic.pause(200)
    }
})
basic.forever(function () {
    if (score > 0) {
        basic.showNumber(score)
    } else {
        music.play(music.stringPlayable("F F E E D E C C ", 231), music.PlaybackMode.UntilDone)
        basic.showString("You dead. L-BOZO")
    }
})
