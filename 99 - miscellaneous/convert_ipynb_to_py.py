from pathlib import Path
import subprocess

# ===========================
# Configuration
# ===========================

PROJECT_ROOT = Path(r"D:\Practice\AI\RAG-Bootcamp")
OUTPUT_ROOT = PROJECT_ROOT / "src"

EXCLUDE_FOLDERS = {
    ".git",
    ".ipynb_checkpoints",
    "src"
}

# ===========================
# Convert notebooks
# ===========================

for notebook in PROJECT_ROOT.rglob("*.ipynb"):

    # Skip excluded folders
    if any(part in EXCLUDE_FOLDERS for part in notebook.parts):
        continue

    # Preserve folder structure
    relative_folder = notebook.parent.relative_to(PROJECT_ROOT)
    output_folder = OUTPUT_ROOT / relative_folder
    output_folder.mkdir(parents=True, exist_ok=True)

    print(f"Converting: {notebook.relative_to(PROJECT_ROOT)}")

    subprocess.run(
        [
            "jupyter",
            "nbconvert",
            "--to",
            "script",
            str(notebook),
            "--output-dir",
            str(output_folder),
        ],
        check=True,
    )

print("\n✅ All notebooks converted successfully!")
print(f"📁 Output Folder: {OUTPUT_ROOT}")