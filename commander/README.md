# commander

## Overview

This is package which handles requests made by other packages.

**Keywords:** commander, ip camera, topics, executor, service.

### License

The source code is released under a [BSD 3-Clause license](LICENSE).

**Author(s): Ugnius Malūkas  
Maintainer: Ugnius Malūkas, ugnius@malukas.lt**

The commander package has been tested under [ROS] Kinetic and Ubuntu 16.04.

## Installation

### Building from Source

#### Dependencies

- [Robot Operating System (ROS)] (Middleware for Robotics),


#### Building

To build from source, clone the latest version from this repository into your catkin workspace and compile the package using

	cd catkin_workspace/src
	git clone https://github.com/ugnelis/ros_cameras_controller.git
	cd ../
	catkin_make


## Usage

Run the main node with

	roslaunch commander commander.launch


## Launch files

* **commander.launch:** commander node is launched.


## Nodes

### commander

Handles requests got by ROS service and launches needed launch files.


#### Services

* **`commander`** (commander)

	Returns the information about the current average. For example, you can trigger the computation from the console with

		rosservice call /ros_package_template/get_average
	
	Returns all cameras in JSON format.
	
		rosservice call /commander "command: 'list' argument: ''"
		
	Return a specific camera by a given camera's ID in JSON format.
	
		rosservice call /commander "command: 'get' argument: '35e14db6b0f911e897bc080027531864'"
		
	Adds a camera by given URL and returns a result in JSON format.
	
		rosservice call /commander "command: 'add' argument: 'http://192.178.1.13/mjpg/video.mjpg'"
		
	Removes a camera by given ID and returns a result in JSON format
		
		rosservice call /commander "command: 'remove' argument: '35e14db6b0f911e897bc080027531864'"


## Bugs & Feature Requests

Please report bugs and request features using the [Issue Tracker](https://github.com/ugnelis/ros-cameras-controller/issues).


[Robot Operating System (ROS)]: http://www.ros.org

