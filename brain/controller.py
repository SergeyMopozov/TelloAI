'''
Created on Oct 7, 2020

@author: mrmopoz
'''


from collections import deque
import time


def initialization(command):
    init_proc_command = ['command', 'streamon']
    for c in init_proc_command:
        command.append(c)
    
    return command


def end_mission(command):
    end_proc_command = ['land', 'streamoff']
    for c in end_proc_command:
        command.append(c)
    return command


def make_decision(model, event):
    """
    get event and make decision
    event - contain information about state anomaly, video stream detections, etc

    """
    next_step = model.predict(event)

    return next_step


def controller(command, respond):
    
    print('Start controller')
    count = 0
    # command backlog
    command_queue = deque(['command', 'streamon', 'takeoff', 'right 20', 'up 50', 
                'forward 40', 'left 20', 'cw 180', 'go 100 100 80 20', 'flip r',
                'cw 180', 'go 100 100 -80 10',
                'back 20', 'land', 'end'])
                
    while True:
        # first init command
        if count == 0:
            msg = command_queue.popleft()
            command.append(msg)
            count += 1

        # check commands in stack and put it in queue
        if respond:
            resp = respond.popleft()
            if 'ok' in resp:
                if command_queue:
                    msg = command_queue.popleft()
                    command.append(msg)
                    print(msg + ' put in queue')
                    count += 1
                else:
                    break
            # repeat last command
            if 'error' in resp:
                command.append(msg)
                print(msg + ' put in queue')
            
        else:
            continue

