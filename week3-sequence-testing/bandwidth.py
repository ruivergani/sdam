# calculate the bandwidth exercise

# variables
max_bandwidth = 1000000000  # bps
concurrent_users = 200
app_a = 200000  # bps
app_b = 100000  # bps
app_c = 350000  # new application bps

# calculations
total_application = (app_b + app_a + app_c)

network_capacity = (1000000 * 1000)  # bps
current_usage = (app_a + app_b)  # application current sum all
current_availability = (network_capacity - current_usage)
applications_requirement = (total_application * concurrent_users)
available_bandwidth = ((network_capacity - applications_requirement) / 1000000)

# output

print("\nNetwork Capacity: {} bps" .format(network_capacity))
print("Current Usage: {} bps" .format(current_usage))
print("Current Availability: {} bps" .format(current_availability))
print("Applications Requirement: {} bps" .format(applications_requirement))
print("Available Bandwidth: {} Mbps" .format(available_bandwidth))

