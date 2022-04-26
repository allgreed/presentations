---
title:  Common Makefile Interface
---
# Somsiedzie jak to się włancza?
### by Olgierd'd "allgreed" Kasprowicz

<!--v-->

## Disclousure
![](./img/pracka-logo.png)
Note: pracuję w Dyna. Wszystkie opinie należą do ich właścicieli.

<!--v-->
## Source
### github.com/allgreed/presentations/$title
![](./img/qr.png)


<!--s-->

## Historyjka
Note: pewnego dnia poszedłem sobie do pracki

<!--v-->
![](./img/pracka-budynek.jpg)
Note: O tutaj, widać stąd mój dom! I zacząłem dzień od...

<!--v-->
![](./img/kafka.jpg)
Note: Kawki

<!--v-->
![](./img/jira.png)

<!--v-->
![](./img/kawka.jpg)

<!--v-->
## czerwone jest szybsze
![](./img/math.gif)
[PS to prawda](https://www.quora.com/Which-color-of-light-moves-fast-red-or-violet)
Note: czerwone jest szybsze, więc wystarczy pomalować front na czerwono

<!--v-->
![](./img/franz.jpg)
Note: kim jest ten człowiek?

<!--v-->

```
git clone git.korpo-serwer.work/jakiśkomponent/frontend
```

<!--v-->

![](./img/pulp.gif)
<!--TODO: colour gif-->

<!--v-->
```
cat README.md
```

<!--v-->
![](./img/readme.jpg)
Note: niezbyt pomocne, nieczytelne i pewnie antyczne, to może zagadamy z autorem

<!--v-->
![](./img/git.png)
Note: szwagier dostał awans... na CTO Wallmarta. Żartuję, na klienta firmy.

<!--v-->
Intentionally left blank

<!--v-->
![](./img/npmstart.png)

<!--v-->
![](./img/hacking.gif)

<!--v-->
![](./img/yay.gif)

<!--v-->

<!--v-->
![](./img/junior.webp)

<!--v-->
![](./img/cj.jpg)

<!--s-->
![](./img/shame-got.gif)

Note: ogólnie trochę cringe, że to tak wygląda
<!--v-->

czas zestawienia projektu * ilość osób

Note:
i zadziwiająco sporo osób ma problem ze stawianiem projektu:
- onboarding
- devops (jestem tu tylko na chwilę)
- open source
- techniczny P[roduct] M
- Ty z przyszłości, nowy laptop kto tam

- czas cykli i opportunity cost

- kalkulator - smutna buźka

- zmiana paradygmatu, Unix, Smalltalk z Xerox Parc, dynamicznie przeładowywalny kod
<!--s-->

## Rozwiązanie?
Note: czy to jest problem programistyczny?
<!--v-->

![](./img/deeper.webp)
Note: programowanie o programowanie -> metaprogramowanie
<!--v-->

![](./img/p0.png)
<!--v-->
![](./img/p1.png)
<!--v-->
![](./img/p2.png)
<!--v-->
![](./img/p3.png)
<!--v-->
![](./img/p4.png)
<!--v-->
![](./img/p5.png)

<!--v-->
![](./img/yay.gif)

<!--s-->
![](./img/triz.png)
Note: a mówią, że Triza nie da się stosowa 

<!--v-->
# Makefile

<!--v-->
```Makefile
# Makefile
.xPHONY: ble
ble:
	echo aloha
	echo mordeczki

.PHONY: fuj
fuj:
	echo siemanejro
```

```sh
>_ make ble
echo aloha
aloha
echo mordeczki
mordeczki

>_ make fuj
echo siemanejro
siemanejro
```

<!--v-->

## Idea
```Makefile
.PHONY: run build test

run: setup ## run the app
	@echo "Not implemented"; false

build: setup ## create artifact
	@echo "Not implemented"; false

test: setup ## run all tests
	@echo "Not implemented"; false

...
```

<!--s-->

## Make

Note: 
- późne lata 70, głównie używany do budowania projektów w C/Cpp
- stabilny, efekt Lindy
- relatywnie praktyczny, te funkcje nie są konieczne

<!--v-->

## Dependnecies
```Makefile
# Makefile
.PHONY: run build
run: build
    @echo odpalam
    # '@' <- prefix, don't output command

build:
	@echo buduję
```

```sh
>_ make run
buduję
odpalam
```

<!--v-->
## Files
```
# Makefile
.PHONY: run ble fuj
# targets run, ble and fuj are not files
run: a
	@echo odpalam

a:
	@echo buduję A
	touch a
```

```sh
>_ make run
buduję A
touch a
odpalam
>_ make run
odpalam
```

Note: uważny obserwator, kolejność nie jest istotna
<!--v-->

## Varaibles
```Makefile
# Makefile
.PHONY: ble fuj

CC := gcc
SIMPLE := zog
COMPLEX := --siema -x=$(SIMPLE)

ble: b
	$(CC) a $(COMPLEX)
 
fuj: a
	$(CC) b
```

```sh
>_ make ble
gcc a --siema -x=zog
# ... gcc output omitted
```
<!--v-->

## Reflection
```Makefile
# Makefile
.PHONY: help run
run: ## run the app
    @echo odpalam

help: ## print this message
	@grep -E ... $(MAKEFILE_LIST) | awk ...
.DEFAULT_GOAL := help
```

```sh
>_ make run
odpalam
>_ make
run                            run the app
help                           print this message
```
<!--v-->

## Misc
```Makefile
COMPONENTS := cli graph ui
init: $(addsuffix _init, $(COMPONENTS))
	@echo initalizing

define component_init
.PHONY: $(1)
  $(1)_init:
	ls $(1)
endef

$(foreach c, \
	$(COMPONENTS), \
	$(eval \
		$(call component_init,$(c))))
```

```sh
# originally it was not `ls`, but you get the point
>_ make
ls cli
ls graph
ls ui
initalizing
```
Note:
- tak, nie ma 'PHONY' i dalej działa
- to był produkcyjny kod
- to, że można nie znaczy, że się powinno

<!--v-->
Note:
- istnieje, może być coś inne w przyszłości
- stary, sprawdzony, wyspecyfikowany
- przydatny, sporo użytecznych funkcji, sporo dziwnych również :D

<!--s-->
## Example
### Digitalocean Token Scoper

<!--v-->
```Makefile
PORT=8080
LINTFLAGS := -e -s
...

run: secrets setup ## run the app
	APP_PERMISSIONS_PATH=./example.yaml \
    APP_LOG_LEVEL=debug \
    APP_LOG_FORMAT=text \
    APP_PORT=$(PORT) \
    ... \
    go run -mod=readonly $(SOURCES)

lint: setup ## run static analysis
	gofmt $(LINTFLAGS) -w .
```

<!--v-->
```Makefile
CLIENT_SECRET=aaaa
secrets: secrets/users/joe/secret ...

...

secrets/users/joe/secret:
	mkdir -p secrets/users/joe
	echo "$(CLIENT_SECRET)" > $@

interact: ## helper process to run predefined inputs
	curl ... -H "Authorization: Bearer $(CLIENT_SECRET)" | jq
```

<!--v-->
```Makefile
env-up: ## set up dev environment
	docker run -d --name $(CONTAINER_NAME) \
        --restart=unless-stopped \
        -p $(CONTAINER_PORT):80 \
        ealen/echo-server:0.5.0 \
        --enable:environment false --enable:host
	sleep 2
```

<!--v-->
```Makefile
todo: ## list all TODOs in the project
	git grep -I --line-number TODO
```

Note:
- tak, ten grep łapie sam siebie
- normalnie używam innej wersji, ale ona nie mieści się na slajdzie
<!--v--> 
```yaml
# .drone.yml
kind: pipeline
type: docker
...

steps:
- ...

- name: lint
   image: allgreed/nix:2.3.10
   commands:
   - nix-shell --quiet --run 'make lint-check'
```
Note:
- inny CI, nie robi :D


<!--s-->
## What about ...?

- environment
- bootstrap paradox
- secret security
- context switching
- interaction

<!--v-->
## Secret security
```Makefile
ACQUIRE_SECRET := cat secret

secure:
	echo $$($(ACQUIRE_SECRET))
```
```sh
>_ make
echo $(cat secret)
tajemnica
>_ echo $(cat secret)
tajemnica
```
Note:
- sekret nie jest eksponowany w komendzie
- ale komendę można skopiować i coś w niej zmienić
<!--v-->
![](./img/nix.png)

<!--s-->
## Call to action!
https://kasprowicz.pro/posts/common-makefile-interface/
- unlisted!

Note:
- use, study, share, improve <- więcej info w blogpoście

<!--v-->
## Questions?
![](./img/qr.png)
