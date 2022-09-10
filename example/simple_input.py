from transformers import pipeline
from loguru import logger

# Allocate a pipeline for sentiment-analysis
classifier = pipeline('sentiment-analysis')
classifications: list[dict[str, str | float]] = classifier(
    'We are very happy to introduce pipeline to the transformers repository.')

logger.debug(classifications)

# 输出结果
# ```shell
# 2022-09-10 21:28:21.032 | DEBUG    | __main__:<module>:8 - [{'label': 'POSITIVE', 'score': 0.9996980428695679}]
# ```
