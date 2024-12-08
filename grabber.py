import requests
import re
import threading
import random
import time
import argparse
import sys
from datetime import datetime
from urllib.parse import urlparse

class DomainGrabber:
    def __init__(self, extension, total_pages=10, threads=5, output_file='domains.txt', timeout=10, delay=0):
        self.extension = extension
        self.total_pages = total_pages
        self.threads = threads
        self.output_file = output_file
        self.timeout = timeout
        self.delay = delay
        self.domains = set()
        self.lock = threading.Lock()
        self.start_time = time.time()
        self.success_count = 0
        self.error_count = 0
        self.user_agents = [
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15',
        ]

    def print_status(self, message):
        with self.lock:
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(f"[{current_time}] {message}")

    def validate_domain(self, domain):
        try:
            parsed = urlparse(f"http://{domain}")
            return all([parsed.netloc, "." in parsed.netloc])
        except:
            return False

    def fetch_domains(self, page):
        try:
            if self.delay > 0:
                time.sleep(random.uniform(0, self.delay))

            url = f"https://www.google.com/search?q=site:{self.extension}&start={page * 10}"
            headers = {'User-Agent': random.choice(self.user_agents)}
            
            response = requests.get(url, headers=headers, timeout=self.timeout)
            
            if response.status_code == 200:
                found_domains = re.findall(r'http[s]?://(?:www\.)?([a-zA-Z0-9-]+\.' + re.escape(self.extension) + r')', response.text)
                valid_domains = [d for d in found_domains if self.validate_domain(d)]
                
                with self.lock:
                    self.domains.update(valid_domains)
                    self.success_count += 1
                    self.print_status(f"Found {len(valid_domains)} domains on page {page}")
            else:
                with self.lock:
                    self.error_count += 1
                    self.print_status(f"Error on page {page}: HTTP {response.status_code}")
                    
        except requests.RequestException as e:
            with self.lock:
                self.error_count += 1
                self.print_status(f"Error on page {page}: {str(e)}")

    def save_results(self):
        try:
            with open(self.output_file, 'w') as file:
                for domain in sorted(self.domains):
                    file.write(f'{domain}\n')
            return True
        except Exception as e:
            self.print_status(f"Error saving results: {str(e)}")
            return False

    def print_summary(self):
        elapsed_time = time.time() - self.start_time
        self.print_status(f"""
Summary:
--------
Total domains found: {len(self.domains)}
Successful requests: {self.success_count}
Failed requests: {self.error_count}
Time elapsed: {elapsed_time:.2f} seconds
Output file: {self.output_file}
        """)

    def run(self):
        self.print_status(f"Starting domain grabber for .{self.extension}")
        self.print_status(f"Using {self.threads} threads and {self.total_pages} pages")

        pages = list(range(self.total_pages))
        random.shuffle(pages)
        
        threads = []
        for page in pages:
            if len(threads) >= self.threads:
                for t in threads:
                    t.join()
                threads.clear()
            
            t = threading.Thread(target=self.fetch_domains, args=(page,))
            threads.append(t)
            t.start()

        for t in threads:
            t.join()

        if self.save_results():
            self.print_status("Results saved successfully")
        else:
            self.print_status("Failed to save results")

        self.print_summary()

def main():
    parser = argparse.ArgumentParser(description='Domain Grabber Tool')
    parser.add_argument('-e', '--extension', required=True, help='Domain extension to search for')
    parser.add_argument('-o', '--output', default='domains.txt', help='Output file path')
    parser.add_argument('-p', '--pages', type=int, default=10, help='Number of pages to search')
    parser.add_argument('-t', '--threads', type=int, default=5, help='Number of threads to use')
    parser.add_argument('-d', '--delay', type=float, default=0, help='Delay between requests in seconds')
    parser.add_argument('--timeout', type=int, default=10, help='Request timeout in seconds')

    args = parser.parse_args()

    try:
        grabber = DomainGrabber(
            extension=args.extension,
            total_pages=args.pages,
            threads=args.threads,
            output_file=args.output,
            timeout=args.timeout,
            delay=args.delay
        )
        grabber.run()
    except KeyboardInterrupt:
        print("\nProcess interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
