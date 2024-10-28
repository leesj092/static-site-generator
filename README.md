# Static Site Generator
A rather simple static site generator that converts markdown files into HTML pages.

## Features
- Converts Markdown files to HTML.
- Recursively processes nested directories within the content folder.
- Uses a customizable HTML template to insert content and titles.
- Outputs generated HTML files into the `public` directory.

## How it works
1. Generator scans the `content` directory (and its subdirectories) for .md files.
2. Each Markdown file is converted to HTML (used OOP) using a provided template.
3. Generator extracts the title (first `# ` line) from the Markdown file and replaces the placeholder {{ Title }} in the template.
4. The body of the Markdown content is converted to HTML and replaces the {{ Content }} placeholder in the template.
5. The generated HTML files are written to the `public` directory, preserving the directory structure from content.

## Directory Structure
```
root/
│
├── content/            # Directory containing Markdown files
│   ├── index.md        # Example Markdown file
│   ├── about.md        # Another Markdown file
│   └── blog/           # Nested directory
│       └── post.md     # Nested Markdown file
│
├── public/             # Destination directory for generated HTML files
│   ├── index.html      # Generated HTML file
│   ├── about.html      # Generated HTML file
│   └── blog/           # Nested directory
│       └── post.html   # Generated HTML file
│
├── template.html       # HTML template with {{ Title }} and {{ Content }} placeholders
└── main.sh             # Script to generate and serve pages
```

## Usage
Run `main.sh`
