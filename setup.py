from setuptools import find_packages, setup

package_name = 'my_robot_controller'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='vrc',
    maintainer_email='vrc@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'my_first_node = my_robot_controller.my_first_node:main',
            'my_timer_node = my_robot_controller.my_timer_node:main',
            'turtlesim_draw_circle = my_robot_controller.turtlesim_draw_circle:main',
            'turtlesim_control = my_robot_controller.turtlesim_control:main',
            
        ],
    },
)
