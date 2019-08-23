---
title: Intro to Validation, QA and the Universe
---
# Intro to Validation, QA and the Universe
### by Olgierd'd "allgreed" Kasprowicz

Note:
- adjust the notes font-size to 3em
<!--v-->

## If we can turn back time...
<img src="/img/tardis.png" style="background: 0; border: 0; box-shadow: none; width: 30%;"/>

<!--v-->

## ...to the good old days - 2010
![](/img/ac2.jpg)
<!-- .element: class="fragment fade-up" -->

Note:
- junior high
- playing Assasin's creed 2
- by Ubisoft.
- (one of) first always-online DRM
- probably had saves in the cloud too.
<!--v-->

![](/img/witcher-mem.png)

<!--v-->
![](/img/bsod.jpg)

Note:
- lost my saves as well :C

<!--v-->
### Boo hoo!

![](img/cry.gif)

Note:
- make a fun of how insignificant my loss was
- first time I was deeply disappointed with computers

<!--s-->

## Current state of affairs

<!-- disclaimer + whoami + info -->
I work at Intel, but I'm **not** representing Intel today.

All your opinions are belong to us.

- source: [github.com/allgreed/presentations](https://github.com/allgreed/presentations)
- questions: during (and after as well!)
- shitstorm: after
- feedback: much appreciated 

Note:
- I somehow finish junior high, time goes on.
- Mentioned I work at Intel? xD
- Law student joke ^^
- All opinions belong to me or whatever was written.
<!--v-->
### The machine?

<img src="/img/eniac.jpg" style="width: 70%;" />

Note:
- few women in a lab. cheerful, well-dressed
- note on security: closed toe shoes.
- behind them
- you know this machine, but the look different nowadays
- eniac - a computer.
<!--v-->

<!-- pic of laptop, telephone and car -->
<img src="/img/c0.jpg" style="width: 30%;" class="fragment" />
<img src="/img/c1.jpg" style="width: 45%;" class="fragment" />
<img src="/img/c2.jpeg" style="width: 45%;" class="fragment" />
<img src="/img/c3.jpeg" style="width: 45%;" class="fragment" />

Note: 
- TP x200 tablet - computer that can display images and play sounds
- Iphone Se - can spy on you + make calls
- Tesla Roadster - weights ~1200 kg (1/2 of an asian elephant) ~300 HP
- computer that accelerates elementary particles

<!--v-->

![](/img/hackercodexd.jpg)

Note:
- what's running on all those computer?
- software!
- we better hope it's a good software
- it's jQuery actually on that picture xD
- oops xD

<!--s-->

## Vilans

<img src="/img/bug.jpg" style="width: 45%;" />
<img src="/img/defect.jpg" style="width: 45%;" />

Note:
- bugs and defects

<!--v-->

### What is ...?
- App <span class=fragment>-> collection of behaviours</span>
- Bug <span class=fragment>-> behaviour that is unexpected by the user</span>
- Defect <span class=fragment>-> deviation from the spec</span>
- Error <span class=fragment>-> bug | defect</span><span class=fragment> - colloquially</span>
- Love <span class=fragment>-> baby, don't hurt me.</span> <span class="fragment">no more.</span>

Note:
- bug might be a feature
- defect might not be bug.
- error -> overloaded :C

<!--v-->

<img src="/img/comememe.jpg" style="width: 45%;" />

Note:
- you might be like: come at me bro!

<!--v-->

### Software is hard - modern software stack

- <span class=fragment>CPU</span>
- <span class=fragment>magic? (type "ring -3" into wikipedia)</span>
- <span class=fragment>kernel (eg. Linux)</span>
- <span class=fragment>shared libraries (eg. glibc)</span>
- <span class=fragment>runtime (eg. cPython)</span>
- <span class=fragment>libraries </span>
- <span class=fragment>framework (eg. Django)</span>
- <span class=fragment>Your code</span>

Note: 
- do a joke about your code in the next step
- each step is complex, evolved through years and has shit-ton of code
- add all the networking stack if you're doing webapps

<!--v-->
### Abstraction to the rescue?

![](/img/duck.jpg)

Note:
- walks like a duck
- quacks like a duck
- needs batteries xD
- Nope, it won't!

<!--v-->
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


<pre><code class="nohighlight" style="background: #3f3f3f" data-noescape>Raw value: 1
Absolute value: 1
Raw value: -5
Absolute value: 5
Raw value: -2147483648
Absolute value: <span class="fragment highlight-red" data-fragment-index="2">-2147483648
</span></code></pre>
<!-- .element: class="fragment fade-up" data-fragment-index="1" -->

Note:
- some code in high level programming language

<!--v-->

- [Gynvael Coldwind on the matter](https://www.youtube.com/watch?v=hcp9ymfbofs&t=16m)

<!--v-->
#### Java good, si?
```
public class JavaGood
{
    public static void main(String []args)
    {
        System.out.println(Math.abs(-2147483648));
    }
}
```
```
-2147483648 // Nope xD
```
<!-- .element: class="fragment fade-up"  -->

Note:
- I'd show you a JS version, but I'm gonna ignore BigInt and make fun that JS doesn't have integers
- This kind of quircks are COUNTLESS!!!
- You can never make mistake (but you do!) and still have defects

<!--s-->
### Let's talk quality

<img src="/gen/thisor.png" style="width: 45%;" />
<img src="/gen/thator.png" style="width: 45%;" />

Note: bug detection at certain stages - which one is better?
Shit breaks == bug detected in production

<!--v-->

### Definition of crap
![](/gen/crap.png)

<!--v-->
### The ultimate fix
![](/gen/hehfix.png)

Note: this will work, 100%, right?

<!--v-->
### Law of diminishing returns

![](/img/pizza.jpg)

Note:
- Sheryl Sandberg - "Finished is better than perfect"
- Pareto rule

<!--v-->

![](/gen/realhehfix.png)

Note:
- now - this is uber, oui?

<!--v-->
### What IBM did...

<div style="max-height: 180px; overflow: hidden;">
<img src="/img/ibm-study-bug-cost.jpg" />
</div>

<small>[full study](ftp://ftp.software.ibm.com/software/rational/info/do-more/RAW14109USEN.pdf)</small>

Note:
- cost of rework,
- Mariner 1,
- 1962, $18.5 million
- attributed to missing comma or extraneous semicolon

<!--v-->
### What do we trully desire :3

![](/gen/desired.png)

Note:
- this is too single-minded however

<!--v-->
### Bugs not created equal

![](img/many-bugs.jpg)

Note:
- specs -> more fine grained => more potential for defects
- because bugs are added and effectively caught at different stages

<!--v-->

### What we'll get

![](/gen/real.png)

Note:
- you can't sleep in advance!

<!--s-->
## The heroes
<img src="/img/venn.png" style="background: 0; border: 0; box-shadow: none"/>

Note:
- Validation - fighting defects
- Testing - fighting bugs
- QA - making the other 2 bearable
<!--s-->

### Let the testers do the testing!

![](gen/testers.png)

Note:
- before we begin - some groud rules for validation.
- Tester -> testing.
- You -> validation.

<!--v-->

### Manual validation? Nope.

![](img/robot.jpeg)
Note:
- robots >> humans at certain tasks.
- pick and place robot - 150 elements per minute with superb accuracy.
- reduces regressions to minimum.
<!--v-->
 
### Why not validate?

<img src="/img/orly.png" style="width: 30%" />

<!--v-->
### The excuses

- <span class=fragment>time pressure</span><span class="fragment"> -> you'll have to get it right anyway</span>
- <span class=fragment>it's hard</span><span class="fragment"> -> **IT is hard**, deal with it</span>
- <span class=fragment>it's teadious</span><span class="fragment"> -> you're doing it wrong</span>
- <span class=fragment>your spirits are crushed</span><span class="fragment"> -> <a href="https://dzone.com/articles/why-wouldnt-you-write-unit-tests">this is real ^^</a></span>
- <span class=fragment>I don't know how!!!</span><span class="fragment"> -> that's a valid one :)</span>

Note:
- engineering -> responsibility + hard craft
<!--s-->
## So... how to validate?
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

Note:
- console.log() is **not** a testing framework
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
```js
const fib = n =>
  n < 2
  ? n
  : fib_matrix_power([1, 1, 0], n - 1)[0];

const fib_matrix_power = (matrix, n) =>
  matrix_times(...new Array(n).fill([1, 1, 0]));

const matrix_times = (...matrices) =>
    matrices.reduce(
        ([a,b,c], [d,e,f]) => [a*d + b*e, a*e + b*f, b*e + c*f]
    );
```

Note:
- Previous implementation was O(2^n), this is O(n) and can be O(log n)
- Does it work?
- Do you have to understand the code?
- Nope! Just run the test suite

<!--s-->

## That was cute

<pre><code style="background: #3f3f3f" data-noescape>function processInvoice(customerID, amount)
{
    const customer = <span class="fragment highlight-blue">await DB.getCustomerbyID(customerID)</span>

    ... // business stuff with lots of ifs, for loops - etc.
          
    await <span class="fragment highlight-blue">stripe.charge(customer.stripeAccount, amount)</span>

    await <span class="fragment nohiglight highlight-blue">pushNotification.send(customer)</span>

    await <span class="fragment highlight-blue">sendEmail()</span>
}
</code></pre>

Note:
- the simple examples != production code
- Because production code is rarely pure function
- !No error handling for the sake of demo

<!--v-->

### Let's monkey patch:

- <span class="fragment">database cursor, push notification</span>
- <span class="fragment">http request to Stripe, email provider</span>
- <span class="fragment">built-in Javascript constructs - Promise monad</span>
- <span class="fragment">ropjar flopnaxer</span>
- <span class="fragment">kernel printer driver</span>

<h1 style="color: #dc322f;" class="fragment">NOPE!</h1>
Note:
- unmaintainable madness!

<!--v-->

![](img/square-peg-round-hole.jpeg)


Note:
- Square Peg Round Hole, almost like 2 girls... xD
- Kwadratowy sworzeń okrągły otwór

<!--v-->
### Test vs. testable code
> There cannot be good laws without good armies, and where there are good laws, there must be good arms, so I he will only discuss arms, not laws.
>
> ~ Niccolò Machiavelli

Note:
- Test -> testable code;
- Testable code -> tests;
- I'll talk about testable code

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
Note:
- but this is just a trick
- sometimes it works, sometimes it doesn't
<!--v-->

### Why we test?
```
function processInvoice(customerID, amount)
{
    const customer = await DB.getCustomerbyID(customerID)
    await stripe.charge(customer.stripeAccount, amount)
    await pushNotification.send(customer)
    await sendEmail()

    // business stuff deliberately ommited
}
```
Note: cyclomatic complexity: 1 => only one path to go through the code
<!--v-->
```
function processInvoice(customerID, amount)
{
    const customer = await DB.getCustomerbyID(customerID)

    const invoiceCalculations = calculateInvoiceStuff(customer)

    await stripe.charge(customer.stripeAccount, amount)
    await pushNotification.send(customer)
    await sendEmail()
}
```
```
function calculateInvoiceStuff(customer: Customer)
{
    ... // business stuff with lots of ifs, for loops - etc.
    
    return something
}
```

Note:
- dependency inversion principle - calculation only relies on Customer
- separate IO from business
- have pure functions!

<!--v-->
### IO works

- <span class="fragment highlight-green">HTTP</span>
- <span class="fragment highlight-green">emails</span>
- <span class="fragment highlight-red">that lad's code, in the back</span>
- <span class="fragment highlight-green">writing text to a file</span>
- <span class="fragment highlight-red">your code</span>

Note:
- what definitely works?
<!--s-->

## But I wanna validate IO!

- does my <span class="fragment highlight-blue" data-fragment-index="1">module</span> work -> <span class="fragment highlight-blue" data-fragment-index="1">unit</span> test
- does my module work <span class="fragment highlight-blue" data-fragment-index="2">with X</span> -> <span class="fragment highlight-blue" data-fragment-index="2">integration</span> test
- did I glue <span class="fragment highlight-blue" data-fragment-index="3">all the stuff</span> correctly -> <span class="fragment highlight-blue" data-fragment-index="3">E2E</span> test

Note:
- maybe only do E2E?
- validating IO is slow and hard to maintain - don't abuse
- but sometimes it makes sense
<!--v-->

<img src="/img/hex.jpg" style="width: 50%;" />
<span class="fragment">hexagonal architecture</span>

Note:
- aren't my new bathroom tiles just plain... awesome? :D
- hexagonal architecture - separating logic from IO app-wide
- making it easy to validate
- there are books and presentations about that
<!--s-->

## Can we transcend units?
<!--v-->
### Of course - data-driven / parametrized tests

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

<!--v-->
### Property based tests

```
const fc = require('fast-check');
...

describe('contains', () => {
    it('should always contain b in a+b+c', () =>
        fc.assert(
            fc.property(
                fc.string(), fc.string(), fc.string(),
                (a, b, c) => 
                    contains(b, a + b + c))));
});
```
<!--v-->

### Stateful property based tests

<img src="/img/tess.jpeg" style="width: 50%" />

Note:
- uses a simpler model to assert stuff about a stateful system

<!--v-->

### Now I'm just rambling

- tdd / bdd
- pair programming
- algebraic datatypes - haskell & rust
- idris - dependant types
- tla+

<!--s-->

## Key takeaways

- make your code testable
- test
- teach others how to test

<!--v-->
### Explore, dream, discover
~ Mark Twain

<img src="/img/mark.jpeg" style="width: 30%" />

<!--s-->
# Fin

<!--v-->
## Questions?

### Contact me!
- physically in HS3
- @allgreed on HS3 Slack / Freenode
- <span style="direction: rtl;unicode-bidi: bidi-override;">orp.zciworpsak@dreiglo</span>

Note: 
- talk, walk, trade, dine, hang
