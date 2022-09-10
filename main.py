from transformers import pipeline
from loguru import logger

# Allocate a pipeline for sentiment-analysis
classifier = pipeline('sentiment-analysis')
result = classifier([
    'fuck you! bitch',
    'We are very happy to introduce pipeline to the transformers repository.'
])

logger.debug(result)
