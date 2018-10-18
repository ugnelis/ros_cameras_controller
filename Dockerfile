FROM ros:kinetic-ros-base

# Install libraries and tools.
RUN apt-get update \
  && apt-get install -y wget \
  && wget -qO- https://deb.nodesource.com/setup_8.x | bash - \
  && apt-get install -y \
    ros-kinetic-web-video-server \
    ros-kinetic-rosbridge-suite \
    python-pip \
    nodejs \
  && pip install Flask

WORKDIR /catkin_ws

# Copy over required source files.
COPY web_console src/web_console
COPY commander src/commander

# Build the source files.
RUN bash -c 'source /opt/ros/kinetic/setup.bash; catkin_make'

# Setup image entry point.
COPY entrypoint.sh /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh", "roslaunch"]
