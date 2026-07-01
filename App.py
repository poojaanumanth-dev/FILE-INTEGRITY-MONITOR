import hashlib
import os
import time
from datetime import datetime

def get_file_hash(filepath):
    try:
        with open(filepath, "rb") as f:
            return hashlib.sha256(f.read()).hexdigest()
    except:
        return None

def create_baseline(directory):
    baseline = {}
    print(f"Creating baseline for: {directory}")
    for root, _, files in os.walk(directory):
        for file in files:
            filepath = os.path.join(root, file)
            file_hash = get_file_hash(filepath)
            if file_hash:
                baseline[filepath] = file_hash
    return baseline

def check_integrity(baseline, directory):
    print(f"\nChecking integrity at {datetime.now()}")
    current = {}
    changes = []
    
    for root, _, files in os.walk(directory):
        for file in files:
            filepath = os.path.join(root, file)
            current_hash = get_file_hash(filepath)
            if current_hash:
                current[filepath] = current_hash
                if filepath in baseline:
                    if baseline[filepath] != current_hash:
                        changes.append(f"🔴 MODIFIED: {filepath}")
                else:
                    changes.append(f"🟢 NEW: {filepath}")
    
    # Check for deleted files
    for filepath in baseline:
        if filepath not in current:
            changes.append(f"❌ DELETED: {filepath}")
    
    if changes:
        print("\nChanges Detected:")
        for change in changes:
            print(change)
    else:
        print("✅ No changes detected. Files are intact.")

# Usage
if __name__ == "__main__":
    target_dir = input("Enter directory to monitor: ").strip()
    if not os.path.exists(target_dir):
        print("Directory not found!")
    else:
        baseline = create_baseline(target_dir)
        print("Baseline created! Monitoring started...")
        while True:
            check_integrity(baseline, target_dir)
            time.sleep(10)  # Check every 10 seconds