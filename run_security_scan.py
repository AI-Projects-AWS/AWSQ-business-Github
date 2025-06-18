#!/usr/bin/env python3
"""
Script to run the security scanner on the repository.
"""

import os
import sys
from security_scanner import SecurityScanner

def main():
    """Run the security scanner on the repository."""
    print("Starting security scan...")
    
    # Create scanner instance
    scanner = SecurityScanner("/workspace")
    
    # Scan the repository
    scanner.scan_directory()
    
    # Generate reports
    scanner.generate_report()
    scanner.generate_html_report()
    
    # Print summary
    scanner.print_summary()
    
    # List generated files
    print("\nGenerated files:")
    for file_name in ["security_report.json", "security_report.html", "security_scan.log"]:
        if os.path.exists(file_name):
            print(f"- {file_name} ({os.path.getsize(file_name)} bytes)")
    
    return 0

if __name__ == "__main__":
    sys.exit(main())