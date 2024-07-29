

def conveyor_dynamics(y, t, pid_controller, max_speed=2.0, max_acceleration=0.1):
    position, velocity = y
    setpoint = 1.0  # Desired position (setpoint)
    
    # PID control for motor speed
    desired_speed = pid_controller.compute(setpoint, position)
    
    # Constrain the desired speed by max speed
    desired_speed = max(min(desired_speed, max_speed), -max_speed)
    
    # Calculate acceleration needed to reach desired speed
    acceleration = (desired_speed - velocity) / pid_controller.dt
    
    # Constrain the acceleration by max acceleration
    acceleration = max(min(acceleration, max_acceleration), -max_acceleration)
    
    dposition_dt = velocity
    dvelocity_dt = acceleration
    
    # Debugging prints
    print(f"time: {t}, position: {position}, velocity: {velocity}, desired_speed: {desired_speed}, acceleration: {acceleration}")
    
    return [dposition_dt, dvelocity_dt]
