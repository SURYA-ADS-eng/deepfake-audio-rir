import os

AUDIO_EXTENSIONS = (".flac", ".wav")

def count_audio_files(directory):
    total = 0
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(AUDIO_EXTENSIONS):
                total += 1
    return total


if __name__ == "__main__":
    dataset_root = "data/ASVspoof2019_LA"

    print("ASVspoof2019 Dataset Statistics")
    print("-" * 40)

    for folder in [
        "ASVspoof2019_LA_train",
        "ASVspoof2019_LA_dev",
        "ASVspoof2019_LA_eval"
    ]:
        path = os.path.join(dataset_root, folder)

        if os.path.exists(path):
            print(f"{folder}: {count_audio_files(path)} audio files")
        else:
            print(f"{folder}: Not Found")
