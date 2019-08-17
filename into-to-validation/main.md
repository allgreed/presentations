---
title: Intro to Validation, QA and the Universe
---
# Intro to Validation, QA and the Universe
### by Olgierd'd "allgreed" Kasprowicz
<!--v-->

## If we can turn back time...
<!-- pic of tardis -->

<!--v-->

## ...to the good old days
<!-- pic of old computers / people -->

<!--s-->

## Disclaimer
I work at Intel, but I'm not representing Intel today. All opinions are my own.

<!--s-->

## Current state of affairs
<!-- pic of laptop, telephone and car -->
Note: 
- computer
- computer that can make calls
- computer that can drive
<!--v-->
### The stack
http://chickencrap.com/media_images/2058.jpg
<!--v-->
### Abstraction leakage
<!-- TODO: quote about duck that needs bateries -->

<!--v-->
#### Example
```c
#include <stdlib.h>
#include <stdio.h>

int main()
{
    const int numbers[] = { 1, -5, -2147483648 };
    
    for (int i = 0; i < (sizeof numbers / sizeof (int)); ++i) {
        int num = numbers[i];
        printf("Raw value: %d\n", num);
        printf("Absolute value: %d\n", abs(num));
    }

}

```

```
Raw value: 1
Absolute value: 1
Raw value: -5
Absolute value: 5
Raw value: -2147483648
Absolute value: -2147483648
```

<!--v-->
#### Explanation
TODO

<!--v-->
#### Java good
TODO


<!--s-->
## What is ...?
- Love <span class=fragment>-> baby, don't hurt me.</span> <span class="fragment">no more.</span>
- App <span class=fragment>-> collection of behaviours</span>
- Bug <span class=fragment>-> behaviour that is unexpected by the user</span>
- Defect <span class=fragment>-> deviation from spec</span>

Note: "Our app has 3 bugs and 4 defects"
bug might be a feature, and defect might not be bad

<!--s-->
## Let's talk quality

QA, validation, testing - venn
+ spot indicating the covered topics

<!--s-->
## ...
<!--s-->
## Ok, but how?
<!--v-->

### The spec
- function that returns n-th number of Fibonacci sequence
<!--v-->

### The testing framework
```js
type TestFn = () => bool

tests: Array<TestFn> = [
    ...
]

for (const test of tests)
{
    if (! test())
    {
        process.exit(8)
    }
}
```
<!--v-->

### The test
```js
function fib(n: number): number { ... }  // interface

const testFibbonachiFunction = () => {
    return fib(8) === 21
}

const tests = [ testFibbonachiFunction ]

for (const test of tests)
{
    if (! test())
    {
        process.exit(8)
    }
}
```
<!--v-->

### The code
```js
function fib(n) {
    if (n == 0) return 0
    if (n == 1) return 1

    return fib (n - 1) + fib (n - 2)
}
```
```
const testFibbonachiFunction = () => {
    return fib(8) === 21
}

const tests = [ testFibbonachiFunction ]

for (const test of tests)
{
    if (! test())
    {
        process.exit(8)
    }
}
```

<!--v-->
### Production grade - with Jest
```js
function fib(n) {
    if (n == 0) return 0
    if (n == 1) return 1

    return fib (n - 1) + fib (n - 2)
}

test("fib(n) returns n-th number of the fibbonachi sequence",
    () => {
        expect(fib(8)).toBe(21);
});
```

<!--v-->

### Refactor! Refactor all the things!

- TODO

<!--s-->

## That was cute

```js
function processInvoice(clientID, amount)
{
    const dbClient = await DB.getClientbyID(clientID)
          
    await stripe.charge(dbClient.stripeAccount, amount)
        .catch(err => {
            console.error("Pay up!") 
        })

    const message = `Successful payment for ${}`
    await pushNotification.send(client.activeSessions, message)

    await sendEmail()
}
```
Note: the simple examples != production code
Because production code is rarely pure function

<!--v-->

### Let's monkey patch:
- database
- http request to Stripe
- console.log()
- email

# NOPE! <!-- TODO: red + slide -->

<!--v-->
### Test vs. testable code
> There cannot be good laws without good armies, and where there are good laws, there must be good arms, so I he will only discuss arms, not laws.
>
> ~ Niccolò Machiavelli

Note: Test -> testable code; Testable code -> tests; I'll talk about testable code

<!--v-->
### Dependency Injection

```js
function processInvoice(clientID, amount,
    DB = psqlConnection,
    stripe = stripeClient,
    console = console,
    pushNotification = socketIOManager,
    sendEmail = sendGridProviderController,
)
{
    ... // pure function now :D
}
```
<!--v-->

### Boundaries

- repositories
- reference the presentation about test boundaries
- TODO

<!--v-->
### Hexagonal architecture

- TODO

<!--s-->

## Technically

- what we just did === unit test
- unit test + setup === integration test
- integration test + more setup === E2E test
<!--v-->

### But...

<!--s-->

## Can we do better?
<!--v-->
### Of course - data-driven tests

```js
test("ein", () => {
    expect(fib(0)).toBe(0);
});

test("zwei", () => {
    expect(fib(1)).toBe(21);
});

test("drei", () => {
    expect(fib(8)).toBe(21);
});

test("zwei", () => {
    expect(fib(9)).toBe(34);
});
```
<!--v-->
```js
const each = require('jest-each').default;

...

each([
    [0, 0],
    [1, 1],
    [8, 21],
    [9, 34]
])
.test("fib(%d) == %d", (n, expected) => {
    expect(fib(n)).toBe(expected);
  }
);
```

