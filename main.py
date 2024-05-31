from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get('/items/')
def get_hello():
    return 'hello world'


@app.get('/items/{item_id}/')
def get_itm_by_id(item_id: int):
    return {
        'item': {
            'id': item_id,
        }
    }


if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)
