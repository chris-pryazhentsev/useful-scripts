# LDAP/Active Directory Scripts

Collection of script to use if you need to talk to Active Directory from Python. Generally I've done this when I've wnated to make changes to Active Directory from a serverless function or any other linux based system without needing to escape to Windows and use PowerShell. A lot of this is just boilerplate to use the `ldap3` library. I don't see any point in rewriting it into something new just for the sake of being unique.

**NOTE:**
I'm testing this using my person AD domain which is running Windows Server 2025 at a 2025 functional level. I'm writing my scripts on MacOS 26 Beta. This largely shouldn't matter but please keep in mind that anything I'm doing here may need to be adapted in order to talk to your Domain Controllers properly