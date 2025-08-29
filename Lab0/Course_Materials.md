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

+++ {"editable": true, "slideshow": {"slide_type": "slide"}}

---
title: Course Materials
skip_execution: true
---

+++

## Access

+++ {"editable": true, "slideshow": {"slide_type": ""}}

To access the course homepage, visit:

::::{attention} Course homepage for registered students

<https://canvas.cityu.edu.hk/courses/64853/>

::::

You will find links to launch the course materials as shown in [](#tbl:notebook-link):

+++ {"editable": true, "slideshow": {"slide_type": ""}}

:::::{table} An example of a notebook link on the course homepage.
:label: tbl:notebook-link

<table>
<div style="border: 1px solid black; padding: 10px;">
<h4 title="Title: Lecture/Lab">Lab0</h4>
<ul>
  <li>
    <a title="Subtitle: Notebook link" href="https://canvas.cityu.edu.hk/courses/64853/external_tools/retrieve?display=borderless&url=https%3A//dive.cs.cityu.edu.hk/cs1302_25a/hub/lti/launch%3Fcustom_next%3Dhttps%253A//dive.cs.cityu.edu.hk/cs1302_25a/hub/user-redirect/git-pull%253Frepo%253Dhttps%25253A//github.com/dive4dec/cs1302_25a%2526urlpath%253Dlab/tree/cs1302_25a/Lab0/Course_Materials.ipynb" target="_blank">Course Materials</a>
</ul>
</div>
</table>

:::::

+++

Course materials are also compiled into an ebook accessible without login:

::::{attention} Jupyter book

<https://ccha23.github.io/cs1302i25a/>

::::

To launch the notebooks from the ebook, use the buttons located on the top right hand corner:

- Click [<kbd>JHub</kbd>](https://canvas.cityu.edu.hk/courses/64853/external_tools/retrieve?display=borderless&url=https%3A//dive.cs.cityu.edu.hk/cs1302_25a/hub/lti/launch%3Fcustom_next%3Dhttps%253A//dive.cs.cityu.edu.hk/cs1302_25a/hub/user-redirect/git-pull%253Frepo%253Dhttps%25253A//github.com/dive4dec/cs1302_25a%2526urlpath%253Dlab/tree/cs1302_25a) for registered students to access the JupyterHub server on our computing platform DIVE. (Details will be explained later in "[](#sec:fetch)")
- Click [<kbd>Binder</kbd>](https://mybinder.org/v2/gh/dive4dec/cs1302nb/HEAD?urlpath=%2Fgit-pull%3Frepo%3Dhttps%3A%2F%2Fgithub.com%2Fdive4dec%2Fcs1302_25a%26urlpath%3Dlab%2Ftree%2Fcs1302_25a) for public access through the [BinderHub (`binder.org`)](https://en.wikipedia.org/wiki/Binder_Project) with *temporary* storage.

+++

For your first lab session, start with the following notebook under the course directory `cs1302_25a`:

> [`Lab0`$\to$`Course Materials`](../Lab0/Course_Materials.ipynb).

For your first lecture session, open

> [`Lecture1`$\to$`Introduction to Computer Programming`](../Lecture1/Introduction_to_Computer_Programming.ipynb).

+++ {"editable": true, "slideshow": {"slide_type": "slide"}}

## Notebooks

+++

Lecture and lab materials are written in the form of [Jupyter notebooks](https://jupyter.org/), which provide an interactive [literate programming](https://en.wikipedia.org/wiki/literate_programming) experience:

- Jupyter notebooks allow programs to be mixed with other contents, including figures, videos, and formatted textual explanations.
- The notebooks can also be opened in a Jupyter server, which enables users to edit and run the programs in addition to other contents.

+++

### How to run notebook cells?

+++

If you already have your notebook opened in a Jupyter server, let's run some code. Otherwise, jump to the [next section](#sec:fetch) to learn how to fetch and open notebooks.

To run a cell, select the cell and press <kbd>Shift + Enter</kbd>. The cell prompt will change from `[ ]` to `[*]`. When the run completes, the asterisk will be changed to a number like `[1]`. Try running the following cell to import the [Mathematical Animation Engine (Manim)](https://docs.manim.community/).[^import] 

[^import]: Importing a library in programming is like bringing a toolbox into your workshop, giving you access to all the tools you need to complete your tasks.

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
---
import os

if not os.getenv(
    "NBGRADER_EXECUTION"
):  # Skip the code or auto-grading may take too long to complete.
    import manim
```

+++ {"editable": true, "slideshow": {"slide_type": ""}}

After the import is complete,  run the following cell to create an animation:

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
---
%%manim -qm Welcome
class Welcome(manim.Scene):
    def construct(self):
        self.play(manim.Write(manim.Text("Welcome to CS1302!")))
```

As you can see, the code creates a scene that displays the message `Welcome to CS1302!` with a "writing" animation.[^manim-magic] To verify that the program runs live, feel free to modify the message to anything you want.

[^manim-magic]: If you are interested in what the first line does, it sets the video quality to medium while disabling caching and progress bars, and setting the verbosity to reporting only ERROR but not other critical information.

+++

(sec:fetch)=
### How to fetch and open notebooks?

+++ {"editable": true, "slideshow": {"slide_type": ""}}

To fetch the notebooks, follow the links to the notebooks on the course homepage such as the one in [](#tbl:notebook-link).

+++

After clicking a notebook link, you may be asked to 

- login with your CityU account if you are not yet logged into Canvas, and
- specify a server option if you do not yet have a running Jupyter server.

Select the `Default` option, and click <kbd>Start</kbd> to begin your session.

+++ {"editable": true, "slideshow": {"slide_type": ""}}

If the server is spawned successfully, the [JupyterLab](https://jupyterlab.readthedocs.io) interface should appear.

:::{tip} Troubleshooting
:class: dropdown

In case the JupyterLab interface fails to show, refresh the page or restart your browser for the javascript to load completely in your browser. If the server fails to spawn, you can restart after clicking the `Home` link. 

You may occasionally run into issues. There are thousands of open issues reported to the JupyterLab repository, where you may find related issues and a kludge (temporary workaround):

- <https://github.com/jupyterlab/jupyterlab/issues>

:::

+++ {"editable": true, "slideshow": {"slide_type": ""}}

As you start your programming journey, you will inevitably encounter [software bugs](https://en.wikipedia.org/wiki/Software_bug), especially in highly sophisticated software such as JupyterLab. Be aware of their existence, and develop a positive attitude towards bugs, as well as cultivate a proper skill set to inspect and debug them effectively.

+++

As an example to inspect a computer program, we will explain how the notebook link works. First, run the following code to start the notebook link generator app.

```{code-cell} ipython3
from notebook_link_generator import setup_notebook_link_widget

display_widget = setup_notebook_link_widget(canvas_id="64853")
display(display_widget)
```

Change the `Notebook path` above to `Lecture1/Introduction_to_Computer_Programming.ipynb` and observe the live update to the generated link.

+++

Now, run the following two cells to see how a notebook link is generated step-by-step:

```{code-cell} ipython3
%load_ext divewidgets
```

```{code-cell} ipython3
%%optlite -r
from urllib.parse import quote

# Course parameters
course_id = "cs1302_25a"
notebook_path = "Lecture1/Introduction_to_Computer_Programming.ipynb"
canvas_id = "64853"

# Base URLs
notebook_repo = f"https://github.com/dive4dec/{course_id}"
course_server = "https://dive.cs.cityu.edu.hk"
course_homepage = f"https://canvas.cityu.edu.hk/courses/{canvas_id}"

# Notebook URL generation
# 1. Construct the URL for git-pull service to clone or pull the notebook repository
gitpull_url = (
    f"{course_server}/{course_id}/hub/user-redirect/git-pull?"
    + f"repo={quote(notebook_repo)}"
    + f"&urlpath={quote(f'lab/tree/{course_id}/{notebook_path}')}"
)
# Construct the LTI (Learning Tools Interoperability) launch URL for JupyterHub
lti_url = (
    f"{course_server}/{course_id}/hub/lti/launch?" + f"custom_next={quote(gitpull_url)}"
)
# Construct the LTI external tool URL to open the notebook
notebook_url = (
    f"{course_homepage}/external_tools/retrieve?display=borderless&"
    + f"url={quote(lti_url)}"
)
notebook_url
```

+++ {"slideshow": {"slide_type": "subslide"}}

After running the code, you can
- see the generated notebook link for `Lecture1/Introduction_to_Computer_Programming.ipynb` in the output cell;
- inspect parts of the code in the input cell by placing the cursor there and press <kbd>Shift + Tab</kbd>; and
- visualize the execution step-by-step by clicking <kbd>Next ></kbd> (<kbd>< Prev</kbd>) to go to the next (previous) line.

+++

::::{note} What does the notebook link do?
:class: dropdown

The notebooks reside in a [GitHub repository](https://github.com/dive4dec/cs1302_25a/blob/main/README.md). Accessing a notebook link will

1. use [LTI Authenticator](https://ltiauthenticator.readthedocs.io) to launch the JupyterHub as an LTI external tool from the course homepage, and
2. use [NbGitPuller](https://jupyterhub.github.io/nbgitpuller/index.html) to [git-pull](https://git-scm.com/docs/git-pull)s all the files in the repository, merge them with any existing files stored under the course folder `cs1302_25a` in your home directory without overwriting your changes, and open the notebook path specified in the JupyterLab interface.

::::

+++ {"slideshow": {"slide_type": "subslide"}}

## Assignments

+++

### How to complete an assignment?

+++

The notebooks can be edited in JupyterLab to include your answers for submission. If this is your first time using JupyterLab, take a look at the [official video tutorial](https://www.youtube.com/embed/A5YyoCKxEOU):


::::{seealso} How to use JupyterLab?
:class: dropdown

:::{iframe} https://www.youtube.com/embed/A5YyoCKxEOU
:width: 100%
:align: left

Official video tutorial on Jupyter
:::
::::

+++ {"slideshow": {"slide_type": "fragment"}, "editable": true}

For more advanced features:

- Checkout the `Help` menu items
    - `Show Keyboard Shortcuts` to try some of the shortcuts to see their effect, and
    -  `Jupyter Reference` to open the [user guide](https://jupyterlab.readthedocs.io/en/latest/user/interface.html) in a new tab.
- Try also the [MyST Markdown](https://mystmd.org/guide/typography) syntax to format your notes.

+++

::::{seealso} An alternative interface: VSCode
:class: dropdown

You may also use a highly customizable editor Visual Studio Code (VSCode) to open a notebook:

- Click `File → New Launcher → VSCode`.
- Click the menu icon on the left and select `Open Folder` and select `cs1302_25a`.

In the file explorer, you can navigate to a notebook to open it. However, to properly run the notebook, you will also need to start the kernel by choosing an appropriate Python environment such as `base`, which is the default [(conda) environment](https://conda.io/projects/conda/en/latest/dev-guide/api/conda/base/index.html) for our JupyterLab setup. Unlike JupyterLab, you may install additional extensions yourself to enrich the interface.[^vscode]

::::

[^vscode]: The VSCode interface is actually [code-server](https://github.com/coder/code-server), so some VSCode extensions may not be listed under the extension panel. You may still try to install them using the command `install-vscode-extension` in a terminal. This is only for advanced users who know what they are doing, or the risk of breaking things can be rather high...

+++

In learning a new programming language, the first program to write is often the ["Hello, World!"](https://en.wikipedia.org/wiki/%22Hello,_World!%22_program) program, which says Hello to the world. As your first lab exercise, you will write such a program in Python.

+++ {"nbgrader": {"solution": false, "schema_version": 3, "grade": false, "locked": true, "grade_id": "qHelloWorld", "task": false}, "slideshow": {"slide_type": "subslide"}, "editable": true}

:::::{exercise} Hello World
:label: ex:Hello-World

Complete the program to print the message `Hello, World!`. 

::::{hint}
:class: dropdown

One possible solution is:

:::{code-block} python
:name: code:Hello-World
:caption: Python, "Hello, World!"

def say_hello():
    print("Hello, World!")
    
say_hello()
:::

:::{caution}
You must use a tab or 4 spaces to indent the second line of code `print(...)`.
:::

::::

:::::

+++ {"slideshow": {"slide_type": ""}, "editable": true}

The following code cell is a [solution cell](https://nbgrader.readthedocs.io/en/stable/configuration/student_version.html#default-behavior). Since you are not expected to know Python yet, you can simply expand the hint above and copy the answer to the solution cell instead.

```{code-cell} ipython3
---
code_folding: []
editable: true
nbgrader:
  grade: false
  grade_id: helloworld
  locked: false
  schema_version: 3
  solution: true
  task: false
slideshow:
  slide_type: '-'
tags: [remove-output]
---
def say_hello():
    ### BEGIN SOLUTION
    print("Hello, World!")
    ### END SOLUTION

say_hello()
```

+++ {"editable": true, "slideshow": {"slide_type": "subslide"}}

:::{attention}

It's important to follow certain guidelines when writing your answers or code in the notebooks:

- Only provide your answers in the cells that are designated for this purpose, which are usually labeled with `YOUR CODE HERE` or `YOUR ANSWER HERE`.
- For coding exercises, be sure to remove the line `raise NotImplementedError()` from the cell before submitting your work.
- Do not clone or duplicate the answer cells, as this can cause issues with version control and grading.

:::

+++

To test your program:

- Run your program by selecting the solution cell and press <kbd>Shift + Enter</kbd>.
- Then, run the following visible test to check whether your program prints the correct message.

```{code-cell} ipython3
---
editable: true
nbgrader:
  grade: true
  grade_id: test-helloworld
  locked: true
  points: 1
  schema_version: 3
  solution: false
  task: false
slideshow:
  slide_type: '-'
tags: [remove-output]
---
# Run this test cell right after running your "Hello, World!" program.
import io
import sys

old_stdout, sys.stdout = sys.stdout, io.StringIO()
say_hello()
printed = sys.stdout.getvalue()
sys.stdout = old_stdout
assert printed == "Hello, World!\n"
```

+++ {"slideshow": {"slide_type": ""}, "editable": true}

The test returns an assertion error if your program does not print the correct message.

+++ {"editable": true, "slideshow": {"slide_type": ""}}

::::{tip}

- You can repeatedly modify your solution and run the test cell until your solution passes the test. There is no mark penalty in failing the test before submission. 
- You should try to understand the error messages from a failed test.
- To assess your solution thoroughly, we will run new tests hidden from you after you have submitted your notebook. Therefore, *you should ensure your solution works in general rather than just the visible tests*.
- If you open the same notebook multiple times in different browser windows, be careful in making changes in different windows as you may overwrite your own changes.
- If your notebook fails to run any code, the kernel might have died. You can restart the kernel with `Kernel`$\to$ `Restart`. If restarting fails, check your code cells to see if there is anything that breaks the kernel.

::::

+++ {"editable": true, "slideshow": {"slide_type": "slide"}}

### How to submit?

+++ {"editable": true, "slideshow": {"slide_type": ""}}

:::{important} Grading policies

- Late submissions will not be accepted without valid justifications.
- You can submit your assignment repeatedly before the deadline without penalty, so it is recommended to submit your assignment in advance. Please note that you are responsible for any issues related to failed submissions due to network outages that occur too close to the deadline.
- It is also important to make a record or backup of your submission that includes the submission timestamp. Double check to ensure that you have submitted the correct lab assignment, since multiple lab assignments may be open for submission at the same time.

:::

+++ {"editable": true, "slideshow": {"slide_type": ""}}

:::{attention}

- Lecture notebooks under the subfolders `Lecture*\` need NOT be submitted. You only need to submit the lab notebooks under `Lab*\`. 

:::

+++ {"slideshow": {"slide_type": "fragment"}, "nbgrader": {"task": false, "solution": false, "grade_id": "Check", "locked": true, "schema_version": 3, "grade": false}, "editable": true}

Before you submit, it is a good idea to make sure everything runs as expected:

1. **Git-pull the notebooks**: Follow any one of the link on the course homepage to a notebook, which will git-pull any updates/corrections to (all) your notebooks.
1. **Save the notebook**: Unsaved changes are not submitted, even though they are in the memory.
1. **Restart the kernel**: `Kernel`$\to$ `Restart Kernel...` to have a clean state before running visible tests.
1. **run all cells**: `Run`$\to$ `Run All Cells` to double check the results of the visible tests are as expected.

Re-executing cells in order in a Jupyter Notebook ensures that all dependencies and state changes are correctly applied, preventing misleading results from out-of-order execution.

+++

::::{tip}

1. By default, JupyterLab autosaves an opened notebook every 120 seconds. This configuration can be changed at `Settings`$\to$`Settings Editor`$\to$`Document Manager`$\to$`Autosave Interval`.
2. An opened file with unsaved changes has a solid circle next to its tab label. You can manually save the file using the save button in the toolbar. 

::::

+++ {"slideshow": {"slide_type": "subslide"}, "editable": true}

To submit your notebook:

1. Select the menu item `Nbgrader`$\to$`Assignment List`.
1. Expand the Lab folder and click the `validate` button next to the notebook(s) to check if all the visible tests pass.
1. Click `Submit` to submit your notebook.

+++

::::{seealso} What is Nbgrader?
:class: dropdown

[Nbgrader](https://nbgrader.readthedocs.io/en/stable/) is a package for grading notebook assignments. It allows students to submit their notebooks directly through the JupyterHub server. Submitted notebooks can be both auto-graded with pre-defined test cases and manually graded with custom feedback. After grading is complete, you can check your scores and access the feedback using the same interface.

::::

+++ {"editable": true, "slideshow": {"slide_type": ""}}

::::{caution}

Your submission may not be graded under the following circumstances:

- The notebook files have been renamed, for example, `Setup.ipynb` being changed or copied to `Setup (Copy).ipynb`.
- An HTML file exists with the same name as a notebook, for example, `Setup.html`.
- The file size is too large, e.g., exceeds `100MB`.
- The code takes too long to run or requires an excessive amount of memory.

It is essential to ensure that your submission meets these guidelines to avoid any issues with grading.

:::{tip} Troubleshooting
:class: dropdown

If you believe your notebooks are corrupted, 
1. download/backup your existing notebooks,
1. remove them from the `Lab*/` folder,
1. click the git-pull links from the course homepage to re-pull the notebooks, and
1. copy your solutions to the new notebooks.

You may also run the course notebooks outside the jupyterhub server and locally on your computer. For more details, see the course homepage.

:::

::::

+++ {"editable": true, "slideshow": {"slide_type": ""}}

## References

+++

Reading is important in learning a new language. This is especially so for learning a programming language, whose syntax has a very precise structure and interpretation. Each topic will have some required readings listed on the course homepage. 

:::::{table} An example of required readings on the course homepage.
:label: tbl:reading

<table>
<div style="border: 1px solid black; padding: 10px;">
<h4 title="Title: Readings">Reading</h4>
<ul>
     <li><a href="https://archive.org/stream/2018Fundamentals.ofPython?ref=ol#page/n11/mode/1up" target="_blank">[Halterman17] 1.1-1.3</a></li>
</ul>
</div>
    
</table>

:::::

+++

As a programming language can evolve quickly over time, especially for a popular language like Python, it is important to be aware of the version you are using, and supplement your readings with the documentations of the newer versions. In particular, check out 
- the documentations for [Python 3.12](https://docs.python.org/3.12/) we are using, and
- the list of other Python versions at <https://www.python.org/doc/versions/>.
  
The version such as `3.12` consists of the major [version number](https://en.wikipedia.org/wiki/Software_versioning) `3` followed by the minor version number `12`.

+++

::::{caution} Is it okay to learn and use different versions of Python?
:class: dropdown

It is true that new features introduced in later versions may not work in earlier versions, and old features in earlier versions may be removed in newer versions. Nevertheless, it is generally okay to learn and use different minor versions of Python under the same major version, such as Python `3.*`. Python's design has made a conscious effort to maintain backwards compatibility for the minor versions, which mean that code written in an earlier minor version runs in a later minor version.

::::

+++

If you have more time, further supplement your learning with materials from similar introductory Python programming courses at other universities:[^1]

[^1]: Note that these assume students have no prior programming experience but they may different topics than our course does.

+++

::::{seealso} MIT Open Courseware
:class: dropdown

An introductory programming course using Python:

- Course homepage: [6.0001
Introduction To Computer Science And Programming In Python](https://ocw.mit.edu/courses/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/pages/readings/)  
  Textbook: [Guttag, John V. Introduction to computation and programming using Python: with application to computational modeling and understanding data. Mit Press, 2021.](https://julac-cuh.primo.exlibrisgroup.com/permalink/852JULAC_CUH/vit3jk/alma991029721214003408)[^guttag]

An introductory programming course using Scheme:

- Course homepage: [6.001 Structure And Interpretation Of Computer Programs](https://ocw.mit.edu/courses/6-001-structure-and-interpretation-of-computer-programs-spring-2005/)  
  Textbook: [Abelson, Harold, and Gerald Jay Sussman. Structure and interpretation of computer programs. The MIT Press, 1996.](https://web.mit.edu/6.001/6.037/sicp.pdf)


::::

[^guttag]: After clicking the link, CityU students can further link to the full text from the `View Online` section of the opened CityU library page.

+++

::::{seealso} UC Berkeley Course
:class: dropdown

An introductory programming course using Python:

- Course homepage: [CS 61A Structure And Interpretation Of Computer Programs](https://cs61a.org)  
  Textbook: [John DeNero. Composing Programs.](https://www.composingprograms.com/)


::::

+++

As a student at CityU, you also have access to a wide range of library resources. A useful e-learning resource to help you dive deeper into the cutting-edge computing technologies is LinkedIn Learning:

1. Open the [LinkedIn Learning](https://www.cityu.edu.hk/its/services-facilities/online-courses-linkedin-learning) page.
2. Click <kbd>LinkedIn Learning Login</kbd> to login with your CityU account.

+++

After logging in, take a look at the following relevant online courses:

::::{seealso} LinkedIn Learning
:class: dropdown

Some courses on introductory Python programming:

- [Python Essential Training](https://www.linkedin.com/learning-login/share?account=76816450&forceAccount=false&redirect=https%3A%2F%2Fwww.linkedin.com%2Flearning%2Fpython-essential-training-18764650%3Ftrk%3Dshare_ent_url%26shareId%3DaXCm1ZkcTTCExEgNCUlh%252Bw%253D%253D)
- [Learning the Python 3 Standard Library](https://www.linkedin.com/learning-login/share?account=76816450&forceAccount=false&redirect=https%3A%2F%2Fwww.linkedin.com%2Flearning%2Flearning-the-python-3-standard-library%3Ftrk%3Dshare_ent_url%26shareId%3DGcv4DyTKSuWBBsKpEmIamQ%253D%253D)


A course on how to use LinkedIn Learning: 

- [How to Use LinkedIn Learning](https://www.linkedin.com/learning-login/share?account=76816450&forceAccount=false&redirect=https%3A%2F%2Fwww.linkedin.com%2Flearning%2Fhow-to-use-linkedin-learning%3Ftrk%3Dshare_ent_url%26shareId%3DT0Oya4yGTOGygXyXbWpMCQ%253D%253D)

::::
