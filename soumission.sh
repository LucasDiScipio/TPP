#!/bin/bash
#SBATCH --job-name=test
#SBATCH --array=1-1000
#SBATCH --time=00:01:00 # days-hh-mm-ss
#SBATCH --mem-per-cpu=512 #megabytes

ml Python
ml matplotlib

i=0
while [ $i -le 10 ]
do
    echo "Task_ID : $SLURM_ARRAY_TASK_ID"
    python main.py $SLURM_ARRAY_TASK_ID $i
    i=$(( $i + 1 ))
done