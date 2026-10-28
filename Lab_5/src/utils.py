import numpy as np
import cv2
from functools import cmp_to_key
import matplotlib.pyplot as plt
from typing import List


def build_vocabulary(dataset: List[str], vocabulary: str = 'vocabulary', feature_type: str = 'SIFT', size: int = 100, iterations: int = 20):
    """Build a vocabulary.

    Args:
        dataset: Paths to the training images.
        vocabulary: Relative path to the file (without extension) where the vocabulary will be saved.
        feature_type: Feature extractor { SIFT, KAZE }.
        size: Number of words in the vocabulary.
        iterations: Maximum number of K-means iterations.

    """
    bow = BoW()
    bow.build_vocabulary(dataset, feature_type=feature_type, vocabulary_size=size, iterations=iterations)
    bow.save_vocabulary(vocabulary)

def train_classifier(dataset: List[str], vocabulary: str = 'vocabulary', classifier: str = 'classifier', iterations: int = 100):
    """Train an SVM classifier.

    Args:
        dataset: Paths to the training images.
        vocabulary: Relative path to the vocabulary file (without extension).
        classifier: Relative path to the file (without extension) where the classifier will be saved.
        iterations: Maximum number of SVM iterations.

    """
    bow = BoW()
    bow.load_vocabulary(vocabulary)

    image_classifier = ImageClassifier(bow)
    image_classifier.train(dataset, iterations=iterations)
    image_classifier.save(classifier)

def predict(dataset: List[str], dataset_name: str = "", vocabulary: str = 'vocabulary', classifier: str = 'classifier'):
    """Perform inference on a dataset.

    Args:
        dataset: Paths to the images.
        dataset_name: Dataset descriptive name.
        vocabulary: Relative path to the vocabulary file (without extension).
        classifier: Relative path to the classifier file (without extension).

    """
    bow = BoW()
    bow.load_vocabulary(vocabulary)

    image_classifier = ImageClassifier(bow)
    image_classifier.load(classifier)
    image_classifier.predict(dataset, dataset_name=dataset_name) 

