# ros_cameras_controller

## Overview

*ros_cameras_controller* uses already stream videos and helps them manages.

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
	
[Robot Operating System (ROS)]: http://www.ros.org
[OpenCV]: https://opencv.org
[Flask]: http://flask.pocoo.org
[npm]: https://www.npmjs.com
[AngularJS]: https://angularjs.org
