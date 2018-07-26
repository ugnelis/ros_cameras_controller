#include "video_stream_to_topic/VideoStreamToTopic.h"

namespace video_stream_to_topic {

VideoStreamToTopic::VideoStreamToTopic(ros::NodeHandle &nodeHandle)
        : nodeHandle_(nodeHandle)
        , imageTransport_(nodeHandle) {

    imagePublisher_ = imageTransport_.advertise("stream/image", 1);

    // Parameters.
    nodeHandle.param<std::string>("stream_url", streamUrl_, "http://192.178.1.13/mjpg/video.mjpg");
    nodeHandle.param<double>("loop_rate", loopRate_, 5.0);

    cv::VideoCapture videoCapture;

    videoCapture.open(streamUrl_);

    if (!videoCapture.isOpened()) {
        ROS_ERROR("The stream is not opened.");
        ros::requestShutdown();
    }

    cv::Mat frame;
    sensor_msgs::ImagePtr messageImagePtr;

    ros::Rate loopRate(loopRate_);

    while (nodeHandle.ok()) {
        videoCapture >> frame;

        // Check if grabbed frame is actually full with some content.
        if (!frame.empty()) {
            messageImagePtr = cv_bridge::CvImage(std_msgs::Header(), "bgr8", frame).toImageMsg();
            imagePublisher_.publish(messageImagePtr);
            cv::waitKey(1);
        }

        loopRate.sleep();
    }
}

VideoStreamToTopic::~VideoStreamToTopic() {

}

} // namespace video_stream_to_topic
