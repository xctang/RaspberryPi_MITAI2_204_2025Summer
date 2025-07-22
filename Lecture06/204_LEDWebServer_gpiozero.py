# This is a program to use flask package
# to build local web server to control
# MIT APP LED controller app


from flask import Flask, render_template
from gpiozero import LED

app=Flask(__name__)

led = LED(2)

#
#start the main program loop, read command from app through
#local web server, decode the msg and control led
#

@app.route("/<device>/<action>")

def action(device, action):
    actuator = LED
    if action == "on":
        led.on()       # turn on LED
    if action == "off":
        led.off()      # turn off LED
    return ""

if __name__ == '__main__':
    app.run(debug=True, port=80, host='0.0.0.0', use_reloader=False)
