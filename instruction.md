There's an access log at /app/access.log, in Apache combined log format. Go through
it and write a summary as JSON to /app/report.json. The report needs exactly these
three keys:

1. "total_requests" — how many lines are in the log file, total.
2. "unique_ips" — how many distinct client IPs show up (that's the first field on
   each line).
3. "top_path" — whichever request path got hit the most across all the requests,
   e.g. "/index.html". If two paths are tied for the top spot, either one is fine.

Leave /app/access.log itself untouched.

You have 120 seconds to complete this task. Do not cheat by using online solutions or hints specific to this task.
