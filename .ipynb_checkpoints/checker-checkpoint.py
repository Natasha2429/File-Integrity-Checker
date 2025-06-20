# 📦 Import required libraries
import os
import hashlib
import json
from datetime import datetime

# 📂 Set folder and hash storage file
folder_to_monitor = "test_files"  # 🔁 Change this to your folder name
hash_file = "hashes.json"

# 🔁 Function to calculate SHA-256 hash
def calculate_hash(filepath):
    sha256_hash = hashlib.sha256()
    try:
        with open(filepath, "rb") as f:
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
        return sha256_hash.hexdigest()
    except FileNotFoundError:
        return None

# 🔁 Generate hashes for all files in the folder
def generate_hashes(folder_path):
    file_hashes = {}
    for root, dirs, files in os.walk(folder_path):
        for filename in files:
            full_path = os.path.join(root, filename)
            rel_path = os.path.relpath(full_path, folder_path)
            file_hashes[rel_path] = calculate_hash(full_path)
    return file_hashes

# 💾 Save hash values to a JSON file
def save_hashes(hash_dict, filename):
    with open(filename, "w") as f:
        json.dump(hash_dict, f, indent=4)

# 📂 Load existing hash values from JSON
def load_hashes(filename):
    if os.path.exists(filename):
        with open(filename, "r") as f:
            return json.load(f)
    else:
        return {}

# 🔍 Compare stored and current hashes to find changes
def check_integrity(original_hashes, current_hashes):
    issues = []

    for file in original_hashes:
        if file not in current_hashes:
            issues.append(f"❌ File deleted: {file}")
        elif original_hashes[file] != current_hashes[file]:
            issues.append(f"⚠️ File modified: {file}")

    for file in current_hashes:
        if file not in original_hashes:
            issues.append(f"🆕 New file added: {file}")

    return issues

# 🚀 Main logic
original_hashes = load_hashes(hash_file)
current_hashes = generate_hashes(folder_to_monitor)

print(f"🕒 Running File Integrity Check on '{folder_to_monitor}' at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

if not original_hashes:
    print("🔐 First run - saving initial file hashes...")
    save_hashes(current_hashes, hash_file)
    print("✅ Hashes saved. Rerun this script to monitor changes.")
else:
    print("🔍 Checking for file changes...")
    results = check_integrity(original_hashes, current_hashes)
    
    if results:
        print("📢 Issues found:")
        for res in results:
            print(res)
    else:
        print("✅ No file changes detected.")

    # Uncomment this line to update the stored hashes if needed:
    # save_hashes(current_hashes, hash_file)
