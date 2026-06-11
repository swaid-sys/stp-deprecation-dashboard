# Burndown Chart Update - June 11, 2026

## Summary
Updated the burndown chart to reflect 5 services moving from FY27 Q2 to FY27 Q3 due to TD Target Build changes (264 → 266).

## Changes Made

### 1. Historical Line (Actual/Confirmed Data)
**Added new data point:**
- **Jun 11, 2026**: 71 services remaining (current as of today)

### 2. Projected Line (Current Trajectory)
**Updated quarterly projections:**

| Quarter End | Old Count | New Count | Change | Notes |
|------------|-----------|-----------|--------|-------|
| **Jun 11** (anchor) | 71 | 71 | - | Current count |
| **Jul 31 (Q2)** | 43 | **48** | +5 | 5 services moved to Q3 |
| **Oct 31 (Q3)** | 36 | 36 | - | Absorbed 5 from Q2 |
| **Jan 31 (Q4)** | 19 | 19 | - | No change |
| **Apr 30 (FY28 Q1)** | 17 | 17 | - | No change |
| **Jul 31 (FY28 Q2)** | 2 | 2 | - | No change |
| **Oct 31 (FY28 Q3)** | 1 | 1 | - | No change |

**Updated breakdowns:**
- **Q2 end (Jul 31)**: Changed from "−28 services" to "−23 services (5 moved to Q3)"
- **Q3 end (Oct 31)**: Changed from "−7 services" to "−12 services (7 original + 5 from Q2)"

### 3. Original Plan Line (FROZEN - No Changes)
✅ Remains completely unchanged as required (static baseline from early FY27 Q2)

### 4. Quarter Drops (Tooltip Details)
**Services moved from Q2 to Q3:**
1. cloudmap-api
2. cloudmap-scanners
3. defender
4. kraken
5. vault-version-publisher

**Q2 (Jul 31) list:**
- Removed the 5 services above
- Updated from 28 remaining to 23 remaining
- Added comment noting the move

**Q3 (Oct 31) list:**
- Added the 5 services from Q2
- Updated from 7 to 12 total services
- Added comment explaining the source

## Impact on Chart

### Before:
```
Jul 31 (Q2): 71 → 43 (drop of 28)
Oct 31 (Q3): 43 → 36 (drop of 7)
```

### After:
```
Jul 31 (Q2): 71 → 48 (drop of 23)
Oct 31 (Q3): 48 → 36 (drop of 12)
```

**Net result:** Same final count (36 by end of Q3), but the pace is adjusted to reflect the TD timeline changes.

## Verification

The chart now accurately reflects:
- ✅ 5 services moved from Q2 to Q3
- ✅ Q2 end count increased from 43 to 48
- ✅ Q3 still ends at 36 (same target)
- ✅ All subsequent quarters remain unchanged
- ✅ Original Plan line remains frozen
- ✅ Tooltip details updated for both quarters

## Date Updated
June 11, 2026
