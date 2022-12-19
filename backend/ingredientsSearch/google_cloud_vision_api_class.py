from __future__ import print_function
from google.cloud import vision
import os

class google_cloud_vision_api:

    def __init__(self):
        # Get the Google API key
        os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = './ingredientsSearch/google-api-key.json'
        # Setup the caller
        self.client = vision.ImageAnnotatorClient()
        self.image = vision.Image()

    # Call Google API to get labels from image's url, store and return it
    def detect_label_from_url(self, image_uri):
        self.image.source.image_uri = image_uri

        response = self.client.label_detection(image=self.image)

        label_and_score = {}
        for label in response.label_annotations:
            label_and_score[label.description] = round(label.score, 3)

        self.label_and_score = label_and_score

        return self.label_and_score

    # Get labels using the locally existing image
    def detect_label_from_local(self, image_path):
        import io
        client = vision.ImageAnnotatorClient()
        with io.open(image_path, 'rb') as image_file:
            content = image_file.read()
        image = vision.Image(content=content)

        response = self.client.label_detection(image=image)

        label_and_score = {}
        for label in response.label_annotations:
            label_and_score[label.description] = round(label.score, 3)

        self.label_and_score = label_and_score

        return self.label_and_score

    # Helper function to beautify printing the labels
    def print_label(self):
        print('Labels (and confidence score):')
        print('=' * 30)
        for key in self.label_and_score.keys():
            print(key + " : " + str(self.label_and_score[key]))

    # Return all labels
    def get_labels(self):
        temp = []
        for key in self.label_and_score.keys():
            temp.append(key)
        return temp

    # Return the confidence score of the input label
    def get_score(self, label: str):
        for key in self.label_and_score.keys():
            if (label.lower().strip() in key.lower()):
                return self.label_and_score[key]
        return -1


# pip install google-cloud-vision
# python3 GoogleCloudVisionAPI.py