#!/usr/bin/env python3
"""
Utility to insert invisible span elements into markdown files for video and ad slots.

Usage: python insert_spans.py <directory_path>
"""

import os
import sys
import re
from pathlib import Path


def find_markdown_files(directory):
    """Recursively find all markdown files in the given directory."""
    path = Path(directory)
    return list(path.rglob("*.md"))


def has_existing_spans(content):
    """Check if the content already has our span elements."""
    patterns = [
        r'<span\s+id="video-slot"',
        r'<span\s+id="ad-slot-[123]"'
    ]
    
    for pattern in patterns:
        if re.search(pattern, content, re.IGNORECASE):
            return True
    return False


def find_first_h2_position(lines):
    """Find the line index of the first ## heading."""
    for i, line in enumerate(lines):
        if line.strip().startswith('## '):
            return i
    return None


def find_paragraph_boundaries(lines):
    """Find all paragraph boundaries (double newlines) in the content."""
    boundaries = []
    for i in range(len(lines) - 1):
        # Check for empty line (paragraph boundary)
        if lines[i].strip() == '' and i > 0 and lines[i-1].strip() != '':
            # Make sure the next line isn't empty too (avoid multiple empty lines)
            if i + 1 < len(lines) and lines[i+1].strip() != '':
                boundaries.append(i)
    return boundaries


def insert_video_slot(lines):
    """Insert video slot before the first ## heading."""
    h2_index = find_first_h2_position(lines)
    if h2_index is not None:
        # Insert before the H2, with proper spacing
        lines.insert(h2_index, '<span id="video-slot"></span>')
        lines.insert(h2_index + 1, '')
        return True
    return False


def insert_ad_slots(lines):
    """Insert ad slots at approximately 40% and 80% of content."""
    # Find paragraph boundaries
    boundaries = find_paragraph_boundaries(lines)
    
    if len(boundaries) < 2:
        # Not enough paragraph boundaries for proper placement
        return False
    
    # Calculate positions (approximately 40% and 80% through the boundaries)
    total_boundaries = len(boundaries)
    pos1_index = int(total_boundaries * 0.4)
    pos2_index = int(total_boundaries * 0.8)
    
    # Make sure positions are different
    if pos2_index <= pos1_index:
        pos2_index = pos1_index + 1
    
    # Ensure we don't go out of bounds
    if pos2_index >= total_boundaries:
        pos2_index = total_boundaries - 1
    
    # Insert ad slots at the calculated positions (insert in reverse order to maintain indices)
    insertions = [
        (boundaries[pos2_index], '<span id="ad-slot-2"></span>'),
        (boundaries[pos1_index], '<span id="ad-slot-1"></span>')
    ]
    
    for position, span in insertions:
        # Insert after the empty line
        lines.insert(position + 1, span)
        lines.insert(position + 2, '')
    
    return True


def process_file(filepath):
    """Process a single markdown file to insert spans."""
    try:
        # Read the file
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if spans already exist
        if has_existing_spans(content):
            print(f"  Skipping (already has spans): {filepath}")
            return False
        
        # Split into lines for processing
        lines = content.splitlines()
        
        # Insert video slot
        video_inserted = insert_video_slot(lines)
        
        # Insert ad slots
        ads_inserted = insert_ad_slots(lines)
        
        if video_inserted or ads_inserted:
            # Write the modified content back
            new_content = '\n'.join(lines)
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            
            print(f"  ✓ Processed: {filepath}")
            return True
        else:
            print(f"  ! No suitable insertion points found: {filepath}")
            return False
            
    except Exception as e:
        print(f"  ✗ Error processing {filepath}: {str(e)}")
        return False


def main():
    """Main function to process all markdown files in a directory."""
    if len(sys.argv) != 2:
        print("Usage: python insert_spans.py <directory_path>")
        sys.exit(1)
    
    directory = sys.argv[1]
    
    if not os.path.isdir(directory):
        print(f"Error: '{directory}' is not a valid directory")
        sys.exit(1)
    
    print(f"Processing markdown files in: {directory}")
    print("-" * 50)
    
    # Find all markdown files
    md_files = find_markdown_files(directory)
    
    if not md_files:
        print("No markdown files found in the specified directory.")
        return
    
    print(f"Found {len(md_files)} markdown file(s)")
    print("-" * 50)
    
    # Process each file
    processed_count = 0
    for md_file in md_files:
        if process_file(md_file):
            processed_count += 1
    
    print("-" * 50)
    print(f"Summary: Processed {processed_count} out of {len(md_files)} files")


if __name__ == "__main__":
    main()