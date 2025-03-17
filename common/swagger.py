from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.openapi.utils import get_openapi
from fastapi.staticfiles import StaticFiles


def swagger_initialize(app, api_title):
    app.mount("/static", StaticFiles(directory="static"), name="static")



    @app.get("/docs", include_in_schema=False)
    async def custom_swagger_ui_html():
        return get_swagger_ui_html(
            openapi_url=app.openapi_url,
            title=api_title,
            swagger_js_url="/static/swagger-ui-bundle.js",
            swagger_css_url="/static/swagger-ui.css",
            swagger_favicon_url="/static/favicon.png",
        )
    
    @app.get("/openapi.json", include_in_schema=False)
    async def get_open_api():
        return get_openapi(title="My API", version="1.0.0", routes=app.routes)
    