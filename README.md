# ros_cameras_controller

## Overview

*ros_cameras_controller* uses already stream videos and helps them manage.

The project consists of these ROS packages (more details in README.md files of each package):
* [commander](commander) - handles requests made by other packages.
* [image_processing_filters](image_processing_filters) - lets to apply image processing filter to ROS image topics.
* [video_stream_to_topic](video_stream_to_topic) - converts video stream (e.g. from IP camera) and makes it as a ROS image topic.
* [web_console](web_console) - runs web consoles for managing cameras. It uses Flask for app back-end and AngularJS for front-end.

## Architecture
![Architecture](architecture.png)

### License

The source code is released under a [BSD 3-Clause license](LICENSE).

**Author(s): Ugnius Malūkas  
Maintainer: Ugnius Malūkas, ugnius@malukas.lt**

The web_console package has been tested under [ROS] Kinetic and Ubuntu 16.04.

## Installation

### Building from Source

#### Dependencies

- [Robot Operating System (ROS)] (Middleware for Robotics),
- [OpenCV] (Computer Vision),
- [Flask] (Back-End App),
- [AngularJS] (Front-End App),
- [npm] (Front-End Package Manager)


#### Building

To build from source, clone the latest version from this repository into your catkin workspace and compile the package using

	cd catkin_workspace/src
	git clone https://github.com/ugnelis/ros_cameras_controller.git
	cd ../
	catkin_make
	
### For Newbies
#### Setting up (Recommended)
1. Install [*Ubuntu 16.04 LTS*](http://releases.ubuntu.com/16.04/), [*ROS Kinetic*](http://wiki.ros.org/kinetic/Installation) and [*OpenCV 3.1+*](https://docs.opencv.org/3.1.0/d7/d9f/tutorial_linux_install.html).

2. Be sure that `ROS` is exported to the shell when new shell is opened: [link](http://wiki.ros.org/kinetic/Installation/Ubuntu#kinetic.2BAC8-Installation.2BAC8-DebEnvironment.Environment_setup).

3. Install *web_video_server*:

	    sudo apt-get install ros-kinetic-web-video-server

4. Install *rosbridge-suite*:

	    sudo apt-get install sudo apt-get install ros-kinetic-rosbridge-suite

5. Install *NodeJS* and *npm*:

	    curl -sL https://deb.nodesource.com/setup_8.x | sudo -E bash -
	    sudo apt-get install -y nodejs
	
6. Install *Flask*:

    	sudo pip install Flask


7. Create catkin workspace for storing ROS source projects:
	
	    mkdir -p ~/catkin_ws/src
	    cd ~/catkin_ws/
	    catkin_make
	
8. Clone this project to `~/catkin_ws/src`.

	    cd ~/catkin_ws/src
	    git clone https://github.com/ugnelis/ros_cameras_controller.git
	    cd ../
	    catkin_make

#### Running Prooject in Production
* Open first terminal and run **commander** package:

	    roslaunch commander commander.launch
	
* Open second terminal and run **web_console** package:

	    roslaunch web_console web_console.launch

* **web_console** is now running on http://localhost:9999.

#### Running Prooject in Development
* Open first terminal and run **commander** package:

	    roslaunch commander commander.launch
	
* Open second terminal and run **rosbridge_server** package:

        roslaunch rosbridge_server rosbridge_websocket.launch

* Open third terminal and run **web_video_server** package:

        rosrun web_video_server web_video_server _port:=8888

* Open fourth terminal and front-end app of **web_console** package:

	    roscd web_console/src/front_end_app
	    npm start

[Robot Operating System (ROS)]: http://www.ros.org
[OpenCV]: https://opencv.org
[Flask]: http://flask.pocoo.org
[npm]: https://www.npmjs.com
[AngularJS]: https://angularjs.org
