#!/bin/bash

REPO_URL="https://github.com/jun521ju/IEEE_SP_2022_WtaGraph.git"
REPO_DIR="Docker/IEEE_SP_2022_WtaGraph"

if [ ! -d "$REPO_DIR" ]; then
    echo "Cloning the repository from $REPO_URL..."
    git clone "$REPO_URL" "$REPO_DIR"
else
    echo "Repository already exists. Pulling the latest changes..."
    cd "$REPO_DIR" || exit
    git pull origin main  # pull from main
    cd ..
fi

if [ -d "./data" ]; then
    echo "Checking for necessary .npy and other files in the 'data' directory..."

    FILES=(
        "full_edge_feat.npy"
        "full_edge_label.npy"
        "full_node_feat.npy"
        "rand5k_edge_feat.npy"
        "rand5k_edge_label.npy"
        "rand5k_node_feat.npy"
    )

    DEST_DIR="$REPO_DIR/data/feat_data/top10k"

    for FILE in "${FILES[@]}"; do
        if [ -f "./data/$FILE" ]; then
            echo "Overwriting $DEST_DIR/$FILE"
            cp "./data/$FILE" "$DEST_DIR/$FILE"

            # remove .placeholder files
            PLACEHOLDER_FILE="$DEST_DIR/[$FILE].placeholder"
            if [ -f "$PLACEHOLDER_FILE" ]; then
                echo "Removing placeholder file: $PLACEHOLDER_FILE"
                rm -f "$PLACEHOLDER_FILE"
            fi
        else
            echo "$FILE does not exist in the 'data' directory."
        fi
    done

    # non .npy files
    OTHER_FILES=(
        "full_graph.edgelist"
        "full_id_edge_map_list.pickle"
        "full_id_node_map.pickle"
        "rand5k_graph.edgelist"
        "rand5k_id_edge_map_list.pickle"
        "rand5k_id_node_map.pickle"
    )

    GRAPH_DIR="$REPO_DIR/data/graph_data/top10k"

    for FILE in "${OTHER_FILES[@]}"; do
        if [ -f "./data/$FILE" ]; then
            echo "Overwriting $GRAPH_DIR/$FILE"
            cp "./data/$FILE" "$GRAPH_DIR/$FILE"

            if [[ "$FILE" == *.edgelist ]]; then
                PLACEHOLDER_FILE="$GRAPH_DIR/[$FILE].placeholder"
            elif [[ "$FILE" == *.pickle ]]; then
                BASE_NAME=$(basename "$FILE" .pickle)
                PLACEHOLDER_FILE="$GRAPH_DIR/[$BASE_NAME].placeholder"
            fi

            if [ -f "$PLACEHOLDER_FILE" ]; then
                echo "Removing placeholder file: $PLACEHOLDER_FILE"
                rm -f "$PLACEHOLDER_FILE"
            fi
        else
            echo "$FILE does not exist in the 'data' directory."
        fi
    done
else
    echo "'data' directory does not exist in the current directory. Download the dataset from: https://zenodo.org/records/5166790"
fi

echo "data copied successfully."

# build Docker image
echo "Building the Docker image from the Dockerfile..."
cd Docker

docker build -t wta_image .

echo "Docker image built successfully."
