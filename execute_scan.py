#!/usr/bin/env python3
"""
Execute the security scanner and display the results.
"""

from security_scanner import SecurityScanner

# Create scanner instance
scanner = SecurityScanner("/workspace")
print(f"Starting security scan of /workspace...")

# Scan the repository
issues = scanner.scan_directory()

# Generate reports
scanner.generate_report()
scanner.generate_html_report()

# Print summary
scanner.print_summary()

print("Security scan completed. Reports and logs have been generated.")