# STP Deprecation Dashboard - Original Plan Baseline Implementation

## Summary
Updated the dashboard code to ensure the "Original Plan" dotted line on the burn-down chart remains a **static baseline** that will never change, even when deprecation projections or service counts are updated.

## What Was Changed

### 1. Enhanced Documentation for `originalPlan` Array
**Location:** Lines 1895-1927 in `path_to_deprecation_dashboard.html`

Added prominent warning comments with a visual banner:
```javascript
// ═══════════════════════════════════════════════════════════════════
// ⚠️  STATIC BASELINE - DO NOT MODIFY ⚠️
// ═══════════════════════════════════════════════════════════════════
// This "Original Plan" represents the baseline snapshot from early FY27 Q2
// (May 26, 2026) and must remain FROZEN to serve as a historical reference.
//
// Even if deprecation projections change or the total number of services
// changes, this array should NEVER be updated...
```

**Purpose:** Makes it crystal clear to any future developer that this data is intentionally frozen.

### 2. Clarified the `projected` Array
**Location:** Lines 1929-1935

Added clear instructions that the `projected` array is where updates should go:
```javascript
// ── Current Projected Plan (UPDATE THIS, NOT originalPlan) ──────────
// This represents the CURRENT projection based on recent progress.
// Update these values as deprecation timelines change or services are added/removed.
// The "Original Plan" above should remain frozen for comparison purposes.
```

**Purpose:** Directs developers to update the correct location when projections change.

### 3. Added Chart Architecture Documentation
**Location:** Lines 1884-1906

Added comprehensive header documentation explaining the three-line architecture:
- **ACTUAL** (solid blue) - Historical confirmed data
- **ORIGINAL PLAN** (dashed green) - FROZEN BASELINE from early FY27 Q2
- **PROJECTED** (dashed purple) - Current trajectory

**Purpose:** Provides high-level understanding of the chart's design before diving into code.

## How It Works

The chart displays three independent data series:

1. **`originalPlan`** array → transforms into `planValues` → renders as "Original Plan" (green dashed line)
   - This is completely hardcoded and isolated
   - Never recalculated from live data

2. **`projected`** array → transforms into `projValues` → renders as "Projected" (purple dashed line)
   - This should be updated when timelines change
   - Reflects current best estimates

3. **`historical`** array → transforms into `histValues` → renders as "Actual" (blue solid line)
   - Updated as actual deprecations are confirmed
   - Shows real progress over time

## Verification

The implementation is safe because:
✅ `originalPlan` is a const array with hardcoded values  
✅ No dynamic calculations reference or modify it  
✅ Chart.js receives it as `planValues` (a separate transformed array)  
✅ Clear warnings prevent accidental modification  
✅ The three datasets are completely independent in the chart configuration

## Future Maintenance

### To update current projections (when deprecation ETAs change):
1. Find the `projected` array (around line 1936)
2. Update the count values and dates as needed
3. Leave `originalPlan` untouched

### To add new confirmed data points:
1. Find the `historical` array (around line 1929)
2. Add new entries with actual dates and counts
3. Leave `originalPlan` untouched

### To never do:
❌ Modify the `originalPlan` array  
❌ Calculate `originalPlan` values dynamically  
❌ Reference service count variables in `originalPlan`

## Files Modified
- `/Users/swaid/Downloads/FKP-Adoption-Dashboard/path_to_deprecation_dashboard.html`

## Date Updated
June 11, 2026
