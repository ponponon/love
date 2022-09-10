from transformers import pipeline
from loguru import logger

# Allocate a pipeline for sentiment-analysis
classifier = pipeline('sentiment-analysis')
classifications: list[dict[str, str | float]] = classifier([
    'fuck you! bitch',
    'We are very happy to introduce pipeline to the transformers repository.'
])

logger.debug(classifications)

# 输出结果
# ```shell
# 2022-09-10 22:53:14.805 | DEBUG    | __main__:<module>:11 - [{'label': 'NEGATIVE', 'score': 0.9966753721237183}, {'label': 'POSITIVE', 'score': 0.9996980428695679}]
# ```