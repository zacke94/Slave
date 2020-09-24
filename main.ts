radio.setGroup(77)
basic.forever(function () {
    radio.sendValue("temp", input.temperature())
    radio.sendValue("light", input.lightLevel())
    basic.pause(1000)
})
