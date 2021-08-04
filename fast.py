import uvicorn
from fastapi import FastAPI
from starlette.responses import FileResponse 

app = FastAPI()

@app.get('/')
def get_main_page(ean):
    print(ean)
    return FileResponse('get_book_information.html')

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=5000)