'''
Created on Oct 7, 2020

@author: mrmopoz
'''


from collections import deque
import presets

MISSION_COMPLETE = False

def initialization(command):
    init_proc_command = presets.INIT_COMMANDS
    for c in init_proc_command:
        command.append(c)
    
    return command


def end_mission(command):
    end_proc_command = presets.END_COMMANDS
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

    # main cycle
    while True:
        # first init command
        if count == 0:
            msg = command_queue.popleft()
            command.append(msg)
            count += 1

        # check respond not empty
        if respond:
            resp = respond.popleft()
            # check respond is ok
            if 'ok' in resp:
                # check commands not empty and get next command
                if command_queue:
                    msg = command_queue.popleft()
                    command.append(msg)
                    print(msg + ' put in queue')
                    count += 1
                else:
                    break
            # if respond error repeat last command
            if 'error' in resp:
                command.append(msg)
                print(msg + ' repeat put in queue')
            
        else:
            continue

