import os
import re


class ReverseEngineeringDetector:

    def __init__(self, source_dir):
        self.source_dir = source_dir


    def scan(self):

        findings = []

        short_names = 0
        total_classes = 0

        has_native_lib = False
        has_proguard = False
        readable_names = 0


        for root, _, files in os.walk(self.source_dir):

            for file in files:

                # Check native libs
                if file.endswith(".so"):
                    has_native_lib = True


                # Check ProGuard rules
                if file in ["proguard-rules.pro", "proguard.cfg"]:
                    has_proguard = True


                # Check Java classes
                if file.endswith(".java"):

                    total_classes += 1

                    # a.java, b.java, aa.java
                    if re.match(r"^[a-z]{1,2}\.java$", file):
                        short_names += 1
                    else:
                        readable_names += 1


        # ---- Detection Logic ----

        # No obfuscation
        if total_classes > 20 and short_names < (total_classes * 0.3):

            findings.append({
                "title": "Lack of Code Obfuscation",
                "severity": "Medium",
                "owasp": "M9: Reverse Engineering",
                "path": "N/A",
                "description": "Most class names are readable, indicating missing obfuscation",
                "remediation": "Enable ProGuard/R8 to obfuscate source code"
            })


        # No native protection
        if not has_native_lib:

            findings.append({
                "title": "Missing Native Protection",
                "severity": "Low",
                "owasp": "M9: Reverse Engineering",
                "path": "N/A",
                "description": "No native libraries detected for anti-reversing protection",
                "remediation": "Use native libraries for sensitive logic"
            })


        # No ProGuard config
        if not has_proguard:

            findings.append({
                "title": "Missing Obfuscation Configuration",
                "severity": "Low",
                "owasp": "M9: Reverse Engineering",
                "path": "N/A",
                "description": "No ProGuard/R8 configuration file found",
                "remediation": "Add and configure ProGuard rules"
            })


        return findings
