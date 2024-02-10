from src.views.https_types.http_request import HttpRequest
from src.views.https_types.http_response import HttpResponse

class TagCreatorView:
    '''
        Responsability from interacting with HTTP
    '''

    def validate_and_create(self, http_request: HttpRequest):
        body = http_request.body
        product_code = body["product_code"]

        # logica de regra de negocio
        print("Estou na minha view")
        # retorno http
        return HttpResponse(status_code=200, body={"Helo": "world"})
    