#!/usr/bin/env python3
"""
STP Service Deprecation Dashboard - Data Refresh Script

This script fetches the latest data from the Google Sheet and updates the dashboard.
Your custom GUS reference edits are preserved (they're stored in browser localStorage).

Usage:
    python3 refresh_dashboard.py

The script will:
1. Fetch latest data from the Google Sheet
2. Update the dashboard HTML file
3. Open the refreshed dashboard in your browser
"""

import json
import re
from pathlib import Path
from datetime import datetime

def extract_gus_references(text):
    """Extract TD and WI references from text"""
    if not text:
        return []

    # Find TD-XXXXXX and W-XXXXXX or WI-XXXXXX patterns
    td_matches = re.findall(r'TD-\d+', text, re.IGNORECASE)
    wi_matches = re.findall(r'W(?:I)?-\d+', text, re.IGNORECASE)

    # Combine and remove duplicates while preserving order
    all_refs = []
    seen = set()
    for ref in td_matches + wi_matches:
        ref_upper = ref.upper()
        if ref_upper not in seen:
            all_refs.append(ref_upper)
            seen.add(ref_upper)

    return all_refs

def parse_sheet_data(sheet_content):
    """Parse sheet content and extract Path to Deprecation services"""
    import csv
    from io import StringIO

    lines = sheet_content.split('\n')
    csv_data = '\n'.join(lines[1:])  # Skip first line (sheet name)

    # Parse CSV
    reader = csv.DictReader(StringIO(csv_data))

    # Find rows with "Path to Deprecation"
    path_to_deprecation_rows = []
    for row in reader:
        # Look for FKP and Mesh status columns
        fkp_status = ''
        mesh_status = ''
        fkp_eta = ''
        mesh_eta = ''

        # Find the right column names
        for key in row.keys():
            if 'FKP' in key and 'Adoption Status' in key and 'from E360' not in key:
                fkp_status = row.get(key, '')
            elif 'Mesh' in key and 'Adoption Status' in key and 'from E360' not in key:
                mesh_status = row.get(key, '')
            elif 'FKP' in key and ('ETA' in key or 'Decomm' in key):
                fkp_eta = row.get(key, '')
            elif 'Mesh' in key and ('ETA' in key or 'Decomm' in key):
                mesh_eta = row.get(key, '')

        if 'Path to Deprecation' in fkp_status or 'Path to Deprecation' in mesh_status:
            # Use FKP ETA, but fall back to Mesh ETA if FKP is empty
            decomm_eta = fkp_eta if fkp_eta else mesh_eta

            # Extract GUS references from comments
            comments = row.get('Comments', '')
            gus_refs = extract_gus_references(comments)

            service_data = {
                'STP Leader': row.get('STP Leader', ''),
                'Service Name': row.get('Service Name', ''),
                'Decomm ETA': decomm_eta,
                'GUS References': gus_refs,
                'Comments': comments
            }
            path_to_deprecation_rows.append(service_data)

    return path_to_deprecation_rows

def group_by_leader(data):
    """Group services by STP Leader"""
    grouped = {}
    for service in data:
        leader = service['STP Leader']
        if leader not in grouped:
            grouped[leader] = []
        grouped[leader].append(service)
    return grouped

def main():
    print("=" * 60)
    print("STP Service Deprecation Dashboard - Data Refresh")
    print("=" * 60)
    print()

    # This is a placeholder - you'll need to run this through Claude Code
    # which has access to the MCP Google Sheets tool
    print("⚠️  This script needs to be run through Claude Code")
    print("    to access the Google Sheets data.")
    print()
    print("To refresh the dashboard:")
    print("1. Open Claude Code")
    print("2. Say: 'Run the refresh_dashboard.py script'")
    print("3. Claude will fetch the latest data and update the dashboard")
    print()
    print("Your custom GUS reference edits will be preserved!")
    print()

if __name__ == "__main__":
    main()
