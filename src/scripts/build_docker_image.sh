# Prompt user for name of dataset (name of Stack Exchange website)
read -p 'Dataset: ' dataset

# Extract data
python -m src.data.etl --dataset $dataset --pipeline docker

# Copy CSVs to docker folder
cp data/processed/$dataset/*.csv docker/data/.

# Build docker image
sudo docker build -t stack-exchange-dwh .

# Delete data files in docker/data
rm docker/data/*.csv