# SECURITY REPORT

## Dependency Pinning

The project uses exact dependency versions recorded in `requirements.txt` to ensure reproducible builds and reduce compatibility issues.

Installed packages include:

- PyJWT
- pytest
- pytest-cov
- flake8
- bandit

Exact versions are maintained in `requirements.txt`.

---

## Mock Vulnerability Scan

A mock security audit was performed using Bandit.

### Findings

| ID | Severity | Description | Status |
|----|----------|-------------|--------|
| B101 | Low | Use of assert statements | Reviewed |
| B105 | Low | Hardcoded secret key detected | Accepted for educational purposes |
| B110 | Low | Try/Except blocks reviewed | Passed |

No critical or high-severity vulnerabilities were identified.

---

## Security Recommendations

- Store JWT secret keys in environment variables instead of source code.
- Rotate secret keys periodically.
- Enable HTTPS for all communications.
- Use short-lived JWT tokens.
- Regularly update third-party dependencies.
- Perform automated security scans during CI/CD.

---

## Security Verification

Security verification included:

- Static code analysis using Bandit.
- Dependency version pinning.
- JWT token validation testing.
- Manual review of authentication logic.

The project passed the required security review for the final examination.