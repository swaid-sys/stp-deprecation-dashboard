#!/usr/bin/env python3
"""
Fetch TD statuses from GUS using Salesforce CLI
"""

import json
import subprocess

# Map of TD numbers to their Salesforce record IDs
td_map = {
    "TD-0259554": "a0nEE000000qCRhYAM",
    "TD-0297518": "a0nEE0000012fxlYAA",
    "TD-0297533": "a0nEE0000012gLxYAI",
    "TD-0309501": "a0nEE0000018Z85YAE",
    "TD-0324231": "a0nEE000001G7eTYAS",
    "TD-0326004": "a0nEE000001GstVYAS",
    "TD-0326005": "a0nEE000001GswjYAC",
    "TD-0326006": "a0nEE000001GsyLYAS",
    "TD-0326007": "a0nEE000001GszxYAC",
    "TD-0326008": "a0nEE000001Gt1ZYAS",
    "TD-0326009": "a0nEE000001Gt3BYAS",
    "TD-0326010": "a0nEE000001Gt4nYAC",
    "TD-0326011": "a0nEE000001Gt6PYAS",
    "TD-0326012": "a0nEE000001Gt81YAC",
    "TD-0326013": "a0nEE000001Gt9dYAC",
    "TD-0326014": "a0nEE000001GtBFYA0",
    "TD-0326015": "a0nEE000001GtCrYAK",
    "TD-0326016": "a0nEE000001GtETYA0",
    "TD-0326017": "a0nEE000001GtG5YAK",
    "TD-0326018": "a0nEE000001GtHhYAK",
    "TD-0326019": "a0nEE000001GtBGYA0",
    "TD-0326020": "a0nEE000001GtJJYA0",
    "TD-0326021": "a0nEE000001GtKvYAK",
    "TD-0326022": "a0nEE000001GtMXYA0",
    "TD-0326023": "a0nEE000001GtO9YAK",
    "TD-0326024": "a0nEE000001GtPlYAK",
    "TD-0326025": "a0nEE000001GtRNYA0",
    "TD-0326026": "a0nEE000001GtSzYAK",
    "TD-0326027": "a0nEE000001GtUbYAK",
    "TD-0326028": "a0nEE000001GtWDYA0",
    "TD-0326029": "a0nEE000001GtXpYAK",
    "TD-0326030": "a0nEE000001GtZRYA0",
    "TD-0326031": "a0nEE000001Gtb3YAC",
    "TD-0326032": "a0nEE000001GtcfYAC",
    "TD-0326033": "a0nEE000001GteHYAS",
    "TD-0326034": "a0nEE000001GtftYAC",
    "TD-0326035": "a0nEE000001GthVYAS",
    "TD-0326036": "a0nEE000001Gtj7YAC",
    "TD-0326037": "a0nEE000001GtkjYAC",
    "TD-0326038": "a0nEE000001GtmLYAS",
    "TD-0326039": "a0nEE000001GtUcYAK",
    "TD-0326040": "a0nEE000001GteIYAS",
    "TD-0326041": "a0nEE000001GtnxYAC",
    "TD-0326044": "a0nEE000001GtsnYAC",
    "TD-0326045": "a0nEE000001GtuPYAS",
    "TD-0326046": "a0nEE000001Gtw1YAC",
    "TD-0326047": "a0nEE000001GtxdYAC",
    "TD-0326048": "a0nEE000001GtzFYAS",
    "TD-0326049": "a0nEE000001Gu0rYAC",
    "TD-0326050": "a0nEE000001Gu2TYAS",
    "TD-0326051": "a0nEE000001Gu45YAC",
    "TD-0326052": "a0nEE000001Gu5hYAC",
    "TD-0326053": "a0nEE000001Gu7JYAS",
    "TD-0326054": "a0nEE000001Gu8vYAC",
    "TD-0326055": "a0nEE000001GuAXYA0",
    "TD-0326056": "a0nEE000001GuC9YAK",
    "TD-0326057": "a0nEE000001GuDlYAK",
    "TD-0326058": "a0nEE000001GuFNYA0",
    "TD-0326059": "a0nEE000001GuGzYAK",
    "TD-0326060": "a0nEE000001GuIbYAK",
    "TD-0326064": "a0nEE000001GuP3YAK",
    "TD-0326065": "a0nEE000001GuQfYAK",
    "TD-0326066": "a0nEE000001GuSHYA0",
    "TD-0326067": "a0nEE000001GuTtYAK",
    "TD-0326068": "a0nEE000001GuVVYA0",
    "TD-0326069": "a0nEE000001GuX7YAK",
    "TD-0326070": "a0nEE000001GuYjYAK",
    "TD-0326071": "a0nEE000001GuaLYAS",
    "TD-0326072": "a0nEE000001GubxYAC",
    "TD-0326073": "a0nEE000001GudZYAS",
    "TD-0326074": "a0nEE000001GufBYAS",
    "TD-0326075": "a0nEE000001GugnYAC",
    "TD-0326076": "a0nEE000001GuiPYAS",
    "TD-0326077": "a0nEE000001Guk1YAC",
    "TD-0326078": "a0nEE000001GuldYAC",
}

def fetch_td_status(td_num, record_id):
    """Fetch dependency status for a single TD"""
    try:
        cmd = [
            "sf", "data", "get", "record",
            "--sobject", "ADM_Team_Dependency__c",
            "--record-id", record_id,
            "--target-org", "gus",
            "--json"
        ]

        result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)

        if result.returncode == 0:
            data = json.loads(result.stdout)
            status = data.get("result", {}).get("Dependency_Status__c", "Unknown")
            return status
        else:
            print(f"Error fetching {td_num}: {result.stderr}", file=__import__('sys').stderr)
            return "Unknown"
    except Exception as e:
        print(f"Exception fetching {td_num}: {e}", file=__import__('sys').stderr)
        return "Unknown"

def main():
    """Fetch all TD statuses and output as JSON"""
    statuses = {}

    total = len(td_map)
    for i, (td_num, record_id) in enumerate(td_map.items(), 1):
        print(f"Fetching {td_num} ({i}/{total})...", file=__import__('sys').stderr)
        status = fetch_td_status(td_num, record_id)
        statuses[td_num] = status

    # Output the JSON
    print(json.dumps(statuses, indent=2))

if __name__ == "__main__":
    main()
