#!/bin/bash
#SBATCH --job-name=mycalc
#SBATCH --output=output.txt
#SBATCH --time=01:00:00
#SBATCH --nodes=2
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=36
#SBATCH --mem=8G
#SBATCH --cluster=accelgor

module load Python/3.11.4-GCCcore-12.3.0
cd /scratch/gent/497/vsc49730/GitHub_HPC
python test.py
