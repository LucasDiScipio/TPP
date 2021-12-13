#!/bin/bash
#SBATCH --job-name=test
#SBATCH --array=1-10000
#SBATCH --test=0
#SBATCH --time=00:01:00 # days-hh-mm-ss
#SBATCH --mem-per-cpu=512 #megabytes

ml Python
ml matplotlib

echo "Task_ID : $SLURM_ARRAY_TASK_ID"
python main.py $SLURM_ARRAY_TASK_ID $TEST
