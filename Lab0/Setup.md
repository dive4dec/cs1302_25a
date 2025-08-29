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
title: Setup
skip_execution: true
---

+++

::::{attention}

This notebook is optional and NOT required for any course assessment activities. Lab tutor may go through them if time is available.

::::

```{code-cell} ipython3
if not input('Load JupyterAI? [Y/n]').lower()=='n':
    %reload_ext jupyter_ai
```

The course's programming environment is conveniently accessible via a [JupyterHub][jh] server, allowing remote access without the need to install any special software, thanks to [Project Jupyter](https://en.wikipedia.org/wiki/Project_Jupyter). Each student will have their own [Jupyter server](https://jupyter-server.readthedocs.io/en/latest/) with individual computing resources including CPU, memory, and even GPU for later materials on language models. This means you can easily write and run programs on your mobile devices using just a web browser.

[jh]: https://jupyterhub.readthedocs.io/en/stable/

+++

In practice, programmers have to use and setup different programming environments based on their tasks, and they have to find ways to work collaboratively with others under the same environment. This notebook will introduce a collaborative server with GPU, and how you may setup the basic environment locally on your computer.

+++

## Remote Access

+++

### Group Server

+++

#### Collaboration

+++

Registered students can collaboratively work on the same Jupyter server using the group (Jupyter) server `all-cs1302` that have higher resource limits than the individual user servers:

- Storage: 100GB
- Memory: 100GB
- CPU: 32 cores for default servers without GPU.
- GPU: 48GB for the GPU server option.

+++

To open the current notebook in the collaborative server, you can use a gitpull link such as:

> https://canvas.cityu.edu.hk/courses/64853/external_tools/retrieve?display=borderless&url=https%3A//dive.cs.cityu.edu.hk/cs1302_25a/hub/lti/launch%3Fcustom_next%3Dhttps%253A//dive.cs.cityu.edu.hk/cs1302_25a/user/all-cs1302/git-pull%253Frepo%253Dhttps%25253A//github.com/dive4dec/cs1302_25a%2526urlpath%253Dlab/tree/cs1302_25a/Lecture1/Introduction_to_Computer_Programming.ipynb

i.e., with `.../hub/user-redirect/...` replaced by `.../user/all-cs1302/...`.

+++

If the Jupyter server is not already running, you have an option to run it with GPU as shown in [](#fig:gpu_option):

+++

:::::{figure} images/options.dio.svg
:label: fig:gpu_option
:alt: Server options
:align: left

Server options for group server.
:::::

+++ {"editable": true, "slideshow": {"slide_type": ""}}

::::{note} What are the other server options?

- Each server runs the [Ubuntu](https://en.wikipedia.org/wiki/Ubuntu) operating system in a [container](https://en.wikipedia.org/wiki/Containerization_(computing)). See the [Dockerfile](https://github.com/dive4dec/jupyter/blob/main/cs1302nb/Dockerfile) for details.
- You can switch between the `Default` and other server options at any time by restarting the server and selecting the desired option.

::::

+++

To access and manage the server from the JupyterHub interface:

1. **Access the Hub Control Panel:**

   - Within the JupyterLab interface, click `File->Hub Control Panel`.

3. **Select the Admin Panel:**

   - In the top navigation bar of the Hub Control Panel, select the `Admin` Panel as shown in [](#fig:admin).

5. **Locate the User:**

   - Within the Admin Panel, look for the user named `all-cs1302`.

7. **Manage the Server:**
    - **If the server has not started:**
        - Click the action button labeled <kbd>Spawn Page</kbd> to select the server options with higher resource limits.
        - If you click the action button labeled <kbd>Start Server</kbd>, the server will start with lower resource limits that apply to individual user servers.
    - **If the group server is already running:**
        - Click the action button labeled <kbd>Access Server</kbd> to access the currently running server.
        - If necessary, click the action button labeled <kbd>Stop Server</kbd> to terminate the existing server.

+++

:::::{figure} images/admin.dio.svg
:label: fig:admin
:alt: Admin panel
:align: left

Admin panel for managing group server.
:::::

+++

Group servers run JupyterLab in collaborative mode, which provides real-time collaboration features as shown in [](#fig:collab). This allows multiple users to chat with each other and live edit the same notebook simultaneously. For more details, see the packages:

- [`jupyterlab-collaboration`](https://jupyterlab-realtime-collaboration.readthedocs.io/en/latest/)
- [`jupyterlab-chat`](https://github.com/jupyterlab/jupyter-chat?tab=readme-ov-file)

+++

:::::{figure} images/collab.dio.svg
:label: fig:collab
:alt: Collaborative mode
:align: left

Collaborative mode in JupyterLab.
:::::

+++

- To view another user's name while they’re editing the same notebook, hover over their cursor.
- To chat with others, you can either write directly in the notebook or invite them to a chat via the chat panel.[^chatbutton]

[^chatbutton]: The AI chat panel button looks identical to that for collaboration, as both use the `jupyterlab-chat` interface.

+++

::::{caution}

It is important to note that anyone in class can control the group server and read/write to it. Avoid storing sensitive information on the group server, and clean up files you are not using anymore. Multiple users editing the same file can potentially cause data loss or conflicts as well, so to mitigate this risk, you should use version control systems like Git to manage changes and collaborate more effectively through the server.

- The [`jupyterlab-git` extension](https://github.com/jupyterlab/jupyterlab-git) is installed to provide a graphical interface for Git within JupyterLab.
- VSCode interface also [supports Git out-of-the-box](https://code.visualstudio.com/docs/sourcecontrol/overview) and has Git-related extensions  such as [Git Graph](https://marketplace.visualstudio.com/items?itemName=mhutchie.git-graph) installed.


:::{seealso} LinkedIn Learning

- [Git Essential Training](https://www.linkedin.com/learning-login/share?account=76816450&forceAccount=false&redirect=https%3A%2F%2Fwww.linkedin.com%2Flearning%2Fgit-essential-training-25677984%3Ftrk%3Dshare_ent_url%26shareId%3DUFyvFtuiS4Go0n32Tuyu%252FA%253D%253D)

:::

::::

+++

#### Learning with GPU

+++ {"editable": true, "slideshow": {"slide_type": ""}}

With the GPU resources, we can run a generative model locally using [Ollama](https://ollama.com/). To do so, start the ollama service as follows.

1. In JupyterLab, navigate to the `File` menu.
1. Select `New` from the drop-down menu and choose `Terminal`.
1. The terminal window will appear. You can use this terminal to run a shell command. Enter the following command into the terminal prompt and hit enter.
   ```bash
   ollama serve
   ```
1. To terminate Ollama, simply type <kbd>Ctrl + C</kbd>, the same way you would terminate any shell command by Keyboard Interrupt.

+++

After running `ollama serve`, you can execute the following cells to chat with different models.

```{code-cell} ipython3
%%ai ollama:qwen3
Why LLM runs much faster on GPU than on CPU?
```

The first run will take a while as the model gets loaded into the memory.

```{code-cell} ipython3
%%ai ollama:gpt-oss
What is the difference between GPU and NPU?
```

Switching models also require additional time to reload the new model into the memory.

+++

To use Ollama with Jupyternaut:

1. Click the chat icon <i class="fas fa-comments"></i> on the left menu bar. A chat panel will open.
2. Click the gear icon <i class="fas fa-cog"></i> on the chat panel to set up the provider.
3. Select the Completion model as `DIVE Ollama :: ...` with `...` replaced by your desired model such as `phi3`. You may also use `Ollama :: *` to enter the model ID.
5. Click the `Save Changes` button.
6. Click the back arrow at the top to go back to the chat panel.
7. Enter some messages to see a response from the Azure OpenAI chat model.

+++

Different models have different sizes and may be good at different things. The following executes the a shell command to list other models that can be served by ollama.

```{code-cell} ipython3
if not input('Execute? [Y/n]').lower()=='n':
    !ollama list
```

The models reside in the directory specified by the environment variable `OLLAMA_MODELS`:[^custom]

[^custom]: To download or run a new ollama model, you need to set the directory to `~/.ollama` or any directory you have write access to. To use the model in JupyterNaut, select the Completion model as `Ollama :: *` and specify the model id. Avoid downloading very big models with over 30b parameters, as those cannot run on the current GPU without quantization.

```{code-cell} ipython3
%env OLLAMA_MODELS
```

+++ {"editable": true, "slideshow": {"slide_type": ""}}

::::{seealso} LinkedIn Learning

- [Installing the Llama 3 API with Ollama][1]

::::

[1]: https://www.linkedin.com/learning-login/share?account=76816450&forceAccount=false&redirect=https%3A%2F%2Fwww.linkedin.com%2Flearning%2Fdeveloping-with-llama-3-meta-s-innovative-and-open-large-language-model%2Finstalling-the-llama-3-api-with-ollama%3Ftrk%3Dshare_video_url%26shareId%3D%252BqFRPLijRLaE%252FglfqzX5Sg%253D%253D

+++

In addition to running ollama, you can learn to use [PyTorch](https://pytorch.org/) and other [machine learning packages](https://github.com/dive4dec/jupyter/blob/9db2952ca1eb734c12197e72765b3aa27daf4f58/cs1302nb/Dockerfile#L467) pre-installed in the server.

```{code-cell} ipython3
import torch

torch.cuda.is_available()
```

### Custom Packages

+++

#### Installing Packages

+++

To list existing packages installed in the Jupyter server:

```{code-cell} ipython3
if not input('Execute? [Y/n]').lower()=='n':
    !conda list
```

```{code-cell} ipython3
if not input('Execute? [Y/n]').lower()=='n':
    !pip list
```

You can install additional packages using the commands 

- [`conda install`](https://docs.conda.io/projects/conda/en/stable/commands/install.html) for packages on [Anaconda](https://anaconda.org/), or
- [`pip install`](https://packaging.python.org/en/latest/tutorials/installing-packages/) for packages on [PyPI](https://pypi.org/search/).

+++

An example using `pip` to install a package `cowsay`:

```{code-cell} ipython3
if not input('Execute? [Y/n]').lower()=='n': 
    !pip install cowsay
```

```{code-cell} ipython3
import cowsay

cowsay.cow("I am a pip installed package ((((((...ip)ip)ip)ip)ip)ip)!")
```

```{code-cell} ipython3
%%ai
What does pip stand for?
```

As another example, you can use conda to install the new super-fast [package manager `uv`](https://github.com/astral-sh/uv) written in Rust:

```{code-cell} ipython3
if not input('Execute? [Y/n]').lower()=='n':
    !conda install uv --yes
```

Let's take a glimpse of the future of Python by installing the latest version with `uv`:

```{code-cell} ipython3
if not input('Execute? [Y/n]').lower()=='n':
    !uv python install 3.14
```

Now, run the following Hello-World program which uses the newly introduced `t`-string:

```{code-cell} ipython3
!uvx python@3.14 -c 'name="World"; msg=t"Hello, {name}!"; print(msg)'
```

```{code-cell} ipython3
%%ai
What are the pros and cons of conda install, pip install, and uv install?
```

#### Conda Environment

+++

::::{caution}

Due to how your server is spawned using docker containers, the above installations do not persist when restarting the Jupyter server because the packages are saved to an emphemeral instead of a persistent storage.

::::

+++

Although this could be viewed as a feature rather than a bug—because you can test by installing a package and reset your environment simply by restarting the server—what if you want the installation to stick?

+++

You can create a conda environment[^conda] using a [YAML file](https://en.wikipedia.org/wiki/YAML) as follows:

[^conda]: See the [documentation](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html) for more details on managing conda environment.

```{code-cell} ipython3
%%writefile myenv.yaml
name: myenv
channels:
  - conda-forge
  - defaults
dependencies:
  - python=3.12
  - ipykernel
  - pip:
    - cowsay
```

```{code-cell} ipython3
%%ai
What does YAML stand for?
```

To create the environment, run

```bash
conda env create --file myenv.yaml
```
To update an existing environment, run

```bash
conda env update --file myenv.yaml --prune
```

+++

The environment will persist because we have reconfigured `conda` to save to environments to the home directory by default:

```{code-cell} ipython3
!cat /opt/conda/.condarc
```

```{code-cell} ipython3
%%ai
What does rc stand for in .condarc?
```

You can create a Jupyter kernel using the environment as shown in [](#fig:myenv) by running the command:[^kernel]

```bash
conda activate myenv
python -m ipykernel install \
    --user \
    --name "myenv" --display-name "myenv"
```

::::{caution}

Reload the browser window for the new kernel to take effect.

::::

[^kernel]: See the [documentation](https://ipython.readthedocs.io/en/stable/install/kernel_install.html#kernels-for-different-environments) for more details on creating kernels for conda environments.

+++

:::::{figure} images/myenv.dio.svg
:label: fig:myenv
:alt: Custom Jupyter kernel
:align: left

Custom Jupyter kernel from a conda environment.
:::::

+++

`conda activate` is the command to activate an environment to use its installed packages.

+++

To deactivate the conda environment in a terminal, run

```bash
conda deactivate
```

+++

To delete the kernel, run the command

```bash
rm -rf ~/.local/share/jupyter/kernels/myenv
```

+++

To delete the conda environment, run

```bash
conda deactivate
conda env remove -n myenv
```

+++

::::{caution}

We are actually using [micromamba](https://mamba.readthedocs.io/en/latest/user_guide/micromamba.html#micromamba) instead of conda, so some features such as `--clone base` would not work.

::::

```{code-cell} ipython3
%%ai
How is micromamba compared to mamba and conda?
```

### Desktop Applications

+++

In addition to using a web browser, you can connect to the JupyterHub server using desktop applications such as **JupyterLab Desktop** or **Visual Studio Code (VS Code)**. Following the links below to install the applications and the required extensions on your computer:

- [JupyterLab Desktop](https://github.com/jupyterlab/jupyterlab-desktop)
- [Visual Studio Code](https://code.visualstudio.com/) with the following extensions:
  - [JupyterHub Extension](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter-hub)
  - [JupyterHub File Explorer](https://marketplace.visualstudio.com/items?itemName=SebastianDazaAranzaes.jupyterhub-file-explorer)
  - [Jupyter Extension](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter)
  - [Python Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python)

::::{caution}

- **JupyterLab Desktop** is not actively maintained. Use it with caution, especially in environments where security is a concern.
- Some VS Code extensions such as the **JupyterHub Extension** are currently in preview mode. You might encounter bugs or instability.

::::

+++

#### Connecting via JupyterLab Desktop

+++

1. Launch the JupyterLab Desktop app.
2. Click **Connect...**
3. Enter the server URL:
   ```
   https://dive.cs.cityu.edu.hk/cs1302_25a/
   ```
5. Login with your EID and password.

::::{tip} Troubleshooting
:class: dropdown

If you encounter connection errors or the interface becomes unresponsive, try **reconnecting** or restarting the app.

::::

+++

#### Connecting via Visual Studio Code

+++

Before connection, make sure your Jupyter server is running since idle Jupyter servers are culled automatically to release the computing resources.

+++

1. Open JupyterHub, go to the [Token page ( 
   `File → Hub Control Panel → Token`)](https://dive.cs.cityu.edu.hk/cs1302_25a/hub/token)  
   and generate a token with your desired settings.
   ::::{caution}
   Do NOT close or move away from the page as you need to copy and paste the token later two times later.
   ::::

+++

2. In your local VS Code app:
   - Open the command palette (`View → Command Palette...`) and run:  
     `JupyterHub: Connect to JupyterHub`
   - Create a new connection with the following details:
     - **Name:** Any name of your choice such as `DIVE`
     - **URL:**
       ```
       https://dive.cs.cityu.edu.hk/cs1302_25a/
       ```
     - **Token:** Use the one you generated.

+++

3. Once connected, you’ll see the **JupyterHub Explorer** panel in the bottom-left corner.

   - Open any notebook file.
   - In the top-right corner, click **Select Kernel**.
   - Choose an existing **Existing JupyterHub Server...** and enter the following details:
       - **Server URL:**
         ```
         https://dive.cs.cityu.edu.hk/cs1302_25a/
         ```
       - **Username:** your EID
       - **Token:** the one you generated
       - **Server Name:** any name you prefer
       - **Kernel:** select **Python 3 (ipykernel)**

+++

You're now equipped to work with JupyterHub from your desktop. Just keep an eye out for quirks and bugs, and you'll be fine!

::::{tip} Troubleshooting
:class: dropdown

If VS Code behaves unexpectedly or fails to connect, try **reloading the window**:  
Go to the command palette and run:  
`Developer: Reload Window`

::::

+++

## Running locally

+++

### Local Installation

+++

You can install the minimal jupyter environment to run the course notebooks locally on your computer.

+++

First, ensure you have the following prerequisites installed:
1. [Conda](https://conda.io/projects/conda/en/latest/user-guide/install/index.html): You have some options on which distribution to install on what platform. Miniforge is recommended as we mainly use packages from `conda-forge`.
2. Git and Make: These can be installed in a terminal by the following command after activating the base Conda environment:
    ```bash
    conda install git make
    ```

+++

To install the jupyter environment for the course:

1. Git clone the [`cs1302nb` repository](https://github.com/dive4dec/cs1302nb.git):
```bash
git clone https://github.com/dive4dec/cs1302nb.git
cd cs1302nb
```

2. Run the [make command](https://github.com/dive4dec/cs1302nb/blob/fa5438bcf86b13bdf2abd646f780bb79fac13486/Makefile#L9) to create/update the conda environment `cs1302nb`:
```bash
make install
```

+++

To use the environment, activate it with:
```bash
conda activate cs1302nb
```

+++

Once activated, you can start JupyterLab under a working directory of your choice:
```bash
jupyter lab
```

+++

If the installation was successful, the following message will appear but with a different token:

```
...
    To access the server, open this file in a browser:
        file:///home/jovyan/.local/share/jupyter/runtime/jpserver-7-open.html
    Or copy and paste one of these URLs:
        http://2d94aee27406:8888/lab?token=afe3d84a4cadff3fe397640f651de4805471e7b19d1d6f1e
        http://127.0.0.1:8888/lab?token=afe3d84a4cadff3fe397640f651de4805471e7b19d1d6f1e
```

+++

Copy and paste the *last URL* into your web browser to access the JupyterLab.

+++

To access the course notebooks, you may use a gitpull link such as

> <http://127.0.0.1:8888/git-pull?repo=https%3A//github.com/dive4dec/cs1302_25a&urlpath=lab/tree/cs1302_25a/Lab0/Setup.ipynb/>

to open the current notebook.

+++

Alternatively, open a new terminal within the JupyterLab interface and run the following command:

```sh
gitpuller https://github.com/dive4dec/cs1302_25a main cs1302_25a
```

This command will:

- Pull the `main` branch of the GitHub repository `dive4dec/cs1302_25a`.
- Clone it into the subfolder `cs1302_25a` under your working directory.

+++

### Docker container

+++

A [docker container](https://en.wikipedia.org/wiki/Docker_(software)) is like a lightweight, standalone, and executable package that includes everything needed to run a piece of software, including the Jupyter server used for our course. If you know about [virtual machines](https://en.wikipedia.org/wiki/Virtual_machine), you may think of a docker container as a separate virtual machine running on your host machine, but with much less overhead.

+++

::::{caution}

For computers using [arm64](https://en.wikipedia.org/wiki/AArch64), [](#local-installation) is a better option than docker since docker has limited support for the architecture. Nevertheless, you are encouraged to play with docker and try to get things to work!

::::

+++

Indeed, you can also build and run the Jupyter server locally in your computer by installing Docker as follows.

+++

1. To install docker:
   - For macOS, install [Orbstack](https://orbstack.dev/), which is faster than the alternative below.
   - For Windows/Linux:
       - install Docker Desktop from the [official Docker website](https://www.docker.com/products/docker-desktop).
       - For Windows, see the [additional setup](https://docs.docker.com/desktop/wsl/) to use docker for WSL2 on Windows. 
   - Once installation is complete, open Orbstack or Docker Desktop and ensure it is running.

+++

2. For Windows WSL2 and Linux on [amd64](https://en.wikipedia.org/wiki/X86-64), open a terminal and run the following command to pull the Docker image:

    ```bash
    docker pull chungc/cs1302nb
    ```

+++

::::{seealso} What is a docker image?

A docker image is a the blueprint for creating Docker containers. When you run a Docker container, it is instantiated from an image. For example, `chungc/cs1302nb` is a docker image created from a text file [`Dockerfile.min`](https://github.com/dive4dec/jupyter/blob/main/cs1302nb/Dockerfile.min), which specifies how and what packages should be installed. The image was built using some [Make commands](https://github.com/dive4dec/jupyter/blob/main/README.md) in the repository. The resulting image was published to the public registry [DockerHub](https://hub.docker.com/r/chungc/cs1302nb/tags). You can also `git clone` the repository locally in your computer and modify the dockerfiles to build your desired image locally. The [Dockerfile](https://github.com/dive4dec/jupyter/blob/main/cs1302nb/Dockerfile) for the image running on the JupyterHub server is, which requires `>40GB` of storage to build.

::::

+++

3. To run the Docker Container:
    - Navigate to your working directory (e.g., `cs1302_home`) where you want to map to the home directory of the docker container:
      ```sh
      cd /part/to/cs1302_home
      ```
    - Run the Docker container with the following command:

      ```sh
      docker run -it --rm \
        -p 8888:8888 \
        -v $(pwd):/home/jovyan/ \
        chungc/cs1302nb \
        start-notebook.sh \
        --IdentityProvider.token=''
      ```
     - If successful, you can follow similar steps in [](#local-installation) to fetch the course notebooks using gitpuller.

+++

::::{seealso} What do the options mean?
:class: dropdown

The `docker run` command
- run the container interactively (`-it`);
- remove the container after it stops (`--rm`);
- map port `8888` on your host to port `8888` on the container (`-p 8888:8888`);
- mount the current working directory to the home directory `/home/jovyan/work` inside the container (`-v $(pwd):/home/jovyan/work`); and
- set the token to an empty string (`''`) so that you don't need to provide a token when logging in (`--IdentityProvider.token=''`).

See the [documentation](https://docs.docker.com/reference/cli/docker/container/run/) for other options.

::::

+++

::::{tip} Troubleshooting
:class: dropdown

If the host port `8888` is occupied, you can change it to another port such as `1302` by running the container with `-p1302:8888`. The port used to launch JupyterLab should be the host port, not the container port printed, i.e., the url to access the JupyterLab should be `http://127.0.0.1:1302`.

::::
