from typing import List
from fastapi import FastAPI

from src.predict import predict
from src.schema import Input


app = FastAPI(
    title='PMDS',
    docs_url='/',
)

@app.get('/predict')
async def main(input: List[Input]):
    result = predict(input).tolist()

    return result
