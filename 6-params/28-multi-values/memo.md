# **_Multiple Parameters_**

> Only the Query parameter can have multiple values, which will be presented as List type in the backend of fastapi.
> (However, the body parameter can also be set multiple times in the model, but it will be wrapped as a single object or JSON)

## **Model List type**

![Alt model list type](pic/09.jpg)

![Alt result - request](pic/10.jpg)

![Alt result - response](pic/11.jpg)

## **Set Default List values**

![Alt set defaul list values](pic/12.jpg)

- Very intuitive, since we will get a list, we set the default value directly to the list.

![Alt result](pic/13.jpg)
