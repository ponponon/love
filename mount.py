from fastapi import FastAPI, File, Form, UploadFile
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.docs import (
    get_redoc_html,
    get_swagger_ui_html,
    get_swagger_ui_oauth2_redirect_html,
)
from mark import BASE_DIR


app = FastAPI(docs_url=None, redoc_url=None)


class Swagger:
    @classmethod
    def doc(self, app: FastAPI) -> None:
        app.mount(
            '/static',
            StaticFiles(directory=BASE_DIR / 'static'/'swagger-ui'),
            name='static'
        )
        @app.get("/docs", include_in_schema=False)
        async def custom_swagger_ui_html():
            return get_swagger_ui_html(
                openapi_url=app.openapi_url,
                title=app.title + " - Swagger UI",
                oauth2_redirect_url=app.swagger_ui_oauth2_redirect_url,
                # swagger_js_url=BASE_DIR/'static'/'swagger-ui'/'swagger-ui-bundle.js',
                # swagger_css_url=BASE_DIR/'static'/'swagger-ui'/'swagger-ui.css',
                swagger_js_url="/static/swagger-ui-bundle.js",
                swagger_css_url="/static/swagger-ui.css",
            )

        @app.get(app.swagger_ui_oauth2_redirect_url, include_in_schema=False)
        async def swagger_ui_redirect():
            return get_swagger_ui_oauth2_redirect_html()

        @app.get("/redoc", include_in_schema=False)
        async def redoc_html():
            return get_redoc_html(
                openapi_url=app.openapi_url,
                title=app.title + " - ReDoc",
                redoc_js_url="/static/redoc.standalone.js",
            )
