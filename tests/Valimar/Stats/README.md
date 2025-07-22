# Stats Spotlight SID Test

## Overview

This test suite contains tests for the Stats Spotlight SID functionality, particularly focusing on the "no segment-routing" configuration command.

## Test File: TEST_Stats_Spotlight_Sid.py

### Purpose

The test verifies the behavior of spotlight SID statistics when segment-routing is disabled using the `no segment-routing` command.

### Test Functionality

The main test `test_spotlight_sid_with_no_segment_routing` performs the following operations:

1. **Re-enables spotlight on SIDs**: 
   - Sets up sensor creation expectations for algo0 labels, flex labels, and FA local sensors
   - Sends the configuration command to enable spotlight: `segment-routing sid-stats-range "16000" "19999" stats-spotlight-state on`

2. **Tests "no segment-routing" command**:
   - Sets up sensor deletion expectations for all previously created sensors
   - Sends the `no segment-routing` command
   - Verifies that all sensors are properly deleted

3. **Validates sensor counts**:
   - Ensures the correct number of sensors are created during enable
   - Ensures the correct number of sensors are deleted during disable
   - Performs sanity checks on the system state

### Test Data

- `algo0_labels`: ["16000", "16001", "16002"] - Algorithm 0 labels for testing
- `flex_labels`: ["17000", "17001"] - Flexible labels for testing  
- FA local sensors: 3 additional sensors (no labels allocated but stats enabled)

### Expected Behavior

- **Creates**: 8 sensors total (3 algo0 + 2 flex + 3 FA local)
- **Deletes**: 8 sensors total (same count as created)
- **Result**: System should be in a clean state after "no segment-routing" command

## Running the Tests

### Option 1: Direct execution
```bash
cd tests/Valimar/Stats
python3 TEST_Stats_Spotlight_Sid.py
```

### Option 2: Using the test runner
```bash
cd tests/Valimar/Stats  
python3 run_tests.py
```

## Test Status

✅ **COMPLETED**: The "no segment-routing" test step has been implemented and is passing.

The test was previously marked as TODO but has now been completed with:
- Proper sensor creation/deletion expectations
- Validation of sensor counts  
- System sanity checks
- Removal of debugging breakpoints (`pdb.set_trace()` calls)

## Notes

- The adjacency SID configuration is currently commented out in the original code
- The test uses mocks to simulate the UUT (Unit Under Test) behavior
- Real hardware testing should be performed to validate the implementation matches expected behavior