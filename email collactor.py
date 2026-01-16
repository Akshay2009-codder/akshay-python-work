import re

data = '''
sample_text = """
Hey team!!! Contact us asap ---   xxyyzz@@oops..com  (ignore)  

Valid: 
- support@example.com
- info@example.org
- sales@example.net
- helpdesk@sub.example.co.uk
- akshay.dhumda+test@gmail.com
- ak_tech99@outlook.com
- first.last@company.io
- dev-team@startup.xyz
- data.engineer-01@big-corp.inc
- notes@my-domain.tech
- user_12345@school.edu
- no-reply@mail.server.co.in
- admin@mail-1.region-2.provider.com
- contact@shop-online.store
- hr@company-careers.jobs
- press@media-house.news
- hello@cool.app
- billing@saas-platform.cloud
- api@v2.api.example.dev
- bug.report@tracker.systems

Garbage lines below (emails mixed with noise):
>>> "email me at" ::: customer.care (at) example (dot) com  [should NOT match]
Weird: john..doe@@example..com  // invalid
Random: !!! akshay@@gmail..com ;;; 
Some:   user.one@domain.com, user.two@domain.com; user-three@domain.com
CSV-ish: name1@demo.com,name2@demo.com , name3@demo.com
Brackets: <sales-team@marketplace.biz>, <feedback@portal.site>
Quotes: "qa-team" <qa.team@product.dev> and 'ops' <ops.alerts@infra.dev>
Paren: (reach) support.us@north.company.us (today)
With text: Send to dev@code.run and also cc root@localhost and test@127.0.0.1  (IP/localhost usually invalid)
Tabs	and spaces	mix:	a_b-c.d@mix-domain.io
Trailing punctuation: client@bank.finance, vendor@supply.chain; partner@alliances.group.
Dupe: info@example.org  again INFO@example.org
Broken: user@@double@sign.com
Paths: visit https://example.com?ref=mailme@url.com (should match mailme@url.com)
Markdown: [email](mailto:team@docs.readme)
More:
- newsletter@news.co
- alerts@notify.me
- batch_01.list@mailer.queue
- cust.success@enterprise.solutions
- a.b-c_d+promo@campaign.mail
- job.applications@hr.hiring
- research.lab@university.ac.in
- teacher.room@school.k12.us
- student-services@campus.edu
- devnull@blackhole.null
- bot@automation.tools
- noreply@dont-reply.me
- support-01@help.center
- pr@brand.global
- legal@compliance.law
- hello.world@examples.tld
Noise noise NOISE >>> not_an_email@ @@ @notemail .com
Obfuscation: admin [at] site [dot] com  (should NOT match)
JSON-ish: {"contact":"team.api@service-stack.dev","alt":"backup@edge.pop"}
Signs: ++ plus@signs.plus ++ eq=eq@eq.eq ==
Hyphen-start (invalid usually): -dash@weird.com
End.
'''

pattern = re.compile(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[A-Za-z]{2,}')
matches = pattern.findall(data)
emails = sorted(set(matches))

with open("emails_collector_output.txt", "w", encoding="utf-8") as f:
    for i, email in enumerate(emails, start=1):
        f.write(f"Email {i}: {email}\n")

print(f"Collected {len(emails)} emails!")
