# Conveyor Belt Simulation with PID Control

## Project Overview

This project simulates the dynamics of a conveyor belt system controlled by a Proportional-Integral-Derivative (PID) controller. The goal is to maintain the position of the conveyor belt at a desired setpoint while controlling its velocity and acceleration within specified limits. The simulation integrates the conveyor dynamics with the PID controller to achieve precise control over the system.

## Technical Details

### PID Controller

The PID controller is a feedback control loop mechanism widely used in industrial control systems. It calculates an error value as the difference between a desired setpoint and a measured process variable and applies a correction based on proportional, integral, and derivative terms (denoted as P, I, and D respectively).

- **Proportional (P)**: This term produces an output value that is proportional to the current error value. The proportional response can be adjusted by multiplying the error by a constant known as the proportional gain (Kp).

- **Integral (I)**: This term is concerned with the accumulation of past errors. If the error has been present for some time, the integral term will accumulate a response to eliminate the residual steady-state error that occurs with a pure proportional controller.

- **Derivative (D)**: This term is a prediction of future error, based on its rate of change. It dampens the system response and improves stability.

### Conveyor Dynamics

The conveyor dynamics are modeled as a system with two state variables: position and velocity. The dynamics are governed by the following differential equations:

- \( \frac{d(position)}{dt} = velocity \)
- \( \frac{d(velocity)}{dt} = acceleration \)

The PID controller computes the desired speed based on the current position error, which is then constrained by a maximum speed limit. The necessary acceleration to achieve this speed is also constrained by a maximum acceleration limit.

### Simulation

The simulation is performed using the `odeint` function from the SciPy library, which integrates the conveyor dynamics over time. The results, including the position and velocity of the conveyor belt, are plotted and saved as PNG images.

## Project Structure

- **conveyor_simulation.py**: This script runs the simulation, integrates the conveyor dynamics with the PID controller, and plots the results.
- **pid_controller.py**: This module defines the `PIDController` class.
- **conveyor_dynamics.py**: This module defines the `conveyor_dynamics` function, which calculates the derivatives of the state variables.
- **requirements.txt**: This file lists the required Python packages for the project.
- **README.md**: Provides an overview of the project and instructions for running the simulation.

## How to Run the Simulation

1. **Install the required packages**:
   ```bash
   pip install -r requirements.txt

