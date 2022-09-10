from loggers import logger
from fastapi import FastAPI, File, UploadFile, Form
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from mount import Swagger
from transformers import pipeline
import time


classifier = pipeline('sentiment-analysis')

app = FastAPI(docs_url=None, redoc_url=None,title='transformers 情感分析 API')

Swagger.doc(app)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/')
async def root():
    return {"message": "Hello World"}


@app.post('/text/')
def upload(text: str = Form()):

    try:
        logger.debug(f'收到请求: {text[:100]}')
        start = time.time()
        classifications: list[dict[str, str | float]] = classifier([text])
        end = time.time()

        return {
            'success': False,
            'data': classifications,
            'pay_time': round(end-start, 3)
        }
    except Exception as error:
        logger.exception(error)
        return {
            'success': False,
            'message': str(error)
        }


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8888, workers=1)
