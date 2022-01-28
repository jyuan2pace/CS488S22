# CS488: Computer Networks and The Internet
[Pace University](http://www.pace.edu)

Instructor: [Dr. Jun Yuan](http://csis.pace.edu/~jyuan2/)

**The content of this course changes as technology evolves**, to keep up to date with changes [follow me on GitHub](https://github.com/jyuan2pace/CS488OER).

# Acknowledgments
This is the OER (open educational resources) repo for _CS488 Computer Networking and the Internet_ in supporting the action plan for *high-quality* and *affordable* learning materials to Pace students. Within the bounds of Creative Commons licensing, materials are developed following 5Rs of OER.  In order to best suit Pace students and meet the particular learning goals of the course, some materials come from remixing materials under common creative licenses or in open access with fair use.

This course would have been impossible without the support from provost's mini-grant and the starting material from Srinivas Narayana, Jennifer Rexford and Badri Nath. We also thank Jim Kurose and Keith Ross for the slide decks accompanying their textbook; some of the slide decks in this course draw heavily from their slides.


# Course Description

This course provides a top-down study of modern computer networking and the Internet. Application layer topics include the Web, HTTP, FTP, SMTP, DNS, and socket programming. Transport layer topics include UDP, TCP, and congestion control. Network layer topics include link state routing, distance vector routing, IPv4, RIP, OSPF, BGP, IPv6, multicasting and IGMP, and mobile IP. Local area network topics include Ethernet, IEEE, 802.11, and Bluetooth.

# Textbook

* **[Required]** None is required to purchase. Reading will be assigned based on the [OER text: principles and practices](./OER_text.pdf) and open-access supplementary materials [OER: Computer network a top down approach](https://eclass.teicrete.gr/modules/document/file.php/TP326/%CE%98%CE%B5%CF%89%CF%81%CE%AF%CE%B1%20(Lectures)/Computer_Networking_A_Top-Down_Approach.pdf)

# Objectives

1. Understand the fundamental concepts of computer networks, particularly as related to the Internet;
2. Understand the multi-layer model of modern network architecture and its advantages and complexities;
3. Understand application layer messages and protocols, and write application layer software using sockets;
4. Understand transport layer functionality and explain how congestion control is implemented on the Internet;
5. Understand inter-networking and network layer functionality, and explain how routing is implemented on the Internet and network management;
6. Understand local area networks and link-layer issues including the details of the Ethernet and
IEEE 802.11 protocols;
7. Demonstrate your understanding of the material through a final project uploaded to GitHub.

# Syllabus
[Check out syllabus for 2022 Spring](https://docs.google.com/document/d/1xm9FhonUHEuMwYttbQLTa5kgFB2k3s4wz1XRF6_BUy4/edit?usp=sharing)

# Live Schedule
Week|Content|Recording|Reading|Quiz|Deadline and Notes
---|--------------|---|---|---|---
<img width=1000/>|<img width=2000/>|<img width=1000/>|<img width=1500/>|<img width=600/>|<img width=1500/>
Week 1: <br>Slides [1-1](https://docs.google.com/presentation/d/1bZMDGVAY49CXrCfYRfJJtwE7nfUSPb1aW2DKTHfFhfc/edit?usp=sharing) and [1-2](slides/intro-circuit-packet-switching.pptx)<br>First class on 01/25/2022 | **Week 1: Course Intro and Logistics** <ul><li>Part 1.1: Admin and Logistics <li>Part 1.2: Intro <li>Part 1.3: Circuit and packet switching <li> Part 1.4: Measuring networks <li> Part 1.5: Network Arch and layering </ul> |<ul><li>[1-1. Course intro and logistics](https://pace.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=ef5c4d57-4846-41b0-836e-ae280181ff00) <li> [1-2. TODO]() </ul>|<ul> <li> [Syllabus]() <li>[OER text: top-down](https://eclass.teicrete.gr/modules/document/file.php/TP326/%CE%98%CE%B5%CF%89%CF%81%CE%AF%CE%B1%20(Lectures)/Computer_Networking_A_Top-Down_Approach.pdf) Chapter 1.1-1.2, 1.5, 1.7  <li>[Evolution of the TCP/IP stack(including the interview with Bob Khan)](http://som.csudh.edu/fac/lpress/471/hout/tcpiphist.htm)  </ul>| Quiz#1 is out on Gradescope | Quiz#1 due 01/30/2022
Week 2:<br>Slides [2-1](./slides/application-sockets-dns.pptx) and [2-2](./slides/application-http.pptx) <br>Week of [TBD] | **Week 2: Application layer** <ul> <li>	Part 2.1: Intro to application layer <li>Part 2.2: DNS <li>Part 2.3: DNS records <li> Part 2.4: Intro to HTTP <li> Part 2.5: HTTP persistence and cookies </ul> |<ul><li>[2-1: TODO]() <li> [2-2: TODO]() </ul>|<ul><li>[Watch: How Packet Travels in Network](https://www.youtube.com/watch?v=xIuBmOufbls) <li> [OER text](./OER_text.pdf) Chapter 3.1-3.4.1 and 3.4.3 </ul>|Quiz#2 is out on [TBD] | Quiz#2 due [TBD] 
Week 3:<br>[Notes](https://colab.research.google.com/drive/1DGjoeOFKo9LTWmEwVvj-Rk_FjRGxvPug?usp=sharing)<br>Week of [TBD] | **Week 3: Python Prelimaries** <ul> <li>	Part 3.1: Variable declaration and assignment <li>Part 3.2: Integers, reals, mathematical operators <li>Part 3.3: Basic strings <li> Part 3.4: Conditions <li> Part 3.5: Lists</ul> |<ul><li>[3-1: TODO]() <li> [3-2: TODO]() </ul>|<ul> <li>[Chapter 2 from Think Python](http://www.greenteapress.com/thinkpython/html/thinkpython003.html) <li>[Numbers from the Python Tutorial](https://docs.python.org/3.4/tutorial/introduction.html#numbers)<li>[Read the while and break statements from Think Python](http://www.greenteapress.com/thinkpython/html/thinkpython008.html#toc79) <li>[Learn python 3 **beginner** 1-4](./python_materials/learn-python3): complete the notebooks first then do exercises </ul>|Quiz#3 is out on [TBD] | <ul> <li> Quiz#3 due [TBD]<li> [Project 1](https://docs.google.com/document/d/1LfAYkEqIO_fdRVsXhaahEP7Fjf-uOVqB5K-50kbYh60/edit?usp=sharing) out</ul>
Week 4:<br>[Notes](https://jerry-git.github.io/learn-python3/notebooks/beginner/html/dictionaries.html) and code of [server](./python_materials/server.ipynb) and [client](./python_materials/client.ipynb) <br>Week of [TBD]| **Week 4: Dive into Python** <ul>  <li>Part 4.1: Loops <li>Part 4.2: Dictionaries <li>Part 4.3: Functions <li> Part 4.4: packets and module <li> Part 4.5: socket programming in Python </ul> |<ul><li>[4-1. TODO]() <li> [4-2. TODO]() </ul>|<ul><li>[OER text](./OER_text.pdf) Chapter 3.5 <li>[Learn python 3 **beginner** 5-7, 9-10, 12 and 14](./python_materials/learn-python3): complete the notebooks first then do exercises </ul>|Quiz#4 is out on [TBD] | <ul> <li> Quiz#4 due [TBD]  <li> [Project 1 milestone 1](https://docs.google.com/document/d/1LfAYkEqIO_fdRVsXhaahEP7Fjf-uOVqB5K-50kbYh60/edit?usp=sharing) due [TBD] </ul>
Week 5:<br>[Notes](https://jamboard.google.com/d/1t14AhwxK17gY9gHIzSBZXeXlZ6tCyo8_SlswNeAI4wE/edit?usp=sharing) and [final server code](./python_materials/web-server-s3.py) <br>Week of [TBD]| **Week 5: Build a simple web server from scratch** <ul> <li> Part 5.1: HTTP responses and requests <li> Part 5.2: Hello Word server <li> Part 5.3: RESTful API <li> Part 5.4: Background: LAMP stack and MVC <li> Part 5.5: study case of login(db persistence) </ul> |<ul><li>[5-1. TODO]() <li> [5-2. TODO]() </ul>|<ul> <li>[Learn python 3 **beginner** 13, 18 and 19](./python_materials/learn-python3): complete the notebooks first then do exercises <li> Optional: [Web server for multi-clients with IPC](https://ruslanspivak.com/lsbaws-part3/) </ul>|Quiz#5 is out on [TBD] | <ul><li> Quiz#5 due [TBD]  <li> [Project 1 milestone 2](https://docs.google.com/document/d/1LfAYkEqIO_fdRVsXhaahEP7Fjf-uOVqB5K-50kbYh60/edit?usp=sharing) due [TBD] </ul>
Week 6:<br>Slides [6-1](./slides/6-1_transport-demultiplexing.pptx) and [6-2](./slides/6-2_transport-udp-error-detection.pptx)<br>Week of [TBD]| **Week 6: Intro to transport layer** <ul> <li>Part 6.1 Intro <li> Part 6.2 Demultiplexing packets <li> Part 6.3 UDP <li> Part 6.4 Error detection </ul> |<ul><li>[6-1. TODO]() <li> [6-2. TODO]() </ul>|<ul><li>[OER text](./OER_text.pdf) Chapter 3.4, 4.1-4.2 <li>[Learn python 3 **beginner** 12 and 15](./python_materials/learn-python3): complete the notebooks first then do exercises </ul>|Quiz#6 is out on [TBD] | <ul><li> Quiz#6 due [TBD] <li> [Project 1, milestone 3](https://docs.google.com/document/d/1LfAYkEqIO_fdRVsXhaahEP7Fjf-uOVqB5K-50kbYh60/edit?usp=sharing) is due [TBD]   <li> [Project 2: Reliability](https://docs.google.com/document/d/12CtvA1fYfuO7pB95WSkA2IR_x0ddyq2CtyLt6kgIlac/edit?usp=sharing) is out </ul>
Week 7:<br>Slides [7-1](./slides/7-1_transport-tcp-reliability-basics.pptx) and [7-2](./slides/7-2_transport-tcp-reliability-sliding-window.pptx)<br>Week of [TBD] | **Week 7: Reliablity** <ul> <li>Part 7.1 Reliablity basics <li>Part 7.2 Stop and wait <li>Part 7.3 Sliding window <li> Part 7.4 Congestion control  </ul> |<ul><li>[7-1. TODO]() <li> [7-2. TODO]() </ul>|<ul><li>[OER text](./OER_text.pdf) Chapter 4.1, 4.3 except congestion control<li>[Learn python 3 **beginner** 12 and 15](./python_materials/learn-python3): complete the notebooks first then do exercises </ul>|No quiz | <ul> <li>  [Project 2: Reliability milestone 1](https://docs.google.com/document/d/12CtvA1fYfuO7pB95WSkA2IR_x0ddyq2CtyLt6kgIlac/edit?usp=sharing) due [TBD] </ul>
Week 8:<br> Slides [8-1](./slides/8-1_transport-tcp-ordering-flow-control.pptx) and [8-2](./slides/8-2_transport-tcp-congestion-control-1.pptx) <br>Week of [TBD] | **Week 8: TCP flow control and congestion control** <ul> <li>Part 8.1 Flow control and ordered delivery <li>Part 8.2 Intro to congestion control <li>Part 8.3 The ready state <li> Part 8.4 Getting to ready state <li> Part 8.5 TCP Reno </ul> |<ul><li>[8-1. TODO]() <li> [8-2. TODO]() </ul>|<ul> <li>[OER text](./OER_text.pdf) 4.3   <li>[Using wireshark to analyze a tcp packet](http://courses.washington.edu/ee461/hw/lab4.pdf). You do not need to complete the questions, just read them to prep for next week </ul>|Quiz#7 is out on [TBD]| <ul><li> Quiz#7 due [TBD] <li>  [Project 2: Reliability milestone 2](https://docs.google.com/document/d/12CtvA1fYfuO7pB95WSkA2IR_x0ddyq2CtyLt6kgIlac/edit?usp=sharing) due [TBD] </ul>  
Week 9:<br>Slides of [9-1](./slides/9-1_transport-tcp-wrapup-intro-network.pptx) and [9-2](./slides/9-2_network-router-design.pptx) <br>Week of [TBD] | **Week 9: Network layer 1: addressing and router** <ul> <li> Part 9.1 TCP wrap up: connection management <li>Part 9.2 Introduction to network layer <li>Part 9.3 Internet addressing <li>Part 9.4 Router design <li> Part 9.5 Longest prefix matching  </ul> |<ul><li>[9-1. TODO]() <li> [9-2. TODO]() </ul>|<ul> <li>[OER text](./OER_text.pdf) Chapter 5.1.1-5.1.2 </ul>|No quiz | <ul><li>  [Project 2: Reliability milestone 3](https://docs.google.com/document/d/12CtvA1fYfuO7pB95WSkA2IR_x0ddyq2CtyLt6kgIlac/edit?usp=sharing) due [TBD] <li> ⚠️Check your 54% progress report ⚠️<li> [Project 3](https://docs.google.com/document/d/1youo4dj2EI8ng42hxoC7TlqWm5XO5hVleElCxjukfMM/edit?usp=sharing) out, due [TBD] </ul>
Week 10:<br> Slides of [10-1](./slides/10-1_network-protocols.pptx) and [10-2](./slides/10-2_network-protocols-2.pptx) <br>Week of [TBD] | **Week 10: Network layer 2: network protocols** <ul> <li> Part 10.1 IPv4 <li> Part 10.2 DHCP  <li> Part 10.3 IPv6 <li> Part 10.4 NAT (and its implication to P2P) <li> Part 10.5 ARP </ul> |<ul><li>[10-1. TODO]() <li> [10-2: TODO]() </ul>|<ul><li> [OER text](./OER_text.pdf) Chapter 5 </ul>|Quiz#8 out on [TBD] | <ul><li>Quiz#8 due [TBD] <li> [Project 3, milestone 1](https://docs.google.com/document/d/1youo4dj2EI8ng42hxoC7TlqWm5XO5hVleElCxjukfMM/edit?usp=sharing) due [TBD]</ul> 
Week 11:<br> slides of [11-1](./slides/11-1_network-intradomain-routing.pptx) and [11-2](./slides/11-2_network-interdomain-routing.pptx) <br>Week of [TBD] | **Week 11: Routing of the internet** <ul> <li> Part 11.1 Intro to routing  <li> Part 11.2 Link state protocols  <li> Part 11.3 Distance vector protocols <li> Part 11.3 BGP <li> Part 11.4 Routing for the internet </ul> |<ul><li>[11-1. TODO]() <li> [11-2. TODO]() </ul>|<ul> <li> [OER text](./OER_text.pdf) Chapter 5  </ul>|No quiz  | 
Week 12:<br> No slides <br>Week of [TBD]| :warning:**Week 12:Exam week**:warning: <ul> <li> Part 12.1 Review <li> Part 12.2 Final exam  </ul> |<ul><li>[12-1. TODO]() <li> 12-2. Final, No recording </ul>| No reading assignment|No quiz | 
Week 13:<br>Slides of [13-1](./slides/13-1_security-symmetric-key-crypto.pptx) and [13-2](./slides/13-2_security-public-key-crypto.pptx) <br>Week of [TBD] | **Week 13: Networking security** <ul><li>Part 13.1 Intro to networking security <li> Part 13.2 Intro to cryptograph <li> Part 13.3 Symmetric/secure key cryptograph <li> Part 13.4 Asymmetric key cryptograph  <li> Part 13.5 RSA crytosystem  </ul> |<ul><li>[13-1. TODO]() <li> [13-2. TODO]() </ul>|<ul><li>[Computer Networks: A Systems Approach](https://book.systemsapproach.org/security.html) 8.1, 8.2 and 8.4  </ul>|Quiz#9 is out on [TBD] | <ul><li> Quiz#9 due on [TBD]<li>  [Project 3 milestone 2](https://docs.google.com/document/d/1youo4dj2EI8ng42hxoC7TlqWm5XO5hVleElCxjukfMM/edit?usp=sharing) due [TBD] </ul>
Week 14:<br>Slides of [14-1](./slides/14-1_link-addressing-error-detection-correction.pptx) and [14-2](./slides/14-2_link-medium-access-control.pptx) <br>Week of [TBD] | **Week 14: Data link layer** <ul> <li> Part 14.1 Intro to data link layer <li> Part 14.2 Error detection <li> Part 14.3 Medium access control <li> Part 14.4 Random access control <li> Part 14.5 Ethernet MAC <li> Part 14.6 Wireless, celluar and 5G  </ul> |<ul><li>[14-1. TODO]() <li> [14-2. TODO]() </ul>|<ul> <li> [OER text](./OER_text.pdf) Chapter 6 </ul>|Quiz#10 out on [TBD] | <ul><li> Quiz#10 due on [TBD]<li>  [Project 3 milestone 3](https://docs.google.com/document/d/1youo4dj2EI8ng42hxoC7TlqWm5XO5hVleElCxjukfMM/edit?usp=sharing) due [TBD] </ul>
  
  
# Hands-out
* [Python 3 Cheating Sheet](./python_materials/python3cheatsheet.pdf)
* [Virtualize Python Execution](http://www.pythontutor.com/visualize.html#mode=edit)
