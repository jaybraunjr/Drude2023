#!/bin/bash

# Define start and end numbers for the CHARMM input files
start_inp=11
end_inp=20

# Define the corresponding start FILENUM (181 for inp_vel11)
start_file_num=311

# Calculate the offset based on start_inp and start_file_num
offset=$((start_file_num - start_inp))

# Loop over each of the CHARMM input files
for inp_num in $(seq $start_inp $end_inp); do
    # Calculate FILENUM based on inp_num
    FILENUM=$(($inp_num + $offset))
    
    # Define the SLURM script name (assuming it matches the inp_num)
    slurm_script="slurm_charmm${inp_num}"  # Ensure the script names are correct and exist

    if [ -f "$slurm_script" ]; then
        # Export FILENUM for use in the SLURM script
        export FILENUM
        
        # Submit the job
        sbatch "$slurm_script"
        
        # Optional: Wait a bit to avoid overloading the scheduler
        sleep 1
    else
        echo "SLURM script $slurm_script not found."
    fi
done

