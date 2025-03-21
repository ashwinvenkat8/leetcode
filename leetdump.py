#!/usr/bin/env python
from argparse import ArgumentParser
from os import makedirs
from requests import get
from time import sleep
from tqdm import tqdm

def fetch_submissions(params: dict[str, str], cookies: dict[str, str], fetch_once: bool=False) -> list[dict]:
    api_url = "https://leetcode.com/api/submissions/"
    headers = {
        'content-type': 'application/json',
        'origin': 'https://leetcode.com',
        'referer': 'https://leetcode.com/submissions/',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36'
    }
    submissions = []

    while True:
        response = get(
            api_url,
            params=params,
            headers=headers,
            cookies=cookies
        )
        
        if response.status_code != 200:
            print(f"HTTP {response.status_code} error.\n")
            break
        
        response_json = response.json()
        submissions += response_json['submissions_dump']
        print(f"Fetched {len(submissions)} submissions.\r", end="")

        if fetch_once or not response_json['has_next']:
            break
        
        params['offset'] += params['limit']
        sleep(1)
    print("\n")
    
    return submissions

def write_source_files(submissions: list[dict], output_dir: str) -> None:
    # Write accepted submissions to files
    for submission in tqdm(submissions, desc='Writing source files', ncols=100):
        if submission['status_display'] != 'Accepted':
            continue
        
        if submission['lang'] == 'python3':
            file_ext = '.py'
            intermediate_dir = '/python3/'
        elif submission['lang'] == 'javascript':
            file_ext = '.js'
            intermediate_dir = '/javscript/'
        elif submission['lang'] == 'java':
            file_ext = '.java'
            intermediate_dir = '/java/'
        elif submission['lang'] == 'postgresql':
            file_ext = '.sql'
            intermediate_dir = '/postgresql/'
        else:
            file_ext = '.txt'
            intermediate_dir = '/'
        
        # Check and create output directory. Then, write the source file.
        makedirs(f"{output_dir}{intermediate_dir}", exist_ok=True)
        filename = f"{submission['question_id']}-{submission['title_slug']}-{submission['timestamp']}{file_ext}"
        
        with open(f"{output_dir}{intermediate_dir}{filename}", 'w', encoding='utf-8') as fh:
            fh.write(submission['code'])
        
    print(f"\nSaved source files to {output_dir}/")

def main() -> None:
    parser = ArgumentParser(description='Fetch and store your accepted Leetcode submissions.', allow_abbrev=False)
    parser.add_argument('csrftoken', help='Your active Leetcode CSRF token', type=str, metavar='CSRF_TOKEN')
    parser.add_argument('leetcode_session_token', help='Your active Leetcode session token', type=str, metavar='LEETCODE_SESSION_TOKEN')
    parser.add_argument('-O', '--output', help='Output directory path (default: src)', type=str, default='src')
    parser.add_argument('-o', '--offset', help='API pagination offset to use (default: 0)', type=int, default=0)
    parser.add_argument('-l', '--limit', help='API pagination limit to use (default: 20)', type=int, default=20)
    parser.add_argument('-1', '--once', help='Fetch only once. Use this with the `offset` and `limit` options to fetch a specific set of submissions.', action='store_true')
    args = parser.parse_args()

    output_dir = args.output
    params = {
        'offset': args.offset,
        'limit': args.limit
    }
    cookies = {
        'csrftoken': args.csrftoken,
        'LEETCODE_SESSION': args.leetcode_session_token
    }
    fetch_once = args.once

    print()
    submissions = fetch_submissions(params, cookies, fetch_once)
    write_source_files(submissions, output_dir)
    print()

if __name__ == '__main__':
    main()
