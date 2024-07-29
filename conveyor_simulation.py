import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from pid_controller import PIDController
from conveyor_dynamics import conveyor_dynamics

# Initialize PID controller
dt = 0.1
pid = PIDController(kp=1, ki=0.05, kd=0.5, dt=dt)

# Initial conditions
initial_conditions = [0.0, 0.0]
time = np.linspace(0, 20, int(20/dt))

# Adjusting the solver parameters
solver_options = {'rtol': 1e-6, 'atol': 1e-8}

# Run the simulation
solution = odeint(conveyor_dynamics, initial_conditions, time, args=(pid,), full_output=1, **solver_options)

# Extract results
solution_values = solution[0]
infodict = solution[1]
if infodict['message'] != 'Integration successful.':
    print("Warning: ODE solver issued a message:", infodict['message'])

position, velocity = solution_values.T

# Plot results
plt.figure(figsize=(14, 8))
plt.subplot(2, 1, 1)
plt.plot(time, position, 'r-', label='Position')
plt.axhline(y=1.0, color='b', linestyle='--', label='Setpoint')
plt.xlabel('Time')
plt.ylabel('Position')
plt.title('Position Over Time with PID Control')
plt.legend()

plt.subplot(2, 1, 2)
plt.plot(time, velocity, 'b-', label='Velocity')
plt.xlabel('Time')
plt.ylabel('Velocity')
plt.title('Velocity Over Time with PID Control')
plt.legend()

plt.tight_layout()

# Save the plot as a file instead of showing it interactively
plt.savefig('conveyor_simulation_results_second_update.png')
print("Simulation complete. Results saved to 'conveyor_simulation_results.png'")
