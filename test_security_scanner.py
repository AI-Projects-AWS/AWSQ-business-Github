#!/usr/bin/env python3
"""
Unit tests for the security scanner module.
"""

import os
import unittest
import tempfile
import json
from security_scanner import SecurityScanner

class TestSecurityScanner(unittest.TestCase):
    """Test cases for the SecurityScanner class."""
    
    def setUp(self):
        """Set up test environment."""
        # Create a temporary directory for test files
        self.test_dir = tempfile.mkdtemp()
        
        # Create test files with known security issues
        self.python_file = os.path.join(self.test_dir, "test_python.py")
        with open(self.python_file, "w") as f:
            f.write("""
import os
import pickle

# Security issue: use of eval
def dangerous_function(user_input):
    return eval(user_input)  # Security issue: eval

# Security issue: use of os.system
def execute_command(cmd):
    os.system(cmd)  # Security issue: os.system

# Security issue: use of pickle.load
def load_data(file_path):
    with open(file_path, 'rb') as f:
        return pickle.load(f)  # Security issue: pickle.load

# Security issue: hardcoded credentials
password = "super_secret_password"  # Security issue: hardcoded password
api_key = "1234567890abcdef"  # Security issue: hardcoded key
""")
        
        self.java_file = os.path.join(self.test_dir, "test_java.java")
        with open(self.java_file, "w") as f:
            f.write("""
import java.util.*;
import java.io.*;

public class TestJava {
    // Security issue: hardcoded credentials
    private static final String PASSWORD = "admin123";  // Security issue: hardcoded password
    
    public static void main(String[] args) {
        // Security issue: printStackTrace
        try {
            File file = new File("nonexistent.txt");
            FileReader reader = new FileReader(file);
        } catch (Exception e) {
            e.printStackTrace();  // Security issue: printStackTrace
        }
        
        // Security issue: System.exit
        if (args.length == 0) {
            System.exit(1);  // Security issue: System.exit
        }
        
        // Security issue: insecure random
        Random random = new Random();  // Security issue: insecure random
        int value = random.nextInt();
    }
    
    // Security issue: Runtime.exec
    public static void executeCommand(String command) throws IOException {
        Runtime.getRuntime().exec(command);  // Security issue: Runtime.exec
    }
}
""")
        
        # Create scanner instance
        self.scanner = SecurityScanner(self.test_dir)
    
    def tearDown(self):
        """Clean up after tests."""
        # Remove test files
        if os.path.exists(self.python_file):
            os.remove(self.python_file)
        if os.path.exists(self.java_file):
            os.remove(self.java_file)
        
        # Remove test directory
        os.rmdir(self.test_dir)
    
    def test_scan_python_file(self):
        """Test scanning a Python file with known security issues."""
        issues = self.scanner.scan_file(self.python_file)
        
        # Check that we found the expected issues
        self.assertGreaterEqual(len(issues), 5)
        
        # Check for specific issues
        patterns_found = [issue["pattern"] for issue in issues]
        self.assertIn("eval_exec", patterns_found)
        self.assertIn("os_system", patterns_found)
        self.assertIn("pickle_load", patterns_found)
        self.assertIn("hardcoded_password", patterns_found)
    
    def test_scan_java_file(self):
        """Test scanning a Java file with known security issues."""
        issues = self.scanner.scan_file(self.java_file)
        
        # Check that we found the expected issues
        self.assertGreaterEqual(len(issues), 5)
        
        # Check for specific issues
        patterns_found = [issue["pattern"] for issue in issues]
        self.assertIn("hardcoded_password", patterns_found)
        self.assertIn("printStackTrace", patterns_found)
        self.assertIn("system_exit", patterns_found)
        self.assertIn("insecure_random", patterns_found)
        self.assertIn("runtime_exec", patterns_found)
    
    def test_scan_directory(self):
        """Test scanning a directory with multiple files."""
        issues = self.scanner.scan_directory()
        
        # Check that we found issues in both files
        self.assertGreaterEqual(len(issues), 10)
        
        # Check that we have issues from both file types
        file_paths = [issue["file"] for issue in issues]
        self.assertIn(self.python_file, file_paths)
        self.assertIn(self.java_file, file_paths)
    
    def test_generate_report(self):
        """Test generating a JSON report."""
        # Scan directory first
        self.scanner.scan_directory()
        
        # Generate report
        report_file = os.path.join(self.test_dir, "report.json")
        self.scanner.generate_report(report_file)
        
        # Check that the report file was created
        self.assertTrue(os.path.exists(report_file))
        
        # Check that the report contains valid JSON
        with open(report_file, "r") as f:
            report_data = json.load(f)
        
        # Check report structure
        self.assertIn("scan_timestamp", report_data)
        self.assertIn("files_scanned", report_data)
        self.assertIn("total_issues", report_data)
        self.assertIn("issues", report_data)
        
        # Clean up
        os.remove(report_file)
    
    def test_generate_html_report(self):
        """Test generating an HTML report."""
        # Scan directory first
        self.scanner.scan_directory()
        
        # Generate report
        report_file = os.path.join(self.test_dir, "report.html")
        self.scanner.generate_html_report(report_file)
        
        # Check that the report file was created
        self.assertTrue(os.path.exists(report_file))
        
        # Check that the report contains HTML
        with open(report_file, "r") as f:
            content = f.read()
        
        self.assertIn("<!DOCTYPE html>", content)
        self.assertIn("<html", content)
        self.assertIn("Security Scan Report", content)
        
        # Clean up
        os.remove(report_file)


if __name__ == "__main__":
    unittest.main()