# Receipt Extractor CLI

This project is a small CLI that scans a directory of receipt images, sends each
image to the OpenAI API, and returns structured JSON with the receipt's date,
total amount, vendor, and category.

## How it works
- `src/receipt-extractor/main.py` walks a directory of files, base64-encodes each image, and
  calls the extractor.
- `src/receipt-extractor/gpt.py` sends the image to the OpenAI Responses API and parses the
  JSON result.
- `src/receipt-extractor/file_io.py` handles basic file listing and base64 encoding.

## Requirements
- Python 3
- OpenAI Python SDK (`openai`)
- An `OPENAI_API_KEY` environment variable

Install dependencies:
```bash
pip install -r src/receipt-extractor/requirements.txt
```

Set your API key (example):
```bash
export OPENAI_API_KEY="your_api_key_here"
```

## Usage
Run the CLI on a directory of receipt images:
```bash
python src/receipt-extractor/main.py path/to/receipts --print
```

There is also a convenience target:
```bash
make run
```

Sample receipts live in `src/receipt-extractor/receipts`.

## Output format
The CLI prints a JSON object keyed by filename. Each entry contains:
- `date` (string or null)
- `amount` (string or null)
- `vendor` (string or null)
- `category` (one of `Meals`, `Transport`, `Lodging`, `Office Supplies`,
  `Entertainment`, or `Other`)

If `--print` is omitted, the script still processes the directory but produces
no terminal output.

## License
This project use MIT License
