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
<!-- TODO -->

<!--v-->
#### Java good
<!-- TODO: java example -->

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
### Technically

- what we just did === unit test
- unit test + setup === integration test
- integration test + more setup === E2E test
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

