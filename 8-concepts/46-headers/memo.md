## **Request Headers**

### _Concept_

![Alt Request Headers](pic/01.jpg)

### _Coding_

![Alt create a new route with custom request header](pic/02.jpg)

### _Test_

![Alt test](pic/03.jpg)

### _List type_

> The difference between a normal type and a list type is whether the header can be used more than once in the same request.

![Alt change type of custom request header to List](pic/04.jpg)

### _Test_

![Alt test](pic/05.jpg)

## **Response Headers**

### _Concept_

![Alt Response Headers](pic/06.jpg)

- The request header is defined using the header constructor, while the response header is a new key-value pair added to response.headers, both of which are completely different.

### _Coding_

![Alt add custom response header](pic/07.jpg)

- The custom request header value is deliberately used as the join of the custom response header, in order to see if the custom request header is really a list btw.

### _Test_

![Alt test](pic/08.jpg)

## **Slightly Issue of Swagger UI**

> So from the above results we see a small problem with Swagger UI, so here we use Postman to test it instead.

![Alt test by postman](pic/09.jpg)
