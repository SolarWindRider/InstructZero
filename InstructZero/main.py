# import os
# from environs import Env

# env = Env()

# os.environ["CUDA_VISIBLE_DEVICES"] = 7
# SFT = 5
# RANDOM_PROJ = "uniform"
# INTRINSIC_DIM = 10
# model_dir = "lmsys/vicuna-7b-v1.3"
# MODEL_NAME = "vicuna"
# # model_dir='WizardLM/WizardLM-13B-V1.1'
# # MODEL_NAME='wizardlm'

# datasets = ["antonyms", "cause_and_effect", "common_concept", "diff"]
# for task in datasets:
#     print(task)
#     python experiments/run_instructzero.py \
#     --task task \
#     --random_proj ${RANDOM_PROJ} \
#     --n_prompt_tokens $SFT \
#     --intrinsic_dim $INTRINSIC_DIM \
#     --HF_cache_dir ${model_dir} \
#     --model_name ${MODEL_NAME}
