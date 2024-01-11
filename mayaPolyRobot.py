import maya.cmds as cmds

def create_robot():
    # Create robot body
    body = cmds.polyCube(name='body', width=2, height=3, depth=1, subdivisionsWidth=5, subdivisionsHeight=7, subdivisionsDepth=3)[0]
    cmds.move(0, 4, 0)

    # Create robot head with beveled edges
    head = cmds.polyCube(name='head', width=1.5, height=1.5, depth=1.5, subdivisionsWidth=3, subdivisionsHeight=3, subdivisionsDepth=3)[0]
    cmds.move(0, 7, 0)

    # Create robot eyes
    eye_left = cmds.polySphere(name='eye_left', radius=0.2, subdivisionsAxis=8, subdivisionsHeight=8)[0]
    cmds.move(-0.5, 7.5, 0.7)

    eye_right = cmds.polySphere(name='eye_right', radius=0.2, subdivisionsAxis=8, subdivisionsHeight=8)[0]
    cmds.move(0.5, 7.5, 0.7)

    # Create robot arms with beveled edges
    arm_left = cmds.polyCube(name='arm_left', width=0.5, height=2, depth=0.5, subdivisionsWidth=3, subdivisionsHeight=5, subdivisionsDepth=3)[0]
    cmds.move(-2, 5.5, 0)

    arm_right = cmds.polyCube(name='arm_right', width=0.5, height=2, depth=0.5, subdivisionsWidth=3, subdivisionsHeight=5, subdivisionsDepth=3)[0]
    cmds.move(2, 5.5, 0)

    # Create robot hands
    hand_left = cmds.polyCube(name='hand_left', width=0.5, height=1, depth=1, subdivisionsWidth=3, subdivisionsHeight=3, subdivisionsDepth=3)[0]
    cmds.move(-2.5, 4, 0)

    hand_right = cmds.polyCube(name='hand_right', width=0.5, height=1, depth=1, subdivisionsWidth=3, subdivisionsHeight=3, subdivisionsDepth=3)[0]
    cmds.move(2.5, 4, 0)

    # Create robot legs with beveled edges
    leg_left = cmds.polyCube(name='leg_left', width=0.5, height=2, depth=0.5, subdivisionsWidth=3, subdivisionsHeight=5, subdivisionsDepth=3)[0]
    cmds.move(-1, 1, 0)

    leg_right = cmds.polyCube(name='leg_right', width=0.5, height=2, depth=0.5, subdivisionsWidth=3, subdivisionsHeight=5, subdivisionsDepth=3)[0]
    cmds.move(1, 1, 0)

    # Create robot feet with beveled edges
    foot_left = cmds.polyCube(name='foot_left', width=1, height=0.2, depth=1, subdivisionsWidth=3, subdivisionsHeight=1, subdivisionsDepth=3)[0]
    cmds.move(-1, 0, 0)

    foot_right = cmds.polyCube(name='foot_right', width=1, height=0.2, depth=1, subdivisionsWidth=3, subdivisionsHeight=1, subdivisionsDepth=3)[0]
    cmds.move(1, 0, 0)

    # Create additional details
    antenna1 = cmds.polyCylinder(name='antenna1', radius=0.1, height=1)[0]
    cmds.move(0.2, 8, 0)

    antenna2 = cmds.polyCylinder(name='antenna2', radius=0.1, height=1)[0]
    cmds.move(-0.2, 8, 0)

    shoulder_left_detail = cmds.polyCube(name='shoulder_left_detail', width=0.3, height=0.5, depth=0.3, subdivisionsWidth=3, subdivisionsHeight=3, subdivisionsDepth=3)[0]
    cmds.move(-2, 6, 0.5)

    shoulder_right_detail = cmds.polyCube(name='shoulder_right_detail', width=0.3, height=0.5, depth=0.3, subdivisionsWidth=3, subdivisionsHeight=3, subdivisionsDepth=3)[0]
    cmds.move(2, 6, 0.5)

# Run the function to create the humanoid robot
create_robot()
