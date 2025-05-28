#!/usr/bin/env python3
"""
Security Scanner for Code Repositories

This module scans Python and Java files for potential security issues and generates
detailed logs of the findings.
"""

import os
import re
import sys
import json
import logging
from datetime import datetime
from typing import Dict, List, Any, Tuple, Set

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("security_scan.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger("SecurityScanner")

class SecurityScanner:
    """
    A class to scan code files for potential security issues.
    """
    
    def __init__(self, repo_path: str = "."):
        """
        Initialize the scanner with the repository path.
        
        Args:
            repo_path: Path to the repository to scan
        """
        self.repo_path = repo_path
        self.issues_found = []
        self.files_scanned = 0
        self.scan_timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Define patterns to look for in Python code
        self.python_patterns = {
            "eval_exec": (r"\b(eval|exec)\s*\(", "Use of eval() or exec() can execute arbitrary code"),
            "os_system": (r"\bos\.(system|popen|spawn|exec[lv][ep]?)\s*\(", "Use of os.system() or similar can execute arbitrary commands"),
            "pickle_load": (r"\bpickle\.(loads?|Unpickler)", "Unpickling data from untrusted sources can lead to code execution"),
            "yaml_load": (r"\byaml\.load\s*\(", "Use yaml.safe_load() instead of yaml.load()"),
            "temp_file_insecure": (r"\btempfile\.(mktemp|TemporaryFile|NamedTemporaryFile)\s*\(", "Insecure temporary file creation"),
            "sql_injection": (r"cursor\.execute\s*\([^,]*%[^,]*\)|cursor\.execute\s*\([^,]*\+[^,]*\)", "Potential SQL injection vulnerability"),
            "hardcoded_password": (r"\b(password|passwd|pwd|secret|key|token)\s*=\s*['\"][^'\"]+['\"]", "Hardcoded credentials"),
            "insecure_hash": (r"\b(md5|sha1)\s*\(", "Use of weak hash functions"),
            "debug_enabled": (r"\bdebug\s*=\s*True", "Debug mode enabled"),
            "assert_usage": (r"\bassert\s+", "Assert statements can be removed in optimized mode"),
        }
        
        # Define patterns to look for in Java code
        self.java_patterns = {
            "system_exit": (r"\bSystem\.exit\s*\(", "System.exit() can be abused to terminate the application"),
            "runtime_exec": (r"\bRuntime\.getRuntime\(\)\.exec\s*\(", "Runtime.exec() can execute arbitrary commands"),
            "hardcoded_password": (r"\b(password|passwd|pwd|secret|key|token)\s*=\s*\"[^\"]+\"", "Hardcoded credentials"),
            "printStackTrace": (r"\.printStackTrace\s*\(\s*\)", "Exposing stack traces can reveal sensitive information"),
            "insecure_random": (r"\bnew\s+Random\s*\(", "Use SecureRandom for cryptographic operations"),
            "sql_injection_java": (r"\.executeQuery\s*\([^,]*\+[^,]*\)", "Potential SQL injection vulnerability"),
            "xxe_vulnerability": (r"\bDocumentBuilderFactory\b|\bSAXParserFactory\b", "Potential XXE vulnerability if not configured properly"),
            "weak_ssl": (r"\"SSL\"|\bSSLv3\b|\bTLSv1\b", "Use of weak SSL/TLS protocols"),
            "insecure_cookie": (r"\.setSecure\s*\(\s*false\s*\)", "Insecure cookie settings"),
            "log_injection": (r"\.log\s*\([^,]*\+[^,]*\)", "Potential log injection vulnerability"),
        }
    
    def scan_file(self, file_path: str) -> List[Dict[str, Any]]:
        """
        Scan a single file for security issues.
        
        Args:
            file_path: Path to the file to scan
            
        Returns:
            List of issues found in the file
        """
        issues = []
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                
            file_ext = os.path.splitext(file_path)[1].lower()
            
            # Select patterns based on file extension
            if file_ext == '.py':
                patterns = self.python_patterns
            elif file_ext in ('.java', '.jsp', '.jspx'):
                patterns = self.java_patterns
            else:
                logger.info(f"Skipping unsupported file type: {file_path}")
                return []
                
            # Scan for patterns
            for line_num, line in enumerate(content.split('\n'), 1):
                for pattern_name, (pattern, description) in patterns.items():
                    matches = re.findall(pattern, line)
                    if matches:
                        issues.append({
                            'file': file_path,
                            'line': line_num,
                            'pattern': pattern_name,
                            'description': description,
                            'code': line.strip(),
                            'severity': self._determine_severity(pattern_name)
                        })
            
            self.files_scanned += 1
            
        except Exception as e:
            logger.error(f"Error scanning file {file_path}: {str(e)}")
            
        return issues
    
    def _determine_severity(self, pattern_name: str) -> str:
        """
        Determine the severity level of an issue based on the pattern name.
        
        Args:
            pattern_name: Name of the pattern that was matched
            
        Returns:
            Severity level: 'HIGH', 'MEDIUM', or 'LOW'
        """
        high_severity = {'eval_exec', 'os_system', 'pickle_load', 'sql_injection', 
                        'hardcoded_password', 'runtime_exec', 'sql_injection_java'}
        medium_severity = {'yaml_load', 'insecure_hash', 'system_exit', 'xxe_vulnerability', 
                          'weak_ssl', 'insecure_cookie', 'log_injection', 'insecure_random'}
        
        if pattern_name in high_severity:
            return 'HIGH'
        elif pattern_name in medium_severity:
            return 'MEDIUM'
        else:
            return 'LOW'
            
    def scan_directory(self, directory: str = None) -> List[Dict[str, Any]]:
        """
        Recursively scan a directory for security issues.
        
        Args:
            directory: Directory to scan. If None, uses the repo_path.
            
        Returns:
            List of issues found in all files
        """
        if directory is None:
            directory = self.repo_path
            
        all_issues = []
        
        try:
            for root, _, files in os.walk(directory):
                for file in files:
                    file_path = os.path.join(root, file)
                    file_ext = os.path.splitext(file)[1].lower()
                    
                    # Only scan Python and Java files
                    if file_ext in ['.py', '.java', '.jsp', '.jspx']:
                        logger.info(f"Scanning file: {file_path}")
                        issues = self.scan_file(file_path)
                        if issues:
                            all_issues.extend(issues)
                            logger.warning(f"Found {len(issues)} issues in {file_path}")
        
        except Exception as e:
            logger.error(f"Error scanning directory {directory}: {str(e)}")
            
        self.issues_found = all_issues
        return all_issues
    
    def generate_report(self, output_file: str = "security_report.json") -> None:
        """
        Generate a JSON report of the security scan results.
        
        Args:
            output_file: Path to the output JSON file
        """
        report = {
            "scan_timestamp": self.scan_timestamp,
            "files_scanned": self.files_scanned,
            "total_issues": len(self.issues_found),
            "issues_by_severity": {
                "HIGH": len([i for i in self.issues_found if i["severity"] == "HIGH"]),
                "MEDIUM": len([i for i in self.issues_found if i["severity"] == "MEDIUM"]),
                "LOW": len([i for i in self.issues_found if i["severity"] == "LOW"])
            },
            "issues": self.issues_found
        }
        
        try:
            with open(output_file, 'w', encoding='utf-8') as f:
                json.dump(report, f, indent=4)
            logger.info(f"Report generated successfully: {output_file}")
        except Exception as e:
            logger.error(f"Error generating report: {str(e)}")
    
    def generate_html_report(self, output_file: str = "security_report.html") -> None:
        """
        Generate an HTML report of the security scan results.
        
        Args:
            output_file: Path to the output HTML file
        """
        if not self.issues_found:
            logger.warning("No issues found to generate HTML report")
            return
            
        # Group issues by file
        issues_by_file = {}
        for issue in self.issues_found:
            file_path = issue["file"]
            if file_path not in issues_by_file:
                issues_by_file[file_path] = []
            issues_by_file[file_path].append(issue)
            
        # Generate HTML content
        html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Security Scan Report</title>
    <style>
        body {{ font-family: Arial, sans-serif; margin: 0; padding: 20px; }}
        h1, h2, h3 {{ color: #333; }}
        .summary {{ background-color: #f5f5f5; padding: 15px; border-radius: 5px; margin-bottom: 20px; }}
        .file-section {{ margin-bottom: 30px; border: 1px solid #ddd; border-radius: 5px; padding: 15px; }}
        .issue {{ margin-bottom: 15px; padding: 10px; border-left: 5px solid #ccc; }}
        .HIGH {{ border-left-color: #d9534f; }}
        .MEDIUM {{ border-left-color: #f0ad4e; }}
        .LOW {{ border-left-color: #5bc0de; }}
        .code {{ background-color: #f8f9fa; padding: 10px; border-radius: 3px; font-family: monospace; overflow-x: auto; }}
        .severity-badge {{ display: inline-block; padding: 3px 8px; border-radius: 3px; color: white; font-size: 0.8em; }}
        .HIGH-bg {{ background-color: #d9534f; }}
        .MEDIUM-bg {{ background-color: #f0ad4e; }}
        .LOW-bg {{ background-color: #5bc0de; }}
        table {{ width: 100%; border-collapse: collapse; }}
        th, td {{ padding: 8px; text-align: left; border-bottom: 1px solid #ddd; }}
        th {{ background-color: #f2f2f2; }}
    </style>
</head>
<body>
    <h1>Security Scan Report</h1>
    
    <div class="summary">
        <h2>Summary</h2>
        <p>Scan completed on: {self.scan_timestamp}</p>
        <p>Files scanned: {self.files_scanned}</p>
        <p>Total issues found: {len(self.issues_found)}</p>
        <table>
            <tr>
                <th>Severity</th>
                <th>Count</th>
            </tr>
            <tr>
                <td><span class="severity-badge HIGH-bg">HIGH</span></td>
                <td>{len([i for i in self.issues_found if i["severity"] == "HIGH"])}</td>
            </tr>
            <tr>
                <td><span class="severity-badge MEDIUM-bg">MEDIUM</span></td>
                <td>{len([i for i in self.issues_found if i["severity"] == "MEDIUM"])}</td>
            </tr>
            <tr>
                <td><span class="severity-badge LOW-bg">LOW</span></td>
                <td>{len([i for i in self.issues_found if i["severity"] == "LOW"])}</td>
            </tr>
        </table>
    </div>
    
    <h2>Issues by File</h2>
"""
        
        # Add file sections
        for file_path, issues in issues_by_file.items():
            html_content += f"""
    <div class="file-section">
        <h3>{file_path}</h3>
        <p>Issues found: {len(issues)}</p>
"""
            
            # Add issues for this file
            for issue in issues:
                html_content += f"""
        <div class="issue {issue['severity']}">
            <h4>
                <span class="severity-badge {issue['severity']}-bg">{issue['severity']}</span>
                {issue['pattern']}
            </h4>
            <p><strong>Line {issue['line']}:</strong> {issue['description']}</p>
            <div class="code">{issue['code']}</div>
        </div>
"""
            
            html_content += """
    </div>
"""
        
        # Close HTML
        html_content += """
</body>
</html>
"""
        
        try:
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(html_content)
            logger.info(f"HTML report generated successfully: {output_file}")
        except Exception as e:
            logger.error(f"Error generating HTML report: {str(e)}")
    
    def print_summary(self) -> None:
        """
        Print a summary of the security scan results to the console.
        """
        print("\n" + "="*80)
        print(f"SECURITY SCAN SUMMARY - {self.scan_timestamp}")
        print("="*80)
        print(f"Files scanned: {self.files_scanned}")
        print(f"Total issues found: {len(self.issues_found)}")
        print(f"HIGH severity issues: {len([i for i in self.issues_found if i['severity'] == 'HIGH'])}")
        print(f"MEDIUM severity issues: {len([i for i in self.issues_found if i['severity'] == 'MEDIUM'])}")
        print(f"LOW severity issues: {len([i for i in self.issues_found if i['severity'] == 'LOW'])}")
        print("="*80)
        
        if self.issues_found:
            print("\nTop issues by severity:")
            for severity in ["HIGH", "MEDIUM", "LOW"]:
                issues = [i for i in self.issues_found if i["severity"] == severity]
                if issues:
                    print(f"\n{severity} SEVERITY ISSUES:")
                    for i, issue in enumerate(issues[:5], 1):  # Show top 5 issues of each severity
                        print(f"{i}. {issue['file']}:{issue['line']} - {issue['pattern']}")
                    
                    if len(issues) > 5:
                        print(f"   ... and {len(issues) - 5} more {severity.lower()} severity issues.")
        
        print("\nSee the generated reports for full details.")
        print("="*80 + "\n")


def main():
    """
    Main function to run the security scanner from the command line.
    """
    import argparse
    
    parser = argparse.ArgumentParser(description="Security Scanner for Code Repositories")
    parser.add_argument("-p", "--path", default=".", help="Path to the repository to scan")
    parser.add_argument("-j", "--json", default="security_report.json", help="Path to the JSON report output file")
    parser.add_argument("-H", "--html", default="security_report.html", help="Path to the HTML report output file")
    parser.add_argument("-v", "--verbose", action="store_true", help="Enable verbose output")
    
    args = parser.parse_args()
    
    # Configure logging level
    if args.verbose:
        logger.setLevel(logging.DEBUG)
    
    # Create scanner and run scan
    scanner = SecurityScanner(args.path)
    print(f"Starting security scan of {args.path}...")
    
    # Scan the repository
    scanner.scan_directory()
    
    # Generate reports
    scanner.generate_report(args.json)
    scanner.generate_html_report(args.html)
    
    # Print summary
    scanner.print_summary()
    
    return 0


if __name__ == "__main__":
    sys.exit(main())