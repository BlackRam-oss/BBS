## Bad Bobby Saga: The Return
![Last Release](https://img.shields.io/github/v/release/DonRP/BBS)
![Last commit](https://img.shields.io/github/last-commit/DonRP/BBS)
![License](https://img.shields.io/github/license/DonRP/BBS)
[![Crowdin](https://badges.crowdin.net/bad-bobby-saga-the-return/localized.svg)](https://crowdin.com/project/bad-bobby-saga-the-return)
<span class="discord">
<a href="https://discord.gg/UdRJ5Yq85E" title="Discord"><img src="https://img.shields.io/discord/688162156151439536" alt="Discord" /></a>
</span>

BBS is a Game/Visual Novel for adults only. This repo was born for those who want to correct errors, improve some aspects of the game or create Mod.

![alt text](https://github.com/DonRP/BBS/blob/master/game/gui/main_menu.webp "Main menu")

Inside the repo there is only the code. Were you looking for another repo?
- [BBS-3D](https://github.com/DonRP/BBS-3D)
- [BBS-art](https://github.com/DonRP/BBS-art)

### Tools used
- [Dating sim toolkit](https://github.com/DonRP/DS-toolkit)
- [Purple in Gold GUI](https://github.com/DonRP/PG-GUI)
- [Navigation Quest Time Routine System](https://github.com/DonRP/NQTR-toolkit)

## Translation
Hi guys, a main goal of this project is to give the possibility to everyone to enjoy it. And since I know what it means to be born as a non-English native speaker I've studied a way to give everyone the possibility to translate it and use the most updated translation.

### Install the latest translation
First open these [links](https://github.com/DonRP/BBS/tree/languages). Then download the files
![alt text](https://github.com/DonRP/BBS/blob/master/images/languages-download.webp "Languages Download")
and extract them into the main folder.

**ATTENTION**: I will always do some tests to verify that the translations done do not affect the game. But I can always miss something ([Bug Report](https://discord.gg/UdRJ5Yq85E)).

### Instructions to translate & improve my English
If you want to help me do it respecting the rules, every time someone doesn't it makes me waste a lot of time.

First of all sign up for [Crowdin](https://crowdin.com/project/bad-bobby-saga-the-return). Then in [Discord](https://discord.gg/UdRJ5Yq85E) go a **#rules** and become a translator (to stay updated and ask for help).

Then before you start, read the [Instructions](https://github.com/DonRP/BBS#Instructions) carefully.

### English
That's why I created a "false English translation", in this way those who notice errors or who want to improve the report can do so, please write a comment in the English translation when you make correction (eg Fix grammar, syntax, punctuation ...).

### Other languages
The translation from English to another language can often change a lot, so in case the text in that context doesn't make much sense you can not translate word for word, but create a meaningful sentence even if it changes a lot from the original one. Note that usually the dialogs are in order.

### Instructions
- Do not translate the sentence after `#` or `old` (Should be hidden).
- The sentences to be translated are always between `""`
- In case of `new "..."` do not translate `new`
- In case of `"..." nointeract` do not translate `nointeract`

#### e.g:

OK:
```renpy
"Hi, my name is Bobby"
```
```renpy
"Hola, me llamo Bobby"
```

OK:
```renpy
"Hi, my name is Bobby.
I am 20 years old"
```

```renpy
"Salut, je m'appelle Bobby.
J'ai 20 ans"
```

OK:
```renpy
new "Hello"
```
```renpy
new "Здравствуйте"
```

OK:
```renpy
"Hello" nointeract
```
```Renpy
"Hola" nointeract
```

NO:
```renpy
new "Hello"
```
```renpy
новый "Здравствуйте"
```

No:
```renpy
"Hello" nointeract
```
```renpy
"Hola" nointeractúa
```
