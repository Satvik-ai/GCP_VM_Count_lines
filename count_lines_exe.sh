#!/bin/bash
gsutil cp gs://satvik-storage-bucket/input_file.txt /home/chandrakarsatvik/ #Download the input_file.txt from the GCS bucket
python3 count_lines.py input_file.txt #Run the python script to count the number of lines in the input_file
gsutil rm gs://satvik-storage-bucket/output_file.txt #Remove the any preexisting output_file.txt
gsutil cp /home/chandrakarsatvik/output_file.txt gs://satvik-storage-bucket/ #Upload the output_file.txt to the GCS bucket
rm output_file.txt input_file.txt #Remove the files after processing them
echo "Successfully completed the process"