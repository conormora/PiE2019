# Team 43 forklift code!

# Motor IDs -- make sure to  use quotes!
left_motor = "56702378516105538047867"
right_motor = "56702629055943970764316"
lift_motor = "56695734118150397621956"

# Motor constants -- all motor velocity values multiplied by these numbers.
# Changing these numbers changes the speed of the robot everywhere in the code. 
rmc = 1 # Right motor constant
lmc = -1 # Left motor constant

# --- SOME FUNCTIONS FOR YOUR CONVENIENCE --- 
async def go_forward(time):
    # move left motor forward 
    Robot.set_value(left_motor, 'duty_cycle', lmc)
    # move right motor forward
    Robot.set_value(right_motor,'duty_cycle', rmc)
    # wait for x (time) number of seconds
    await Actions.sleep(time)
    # tell left motor to stop
    Robot.set_value(left_motor,'duty_cycle', 0)
    # tell right motor to stop 
    Robot.set_value(right_motor,'duty_cycle', 0)

async def go_backward(time):
    #move left motor backward
    Robot.set_value(left_motor, 'duty_cycle', -lmc)
    #move right motor backward
    Robot.set_value(right_motor, 'duty_cycle', -rmc)
    #wait for x (time) number of seconds
    await Actions.sleep(time)
    #tell left motor to stop
    Robot.set_value(left_motor, 'duty_cycle', 0)
    #tell right motor to stop
    Robot.set_value(right_motor, 'duty_cycle', 0)

async def turn_angle(time):
    #move left motor forward
    Robot.set_value(left_motor, 'duty_cycle', lmc
    #move right motor reverse
    Robot.set_value(right_motor, 'duty_cycle', -rmc
    #wait for x (time) number of seconds
    await Actions.sleep(time)
    #tell left motor to stop
    Robot.set_value(left_motor, 'duty_cycle', 0)
    #tell right motor to stop
    Robot.set_value(right_motor, 'duty_cycle', 0)

''' DO NOT USE -- FAULTY 
async def robot_drive_direct(vleft, vright):
    Robot.set_value(left_motor, 'duty_cycle', lmc * vleft)    
    Robot.set_value(right_motor, 'duty_cycle', rmc * vright)
'''

async def activate_lift(vlift, time): # Takes desired velocity of lift (from -1 to 1) and time (in seconds) as input
    Robot.set_value(lift_motor, 'duty_cycle', -vlift)
    await Actions.sleep(time)
    Robot.set_value(lift_motor, 'duty_cycle', 0)

# --- COMPETITION CODE ---
                    
def autonomous_setup(): # Runs once
    Robot.run(go_forward, 5) # Go forward for 5 seconds

def autonomous_main(): # Runs on loop until autonomous period ends
    pass

def teleop_setup(): # Runs once
    pass

def teleop_main(): # Runs on loop until teleoperated period ends
    # All gamepad controls go here!
    
    # --- FORKLIFT CONTROLS ---

    # If left trigger is being pressed:
    if Gamepad.get_value("l_trigger"):
        print("Left trigger pressed -- going down!")
        # Move forklift motor with positive pulse value (lift down)
        Robot.set_value(lift_motor, "duty_cycle", 1)
    # Or, if right trigger is being pressed:
    elif Gamepad.get_value("r_trigger"):
        print("Right trigger pressed -- going up!")
        # Move forklift motor with negative pulse value (lift up)
        Robot.set_value(lift_motor, "duty_cycle", -1)
    # Otherwise:
    else:
        # Stop the forklift
        Robot.set_value(lift_motor, "duty_cycle", 0)
    
    # --- DRIVE CONTROLS --- 

    # If left joystick has moved:
    if Gamepad.get_value("joystick_left_y") != 0.0:
        # Drive left motor proportional to left joystick position (multiplied by left motor constant)
        print("Left motor driving at %s" lmc * Gamepad.get_value("joystick_left_y"))
        Robot.set_value(left_motor, "duty_cycle", lmc * Gamepad.get_value("joystick_left_y"))
    # Otherwise (left joystick centered):
    else:
        # Left wheel should not be moving -- stop the left motor
        Robot.set_value(left_motor, "duty_cycle", 0)
       
     # If right joystick has moved:
    if Gamepad.get_value("joystick_right_y") != 0.0:
        # Drive right motor proportional to right joystick position (multiplied by right motor constant)
        print("Right motor driving at %s" lmc * Gamepad.get_value("joystick_right_y"))
        Robot.set_value(right_motor, "duty_cycle", rmc * Gamepad.get_value("joystick_right_y"))
    # Otherwise (right joystick centered):
    else:
        # Right wheel should not be moving -- stop the right motor
        Robot.set_value(right_motor, "duty_cycle", 0)
    
# That's all, folks. 
