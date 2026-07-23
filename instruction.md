There is an access log at /app/access.log in Apache combined log format. Parse it
and write a summary report as JSON to /app/report.json with exactly these keys:

1. "total_requests": the total number of log lines in the file.
2. "unique_ips": the count of distinct client IP addresses (first field of each line).
3. "top_path": the request path (e.g. "/index.html") that appears most often across
   all requests. If there is a tie, any of the tied paths is acceptable.

Do not modify /app/access.log.

You have 120 seconds to complete this task. Do not cheat by using online solutions or hints specific to this task.
