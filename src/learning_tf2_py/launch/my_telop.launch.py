from launch import LaunchDescription
from launch_ros.actions import Node
 
def generate_launch_description():
    return LaunchDescription([
        Node(
            package='turtlesim',
            executable='turtle_teleop_key',
            name='sim'
        ),
    ])



# from launch import LaunchDescription
# from launch_ros.actions import Node

# def generate_launch_description():
#     ld = LaunchDescription()

#     turtle_teleop = Node(
#         package='turtlesim',
#         executable='turtle_teleop_key',  # Ensure the executable name is correct
#         name='teleop',
#         output='screen'

#     )

#     ld.add_action(turtle_teleop)  # Corrected variable name
#     return ld

# from launch import LaunchDescription
# from launch_ros.actions import Node
 
# def generate_launch_description():
#     ld = LaunchDescription()
#     turtlesim_node = Node(
#         package="turtlesim",
#         executable="turtlesim_node",
#         name='sim'
#     )
 
#     ld.add_action(turtlesim_node)
#     return ld