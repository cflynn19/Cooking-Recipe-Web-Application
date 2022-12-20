import sys
sys.path.append('./Google_Cloud_Vision_API')
import google_cloud_vision_api_class

google_api = google_cloud_vision_api_class.google_cloud_vision_api()

def test_google_image_detection_simple_1():
    image_uri = 'https://img.freepik.com/free-photo/baked-chicken-wings-asian-style_2829-10159.jpg?w=2000'

    google_api.detect_label(image_uri)
    assert google_api.get_score('chicken') > 0.8
    google_api.print_label()

def test_google_image_detection_simple_2():
    image_uri = 'https://media-cldnry.s-nbcnews.com/image/upload/newscms/2020_27/1586836/hotdogs-te-square-200702.jpg'

    google_api.detect_label(image_uri)
    assert google_api.get_score('hot dog') > 0.8
