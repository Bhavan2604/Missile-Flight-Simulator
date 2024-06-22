"""
This Prrogram is the main for the simulation of a missile's trajectory.
Main functionality: 
0. Make it simulate projectile motion
1. Handle the rockets velocity, position, acceleration vectors
2. Interpret the Impulse-vs-time graph to decide the impulse in any specified interval
3. The Corodinates and corresponding time should be saved in an excel sheet 
4. The rogram should be able to give us some important flight data like: Max Height, Max Range(for a given Impulse-vs-time graph)
5. Try to incorporate support for rockets with multiple stages and reducing mass
"""


import math
import scipy
from scipy.integrate import quad
import csv
file_path = 'data.csv'
iter_no = 0


t = 0 
p_time = 1e-2
current_position_y = 0

def mode_selector():
    initiate()

def initiate():
    global initial_mass
    initial_mass= 100.00
    global launch_angle
    launch_angle= math.pi * (30/180)
    global angle
    angle= launch_angle
    global impulse_v_time 
    impulse_v_time = " i = -2.5t^2 + 5t + 7.5" 
    print (impulse_v_time)
    # i -- impulse
    # t -- time
    global initial_velocity 
    initial_velocity = 10
    global initial_position_x
    initial_position_x = 0
    global initial_position_y 
    initial_position_y = 0
    #global initial_position_z
    #initial_position_z =0 

    
def v(t):    
    return initial_velocity
def v_x(t):
    return v(t)*math.sin(angle)
def v_y(t):
    return (v(t)*math.cos(angle) - (10*(t)))

#velocity = initial_velocity
def read_specific_line(file_path, line_number):
    with open(file_path, 'r') as file:
        for current_line_number, line in enumerate(file, start=1):
            if current_line_number == line_number:
                return line.strip().split(',')
def update():
    global t
    global iter_no
    previous_data = read_specific_line(file_path, iter_no+2)
    previous_position_x = float(previous_data[0])
    previous_position_y = float(previous_data[1])
    
    global current_position_x
    change_position_x, error = quad(v_x,t,t+p_time)
    current_position_x = previous_position_x + change_position_x
    change_position_y, error = quad(v_y,t, t+ p_time)
    global current_position_y
    current_position_y = previous_position_y + change_position_y
    iter_no +=1
    values = [current_position_x, current_position_y, t]
    #print (values)
    with open(file_path, mode = 'a+' , newline = '') as file:
        writer = csv.writer(file)
        writer.writerow(values)
    t= t+ p_time
    return current_position_y, current_position_x




def main():
    
    mode_selector()
    columns = ["X - coordinate", "Y - coordinate", "Time"]
    data_initial = [initial_position_x, initial_position_y, 0]
    with open(file_path, mode = 'a+' , newline = '') as file:
        writer = csv.writer(file)
        writer.writerow(columns)
        writer.writerow(data_initial)
    while current_position_y >= 0:
        update()
    """
    for value in range(1000):
        update()
    """    
if __name__ == "__main__":
    main()    


    

