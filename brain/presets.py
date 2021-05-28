import numpy as np

INIT_COMMANDS = ('command', 'streamon', 'takeoff')

END_COMMANDS = ('land', 'streamoff', 'end')

COMMANDS_LIST = ('up', 'down', 'left', 'right', 'forward', 'back',
                 'cw', 'ccw',
                 'go')

LINEAR_STEPS = np.arange(20, 110, 10)  # max 500
ROTATE_STEPS = np.arange(1, 360, 1)

SPEED = 20

READ_COMMANDS = ('speed?', 'battery?', 'time?')


def initialization(command_queue):
    init_proc_command = INIT_COMMANDS
    for c in init_proc_command:
        command_queue.append(c)


def end_mission(command_queue):
    end_proc_command = END_COMMANDS
    for c in end_proc_command:
        command_queue.append(c)


def make_decision(model, event):
    """
    get event and make decision
    event - contain information about state anomaly, video stream detections, etc

    """
    next_step = model.predict(event)

    return next_step


def parse_command(command_string, state):
    string_list = command_string.split(' ')
    # check arguments in command

    if string_list[0] == 'cw':
        state['r'] += string_list[1]
    elif string_list[0] == 'ccw':
        state['r'] -= string_list[1]
    elif string_list[0] == 'up':
        state['z'] += string_list[1]
    elif string_list[0] == 'down':
        state['z'] -= string_list[1]
    elif string_list[0] == 'forward':
        state['x'] += string_list[1]
    elif string_list[0] == 'back':
        state['x'] -= string_list[1]
    elif string_list[0] == 'left':
        state['y'] += string_list[1]
    elif string_list[0] == 'right':
        state['y'] -= string_list[1]
    else:
        return


def get_rnd_command():
    com_w = COMMANDS_LIST[np.random.randint(len(COMMANDS_LIST))]
    if com_w in ['cw', 'ccw']:
        com_arg = ROTATE_STEPS[np.random.randint(len(ROTATE_STEPS))]
        command = com_w + ' ' + str(com_arg)
    elif com_w == 'go':
        com_arg_x = LINEAR_STEPS[np.random.randint(len(LINEAR_STEPS))]
        com_arg_y = LINEAR_STEPS[np.random.randint(len(LINEAR_STEPS))]
        com_arg_z = LINEAR_STEPS[np.random.randint(len(LINEAR_STEPS))]
        command = com_w + ' ' + str(com_arg_x) + ' ' + str(com_arg_y) + ' ' + str(com_arg_z) + ' ' + str(SPEED)
    else:
        com_arg = LINEAR_STEPS[np.random.randint(len(LINEAR_STEPS))]
        command = com_w + ' ' + str(com_arg)

    return command


def read_command_from_file(path, command_queue):
    with open(path) as file:
        for line in file:
            command_queue.append(line.strip())


# for i in range(10):
#     print(get_rnd_command())


# commands = []
# read_command_from_file('../fly_programs/program_1', commands)
# for c in commands:
#     print(c)
