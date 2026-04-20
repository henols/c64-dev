#!/usr/bin/env python3
"""
Skill packager for creating a distributable skill ZIP archive.
"""

import sys
import zipfile
from pathlib import Path
from quick_validate import validate_skill

MAX_SKILL_ZIP_BYTES = 15 * 1024 * 1024


def package_skill(skill_path, output_dir=None):
    skill_path = Path(skill_path).resolve()

    if not skill_path.exists():
        print(f"Error: Skill folder not found: {skill_path}")
        return None

    if not skill_path.is_dir():
        print(f"Error: Path is not a directory: {skill_path}")
        return None

    skill_md = skill_path / "SKILL.md"
    if not skill_md.exists():
        print(f"Error: SKILL.md not found in {skill_path}")
        return None

    print("Validating skill...")
    valid, message = validate_skill(skill_path)
    if not valid:
        print(f"Validation failed: {message}")
        return None
    print(message)

    output_path = Path(output_dir).resolve() if output_dir else Path.cwd()
    output_path.mkdir(parents=True, exist_ok=True)
    skill_filename = output_path / "skill.zip"

    try:
        with zipfile.ZipFile(skill_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for file_path in skill_path.rglob('*'):
                if not file_path.is_file():
                    continue
                if '__pycache__' in file_path.parts or file_path.suffix == '.pyc':
                    continue
                arcname = file_path.relative_to(skill_path.parent)
                zipf.write(file_path, arcname)

        archive_size = skill_filename.stat().st_size
        print(f"Archive size: {archive_size:,} bytes")
        if archive_size > MAX_SKILL_ZIP_BYTES:
            print("Warning: skill.zip exceeds the 15 MB upload limit.")

        print(f"Successfully packaged skill to: {skill_filename}")
        return skill_filename

    except Exception as e:
        print(f"Error creating zip file: {e}")
        return None


def main():
    if len(sys.argv) < 2:
        print("Usage: python package_skill.py <path/to/skill-folder> [output-directory]")
        sys.exit(1)

    skill_path = sys.argv[1]
    output_dir = sys.argv[2] if len(sys.argv) > 2 else None
    result = package_skill(skill_path, output_dir)
    sys.exit(0 if result else 1)


if __name__ == "__main__":
    main()
