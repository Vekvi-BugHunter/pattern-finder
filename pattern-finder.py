#!/usr/bin/env python3
import re
import requests
import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed

def fetch_and_search(url, pattern, headers):
    try:
        response = requests.get(url, headers=headers, timeout=10, allow_redirects=True)
        if response.status_code == 200:
            matches = sorted(set(re.findall(pattern, response.text, re.IGNORECASE)))
            if matches:
                return (url, matches)
    except requests.RequestException:
        pass
    return None


def main():
    parser = argparse.ArgumentParser(description="Multi-threaded URL regex finder and keyword extractor.")
    parser.add_argument("url_file", help="File containing list of URLs")
    parser.add_argument("regex", help="Regex pattern to search for (e.g. '\\b[\\w-]+\\.aspx\\b')")
    parser.add_argument("-H", "--header", help="Optional header, e.g. 'Cookie: session=abc123'")
    parser.add_argument("-t", "--threads", type=int, default=20, help="Number of concurrent threads (default=20)")
    parser.add_argument("-o", "--output", default="results.txt", help="Output file to save found keywords (default=results.txt)")
    args = parser.parse_args()

    # Load URLs
    try:
        with open(args.url_file, "r") as f:
            urls = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print(f"Error: File '{args.url_file}' not found.")
        return

    headers = {}
    if args.header:
        try:
            key, value = args.header.split(":", 1)
            headers[key.strip()] = value.strip()
        except ValueError:
            print("Invalid header format. Use: 'HeaderName: value'")
            return

    print(f"=== Pattern Finder (Threads: {args.threads}) ===")
    print(f"File: {args.url_file}")
    print(f"Regex: {args.regex}")
    print(f"Output File: {args.output}")
    if headers:
        print(f"Header: {headers}")
    print("==============================================\n")

    results = []
    all_matches = set()

    with ThreadPoolExecutor(max_workers=args.threads) as executor:
        future_to_url = {executor.submit(fetch_and_search, url, args.regex, headers): url for url in urls}
        for future in as_completed(future_to_url):
            result = future.result()
            if result:
                url, matches = result
                print(f"{url} - found: {', '.join(matches)}")
                results.append((url, matches))
                all_matches.update(matches)

    # Save all unique matches to file
    if all_matches:
        with open(args.output, "w") as out:
            for match in sorted(all_matches):
                out.write(match + "\n")
        print(f"\n✅ {len(all_matches)} unique matches saved to '{args.output}'.")
    else:
        print("\nNo matches found.")

    print(f"Scan complete. Found matches in {len(results)} of {len(urls)} URLs.")


if __name__ == "__main__":
    main()
