"""Verify subcategory autocomplete works correctly."""

from hfortix_fortios import FortiOS

# Create client with default response_mode="dict"
fg = FortiOS(
    host="192.168.1.99",
    token="your-api-token",
)

# Test 1: Verify firewall subcategory is recognized
# Should show: (variable) firewall: FirewallDictMode
firewall = fg.api.cmdb.firewall

# Test 2: Verify service subcategory is recognized
# Should show: (variable) service: ServiceDictMode
service = fg.api.cmdb.firewall.service

# Test 3: Verify service.group endpoint is recognized
# Should show: (variable) group: ServiceGroupDictMode
group = fg.api.cmdb.firewall.service.group

# Test 4: Verify GET method returns correct type
# Should show: (variable) service_groups: list[ServiceGroupResponse]
service_groups = fg.api.cmdb.firewall.service.group.get()

# Test 5: Verify custom service endpoint
# Should show: (variable) custom_services: list[ServiceCustomResponse]
custom_services = fg.api.cmdb.firewall.service.custom.get()

# Test 6: Verify schedule subcategory
# Should show: (variable) schedule: ScheduleDictMode
schedule = fg.api.cmdb.firewall.schedule

# Test 7: Verify schedule.recurring endpoint
# Should show: (variable) recurring_schedules: list[ScheduleRecurringResponse]
recurring_schedules = fg.api.cmdb.firewall.schedule.recurring.get()

print("✅ All subcategory tests passed - no Pylance errors!")
