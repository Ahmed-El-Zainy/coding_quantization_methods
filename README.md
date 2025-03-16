# Coding Quantization Methods

----
## if any one want to contribute to this repo,
- juse send email : ahmedelzainy44@gmail.com
to add you with user name to the repo.
-----


This section provides an overview of various quantization methods used in LLMs, along with their implementation progress.

## Mapping:
| Method  | Release Date | Link | Progress |
|---------|-------------|------|-----------|
| LLM.int8() | Aug 2022 | [🔗 Link](https://huggingface.co/blog/hf-bitsandbytes-integration) | 🚧 Under Progress |
| GPTQ | Oct 2022 | [🔗 Link](https://arxiv.org/abs/2210.17323) | 🚧 Under Progress |
| QLoRA | May 2023 | [🔗 Link](https://arxiv.org/abs/2305.14314) | 🚧 Under Progress |
| AWQ | Jun 2023 | [🔗 Link](https://arxiv.org/abs/2306.00978) | 🚧 Under Progress |
| Quip# | Jul 2023 | [🔗 Link](https://arxiv.org/abs/2307.13304) | 🚧 Under Progress |
| GGUF | Aug 2023 | [🔗 Link](https://github.com/ggerganov/llama.cpp/pull/2333) | 🚧 Under Progress |
| HQQ | Nov 2023 | [🔗 Link](https://arxiv.org/abs/2311.07678) | 🚧 Under Progress |
| AQLM | Feb 2024 | [🔗 Link](https://arxiv.org/abs/2402.07634) | 🚧 Under Progress |




### Installation Steps
1. Clone the repo:
    ```sh
    https://github.com/Ahmed-El-Zainy/coding_quantization_methods.git
    cd coding_quantization_methods
    ```
2. Install the dependencies:
    for starting direct to the running:
    ```sh
    . ./setup.sh --new-env
    ```
    
    **Before running the following command there are somethings to note:**
    - By adding `--new-env`, a new conda environment named `trellis` will be created. If you want to use an existing conda environment, please remove this flag.
    - By default the `trellis` environment will use pytorch 2.4.0 with CUDA 11.8. If you want to use a different version of CUDA (e.g., if you have CUDA Toolkit 12.2 installed and do not want to install another 11.8 version for submodule compilation), you can remove the `--new-env` flag and manually install the required dependencies. Refer to [PyTorch](https://pytorch.org/get-started/previous-versions/) for the installation command.
    - If you have multiple CUDA Toolkit versions installed, `PATH` should be set to the correct version before running the command. For example, if you have CUDA Toolkit 11.8 and 12.2 installed, you should run `export PATH=/usr/local/cuda-11.8/bin:$PATH` before running the command.
    - By default, the code uses the `flash-attn` backend for attention. For GPUs do not support `flash-attn` (e.g., NVIDIA V100), you can remove the `--flash-attn` flag to install `xformers` only and set the `ATTN_BACKEND` environment variable to `xformers` before running the code. See the [Minimal Example](#minimal-example) for more details.
    - The installation may take a while due to the large number of dependencies. Please be patient. If you encounter any issues, you can try to install the dependencies one by one, specifying one flag at a time.
    - If you encounter any issues during the installation, feel free to open an issue or contact us.
    
    Create a new conda environment named `trellis` and install the dependencies:
    ```sh
    . ./setup.sh --new-env --basic --xformers --flash-attn --diffoctreerast --spconv --mipgaussian --kaolin --nvdiffrast
    ```
    The detailed usage of `setup.sh` can be found by running `. ./setup.sh --help`.
    ```sh
    Usage: setup.sh [OPTIONS]
    Options:
        -h, --help              Display this help message
        --new-env               Create a new conda environment
        --basic                 Install basic dependencies
        --xformers              Install xformers
        --flash-attn            Install flash-attn
        --diffoctreerast        Install diffoctreerast
        --vox2seq               Install vox2seq
        --spconv                Install spconv
        --mipgaussian           Install mip-splatting
        --kaolin                Install kaolin
        --nvdiffrast            Install nvdiffrast
        --demo                  Install all dependencies for demo
    ```


## References:
* https://archive.ph/rGZ2H
* https://github.com/Cornell-RelaxML/QuIP
* https://github.com/microsoft/TRELLIS


