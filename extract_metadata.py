import os
import sys
import mimetypes
from datetime import datetime


def get_file_metadata(filepath):
    if not os.path.isfile(filepath):
        raise FileNotFoundError(f"File not found: {filepath}")
    stat = os.stat(filepath)
    metadata = {
        "filename": os.path.basename(filepath),
        "size_bytes": stat.st_size,
        "created": datetime.fromtimestamp(stat.st_ctime).isoformat(),
        "modified": datetime.fromtimestamp(stat.st_mtime).isoformat(),
        "mime_type": mimetypes.guess_type(filepath)[0] or "unknown"
    }
    return metadata


def main():
    if len(sys.argv) < 2:
        print("Usage: python extract_metadata.py <file_path>")
        sys.exit(1)
    filepath = sys.argv[1]
    try:
        meta = get_file_metadata(filepath)
        for k, v in meta.items():
            print(f"{k}: {v}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
