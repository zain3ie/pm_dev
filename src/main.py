from typing import List

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.predict import predict
from src.schema import Input


app = FastAPI(
    title='PMDS',
    docs_url='/',
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*', 'https://pmds-groupf.vercel.app'],
    allow_credentials=True,
    allow_headers=['*'],
    allow_methods=['*'],
)

@app.post('/predict')
async def main(input: List[Input]):
    result = predict(input).tolist()

    return result
