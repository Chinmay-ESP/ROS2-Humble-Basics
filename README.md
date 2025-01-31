# ROS2-Humble Basics

This repository contains basic implementations of ROS2 (Humble) nodes, covering publisher-subscriber mechanisms and turtlesim automation.

## Features

### 1. Basic ROS2 Node
- Creating a simple ROS2 node in Humble.
- Understanding the structure of a ROS2 package.

### 2. Publisher Node
- Publisher node with a timer callback and counter.
- Sends periodic messages over a topic.

### 3. Subscriber Node
- Receives messages from the publisher node.
- Processes and prints received data.

### 4. Publisher for Turtlesim
- Controls the turtlesim using a ROS2 publisher.
- Sends velocity commands to move the turtle.

### 5. Subscriber for Turtlesim
- Subscribes to turtlesim position updates.
- Retrieves and processes the turtle's pose.

### 6. Drawing a Circle in Turtlesim
- Uses a ROS2 publisher to make the turtle move in a circular pattern.

### 7. Automating Turtlesim Without Touching Edges
- Implements a logic to prevent the turtle from colliding with the screen edges.
- Dynamically adjusts movement to stay within bounds.

## Getting Started

### Prerequisites
- Install ROS2 Humble ([Installation Guide](https://docs.ros.org/en/humble/Installation.html))
- Install turtlesim package:
  ```bash
  sudo apt install ros-humble-turtlesim
  ```
- Source ROS2 environment:
  ```bash
  source /opt/ros/humble/setup.bash
  ```

### Clone the Repository
```bash
git clone https://github.com/Chinmay-ESP/ROS2-Humble-Basics.git
cd ROS2-Humble-Basics
```

### Build and Run
```bash
colcon build
source install/setup.bash
```

#### Running the Publisher Node
```bash
ros2 run <your_package> publisher_node
```

#### Running the Subscriber Node
```bash
ros2 run <your_package> subscriber_node
```

#### Running Turtlesim Automation
```bash
ros2 run <your_package> turtlesim_controller
```

---

Feel free to contribute by submitting issues or pull requests!

