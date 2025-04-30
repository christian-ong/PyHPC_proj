#!/bin/bash
#BSUB -J job1
#BSUB -q c02613
#BSUB -W 5
#BSUB -R "span[hosts=1]"
#BSUB -R "rusage[mem=2GB]"
#BSUB -n 1
#BSUB -o job1_%J.out
#BSUB -e job1_%J.err

# activate the virtual environment
source /dtu/projects/02613_2024/conda/conda_init.sh
conda activate 02613

python Tasks1234/Task3.py 3