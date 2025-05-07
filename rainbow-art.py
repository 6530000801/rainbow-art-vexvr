RedBorder = Event()
OrangeBorder = Event()
YellowBorder = Event()
GreenBorder = Event()
BluePurpBorder = Event()
Reset = Event()

def when_started1():
    global RedBorder, OrangeBorder, YellowBorder, GreenBorder, BluePurpBorder, Reset
    drivetrain.set_drive_velocity(1000, PERCENT)
    drivetrain.set_turn_velocity(1000, PERCENT)
    RedBorder.broadcast_and_wait()
    OrangeBorder.broadcast_and_wait()
    YellowBorder.broadcast_and_wait()
    GreenBorder.broadcast_and_wait()
    BluePurpBorder.broadcast_and_wait()
    Reset.broadcast_and_wait()
    stop_project()

def onevent_RedBorder_0():
    global RedBorder, OrangeBorder, YellowBorder, GreenBorder, BluePurpBorder, Reset
    for repeat_count2 in range(3):
        for repeat_count in range(9):
            pen.fill(255, 0, 0, 100)
            drivetrain.drive_for(FORWARD, 200, MM)
        drivetrain.turn_for(RIGHT, 90, DEGREES)
    pen.fill(255, 0, 0, 100)
    for repeat_count3 in range(8):
        drivetrain.drive_for(FORWARD, 200, MM)
        pen.fill(255, 0, 0, 100)

def onevent_OrangeBorder_0():
    global RedBorder, OrangeBorder, YellowBorder, GreenBorder, BluePurpBorder, Reset
    drivetrain.turn_for(RIGHT, 90, DEGREES)
    for repeat_count4 in range(8):
        drivetrain.drive_for(FORWARD, 200, MM)
        pen.fill(255, 113, 0, 100)
    drivetrain.turn_for(RIGHT, 90, DEGREES)
    for repeat_count6 in range(2):
        for repeat_count5 in range(7):
            drivetrain.drive_for(FORWARD, 200, MM)
            pen.fill(255, 113, 0, 100)
        drivetrain.turn_for(RIGHT, 90, DEGREES)
    for repeat_count7 in range(6):
        drivetrain.drive_for(FORWARD, 200, MM)
        pen.fill(255, 113, 0, 100)

def onevent_YellowBorder_0():
    global RedBorder, OrangeBorder, YellowBorder, GreenBorder, BluePurpBorder, Reset
    drivetrain.turn_for(RIGHT, 90, DEGREES)
    for repeat_count8 in range(6):
        drivetrain.drive_for(FORWARD, 200, MM)
        pen.fill(255, 255, 0, 100)
    drivetrain.turn_for(RIGHT, 90, DEGREES)
    for repeat_count10 in range(2):
        for repeat_count9 in range(5):
            drivetrain.drive_for(FORWARD, 200, MM)
            pen.fill(255, 255, 0, 100)
        drivetrain.turn_for(RIGHT, 90, DEGREES)
    for repeat_count11 in range(4):
        drivetrain.drive_for(FORWARD, 200, MM)
        pen.fill(255, 255, 0, 100)

def onevent_GreenBorder_0():
    global RedBorder, OrangeBorder, YellowBorder, GreenBorder, BluePurpBorder, Reset
    drivetrain.turn_for(RIGHT, 90, DEGREES)
    for repeat_count12 in range(4):
        drivetrain.drive_for(FORWARD, 200, MM)
        pen.fill(0, 255, 0, 100)
    drivetrain.turn_for(RIGHT, 90, DEGREES)
    for repeat_count14 in range(2):
        for repeat_count13 in range(3):
            drivetrain.drive_for(FORWARD, 200, MM)
            pen.fill(0, 255, 0, 100)
        drivetrain.turn_for(RIGHT, 90, DEGREES)
    for repeat_count15 in range(2):
        drivetrain.drive_for(FORWARD, 200, MM)
        pen.fill(0, 255, 0, 100)

def onevent_BluePurpBorder_0():
    global RedBorder, OrangeBorder, YellowBorder, GreenBorder, BluePurpBorder, Reset
    drivetrain.turn_for(RIGHT, 90, DEGREES)
    drivetrain.drive_for(FORWARD, 200, MM)
    pen.fill(0, 0, 255, 100)
    drivetrain.drive_for(FORWARD, 200, MM)
    pen.fill(88, 0, 255, 100)
    drivetrain.turn_for(RIGHT, 90, DEGREES)
    drivetrain.drive_for(FORWARD, 200, MM)
    pen.fill(0, 0, 255, 100)
    drivetrain.turn_for(RIGHT, 90, DEGREES)
    drivetrain.drive_for(FORWARD, 200, MM)
    pen.fill(88, 0, 255, 100)

def onevent_Reset_0():
    global RedBorder, OrangeBorder, YellowBorder, GreenBorder, BluePurpBorder, Reset
    drivetrain.drive_for(FORWARD, 800, MM)
    drivetrain.turn_for(RIGHT, 90, DEGREES)
    drivetrain.drive_for(FORWARD, 1000, MM)
    drivetrain.turn_for(RIGHT, 90, DEGREES)

# system event handlers
RedBorder(onevent_RedBorder_0)
OrangeBorder(onevent_OrangeBorder_0)
YellowBorder(onevent_YellowBorder_0)
GreenBorder(onevent_GreenBorder_0)
BluePurpBorder(onevent_BluePurpBorder_0)
Reset(onevent_Reset_0)
# add 15ms delay to make sure events are registered correctly.
wait(15, MSEC)

vr_thread(when_started1)
