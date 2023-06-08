# InstructZero: Efficient Instruction Optimization for Black-Box Large Language Models

Lichang Chen*, Jiuhai Chen*, Tom Goldstein, Heng Huang, Tianyi Zhou

### [Project page](https://lichang-chen.github.io/InstructZero/) | [Paper](https://arxiv.org/abs/2306.03082)

<p align="center">
<img src=images/leviosa.jpg  width="80%" height="60%">
</p>
Find the optimal instruction is extremely important for achieving the "charm", and this holds true for Large Language Models as well. ("Wingardium Leviosa" was a charm used to make objects fly, or levitate. If you are interested in "leviOsa", please check the video in our project page).

<br>

If you have any questions, feel free to email Lichang Chen and Jiuhai Chen. (bobchen, jchen169 AT umd.edu)

## Abstract

Large language models~(LLMs) are instruction followers, but it can be challenging to find the best instruction for different situations, especially for black-box LLMs on which backpropagation is forbidden. Instead of directly optimizing the discrete instruction, we optimize a low-dimensional soft prompt applied to an open-source LLM to generate the instruction for the black-box LLM. On each iteration of the proposed method, which we call InstructZero, a soft prompt is converted into an instruction using the open-source LLM, which is then submitted to the black-box LLM for zero-shot evaluation, and the performance is sent to Bayesian optimization to produce new soft prompts improving the zero-shot performance. We evaluate InstructZero on different combinations of open-source LLMs and APIs including Vicuna and ChatGPT. Our results show that InstructZero outperforms SOTA auto-instruction methods across a variety of downstream tasks.
<br>
<br>


## Code Structure
We have two folders in InstructZero:
- automatic_prompt_engineering: this folder contains the functions from [APE](https://github.com/keirp/automatic_prompt_engineer), like you could use functions in generate.py to calculate the cost of the whole training required. BTW, to ensure a more efficient OPENAI querying, we make asynchronous calls of ChatGPT which is adapted from [Graham's code](https://gist.github.com/neubig/80de662fb3e225c18172ec218be4917a)

- experiments: contains the implementation of our pipeline and instruction-coupled kernels. 

## Installation
- create env
```
conda create -n InstructZero
```
- install torch >= 1.12 (choose the version that are suitable for your machine), ours:
```
conda install pytorch==1.13.1 torchvision==0.14.1 torchaudio==0.13.1 pytorch-cuda=11.6 -c pytorch -c nvidia
```
- install Botorch
```
conda install botorch -c pytorch -c gpytorch -c conda-forge
```
- install other requirements
```
pip install -r requirements.txt
```
- setup APE
```
cd InstructZero
python setup.py install
```
## Usage
1. Firstly, you need to prepare your OPENAI KEY.
```
export OPENAI_API_KEY=Your_KEY
```
2. Secondly, run the script to reproduce the experiments.
```
bash experiments/run_instructzero.sh
```

## Hyperparameters
Here we introduce the hyperparameters in our algorithm.
- instrinsic_dim: the dimension of the projection matrix, default=10
- soft tokens: the length of the tunable prompt embeddings, you can choose from [3, 10]

## Comments
Our codebase is based on the following repo:
- [Botorch](https://github.com/pytorch/botorch)
- [APE](https://github.com/keirp/automatic_prompt_engineer)

Thanks for their efforts to make the code public!

Stay tuned! We will make the usage and  installation of our packages as easy as possible!