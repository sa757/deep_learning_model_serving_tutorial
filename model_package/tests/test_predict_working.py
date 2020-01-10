import math

from modeling_pipeline.predict import make_single_prediction


def test_make_single_prediction():
    # Given / When
    subject = make_single_prediction(image_name='1.png', image_directory='../datasets/test_data/Black-grass')
    print(subject)
    # Then
    assert subject is not None
    assert isinstance(subject.get('predictions')[0], int)
    assert isinstance(subject.get('readable_predictions')[0], str)

if __name__ == "__main__":
    test_make_single_prediction()

# def test_make_multiple_predictions():
#     # Given
#     test_data = load_dataset(file_name='test.csv')
#     original_data_length = len(test_data)
#     multiple_test_input = test_data
#
#     # When
#     subject = make_prediction(input_data=multiple_test_input)
#
#     # Then
#     assert subject is not None
#     assert len(subject.get('predictions')) == 1451
#
#     # We expect some rows to be filtered out
#     assert len(subject.get('predictions')) != original_data_length
