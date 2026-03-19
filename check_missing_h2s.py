import csv
import os

root = "datasets/how2sign"
split = "train"

csv_path = os.path.join(
    root, split, "re_aligned",
    f"how2sign_realigned_{split}_preprocessed_fps.csv"
)
poses_dir = os.path.join(root, split, "poses")

with open(csv_path, newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    csv_names = {row["SENTENCE_NAME"] for row in reader}

pose_dirs = {
    name for name in os.listdir(poses_dir)
    if os.path.isdir(os.path.join(poses_dir, name))
}

missing = csv_names - pose_dirs
extra = pose_dirs - csv_names

print(f"CSV entries: {len(csv_names)}")
print(f"Pose dirs:    {len(pose_dirs)}")
print(f"Missing dirs: {len(missing)}")
print(f"Extra dirs:   {len(extra)}")
