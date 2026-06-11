# Complete Dashboard Update Summary - June 11, 2026

## Overview
Updated the STP Service Deprecation Dashboard to reflect TD Target Build changes from 264 to 266 for 5 services, affecting both service ETAs and the burndown chart projections.

## Part 1: Service Decomm ETA Updates

### Services Updated (FY27 Q2 → FY27 Q3)

| Service | TD Number | Leader | TD Change Date |
|---------|-----------|--------|----------------|
| vault-version-publisher | TD-0326015 | Fiaz Hossain | June 11, 2026 |
| cloudmap-api | TD-0326018 | Ajith Jayamohan | June 9, 2026 |
| cloudmap-scanners | TD-0326019 | Ajith Jayamohan | June 9, 2026 |
| defender | TD-0326025 | Ajith Jayamohan | June 10, 2026 |
| kraken | TD-0326027 | Ajith Jayamohan | June 9, 2026 |

**Changes Made:**
- Updated `"Decomm ETA"` field from `"FY27 Q2"` to `"FY27 Q3"` for each service
- Added timestamped comment noting the TD Target Build update
- Preserved all existing historical comments

## Part 2: Burndown Chart Updates

### Historical Line (Blue Solid - Actual/Confirmed Data)
**Added:**
- June 11, 2026: 71 services (current count)

### Projected Line (Purple Dashed - Current Trajectory)
**Updated quarterly projections:**

| Quarter End | Old Projection | New Projection | Change | Explanation |
|------------|----------------|----------------|--------|-------------|
| Jun 11, 2026 (anchor) | 71 | 71 | - | Current baseline |
| Jul 31, 2026 (Q2) | 43 | **48** | +5 | 5 services moved to Q3 |
| Oct 31, 2026 (Q3) | 36 | 36 | - | Absorbed 5 from Q2 |
| Jan 31, 2027 (Q4) | 19 | 19 | - | No change |
| Apr 30, 2027 (FY28 Q1) | 17 | 17 | - | No change |
| Jul 31, 2027 (FY28 Q2) | 2 | 2 | - | No change |
| Oct 31, 2027 (FY28 Q3) | 1 | 1 | - | No change |

**Updated breakdown text:**
- Q2: "−23 services (5 moved to Q3)" (was "−28 services")
- Q3: "−12 services (7 original + 5 from Q2)" (was "−7 services")

### Original Plan Line (Green Dashed - Frozen Baseline)
✅ **NO CHANGES** - Remains completely unchanged as required
- This is the static baseline from early FY27 Q2
- Protected by warning comments to prevent future modifications

### Tooltip Details (quarterDrops)
**Q2 (Jul 31, 2026) services:**
- **Removed:** cloudmap-api, cloudmap-scanners, defender, kraken, vault-version-publisher
- **Count:** 23 remaining (down from 28)
- **Added comment:** Noting the 5 services moved to Q3

**Q3 (Oct 31, 2026) services:**
- **Added:** cloudmap-api, cloudmap-scanners, defender, kraken, vault-version-publisher
- **Count:** 12 total (up from 7)
- **Added comment:** Explaining the source of the additional 5 services

## Part 3: Documentation Improvements

### Original Plan Baseline Protection
Added comprehensive warning banners around the `originalPlan` array:
- ⚠️ "STATIC BASELINE - DO NOT MODIFY" headers
- Clear explanation that it must remain frozen
- Visual separation from updateable `projected` array
- Instructions on where to make future updates

### Chart Architecture Documentation
Added header documentation explaining the three-line structure:
- **ACTUAL** (blue solid): Historical confirmed data - update as confirmed
- **ORIGINAL PLAN** (green dashed): FROZEN baseline from early FY27 Q2 - never update
- **PROJECTED** (purple dashed): Current trajectory - update as timelines change

## Visual Impact on Chart

```
Before (incorrect):
┌─────────────────────────────────────┐
│ Jun 11: 71 services                 │
│   ↓ (drop 28 by Q2)                 │
│ Jul 31: 43 services                 │
│   ↓ (drop 7 by Q3)                  │
│ Oct 31: 36 services                 │
└─────────────────────────────────────┘

After (correct):
┌─────────────────────────────────────┐
│ Jun 11: 71 services                 │
│   ↓ (drop 23 by Q2) ← 5 moved out  │
│ Jul 31: 48 services                 │
│   ↓ (drop 12 by Q3) ← 5 moved in   │
│ Oct 31: 36 services                 │
└─────────────────────────────────────┘
```

**Key insight:** The Q3 endpoint stays the same (36 services), but the Q2 pace slows down to reflect the TD timeline changes.

## Files Modified
- `path_to_deprecation_dashboard.html` - Main dashboard file
  - Updated 5 service Decomm ETAs
  - Updated historical data point (Jun 11)
  - Updated projected quarterly counts
  - Updated quarterDrops tooltip data
  - Added comprehensive documentation

## Files Created
- `.agents/original-plan-baseline-documentation.md` - Baseline protection docs
- `.agents/td-target-build-updates.md` - Service ETA update details
- `.agents/burndown-chart-update.md` - Chart update details
- `.agents/complete-update-summary.md` - This file

## GUS Query Reference

```sql
SELECT Name, Target_Build__c, LastModifiedDate, 
  (SELECT Field, OldValue, NewValue, CreatedDate 
   FROM Histories 
   WHERE Field = 'Target_Build__c' 
   AND CreatedDate = LAST_N_DAYS:7
   ORDER BY CreatedDate DESC)
FROM ADM_Team_Dependency__c
WHERE Name IN ('TD-0259554', 'TD-0297518', ...)
```

**Results:** Found 5 TDs with Target Build changes from 264→266 in the last 7 days

## Target Build to Decomm ETA Mapping
- 264 → FY27 Q2
- 266 → FY27 Q3
- 268 → FY28 Q1
- 270 → FY28 Q2
- 272 → FY28 Q3

## Next Steps
1. Review the changes in the dashboard
2. Test the dashboard in a browser to verify chart rendering
3. Commit changes to git if satisfied
4. Deploy updated dashboard to GitHub Pages

## Date Updated
June 11, 2026

## Validation Checklist
- ✅ 5 services have updated ETAs (Q2 → Q3)
- ✅ All 5 services have timestamped comments
- ✅ Historical line includes Jun 11 data point
- ✅ Projected Q2 count changed from 43 to 48
- ✅ Projected Q3 count remains 36
- ✅ Original Plan line unchanged (frozen baseline)
- ✅ Q2 quarterDrops list updated (5 services removed)
- ✅ Q3 quarterDrops list updated (5 services added)
- ✅ Breakdown text updated for Q2 and Q3
- ✅ Documentation added for baseline protection
- ✅ All changes documented
