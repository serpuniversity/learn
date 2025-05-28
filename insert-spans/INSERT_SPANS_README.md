# Invisible Span Insertion Utility

## Overview
`insert_spans.py` is a Python utility that automatically inserts invisible HTML span elements into markdown files. These spans serve as anchor points for video and advertisement slots while remaining invisible in the rendered GitHub markdown.

## What It Does
The script inserts the following invisible span elements:
- `<span id="video-slot"></span>` - Before the first H2 (`##`) heading
- `<span id="ad-slot-1"></span>` - Approximately 40% through the article
- `<span id="ad-slot-2"></span>` - Approximately 80% through the article

These spans:
- Are completely invisible when rendered on GitHub
- Exist in the DOM for JavaScript targeting
- Don't affect the visual layout or content flow

## Usage

### Basic Usage
```bash
python insert_spans.py <directory_path>
```

### Example
```bash
# Process all markdown files in the css directory
python insert_spans.py css/

# Process all markdown files in the javascript directory
python insert_spans.py javascript/
```

## How It Works

1. **File Discovery**: Recursively finds all `.md` files in the specified directory
2. **Duplicate Check**: Skips files that already contain the span elements
3. **Smart Placement**:
   - Video slot: Inserted before the first `##` heading with proper spacing
   - Ad slots: Placed at paragraph boundaries (empty lines) to avoid breaking content
4. **Safe Processing**: Only modifies files that need spans inserted

## Features

- **Automatic Skip**: Files already containing spans are automatically skipped
- **Smart Positioning**: Spans are inserted at paragraph boundaries to maintain content integrity
- **Recursive Processing**: Processes all markdown files in subdirectories
- **Clear Output**: Shows processing status for each file

## Output Example
```
Processing markdown files in: css
--------------------------------------------------
Found 56 markdown file(s)
--------------------------------------------------
  ✓ Processed: css/CSS Align.md
  ✓ Processed: css/CSS Background.md
  Skipping (already has spans): css/CSS Border.md
  ! No suitable insertion points found: css/README.md
--------------------------------------------------
Summary: Processed 45 out of 56 files
```

## Requirements
- Python 3.6 or higher
- No external dependencies (uses only Python standard library)

## Notes
- The script modifies files in place - consider backing up your files first if needed
- Files without suitable insertion points (e.g., very short files) will be skipped
- The spans are empty and have zero visual impact on the rendered markdown