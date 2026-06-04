# STP Service Deprecation Dashboard - Updates & Maintenance

## 🎯 Recent Updates (June 4, 2026)

### 1. ✅ Added "TD Status" Column
- **Location**: In tables beneath "Expand All Sections" button
- **Position**: Between "GUS References" and "Comments" columns
- **Functionality**: Shows the Dependency Status from GUS for each TD reference
- **Status Colors**:
  - 🟡 **New** (Yellow) - Not yet started
  - 🔵 **Committed / Prioritized** (Blue) - Active work
  - 🟣 **Under Review** (Purple) - Being reviewed
  - 🔴 **Blocked** (Red) - Issues preventing progress
  - ✅ **Completed** (Green) - Done

### 2. 📊 Enhanced Burndown Chart
- **Added "Original Plan" Line**: Green dotted line showing the FY27 Q2 baseline plan
- **Three Lines Now**:
  - 🔵 **Actual** (solid blue) - Current reality
  - 🟢 **Original Plan** (dotted green) - FY27 Q2 baseline expectations
  - 🟣 **Projected** (dotted purple) - Current trajectory
- **Purpose**: Makes delays visible by comparing actual progress vs. original plan

## 📂 File Structure

```
/Users/swaid/Downloads/FKP-Adoption-Dashboard/
├── path_to_deprecation_dashboard.html  # Main dashboard file
├── fetch-td-statuses.py                # Script to refresh TD statuses
├── td-statuses.json                    # Current TD status data
└── README.md                           # This file
```

## 🔄 How to Update TD Statuses

When TD statuses change in GUS, refresh them:

```bash
cd "/Users/swaid/Downloads/FKP-Adoption-Dashboard"
python3 fetch-td-statuses.py > td-statuses.json
```

Then manually update the `tdStatuses` object in `path_to_deprecation_dashboard.html` (around line 555) with the new data from `td-statuses.json`.

## 📈 How to Update Burndown Chart Data

### Update Actual Data Points
Find the `historical` array in the chart section (around line 1280) and add new data points:

```javascript
const historical = [
    { label: 'May 26',  date: '2026-05-26', count: 74 },
    { label: 'Jun 1',   date: '2026-06-01', count: 71 },
    // Add new points here with same format
];
```

### Update Original Plan (if baseline changes)
Find the `originalPlan` array (around line 1210) - these are the hardcoded FY27 Q2 targets.

### Update Projected (for new forecasts)
Find the `projected` array (around line 1290) and update the quarter-end projections.

## 🚀 Features

- **Two Views**: Commercial and Gia2h tabs
- **Organized by STP Leader**: Collapsible sections for each leader
- **TD Status Column**: Real dependency status from GUS
- **Burndown Chart**: Visual comparison of actual vs. plan vs. projected
- **Editable GUS References**: Click "Edit" to add or modify TD/WI references
- **Search & Filter**: Search by service name/comments, filter by GUS presence
- **Auto-Save**: Your GUS reference edits are saved in browser localStorage
- **Clickable GUS Links**: Click badges to open in GUS or copy reference

## 🔧 Technical Details

- **GUS API**: Uses Salesforce CLI (`sf`) to fetch TD statuses
- **Authentication**: Requires `sf org list` to show connected GUS org (alias: `gus`)
- **TD Status Field**: Reads `Dependency_Status__c` from `ADM_Team_Dependency__c` records
- **Embedded Data**: All TD statuses are embedded in HTML to avoid CORS issues

## 📊 Data Source

Google Sheet: https://docs.google.com/spreadsheets/d/1OAQ8L-XR0zaUwZb_fWFIy_lrykc-Y14lFweSMhLuwoQ/edit?gid=921844013

**Tabs Used:**
- FKP & Mesh Onboarding - Commercial
- FKP & Mesh Onboarding - Gia2h

**Filter:** Services with "Path to Deprecation" status

## 🔗 Quick Reference Links

- **Dashboard URL**: https://swaid-sys.github.io/stp-deprecation-dashboard/
- **GUS**: https://gus.lightning.force.com

## 💡 Tips for Finding Code

- Search for `"TD Status"` to find the TD Status column code
- Search for `buildChart()` to find the burndown chart code
- Search for `tdStatuses` to find the embedded TD status data
- Search for `historical` to find actual data points
- Search for `originalPlan` to find baseline targets

## 🆘 Questions or Issues?

Reference this README or search for keywords in the HTML file to find relevant code sections.

---
*Last updated: June 4, 2026*
