## H2 Goat

### x) Read and summarize OWASP: OWASP 10 2021

### Summary of the article [A05:2021-Security Misconfiguration](https://owasp.org/Top10/A05_2021-Security_Misconfiguration/)

Systems might be vulnerable if the application is missing appropriate security hardening across any part of the application stack or improperly configured permissions on cloud services. 90% of applications were tested for some form of misconfiguration, with an average incidence rate of 4%, and over 208k occurences of a Common Weakness Enumeration.
<br >
#### Some reasons 
* Unneeded features are deployed 
* Default accounts and passwords remain enabled.
* User error messages include stack traces.
* Upgraded systems disable or misconfigure the latest security features.
* Application servers, frameworks (Struts, Spring, ASP.NET), libraries, databases, and others have insecure security settings.
* The server sends no security headers or directives.
* Outdated or insecure software

#### How to prevent
* Secure installation process
* Different set of credentials
* Remove or don't install features and frameworks that aren't being used.
* Review and change the settings for all security notes, updates, and patches.
* segmentation, containerization, or cloud security groups, a segmented application architecture keeps components or tenants safe and separate 
* Security directives, like Security Headers, are sent to clients.
* A program that checks the configurations and settings in all environments to make sure they work

### Summary of the article [A06:2021-Vulnerable and Outdated Components](https://owasp.org/Top10/A06_2021-Vulnerable_and_Outdated_Components/)

Vulnerable Components are a known problem that we have trouble testing and figuring out how dangerous they are. They are also the only category that doesn't have any Common Vulnerabilities and Exposures (CVEs) mapped to the included CWEs, so an exploits/impact weight of 5.0 is used by default
<br >
#### Some reasonns of high percent of vulnerabilty
* the software is unsupported, or out of date. This includes the OS, web/application server, database management system (DBMS), applications, APIs and all components, runtime environments, and libraries.
* not scanning for vulnerabilities regularly 
* not fixing or upgrading the underlying platform, frameworks, and dependencies in a risk-based, timely fashion.
* not securing the components’ configurations
* software developers not testing the compatibility of updated, upgraded, or patched libraries.

### How to prevent 
Remove unneeded features, components, files, and documentation.

* Use versions, OWASP Dependency Check, retire.js, etc. to track client-side and server-side frameworks, libraries, and dependencies. Check CVE and NVD for component vulnerabilities. 
* Automate with software composition analysis tools. Get email alerts for component security vulnerabilities.

* Only use official sources via secure channels. To avoid harmful components, use signed packages 

* Check for unmaintained libraries and components that lack security fixes for previous versions. If patching is impossible, use a virtual patch to monitor, identify, or prevent the issue.

