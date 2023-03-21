## **What is exception**

![Alt what is exception](pic/01.jpg)

- Even if there are many layers, raising an exception at any one layer will abort the entire codes operation.

## **Use HTTPException to handler non-existed id**

> In some cases, even if we think it's an exception, we still get status code = 200, so we have to raise the exception manually to get the correct message to the client.

### _articles_

![Alt goal: handle non id](pic/02.jpg)

![Alt raise HTTPException manually in articles](pic/03.jpg)

![Alt test](pic/04.jpg)

### _users_

![Alt users func](pic/05.jpg)

![Alt raise HTTPException manually in users](pic/06.jpg)

![Alt test](pic/07.jpg)

## **Custom Exception and its handler**

> Sometimes we need to do more specific things in the exception, we can customize the exception.

![Alt if we don't want story content in article](pic/08.jpg)

![Alt create a custom exc for it and raise it](pic/09.jpg)

- We use a simple custom exception here for explanation, but in reality, custom exceptions are needed only when there are really special requirements, otherwise HTTPException is enough.

![Alt test input](pic/10.jpg)

![Alt test result](pic/11.jpg)

![Alt console error](pic/12.jpg)

### _Exception Handler_

![Alt handler for it](pic/13.jpg)

![Alt test](pic/14.jpg)

## **Custom handler for HTTPException**

> This will change the way most exceptions are handled except for custom exceptions.

![Alt custom handler for HTTPException](pic/15.jpg)

![Alt test](pic/16.jpg)
