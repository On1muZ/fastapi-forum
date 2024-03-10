import uvicorn
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastui import prebuilt_html

app = FastAPI(root_path='/api', debug=True)


@app.get('/{path:path}')
async def html_landing() -> HTMLResponse:
    return HTMLResponse(prebuilt_html(title='Forum'))


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
