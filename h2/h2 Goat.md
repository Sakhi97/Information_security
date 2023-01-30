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

## Summary and what I learned [Darknet Diaries Episode 131](https://darknetdiaries.com/episode/131/)

On the podcast, Jack and Andy revealed a website with inappropriate content (child pornography, child abuse) that existed on the darknet. The website granted users access if they transferred a particular quantity of Bitcoin to the website's owner's wallet. Agents investigating the case employed technologies to follow through blockchain Bitcoin transactions among users and web site administrators, but it didn't help them much. Only until the administrator made a major error and opened the website to the public were the agents able to obtain IP addresses of users and administrators. They chose to begin with users who had access to minors and may exploit them. After locking up hazardous website members, they proceeded to Korea to find the admin. The agents successfully imprisoned the administrator and pulled down the website.

* What I learned?

It was fascinating to hear about the structure of the blockchain and how agents investigated the case. Users feel that cryptocurrency allows them to conduct secret transactions, but it is really more visible in some ways than the banking system since, in the end, people need to cash out their money, which is impossible without providing personal information. Also, agents tracked nonstop until the website's owner made a mistake, just as hackers do when they have a target.

* My thougth
It is unfortunate that people might utilize the darknet in heinous ways, but being aware of and understanding about the darknet is always beneficial to people.

## [CVE](https://www.imperva.com/learn/application-security/cve-cvss-vulnerability/)
* CVE (Common Vulnerabilities and Exposures) is a standardized database for identifying and listing security flaws in software and systems. It serves as a single point of reference for researchers, practitioners, and consumers to identify, track, and prioritize the vulnerabilities that must be addressed. 

* CVE serves as a systematic and comprehensive technique for detecting, tracking, and mitigating security vulnerabilities in order to assist avoid cyber attacks and improve overall security.
* CVE-2022-3990 
HP with CVE-2022-3990 fixed bugs in HPSFViewer versions lower than 8.6.3.1. 


## a) Sequel. Solve [SQLZoo](https://sqlzoo.net/wiki/SQL_Tutorial)




