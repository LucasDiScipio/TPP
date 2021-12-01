#!/bin/bash
#SBATCH --job-name=test
#SBATCH --array=1-200
#SBATCH --time=00:01:00 # days-hh-mm-ss
#SBATCH --mem-per-cpu=512 #megabytes

ml Python
ml matplotlib

echo "Task_ID : $SLURM_ARRAY_TASK_ID"
python test_cluster.py $SLURM_ARRAY_TASK_ID
