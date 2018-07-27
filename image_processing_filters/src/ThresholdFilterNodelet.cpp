#include "image_processing_filters/ThresholdFilterNodelet.h"

#include <pluginlib/class_list_macros.h>

PLUGINLIB_EXPORT_CLASS(image_processing_filters::ThresholdFilterNodelet, nodelet::Nodelet)


namespace image_processing_filters {

ThresholdFilterNodelet::ThresholdFilterNodelet()
        : imageTransport_(),
          imagePublisher_(),
          imageSubscriber_() {

}

ThresholdFilterNodelet::~ThresholdFilterNodelet() {

}

void ThresholdFilterNodelet::onInit() {
    ros::NodeHandle &nodeHandle = getNodeHandle();
    ros::NodeHandle &privateNodeHandle = getPrivateNodeHandle();

    imageTransport_ = std::make_shared<image_transport::ImageTransport>(nodeHandle);
    imagePublisher_ = imageTransport_->advertise("threshold", 1);
    imageSubscriber_ = imageTransport_->subscribe("image_raw", 1, &ThresholdFilterNodelet::imageCallback, this);

    privateNodeHandle.param<int>("threshold_value", thresholdValue_, 100);
}

void ThresholdFilterNodelet::imageCallback(const sensor_msgs::ImageConstPtr &message) {
    cv_bridge::CvImagePtr cvImagePtr;
    try {
        cvImagePtr = cv_bridge::toCvCopy(message, sensor_msgs::image_encodings::BGR8);

    } catch (cv_bridge::Exception &e) {
        ROS_ERROR("cv_bridge exception: %s", e.what());
    }

    cv::Mat receivedImage = cvImagePtr->image;

    cv::Mat greyImage;
    cv::cvtColor(receivedImage, greyImage, CV_RGB2GRAY);

    // Apply threshold.
    cv::Mat thresholdImage;
    cv::threshold(greyImage, thresholdImage, thresholdValue_, 255, cv::THRESH_BINARY);
    cv::cvtColor(thresholdImage, thresholdImage, CV_GRAY2RGB);

    // Prepare result ROS image.
    cv_bridge::CvImage resultCvImage;
    resultCvImage.header = cvImagePtr->header;
    resultCvImage.encoding = sensor_msgs::image_encodings::RGB8;
    resultCvImage.image = thresholdImage;

    imagePublisher_.publish(resultCvImage.toImageMsg());
}

} // namespace image_processing_filters
