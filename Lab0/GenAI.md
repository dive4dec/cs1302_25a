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
title: GenAI
skip_execution: true
---

+++ {"editable": true, "slideshow": {"slide_type": ""}}

[Generative AI (GenAI)](https://en.wikipedia.org/wiki/Generative_artificial_intelligence) is a powerful tool in programming. You can play with them in various ways in the Jupyter server as explained in this notebook.

+++ {"editable": true, "slideshow": {"slide_type": ""}}

## Integration with Jupyter

+++ {"editable": true, "slideshow": {"slide_type": ""}}

 GenAI is integrated into the Jupyter interface using [`jupyter-ai`](https://github.com/jupyterlab/jupyter-ai/blob/main/README.md). You can interact with it directly inside the notebook or through a chat panel.

+++

### Jupyter Notebook

+++

To be able to chat with a [large language model (LLM)](https://en.wikipedia.org/wiki/Large_language_model) directly inside a notebook, run the {term}`line magic` below:

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

::::{caution}

It is important to load `jupyter_ai` conditionally, as shown above; otherwise, validation or auto‑grading may take an excessive amount of time because of the numerous LLM queries. If a notebook fails validation, it will also fail auto‑grading, potentially earning zero marks.

::::

+++ {"editable": true, "slideshow": {"slide_type": ""}}

After loading the `jupyter_ai` extension, run the following {term}`cell magic` to ask an LLM what an LLM is.

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
tags: [skip-execution]
---
%%ai
Explain what LLM is in one line.
```

+++ {"editable": true, "slideshow": {"slide_type": ""}}

Let's try different output formats:

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
tags: [skip-execution]
---
%%ai -f math
What is the Pythagoras theorem?
```

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
tags: [skip-execution]
---
%%ai -f html
What is the Pythagoras theorem?
```

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
tags: [skip-execution]
---
%%ai -f html
Illustrate the Pythagoras theorem using a diagram in SVG.
```

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
tags: [skip-execution]
---
%%ai
Can I trust you?
```

+++ {"editable": true, "slideshow": {"slide_type": ""}}

::::{caution}


- **Do NOT trust LLM**: [LLM can hallucinate](https://en.wikipedia.org/wiki/Hallucination_(artificial_intelligence)) and produce wrong answers. You should verify the correctness using reliable sources.

::::

```{code-cell} ipython3
%%ai
Can you give me answers to programming assignments directly?
```

Regardless of what the response is, LLM is surprisingly good at programming at
a basic level, thanks to the corpus of good program and software documentation. Let's use the following exercise as an example:

+++

::::{exercise}

Write a function `gcd` to calculate the GCD of two non-zero integers.

:::{caution}

The answer requires concepts you will learn later in the course!

:::

::::

```{code-cell} ipython3
---
nbgrader:
  grade: true
  grade_id: gcd
  locked: false
  points: 0
  schema_version: 3
  solution: true
  task: false
---
def gcd(a, b):
    ### BEGIN SOLUTION
    return gcd(b%a, a) if a else abs(b)
    ### END SOLUTION
```

```{code-cell} ipython3
---
nbgrader:
  grade: true
  grade_id: test-gcd
  locked: true
  points: 1
  schema_version: 3
  solution: false
  task: false
---
# tests
assert gcd(48, 18) == 6
assert gcd(-20, 30) == 10
```

```{code-cell} ipython3
---
nbgrader:
  grade: true
  grade_id: htest-gcd
  locked: true
  points: 1
  schema_version: 3
  solution: false
  task: false
---
# hidden tests
# DON'T remove this cell
### BEGIN HIDDEN TEST
assert gcd(-55, 89) == 1
### END HIDDEN TEST
```

Don't worry! You are allowed to use GenAI for [formative assessments (such as lab assignments) but *not* summative assessments (midterm quiz and final examination)](https://www.cityu.edu.hk/ted/stafflan/staff_development/assessment/ai_usage.html). So, let's use it now:

```{code-cell} ipython3
%%ai
Answer Exercise 1.
```

[Garbage-in, Garbage out.](https://en.wikipedia.org/wiki/Garbage_in,_garbage_out) We should give clear, context‑rich prompts to sharpen the model’s focus to give more relevant responses.

```{code-cell} ipython3
%%ai
Write a function `gcd` to calculate the GCD of two non-zero integers.
```

Mission impossible accomplished? Two key questions to reflect on this approach to GenAI:

- Is the program efficient?
- If it is, have I gained enough understanding to replicate the solution for similar problems?

+++ {"editable": true, "slideshow": {"slide_type": ""}}

::::{important} [Socratic Method to AI](https://en.wikipedia.org/wiki/Socratic_method)

- **Ask for hints, not answers**: Rushing to a solution hinders the development of the [computational‑thinking skills](https://en.wikipedia.org/wiki/Computational_thinking) required for problem solving.

::::

+++

As an example, the following prints a one-liner solution for the GCD.

```{code-cell} ipython3
def gcd(a, b): return gcd(a%b, a) if a else abs(b)  # one-liner for GCD
gcd_code = ''.join(In[-1].split('\n')[:-2])   # storing the code to query AI
print(gcd_code)
```

What's worth learning are the ingredients involved in writing such program:

```{code-cell} ipython3
%%ai
Explain the ingredients involved in writing the following program:
--
{gcd_code}
```

What is more challenging is the computational thinking involved that you will develop over time, mostly outside the classroom. Dive into it with the help of AI:

```{code-cell} ipython3
%%ai
Explain how Euclidean algorithm works and whether there are better methods.
```

### Chat Panel

+++ {"editable": true, "slideshow": {"slide_type": ""}}

There is also a [chat interface to chat with an LLM called Jupyternaut](https://jupyter-ai.readthedocs.io/en/v2/users/index.html#initial-question):

1. Click the chat icon <i class="fa-duotone fa-solid fa-messages"></i> <i class="fas fa-comments"></i> on the left menu bar. A chat panel will open.
2. Enter some prompts to chat with Jupyternaut:
   - ```
     What is computational thinking?
     ```
   - ```
     /clear
     ```
   - ```
     Explain file:cs1302i25a/source/Lab0/notebook_link_generator.py
     ```

+++

You can [add a cell’s text as context for Jupyternaut](https://jupyter-ai.readthedocs.io/en/v2/users/index.html#asking-about-something-in-your-notebook). E.g., try this for the following `gcd` function:

1. Select the cell you want to use.
2. Switch to Edit mode if it is a markdown cell. (Double click or press <kbd>Enter</kbd>.)
3. Highlight the desired text inside the cell.  
4. In the Jupyternaut panel, enter a prompt, click the down arrow button and choose `Send message with selection`.

```{code-cell} ipython3
from math import gcd   # yet another one-liner for gcd!
```

Another way to add context is [through an embedding model](https://jupyter-ai.readthedocs.io/en/v2/users/index.html#learning-about-local-data):

1. `/learn cs1302_25a/Lab0/` – tell the LLM to ingest the documents in *Lab0*.
2. `/ask Summarize what I need to do for Lab0` – request a concise summary of the lab tasks.
3. `/learn -d` – delete everything that was previously learned.

```{code-cell} ipython3
%%ai
Explain how a chat model and an embedding model work together to give 
domain-specific response.
```

You may check the default model configuration as follows:

1. Click the gear icon (⚙️) at the top‑right of the chat panel.
2. In the *Completion model* dropdown, select `DIVE :: chat`.
3. In the *Embedding model* dropdown, select `DIVE :: embed`.
4. Click <kbd>Save Changes</kbd>.
5. Click the back arrow to return to the chat panel.
6. Send a test message to confirm the chat model works.

If you are using other AI services (e.g., [Azure OpenAI](https://azure.microsoft.com/en-us/products/ai-services/openai-service), you may [reconfigure JupyterAI](https://jupyter-ai.readthedocs.io/en/v2/users/index.html#model-providers) to use them.

+++

If you want to reset the configuration in case of error, remove the configuration folder using the {term}`shell capture` below:

```{code-cell} ipython3
if input('Reset Jupyter AI configuration? [y/N]').lower() == 'y':
    !rm -rf ~/.local/share/jupyter/jupyter_ai
```

After deleting the folder, simply restart the Jupyter server to recreate it.

+++ {"editable": true, "slideshow": {"slide_type": ""}}

## Integration with VSCode

+++ {"editable": true, "slideshow": {"slide_type": ""}}

GenAI has been integrated into the Code server via the extensions below.

- [Continue](https://docs.continue.dev/): Configured to run our deployed models. 
- [Copilot](https://docs.github.com/en/copilot): Connects to a subscription-based service by Microsoft.

+++ {"editable": true, "slideshow": {"slide_type": ""}}

### Continue

+++ {"editable": true, "slideshow": {"slide_type": ""}}

To open the current folder `Lab0` in vscode, execute the following cell to generate the link:

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
---
from vscode_link_generator import vscode

vscode('.')
```

+++ {"editable": true, "slideshow": {"slide_type": ""}}

- [Start a chat](https://docs.continue.dev/features/chat/quick-start#how-to-use-chat-basic-usage) with
  ```
  Explain @vscode_link_generator.py
  ```
- [Switch to agent](https://docs.continue.dev/features/agent/quick-start), open the file `vscode_link_generator.py`, and ask:
  ```
  Which file do I have open?
  ```

+++

The configuration files for the Continue extension are stored in `.continue` under your home directory:

```{code-cell} ipython3
!ls ~/.continue
```

Similar to JupyterAI, you may [reconfigure Continue to use other providers.](https://docs.continue.dev/customize/model-providers/top-level/openai)

```{code-cell} ipython3
%%ai
How is an AI agent different from an AI chatbot?
```

If you want to reset the configuration in case of error, remove the configuration folder and then restart the Jupyter server to recreate it:

```{code-cell} ipython3
if input('Reset Jupyter AI configuration? [y/N]').lower() == 'y':
    !rm -rf ~/.continue
```

+++ {"editable": true, "slideshow": {"slide_type": ""}}

### Github Copilot

+++ {"editable": true, "slideshow": {"slide_type": ""}}

A popular AI-assisted programming tool is the Github Copilot for Visual Studio Code (VSCode).

+++ {"editable": true, "slideshow": {"slide_type": ""}}

::::{seealso} LinkedIn Learning

- [What is Github Copilot?][1]
- [What is Github?][2]
::::

[1]: https://www.linkedin.com/learning-login/share?account=76816450&forceAccount=false&redirect=https%3A%2F%2Fwww.linkedin.com%2Flearning%2Fai-pair-programming-with-github-copilot%2Fwhat-is-copilot%3Ftrk%3Dshare_video_url%26shareId%3Dm1KXWA7HTqaZU1P8byqvgA%253D%253D
[2]: https://www.linkedin.com/learning-login/share?account=76816450&forceAccount=false&redirect=https%3A%2F%2Fwww.linkedin.com%2Flearning%2Flearning-github-18719601%2Fwhat-is-github%3Ftrk%3Dshare_video_url%26shareId%3Dl%252Bbl2Q4nSMuZ5%252BkgXmIcWg%253D%253D

+++ {"editable": true, "slideshow": {"slide_type": ""}}

To get started, open the [setup guide](https://docs.github.com/en/copilot/setting-up-github-copilot/setting-up-github-copilot-for-yourself):

1. Follow Step 1 last bullet point to [get free access as a verified student](https://docs.github.com/en/copilot/managing-copilot/managing-copilot-as-an-individual-subscriber/getting-free-access-to-copilot-as-a-student-teacher-or-maintainer).
2. Instead of Step 2, you can access VSCode through the JupyterHub:
   1. Click `File → New launcher → VSCode` to open VSCode.
   2. Click the profile icon <i class="fas fa-user"></i> on the left menu and select `Sign in with Github to use Github Copilot`.
   3. After logging into Github, click the copilot icon at the top of VSCode to start chatting.
3. Step 3 is for advanced user who would like to use Github Copilot in the command line interface (CLI), which is available in both the JupyterLab and VSCode. You may directly jump to the [step](https://docs.github.com/en/copilot/managing-copilot/configure-personal-settings/installing-github-copilot-in-the-cli#installing-copilot-in-the-cli) following the prerequisites.

+++ {"editable": true, "slideshow": {"slide_type": ""}}

::::{seealso} How to chat with Copilot effectively?
:class: dropdown

See the [prompt engineering guide](https://docs.github.com/en/copilot/using-github-copilot/prompt-engineering-for-github-copilot) for some suggestions.

::::

+++ {"editable": true, "slideshow": {"slide_type": ""}}

## Glossary

:::::{admonition}
:class: dropdown

::::{glossary}

line magic
: A command in Jupyter notebook that starts with `%` such as `%load_ext` is called a [line magic](https://ipython.readthedocs.io/en/stable/interactive/magics.html#magic-load_ext). It can be used to performs tasks to change the notebook behavior, such as loading the `%%ai` cell magic.

cell magic
: A command in Jupyter notebook that starts with `%%` such as `%%ai` is called a [cell magic](https://ipython.readthedocs.io/en/stable/interactive/magics.html#cell-magics). It can be used to change the beavior of the cell, such as sending the text as a prompt to an LLM.

shell capture
: A command in Jupyter notebook that starts with `!` or `!!` is called a [shell capture](https://ipython.readthedocs.io/en/stable/interactive/magics.html#magic-sc). It can be used to execute a shell/terminal command.

REST API
: REST API stands for Representational State Transfer Application Programming Interface. It is a set of rules for building and interacting with web services that use standard HTTP methods to enable communication between client and server.

::::
:::::
