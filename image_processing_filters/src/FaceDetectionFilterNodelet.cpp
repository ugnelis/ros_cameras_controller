#include <pluginlib/class_list_macros.h>

#include "image_processing_filters/FaceDetectionFilterNodelet.h"

PLUGINLIB_EXPORT_CLASS(image_processing_filters::FaceDetectionFilterNodelet, nodelet::Nodelet)


namespace image_processing_filters {

FaceDetectionFilterNodelet::FaceDetectionFilterNodelet()
      : imageTransport_(),
        imagePublisher_(),
        imageSubscriber_(),
        faceCascadeString_() {
}

FaceDetectionFilterNodelet::~FaceDetectionFilterNodelet() {

}

void FaceDetectionFilterNodelet::onInit() {
    ros::NodeHandle &nodeHandle = getNodeHandle();
    ros::NodeHandle &privateNodeHandle = getPrivateNodeHandle();

    imageTransport_ = std::make_shared<image_transport::ImageTransport>(nodeHandle);
    imagePublisher_ = imageTransport_->advertise("face_detect", 1);
    imageSubscriber_ = imageTransport_->subscribe("image_raw", 1, &FaceDetectionFilterNodelet::imageCallback, this);

    privateNodeHandle.param<std::string>("classifier_file", faceCascadeString_, "haarcascade_frontalface_alt.xml");

    if(!faceCascade_.load(faceCascadeString_)) {
      ROS_ERROR_STREAM("error loading cascade classifier: " << faceCascadeString_);
    }
}

void FaceDetectionFilterNodelet::imageCallback(const sensor_msgs::ImageConstPtr &message) {
    cv_bridge::CvImagePtr cvImagePtr;
    try {
        cvImagePtr = cv_bridge::toCvCopy(message, sensor_msgs::image_encodings::BGR8);

    } catch (cv_bridge::Exception &e) {
        ROS_ERROR("cv_bridge exception: %s", e.what());
    }

    cv::Mat receivedImage = cvImagePtr->image;
    cv::Mat greyImage;
    cv::cvtColor(receivedImage, greyImage, CV_RGB2GRAY);

    //-- Detect faces
    std::vector<cv::Rect> faces;
    faceCascade_.detectMultiScale(greyImage, faces, 1.1, 2, 0|CV_HAAR_SCALE_IMAGE, cv::Size(30, 30));

    for( size_t i = 0; i < faces.size(); i++ )
    {
      cv::Point center(faces[i].x + faces[i].width * 0.5, faces[i].y + faces[i].height * 0.5);
      cv::ellipse(receivedImage, center,
                  cv::Size(faces[i].width * 0.5, faces[i].height * 0.5),
                  0, 0, 360, cv::Scalar( 255, 0, 255 ), 4, 8, 0);
    }

    // Prepare result ROS image.
    cv_bridge::CvImage resultCvImage;
    resultCvImage.header = cvImagePtr->header;
    resultCvImage.encoding = sensor_msgs::image_encodings::RGB8;
    resultCvImage.image = receivedImage;

    imagePublisher_.publish(resultCvImage.toImageMsg());
}

} // namespace image_processing_filters
