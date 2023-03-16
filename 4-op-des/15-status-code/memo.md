## **Adding error scenarios**

![Alt add error condition](pic/01.jpg)

![Alt swagger test](pic/02.jpg)

- will automatically generate status code 200, if nothing is set.
- The status code represents the result of the operation function.
  - The client-side application relies a lot on the status code to determine what follow-up actions to take.

## **Set default status code**

![Alt set default status code](pic/03.jpg)

![Alt swagger test](pic/04.jpg)

- Obviously what we need is the ability to dynamically switch the status code based on the id value, so the default value is not enough.

## **status ns and Response type**

### _status ns_

![Alt import status](pic/05.jpg)

### _Response type_

![Alt Response type](pic/06.jpg)

### _test_

![Alt test 1](pic/07.jpg)

![Alt test 2](pic/08.jpg)
