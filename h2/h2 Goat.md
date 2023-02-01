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

### Summary of the article [A03:2021-Injection](https://owasp.org/Top10/A03_2021-Injection/)

An attacker injects data into an application to modify the meaning of commands issued to an interpreter. SQL injection is the most typical example. An attacker sends "101 OR 1=1" instead of "101". This data makes SQL queries return all records instead of one. SQL, LDAP, Operating System, XPath, XQuery, Expression Language, and others are common web interpreters. Data-to-command interfaces are vulnerable. Even XSS is HTML injection.

* User-supplied data is not validated, filtered, or sanitized by the application.

* Dynamic queries or non-parameterized calls without context-aware escaping are used directly in the interpreter.

* Hostile data is used within object-relational mapping (ORM) search parameters to extract additional, sensitive records.

* Hostile data is directly used or concatenated. The SQL or command contains the structure and malicious data in dynamic queries, commands, or stored procedures.



### How to prevent 

* Use LIMIT and other SQL controls within queries to prevent mass disclosure of records in case of SQL injection.
* For any residual dynamic queries, escape special characters using the specific escape syntax for that interpreter.
* Use positive server-side input validation. This is not a complete defense as many applications require special characters, such as text areas or APIs for mobile applications
* The preferred option is to use a safe API, which avoids using the interpreter entirely, provides a parameterized interface, or migrates to Object Relational Mapping Tools (ORMs).


### Summary of [Darknet Diaries Episode 131](https://darknetdiaries.com/episode/131/)

On the podcast, Jack and Andy revealed a website with inappropriate content (child pornography, child abuse) that existed on the darknet. The website granted users access if they transferred a particular quantity of Bitcoin to the website's owner's wallet. Agents investigating the case employed technologies to follow through blockchain Bitcoin transactions among users and web site administrators, but it didn't help them much. Only until the administrator made a major error and opened the website to the public were the agents able to obtain IP addresses of users and administrators. They chose to begin with users who had access to minors and may exploit them. After locking up hazardous website members, they proceeded to Korea to find the admin. The agents successfully imprisoned the administrator and pulled down the website.

* What I learned?

It was fascinating to hear about the structure of the blockchain and how agents investigated the case. Users feel that cryptocurrency allows them to conduct secret transactions, but it is really more visible in some ways than the banking system since, in the end, people need to cash out their money, which is impossible without providing personal information. Also, agents tracked nonstop until the website's owner made a mistake, just as hackers do when they have a target.

* My thougth
It is unfortunate that people might utilize the darknet in heinous ways, but being aware of and understanding about the darknet is always beneficial to people.

## [CVE](https://www.imperva.com/learn/application-security/cve-cvss-vulnerability/)
* CVE (Common Vulnerabilities and Exposures) is a standardized database for identifying and listing security flaws in software and systems. It serves as a single point of reference for researchers, practitioners, and consumers to identify, track, and prioritize the vulnerabilities that must be addressed. 

* CVE serves as a systematic and comprehensive technique for detecting, tracking, and mitigating security vulnerabilities in order to assist avoid cyber attacks and improve overall security.
* CVE-2022-3990 
HP with [CVE-2022-3990](https://cve.report/CVE-2022-3990) fixed bugs in HPSFViewer versions lower than 8.6.3.1. 


## a) Sequel. Solve [SQLZoo](https://sqlzoo.net/wiki/SQL_Tutorial)

SqlZoo is a fantastic site for learning SQL and practicing with interesting tasks.

<img src="https://github.com/Sakhi97/Information_security/blob/main/h2/sqlzoo.png" width="750" height="400">

In the beginning, you can practice easy tasks by modifying the sql statement slightly. However, as you progress, the difficulty will increase.
### 0 SELECT BASICS
<img src="https://github.com/Sakhi97/Information_security/blob/main/h2/sql0.png" width="750" height="400">

### 2 SELECT FROM WORLD
The first three exercises were simple; all I had to do was follow the instructions.
in 1 one I had to select name, population and continent from table world
in 2 one I had to add where statement which shows only if population is over 200 mil.
in 3 one I had to find gdp per capita, so I just divided gdp on population

<img src="https://github.com/Sakhi97/Information_security/blob/main/h2/sql2-1.2.3.png" width="750" height="400">

in 4 one I divided population on 1 mil and added the where statement equals to South Africa
in 5 one I used IN to find name and population for three countries
in 6 one I used LIKE because I had to find any country which has in it's name United.
<img src="https://github.com/Sakhi97/Information_security/blob/main/h2/sql2-4.5.6.png" width="750" height="400">
Others were voluntary tasks so I did all 13 tasks and only 8 one I could not do because I could not use XOR statement.
<img src="https://github.com/Sakhi97/Information_security/blob/main/h2/sql2-7.8.png" width="750" height="400">
<img src="https://github.com/Sakhi97/Information_security/blob/main/h2/sql2-9.10.png" width="750" height="400">
<img src="https://github.com/Sakhi97/Information_security/blob/main/h2/sql2-11.12.png" width="750" height="400">
<img src="https://github.com/Sakhi97/Information_security/blob/main/h2/sql2-13.png" width="750" height="400">

## b) Injected. Solve Webgoat A1 Injection (intro)
#### Task 2
I did completed the task with the command 'select department from employees where userid=96134'

<img src="https://github.com/Sakhi97/Information_security/blob/main/h2/webgoat2.png" width="650" height="250">

#### Task 3
I completed with the command 'update employees set department ='Sales' where userid=89763

<img src="https://github.com/Sakhi97/Information_security/blob/main/h2/webgoat3.png" width="650" height="250">

#### Task 4

Added phone column to the table

<img src="https://github.com/Sakhi97/Information_security/blob/main/h2/webgoat4.png" width="650" height="250">

#### Task 5

In this task I granted admin rights to unauthorized user

<img src="https://github.com/Sakhi97/Information_security/blob/main/h2/webgoat5.png" width="650" height="250">

#### When user input is not correctly managed, it can result in data being revealed, deleted, or manipulated by an attacker. To avoid SQL injection attacks: employ a least-privilege approach to input validation/sanitation select a database technology that: supports parameterized query options but does not permit command chaining



#### Task 9

Injection occurs when the input is directly entered into the query:
`SELECT * FROM user_data WHERE first_name='John' AND last_name='' OR '1'='1';`

<img src="https://github.com/Sakhi97/Information_security/blob/main/h2/webgoat9.png" width="650" height="250">

#### Task 10

In the following exercise, I play the role of a regular user, John Smith (no admin privileges), who is curious and willing to commit criminal actions to obtain all income data.

Entering text onto input fields (Employee Name and Authentication TAN)

<img src="https://github.com/Sakhi97/Information_security/blob/main/h2/webgoat10.png" width="650" height="250">

#### Task 11

With the command `Smith' or '1'1` and `3SL99A or '1'1`I got access to databse

<img src="https://github.com/Sakhi97/Information_security/blob/main/h2/webgoat11.png" width="650" height="250">

#### Task 12

With the command `3SL99A';UPDATE Employees SET salary=100000 WHERE last_name='Smith' AND auth_tan='3SL99A';--` I changed salary of Smith.

<img src="https://github.com/Sakhi97/Information_security/blob/main/h2/webgoat12.png" width="650" height="250">

#### Task 13
The final step of the Injection introduction is to delete the access log- table.
with ´; DROP TABLE access_log;--´ I deleted information about manipulation with salary.

<img src="https://github.com/Sakhi97/Information_security/blob/main/h2/webgoat13.png" width="650" height="250">

## Sources and references

https://terokarvinen.com/2023/information-security-2023/

https://owasp.org/Top10/A03_2021-Injection/

https://owasp.org/Top10/A06_2021-Vulnerable_and_Outdated_Components/

https://owasp.org/Top10/A05_2021-Security_Misconfiguration/

https://darknetdiaries.com/

https://sqlzoo.net/wiki/SQL_Tutorial

https://cvetrends.com/

https://cve.mitre.org/


