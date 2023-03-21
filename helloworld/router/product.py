from typing import List, Optional
from fastapi import APIRouter, Header, Response, status
from fastapi.responses import HTMLResponse, PlainTextResponse


router = APIRouter(
        prefix='/product',
        tags=['product']
        )

products = ['watch', 'table', 'computer']

@router.get('/withheader')
def get_products(response: Response, cust_header: Optional[List[str]] = Header(None)):
    if cust_header:
        response.headers['cust_res_header'] = " and ".join(cust_header)
    return products


@router.get('')
def get_all_products():
    data = ' '.join(products)
    return Response(content=data, media_type="text/plain")

@router.get('/{id}', responses={
    200: {
        "content": {
            "text/html": {
                "example": "<div>Product</div>"
                }
            },
        "description": "Return the HTML for an object"
        },
    404: {
        "content": {
            "text/plain": {
                "example": "Product not available"
                }
            },
        "description": "A cleartext error message"
        },
    })
def get_product(id: int):
    if id > len(products):
        return PlainTextResponse('Product not available', status_code=status.HTTP_404_NOT_FOUND)

    product = products[id]
    out = f"""
    <head>
        <style>
        .product {{
            width: 500px;
            height: 30px;
            border: 2px inset green;
            background-color: lightblue;
            text-align: center;
            }}
        </style>
    </head>
    <div class="product">{product}</div>
    """
    return HTMLResponse(content=out)

