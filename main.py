import argparse
from flask import Flask, request, jsonify
import subprocess
import sys
import json
from typing import Dict, Any

# Webhook handler for GitHub
def handle_github_webhook(payload: Dict[str, Any]) -> None:
    """Handle incoming GitHub webhook events."""
    event_type = payload.get('event_type')
    if event_type == 'push':
        print('Received push event, processing...')
        # Example: Extract branch and commit info
        head_commit = payload.get('head_commit', {})
        branch = payload.get('ref', '').split('/')[-1]
        print(f'Push to branch: {branch}')
        print(f'Commit message: {head_commit.get('message')}')
    elif event_type == 'pull_request':
        print('Received pull request event')
        action = payload.get('action')
        print(f'PR {action}')
    else:
        print(f'Unhandled event type: {event_type}')

# CLI command runner
def run_git_command(args: list) -> None:
    try:
        result = subprocess.run(['git'] + args, capture_output=True, text=True, check=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f'Git command failed: {e.stderr}', file=sys.stderr)

# CLI argument parser
def parse_cli_args() -> None:
    parser = argparse.ArgumentParser(description='Git Source Manager CLI')
    parser.add_argument('command', nargs='?', help='Git command to run')
    parser.add_argument('args', nargs=argparse.REMAINDER, help='Arguments for the Git command')
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        return
    
    command_map = {
        'init': ['init'],
def handle_webhook_request() -> None:
    """Handle incoming webhook requests from GitHub."""
    if not sys.stdin.isatty():
        try:
            payload = json.load(sys.stdin)
            handle_github_webhook(payload)
        except json.JSONDecodeError as e:
            print(f'Invalid JSON in webhook: {e}', file=sys.stderr)
    else:
        print('No input provided', file=sys.stderr)
        'add': ['add'] + args.args,
        'commit': ['commit', '-m'] + args.args,
        'status': ['status'],
        'log': ['log'],
        'branch': ['branch'],
        'checkout': ['checkout'] + args.args,
        'merge': ['merge'] + args.args,
        'push': ['push'] + args.args,
        'pull': ['pull'] + args.args
    }
    
    if args.command in command_map:
        run_git_command(command_map[args.command])
    else:
        print(f'Unknown command: {args.command}', file=sys.stderr)
        parser.print_help()

# Main entry point
def main() -> None:
    # Check if input is from stdin (webhook)
    if not sys.stdin.isatty():
        try:
            payload = json.load(sys.stdin)
            handle_github_webhook(payload)
        except json.JSONDecodeError as e:
            print(f'Invalid JSON in webhook: {e}', file=sys.stderr)
    else:
        # Run CLI mode
        parse_cli_args()

if __name__ == '__main__':
    main()
    else:
        print(f'Unknown command: {args.command}', file=sys.stderr)
        parser.print_help()
    # Webhook server endpoint
    from http.server import HTTPServer, BaseHTTPRequestHandler
    import threading
    class WebhookHandler(BaseHTTPRequestHandler):
        def do_POST(self):
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
def start_webhook_server():
    app.run(host='127.0.0.1', port=8000, threaded=True)
    except Exception as e:
        return jsonify({'error': str(e)}), 500
                payload = json.loads(post_data.decode('utf-8'))
                handle_github_webhook(payload)
                self.send_response(200)
                self.end_headers()
            except json.JSONDecodeError as e:
                self.send_response(400)
                self.end_headers()
                print(f'Invalid JSON in webhook: {e}', file=sys.stderr)
    def start_webhook_server():
        server = HTTPServer(('127.0.0.1', 8000), WebhookHandler)
        print('Webhook server running on http://127.0.0.1:8000')
        server.serve_forever()
    # Main entry point
    def main() -> None:
        # Check if input is from stdin (webhook)
        if not sys.stdin.isatty():
            try:
                payload = json.load(sys.stdin)
                handle_github_webhook(payload)
            except json.JSONDecodeError as e:
                print(f'Invalid JSON in webhook: {e}', file=sys.stderr)
        else:
            # Run CLI mode
            parse_cli_args()
    # Start webhook server in background thread
    def run_server():
        server_thread = threading.Thread(target=start_webhook_server, daemon=True)
        server_thread.start()
    if __name__ == '__main__':
        run_server()
        main()
    # Start webhook server in background thread
    def run_server():
        server_thread = threading.Thread(target=start_webhook_server, daemon=True)
        server_thread.start()

    if __name__ == '__main__':
        run_server()
        main()