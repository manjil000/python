#!/usr/bin/env python3
import json, requests, sys
from urllib.parse import urljoin

def load_openapi(spec_path):
    with open(spec_path) as f:
        return json.load(f)

def extract_endpoints(spec):
    endpoints = {}
    paths = spec.get('paths', {})
    for path, methods in paths.items():
        for method, details in methods.items():
            endpoints.setdefault(path, []).append(method.upper())
    return endpoints

def test_cors(base_url, path, method='GET'):
    test_origin = 'http://192.168.101.14:8000'
    headers = {'Origin': test_origin}
    try:
        r = requests.options(f"{base_url}{path}", headers=headers, timeout=5)
        if r.status_code == 200 and test_origin in r.headers.get('Access-Control-Allow-Origin', ''):
            return f"{method} {path}"
    except:
        pass
    return None

if __name__ == '__main__':
    spec = load_openapi('lukla-openapi.json')
    endpoints = extract_endpoints(spec)
    
    for path, methods in sorted(endpoints.items()):
        print(f"{path}") #: {', '.join(methods)}")
        
        # Test CORS on each
        vuln = test_cors('https://demobackend.lukla.ai', path)
        if vuln:
            print(f"  {vuln}")
    
    print(f"\nTotal endpoints: {len(endpoints)}")
