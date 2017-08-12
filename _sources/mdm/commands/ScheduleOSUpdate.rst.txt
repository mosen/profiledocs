ScheduleOSUpdate
================

- Requires you to run `ScheduleOSUpdateScan` (which will execute softwareupdate on macOS).
- `ScheduleOSUpdateScan` does not report products found.
- send `AvailableOSUpdates` to find available products.
- You won't know when `ScheduleOSUpdateScan` has finished.

- Doing a `ScheduleOSUpdate` wont tell you the status of the update, you need to send `OSUpdateStatus`, continuously.
- `OSUpdateStatus` might say installing when it isnt.
- if you send `OSUpdateStatus` after the install finishes you get nothing.
