serial.redirect(SerialPin.USB_TX, SerialPin.USB_RX, BaudRate.BAUD_RATE115200)
serial.redirect_to_usb()

def on_forever():
    serial.write_numbers([input.temperature(), input.light_level()])
    basic.pause(1000)
basic.forever(on_forever)
