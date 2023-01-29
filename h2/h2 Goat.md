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
