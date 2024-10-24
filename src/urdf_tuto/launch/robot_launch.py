import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import LogInfo
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration
from launch.actions import DeclareLaunchArgument
def generate_launch_description():
    # Define the URDF file name

    urdf_file_name = 'robot.urdf'
    use_sim_time = LaunchConfiguration('use_sim_time', default='false')
    urdf = os.path.join(
        get_package_share_directory('urdf_tuto'),
        urdf_file_name)
    
    with open(urdf, 'r') as infp:
        robot_desc = infp.read()
    # Log the URDF path
    ld = LaunchDescription()

    dc= DeclareLaunchArgument(
            'use_sim_time',
            default_value='false',
            description='Use simulation (Gazebo) clock if true')
    ld.add_action(dc)
    R_S_B=Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            output='screen',
            parameters=[{'use_sim_time': use_sim_time, 'robot_description': robot_desc}],
            arguments=[urdf])
    ld.add_action(R_S_B)
    J_S_B=Node(
            package='joint_state_publisher',
            executable='joint_state_publisher',
            name='joint_state_publisher',
            output='screen',
            parameters=[{'use_sim_time': use_sim_time, 'robot_description': robot_desc}],
            arguments=[urdf])
    ld.add_action(J_S_B)
    return ld
