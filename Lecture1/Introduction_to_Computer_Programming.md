---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.17.2
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
---

+++ {"tags": ["remove-cell"], "slideshow": {"slide_type": ""}, "editable": true}

---
title: Introduction to Computer Programming
abstract: |
   By the end of this material, readers will understand the intimate relationship between computers and programming, and appreciate the evolutions and motivations of programming languages. They will learn about basic computer architecture, binary data representation, and the structure of a Python program.
skip_execution: false
---

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
tags: [skip-execution]
---
if not input('Load JupyterAI? [Y/n]').lower()=='n':
    %reload_ext jupyter_ai
```

+++ {"slideshow": {"slide_type": "slide"}, "editable": true}

## Computer

+++ {"slideshow": {"slide_type": "subslide"}}

### What is a computer?

+++ {"slideshow": {"slide_type": "subslide"}}

A calculator that is bigger and more advanced?

+++ {"slideshow": {"slide_type": "-"}}

:::{figure} https://upload.wikimedia.org/wikipedia/commons/thumb/4/48/Calculator_app.png/512px-Calculator_app.png
:name: fig:calculator-app
:alt: Calculator app
:align: left

A calculator on a computer.
:::

+++ {"slideshow": {"slide_type": "subslide"}, "editable": true}

If so, is [abacus](https://en.wikipedia.org/wiki/Abacus) the first computer ever invented?

+++ {"slideshow": {"slide_type": "-"}, "editable": true}

::::{figure} https://upload.wikimedia.org/wikipedia/commons/a/af/Abacus_6.png
:name: fig:abacus
:alt: Abacus
:align: left

Abacus - an ancient mechanical computing device.
::::

+++ {"slideshow": {"slide_type": "fragment"}}

Is your [smartphone](https://en.wikipedia.org/wiki/Samsung_DeX) a computer?

+++ {"slideshow": {"slide_type": "fragment"}, "editable": true}

:::::{important} What defines a computer?[^click]
:class: dropdown

In addition to performing arithmetic calculations,
- a computer can be *programmed*
- to perform different tasks.

::::{card}
:header: Who invented the first computer?
:footer: [open in new tab](https://www.youtube.com/embed/d1pvc9Zh7Tg?si=99SDuN_zydUl_x4p)

:::{iframe} https://www.youtube.com/embed/d1pvc9Zh7Tg?si=99SDuN_zydUl_x4p
:width: 100%
:::

::::

:::::

[^click]: Click me to see an answer.

+++ {"editable": true, "slideshow": {"slide_type": ""}}

Run the following cell to ask AI how to defines a computer:[^run]
[^run]: You can run a cell by selecting the cell and press <kbd>Shift + Enter</kbd>.

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
---
%%ai
What defines a computer? Explain in one line.
```

+++ {"slideshow": {"slide_type": "slide"}, "editable": true}

### What is the architecture of a computer?

+++ {"slideshow": {"slide_type": "fragment"}, "editable": true}

A computer contains three main hardware components:

- Input device
- Processing unit
- Output device

+++ {"slideshow": {"slide_type": "subslide"}}

#### Peripherals

+++ {"slideshow": {"slide_type": "-"}, "editable": true}

::::{figure} https://images.unsplash.com/flagged/photo-1551954810-43cd6aef5b1f?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=3580&q=80
:name: fig:peripherals
:alt: Peripherals
:align: left

Computer peripherals.
::::

+++ {"slideshow": {"slide_type": "fragment"}, "editable": true}

Input and output devices connected to a computer are called *peripherals*.  
They allow users to interact with the computer in different ways.

+++ {"slideshow": {"slide_type": "subslide"}}

::::{exercise}
:label: ex:output-device

Some examples of output devices are:
- Monitor
- Speaker

Can you give an awesome example in the following solution cell?[^edit]
::::

[^edit]: To edit a markdown cell, double click the cell until you see a cursor. Run the cell to render the markdown code.

+++ {"slideshow": {"slide_type": "-"}, "nbgrader": {"grade_id": "cell-3ea9d712eccdf31c", "locked": false, "schema_version": 3, "solution": true, "task": false, "grade": true, "points": 0}, "editable": true}

::::{solution} ex:output-device
:class: dropdown
:label: sol:output-device

- 3D printer available at [CityU](https://www.cityu.edu.hk/lib/create/3dprint.htm)
::::

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
---
%%ai
Summarize what an output device of a computer is and explain briefly why 
a monitor and a speaker are examples?
```

+++ {"slideshow": {"slide_type": "subslide"}}

::::{exercise}
:label: ex:input-device

Some examples of input devices are:
- Keyboard
- Mouse

Can you give an awesome example?
::::

+++ {"nbgrader": {"grade_id": "cell-1c411172f0ed411b", "locked": false, "points": 0, "schema_version": 3, "solution": true, "task": false, "grade": true}, "slideshow": {"slide_type": "-"}}

::::{solution} ex:input-device
:class: dropdown
:label: sol:input-device

- 3D scanner available at [CityU](https://www.cityu.edu.hk/lib/create/3dscan.htm)
::::

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
---
%%ai
Summarize what an input device of a computer is and explain briefly why 
a keyboard and a mouse are examples?
```

+++ {"slideshow": {"slide_type": "subslide"}}

::::{exercise} 
:label: ex:input-output

Many devices are both input and output device. Can you give at least 3 examples?
::::

+++ {"nbgrader": {"grade": true, "grade_id": "cell-e1982fbce01506b3", "points": 0, "locked": false, "schema_version": 3, "solution": true, "task": false}, "slideshow": {"slide_type": "-"}}

::::{solution} ex:input-output
:class: dropdown
:label: sol:input-output

- Hard disk
- CD/DVD Rom (writable)
- Touch screen
::::

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
---
%%ai
Explain in one line why a headset is both an input device and an output device 
at the same time.
```

+++ {"slideshow": {"slide_type": "slide"}}

#### Central Processing Unit

+++ {"slideshow": {"slide_type": "-"}}

::::{figure}
:name: fig:cpu
:alt: CPU
:align: left

![An Intel CPU](https://images.unsplash.com/photo-1555617981-dac3880eac6e?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1950&q=80)

![An AMD CPU](https://images.unsplash.com/photo-1591799265444-d66432b91588?q=80&w=1760&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D)

Central processing units (CPUs) on motherboards.
::::

+++ {"slideshow": {"slide_type": "fragment"}}

The brain of a computer is its processor or the [**C**entral **P**rocesisng **U**nit (CPU)](https://en.wikipedia.org/wiki/Central_processing_unit). As shown in [](#fig:cpu), it is located on the [*motherboard*](https://en.wikipedia.org/wiki/Motherboard) and connected to different peripherals using different [*connectors*](https://en.wikipedia.org/wiki/Category:Computer_connectors).

+++

For instance, you can check the CPU of your Jupyter Server by running the following command:

```{code-cell} ipython3
!lscpu
```

+++ {"slideshow": {"slide_type": "fragment"}}

Two important components in the CPU are:
-  **A**rithmetic and **L**ogic **U**nit (**ALU**): Performs arithmetics like a calculator (but for binary numbers)
-  **C**ontrol **U**nit (**CU**): Directs the operations of the processor in executing a program.

+++ {"slideshow": {"slide_type": "subslide"}}

To visualize how CPU works, run the [CPU Simulator below](https://github.com/pddring/cpu-simulator).
- Note that all values are zeros in the RAM (**R**andom **A**cess **M**emory) initially.
- Under Settings, click `Examples`$\to $`Add two numbers`. Observe that the values in the RAM have changed.
- Click `Run` at the bottom right-hand corner.

+++

:::::{card}
:footer: [Open in new tab](https://tools.withcode.uk/cpu)

::::{iframe} https://tools.withcode.uk/cpu
:width: 100%
::::

:::::

+++

::::{seealso} Is there a rigorous definition of a computer?
:class: dropdown

Computer architecture may evolve over time, with new technologies and innovations emerging. However, modern computers follow the same mathematical principles of the [universal machine](https://doi.org/10.1112/plms/s2-42.1.230) defined by [Alan Turing, Father of Modern Computing](https://en.wikipedia.org/wiki/Alan_Turing). The definition is made to address the problem of computing, i.e., what numbers are computable by programming a machine. Do you have an easy way to understand [Turing's proof](https://en.wikipedia.org/wiki/Turing%27s_proof)?

::::

+++ {"slideshow": {"slide_type": "slide"}}

## Programming

+++ {"slideshow": {"slide_type": "subslide"}}

### What is programming?

+++ {"slideshow": {"slide_type": "fragment"}}

::::{important} What defines programming?
:class: dropdown

*Programming*, also called *software development*, is the process of writing programs for the computer to execute different tasks. But what is a program?
::::

+++ {"slideshow": {"slide_type": "fragment"}, "nbgrader": {"grade": false, "locked": true, "task": false, "grade_id": "cell-7675978e85548d96", "schema_version": 3, "solution": false}}

::::{exercise} 
:label: ex:machine-language

You have just seen a program written in [machine language](https://en.wikipedia.org/wiki/Machine_code). Where?

:::{hint}
:class: dropdown

It is stored somewhere in RAM (**R**andom **A**cess **M**emory), which is used to store data and programs.[^architecture]

:::

::::

[^architecture]: The CPU simulator follows the [von Neumann architecture](https://doi.org/10.1109/85.238389), which realizes Turing's conception of the [*stored-program computer*](https://en.wikipedia.org/wiki/Stored-program_computer), where program and data are stored in the same memory. This is in contrast to the Harvard architecture, which uses separate memories for program and data.

+++ {"nbgrader": {"grade_id": "cell-08298600f10cfc25", "schema_version": 3, "points": 0, "grade": true, "task": false, "locked": false, "solution": true}, "slideshow": {"slide_type": "-"}}

::::{solution} ex:machine-language
:class: dropdown
:label: sol:machine-language

The first six lines of binary sequences in the RAM. The last line `End`s the program.
::::

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
tags: [skip-execution]
---
%%ai
Summarize what a machine language is and give an example of a program in 
machine language.
```

+++ {"slideshow": {"slide_type": "fragment"}}

The CPU is capable of carrying out 
- a set of instructions such as `Add`, `Subtract`, `Store`, etc.,
- for some numbers stored in the RAM.

+++

Both the instructions and the numbers are represented as binary sequences.

+++ {"slideshow": {"slide_type": "subslide"}}

### Why computer uses binary representation?

+++

:::{figure} https://upload.wikimedia.org/wikipedia/commons/8/8c/Two_women_operating_ENIAC_%28full_resolution%29.jpg
:name: fig:ENIAC
:alt: Two programmers operating ENIAC.
:align: left

Programmers controlling the switches of ENIAC.
:::

+++ {"slideshow": {"slide_type": "fragment"}}

::::::{exercise}
:label: ex:ENIAC

[](#fig:ENIAC) is a photograph of the first electronic computer, called [Electronic Numerical Integrator and Computer (ENIAC)](https://en.wikipedia.org/wiki/ENIAC). It was programmed using binary circuitries, namely *switches* that can be either `On` or `Off`. However, it did not represent numbers efficiently in binary. 10 switches (bits) were used to represent a digit: Each switch indicates a possible value from 0 to 9. Indeed, how many decimal number can be represented by 10 bits?

:::::{hint}
:class: dropdown

::::{card}
:header: Binary representation
:footer: [open in new tab](https://youtu.be/Xpk67YzOn5w)

:::{iframe} https://www.youtube.com/embed/Xpk67YzOn5w
:width: 100%
:::

::::
:::::

::::::

```{code-cell} ipython3
---
nbgrader:
  grade: true
  grade_id: cell-1023083cd0aca779
  locked: false
  points: 0
  schema_version: 3
  solution: true
  task: false
slideshow:
  slide_type: '-'
tags: [hide-cell]
---
### BEGIN SOLUTION
2 ** 10 # because there are that many binary sequences of length 10.
### END SOLUTION
```

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
tags: [skip-execution]
---
%%ai
Explain the multiplication rule in combinatorics.
```

::::{seealso} Why use binary numbers?
:class: dropdown

Unlike ENIAC, the subsequent design of the Electronic Discrete Variable Computer (EDVAC) utilized the binary number system. The decision was explained in Section 5.1 of the [design report](https://doi.org/10.1109/85.238389) authored by [John von Neumann](https://en.wikipedia.org/wiki/John_von_Neumann) in 1945. While humans are accustomed to using the decimal number system, von Neumann justified the use of binary by noting that human neurons operate in a binary manner: 

> The analogs of human neurons ... are equally all-or-none elements. It will appear that they are quite useful for all preliminary, orienting, considerations of vacuum tube systems ... It is therefore satisfactory that here too the natural arithmetical system to handle is the binary one.  
> — John von Neumann

::::

+++ {"slideshow": {"slide_type": "fragment"}}

There are *International Standards* for representing characters:
- [ASCII](https://en.wikipedia.org/wiki/ASCII) (**A**merican **S**tandard **C**ode for **I**nformation **I**nterchange) maps English letters and some other symbols to 8-bits (8 binary digits, also called a byte). E.g., `A` maps to `01000001`.
- [Unicode](https://en.wikipedia.org/wiki/Unicode) can also represent characters in different languages such as Chinese, Japanese...etc.

+++ {"slideshow": {"slide_type": "fragment"}}

There are also additional standards to represent numbers other than non-negative integers:
- [2's complement format](https://en.wikipedia.org/wiki/Two%27s_complement) for negative integers (e.g. -123)
- [IEEE floating point format](https://en.wikipedia.org/wiki/IEEE_754) for floating point numbers such as $1.23 \times 10^{-4}$.

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
tags: [skip-execution]
---
%%ai
Why define standards such as ASCII and Unicode?
```

+++ {"slideshow": {"slide_type": "fragment"}}

::::{important} Why define different standards?
:class: dropdown

Different standards have different benefits. 
- ASCII requires less storage for a character, but it represents less characters.
- Although digits are also represented in ASCII, the 2's complement format is designed for more efficient arithmetic operations.

::::

+++ {"slideshow": {"slide_type": "slide"}}

## Generations of programming languages

+++ {"slideshow": {"slide_type": "fragment"}}

::::{important}

A *machine language* written in *binary sequences* is known as a *1st Generation Programming Language*.
::::

+++ {"slideshow": {"slide_type": "fragment"}}

**Are we going to start with machine language?**
Start with learning 2's complement and the binary codes for different instructions?

+++ {"slideshow": {"slide_type": "fragment"}}

No. Programmers do not write machine codes directly because it is too hard to think in binary representations.

+++ {"slideshow": {"slide_type": "fragment"}}

Instead, programmers write human-readable **mnemonics** such as `ADD`, `SUB`, ...  
This is called the *assembly language*. An example is shown in [](#fig:assembly-language).

+++ {"slideshow": {"slide_type": "fragment"}}

::::{figure} https://upload.wikimedia.org/wikipedia/commons/f/f3/Motorola_6800_Assembly_Language.png
:name: fig:assembly-language
:alt: Assembly language
:align: left

A Code written in an assembly language.
::::

+++

::::{important}

An *assembly language* written in *mnemonics* is the *2nd Generation Programming Language*.
::::

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
tags: [skip-execution]
---
%%ai
What is the assembly language most commonly used by programmers and what is its
main application?
```

+++ {"slideshow": {"slide_type": "subslide"}}

**Are you going to learn an assembly language?**

+++ {"slideshow": {"slide_type": "fragment"}}

Both machine language and assembly language are low-level languages which are
- difficult to write for complicated tasks (requiring many lines of code), and
- platform-specific, i.e.,
    - the sets of instructions and their binary codes can be different for different [types of CPUs](https://en.wikipedia.org/wiki/Comparison_of_CPU_microarchitectures), and
    - different operating systems use [different assembly languages/styles](https://en.wikipedia.org/wiki/X86_assembly_language).

+++ {"slideshow": {"slide_type": "fragment"}}

::::{note} Should we learn assembly languages?
:class: dropdown

Probably for programmers who need to write fast or energy-efficient code such as
- a driver that controls a 3D graphics card, or
- a program that control a microprocessor with limited power supply.

But even in the above cases, there are often better alternatives. Play with the following microprocessor simulator:

- Open <https://micropython.org/unicorn/> in a browser.
- Click `CHOOSE A DEMO`$\to $`LED`.
- Click `RUN SCRIPT` and observes the LED of the board.
- Run the demos `ASSEMBLY` and `MATH` respectively and compare their capabilities.

::::

+++ {"slideshow": {"slide_type": "slide"}}

## High-level Language

+++ {"slideshow": {"slide_type": "slide"}}

**What is a high-level language?**

+++ {"slideshow": {"slide_type": "fragment"}}

:::::{card}
:header: The art of programming
:footer: [open in new tab](https://youtu.be/QdVFvsCWXrA)

::::{iframe} https://www.youtube.com/embed/QdVFvsCWXrA
:width: 100%
::::

:::::

+++ {"slideshow": {"slide_type": "subslide"}}

Programmer nowadays write in human-readable languages such as 

- Python
- Rust
- C/C++
- Java
- JavaScript
- Typescript
- Pascal
- Basic 
- HTML
- PHP
- ...

called *high-level languages*.

+++

::::{important}

A *high-level language* intended to be *human understandable* is a *3rd Generation Programming Language*.

::::

+++ {"slideshow": {"slide_type": "fragment"}}

- A program written in a high-level language gets converted automatically to a low-level machine code for the desired platform. 
- This *abstracts* away low-level details that can be handled by the computer automatically.

+++ {"slideshow": {"slide_type": "fragment"}}

For instance, a programmer needs not care about where a value should be physically stored if the computer can find a free location automatically to store the value.

+++ {"slideshow": {"slide_type": "fragment"}}

Different high-level languages can have different implementations of the conversion processes:
- **Compilation** means converting a program well before executing the program.  
  E.g., C++ and Java programs are compiled.
- **Interpretation** means converting a program on-the-fly during the execution of a program.  
  E.g., JavaScript and Python programs are often interpreted.

+++

::::{seealso} Compiled vs interpreted languages
:class: dropdown

Roughly speaking, compiled programs run faster but interpreted programs are more flexible and can be modified at run time. The [truth](https://finematics.com/compiled-vs-interpreted-programming-languages/) is indeed more complicated. Python also has a compiler, and recently, a [JIT compiler](https://github.com/python/cpython/pull/113465). Is Python really an interpreted language?

::::

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
tags: [skip-execution]
---
%%ai
Explain in one or two paragraphs whether Python is really an interpreted
language, given that it also has a compiler and, recently, a JIT compiler, and
it can be run as a script like a scripting language.
```

+++ {"slideshow": {"slide_type": "slide"}}

**What programming language will you learn?**

+++ {"slideshow": {"slide_type": "fragment"}}

You will learn to program in [*Python*](https://youtu.be/J0Aq44Pze-w?si=NLwclo8jaqUla1bx), which is currently the most popular language according to the [*TIOBE (The Importance of Being Efficient) Programming Community Index*](https://www.tiobe.com/tiobe-index/).

We will cover
-  basic topics including *values*, *variables*, *conditional*, *iterations*, *functions*, *composite data types*,
-  advanced topics that touch on functional and object-oriented programming, and
-  engineering topics such as *numerical methods*, *optimizations*, and *machine learning*.

+++ {"slideshow": {"slide_type": "fragment"}}

:::::{note} Why Python?
:class: dropdown

Python is:
- *expressive* and can get things done with fewer lines of code as compared to other languages.
- *popular*. It has an extensive set of libraries for Mathematics, graphics, AI, Machine Learning, etc.
- *free and open-source*, so you get to see everything and use it without restrictions.
- *portable*, i.e., the same code runs in different platforms without modifications.

::::{card}
:footer: [open in new tab](https://youtu.be/Y8Tko2YC5hA)

:::{iframe} https://www.youtube.com/embed/Y8Tko2YC5hA?end=200
:width: 100%
:::

::::

:::::

+++ {"slideshow": {"slide_type": "subslide"}}

**How does a Python program look like?**

```{code-cell} ipython3
---
slideshow:
  slide_type: '-'
editable: true
tags: [skip-execution]
---
import datetime  # library to obtain current year

cohort = input("In which year did you join CityU? [e.g., 2020]")
year = datetime.datetime.now().year - int(cohort) + 1
print("So you are a year", year, "student.")
```

+++ {"slideshow": {"slide_type": "fragment"}}

A Python program contains *statements* just like sentences in natural languages. E.g.,
```python
cohort = input("In which year did you join CityU? ")
```
which obtains some information from user input.

+++ {"slideshow": {"slide_type": "fragment"}}

For the purpose of computations, a statement often contains *expressions* that evaluate to certain values.  E.g.,
```python
input("In which year did you join CityU? ")
``` 
is an expression with the value equal to what you input to the prompt.  
That value is then given the name `cohort`.

+++ {"slideshow": {"slide_type": "fragment"}}

Expressions can be composed of the following objects:
- *Functions* such as `input`, `now`, and `int`, etc., which are like math functions the return some values based on its arguments, if any.
- *Literals* such as the string `"In which year did you join CityU? "` and the integer `1`. They are values you type out literally.
- *Variables* such as `cohort` and `year`, which are meaningful names to values.

+++ {"slideshow": {"slide_type": "fragment"}}

To help others understand the code, there are also *comments* that start with `#`.  
These are meant to explain the code to human but not to be executed by the computer.

+++ {"slideshow": {"slide_type": "subslide"}, "nbgrader": {"grade_id": "cell-6c906df220a97280", "task": false, "grade": false, "locked": true, "solution": false, "schema_version": 3}}

::::{exercise}
:label: ex:future-programming

What do you think the next generation programming should be?
::::

+++ {"slideshow": {"slide_type": "fragment"}, "nbgrader": {"points": 0, "schema_version": 3, "solution": true, "task": false, "locked": false, "grade": true, "grade_id": "cell-205d445ede20461d"}}

:::::{solution} ex:future-programming
:class: dropdown

- Programming using natural language. A step towards this direction: [](https://en.wikipedia.org/wiki/Vibe_coding).

- Write programs that people enjoy reading, like [literate programming](https://www.youtube.com/watch?v=bTkXg2LZIMQ). A step towards this direction: [nbdev](https://github.com/fastai/nbdev).

    ::::{card}
    :header: Literate programming
    
    :::{iframe} https://www.youtube.com/embed/bTkXg2LZIMQ
    :width: 100%
    :::
    ::::
:::::

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
---
%%ai
What do you think the next generation programming should be?
```
