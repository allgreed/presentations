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
