from sklearn.pipeline import Pipeline

from modeling_pipeline.config import config
from modeling_pipeline.processing import preprocessors as pp
from modeling_pipeline import model

model_pipeline = Pipeline([
    ('datasets', pp.CreateDataset(config.IMAGE_SIZE)),
    ('model', model.cnn_clf)
])