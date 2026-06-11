# TD Target Build Updates - Decomm ETA Changes

## Summary
Updated Decomm ETAs for 5 services whose TDs had Target Build changes from 264 to 266 in the past week (June 9-11, 2026).

## Target Build to Decomm ETA Mapping
- 264 → FY27 Q2
- 266 → FY27 Q3
- 268 → FY28 Q1
- 270 → FY28 Q2
- 272 → FY28 Q3

## Services Updated

### 1. vault-version-publisher
- **STP Leader:** Fiaz Hossain
- **TD:** TD-0326015
- **Change Date:** June 11, 2026
- **Old ETA:** FY27 Q2
- **New ETA:** FY27 Q3
- **Reason:** Target Build changed from 264 to 266

### 2. cloudmap-api
- **STP Leader:** Ajith Jayamohan
- **TD:** TD-0326018
- **Change Date:** June 9, 2026
- **Old ETA:** FY27 Q2
- **New ETA:** FY27 Q3
- **Reason:** Target Build changed from 264 to 266

### 3. cloudmap-scanners
- **STP Leader:** Ajith Jayamohan
- **TD:** TD-0326019
- **Change Date:** June 9, 2026
- **Old ETA:** FY27 Q2
- **New ETA:** FY27 Q3
- **Reason:** Target Build changed from 264 to 266

### 4. defender
- **STP Leader:** Ajith Jayamohan
- **TD:** TD-0326025
- **Change Date:** June 10, 2026
- **Old ETA:** FY27 Q2
- **New ETA:** FY27 Q3
- **Reason:** Target Build changed from 264 to 266

### 5. kraken
- **STP Leader:** Ajith Jayamohan
- **TD:** TD-0326027
- **Change Date:** June 9, 2026
- **Old ETA:** FY27 Q2
- **New ETA:** FY27 Q3
- **Reason:** Target Build changed from 264 to 266

## GUS Query Used
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

## Changes Made to Dashboard
For each service:
1. Updated `"Decomm ETA"` field from `"FY27 Q2"` to `"FY27 Q3"`
2. Added comment noting the TD Target Build update date and change

## Date Updated
June 11, 2026
