# My Tools

## Requirements

- Python 3.12+
- uv

## Quick Start

```bash
uv sync
source .venv/bin/activate
python tools/FEATURES.py
```

## Features

1. IP Calculator

```bash
python tools/ip_caculator.py

# example outputs
Example 1 - 10.0.0.0/16 to /24:
Total subnets: 256
Hosts per subnet: 254
subnets: ['10.0.0.0/24', '10.0.1.0/24', '10.0.2.0/24'], etc.

Example 2 - 192.168.0.0/24 to /26:
Total subnets: 4
Hosts per subnet: 62
subnets: ['192.168.0.0/26', '192.168.0.64/26', '192.168.0.128/26', '192.168.0.192/26']
```
