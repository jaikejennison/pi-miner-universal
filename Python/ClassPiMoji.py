from sense_hat import SenseHat

hat = SenseHat()
red = [255, 0, 0]
black = [0, 0, 0]

def clear_hat(red_int = 0, green_int = 0, blue_int = 0):
    hat.clear(red_int, green_int, blue_int)

def smile(x = red, o = black):
    hat.set_pixels([
        o, o, x, x, x, x, o, o,
        o, x, o, o, o, o, x, o,
        x, o, x, o, o, x, o, x,
        x, o, o, o, o, o, o, x,
        x, o, x, o, o, x, o, x,
        x, o, o, x, x, o, o, x,
        o, x, o, o, o, o, x, o,
        o, o, x, x, x, x, o, o
    ])

def question_mark(x = red, o = black):
    hat.set_pixels([
        o, o, o, x, x, o, o, o,
        o, o, x, o, o, x, o, o,
        o, o, o, o, o, x, o, o,
        o, o, o, o, x, o, o, o,
        o, o, o, x, o, o, o, o,
        o, o, o, x, o, o, o, o,
        o, o, o, o, o, o, o, o,
        o, o, o, x, o, o, o, o
    ])

def ethereum_coin(x = red, o = black):
    hat.set_pixels([
        o, o, o, x, o, o, o, o,
        o, o, o, x, x, o, o, o,
        o, o, x, x, x, x, o, o,
        o, x, x, x, x, x, x, o,
        o, x, x, x, x, x, x, o,
        o, o, x, x, x, x, o, o,
        o, o, o, x, x, o, o, o,
        o, o, o, x, o, o, o, o
    ])
