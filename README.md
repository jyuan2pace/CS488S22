# CS488 (OER): Computer Networks and The Internet
[Pace University](http://www.pace.edu)

Instructor: [Dr. Jun Yuan](http://csis.pace.edu/~jyuan2/)

**The content of this course changes as technology evolves**, to keep up to date with changes [follow me on GitHub](https://github.com/jyuan2pace/CS488OER).

# Acknowledgments
This is the OER (open educational resources) repo for _CS488 Computer Networking and the Internet_ in supporting the action plan for *high-quality* and *affordable* learning materials to Pace students. Within the bounds of Creative Commons licensing, materials are developed following 5Rs of OER.  In order to best suit Pace students and meet the particular learning goals of the course, some materials come from remixing materials under common creative licenses or in open access with fair use.

This course would have been impossible without starting material from Srinivas Narayana, Jennifer Rexford and Badri Nath. We also thank Jim Kurose and Keith Ross for the slide decks accompanying their textbook; some of the slide decks in this course draw heavily from their slides.


# Course Description

This course provides a top-down study of modern computer networking and the Internet. Application layer topics include the Web, HTTP, FTP, SMTP, DNS, and socket programming. Transport layer topics include UDP, TCP, and congestion control. Network layer topics include link state routing, distance vector routing, IPv4, RIP, OSPF, BGP, IPv6, multicasting and IGMP, and mobile IP. Local area network topics include Ethernet, IEEE, 802.11, and Bl

# Textbook

* **[Required]** None is required to purchase. Reading will be assigned based on the [OER text](./OER_text.pdf). 

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
This syllabus for 2022 Spring is yet to be developed.  [Check out a sample syllabus from past](https://docs.google.com/document/d/1xm9FhonUHEuMwYttbQLTa5kgFB2k3s4wz1XRF6_BUy4/edit?usp=sharing)

# Live Schedule
Week|Content|Recording|Reading|Quiz|Deadline
---|---|---|---|---|---
Week 1: <br>Slides [1-1](./slides/intro-course-overview.pptx) and [1-2](slides/intro-circuit-packet-switching.pptx)<br>First class on [TBD] | **Week 1: Course Intro and Logistics** <ul><li>Part 1.1: Admin and Logistics <li>Part 1.2: Intro <li>Part 1.3: Circuit and packet switching <li> Part 1.4: Measuring networks <li> Part 1.5: Network Arch and layering </ul> |<ul><li>[1-1. TODO]() <li> [1-2. TODO]() </ul>|<ul> <li> [Syllabus: TODO]() <li>[OER text](./OER_text.pdf) Chapter 2.1-2.4 <li>[Evolution of the TCP/IP stack(including the interview with Bob Khan)](http://som.csudh.edu/fac/lpress/471/hout/tcpiphist.htm) <li>[Watch: How Packet Travels in Network](https://www.youtube.com/watch?v=xIuBmOufbls) </ul>| Quiz#1 is out on [TODO] | Quiz#1 due [TODO]
Week 2:<br>Slides [2-1](./slides/application-sockets-dns.pptx) and [2-2](./slides/application-http.pptx) <br>Week of [TBD] | **Week 2: Application layer** <ul> <li>	Part 2.1: Intro to application layer <li>Part 2.2: DNS <li>Part 2.3: DNS records <li> Part 2.4: Intro to HTTP <li> Part 2.5: HTTP persistence and cookies </ul> |<ul><li>[2-1: TODO]() <li> [2-2: TODO]() </ul>|<ul> <li> [OER text](./OER_text.pdf) Chapter 3.1-3.4.1 and 3.4.3 </ul>|Quiz#2 is out on [TODO] | Quiz#2 due [TODO] 
Week 3:<br>[Notes](https://colab.research.google.com/drive/1DGjoeOFKo9LTWmEwVvj-Rk_FjRGxvPug?usp=sharing)<br>Week of [TBD] | **Week 3: Python Prelimaries** <ul> <li>	Part 3.1: Variable declaration and assignment <li>Part 3.2: Integers, reals, mathematical operators <li>Part 3.3: Basic strings <li> Part 3.4: Conditions <li> Part 3.5: Lists</ul> |<ul><li>[3-1: TODO]() <li> [3-2: TODO]() </ul>|<ul> <li>[Chapter 2 from Think Python](http://www.greenteapress.com/thinkpython/html/thinkpython003.html) <li>[Numbers from the Python Tutorial](https://docs.python.org/3.4/tutorial/introduction.html#numbers)<li>[Read the while and break statements from Think Python](http://www.greenteapress.com/thinkpython/html/thinkpython008.html#toc79) <li>[Learn python 3 **beginner** 1-4](./python_materials/learn-python3): complete the notebooks first then do exercises </ul>|Quiz#3 is out on [TODO] | Quiz#3 due [TODO] 
Week 4:<br>[Notes](https://jerry-git.github.io/learn-python3/notebooks/beginner/html/dictionaries.html) and code of [server](./python_materials/server.ipynb) and [client](./python_materials/client.ipynb) <br>Week of [TBD]| **Week 4: Dive into Python** <ul>  <li>Part 4.1: Loops <li>Part 4.2: Dictionaries <li>Part 4.3: Functions <li> Part 4.4: packets and module <li> Part 4.5: socket programming in Python </ul> |<ul><li>[4-1. TODO]() <li> [4-2. TODO]() </ul>|<ul><li>[OER text](./OER_text.pdf) Chapter 3.5 <li>[Learn python 3 **beginner** 5-7, 9-10, 12 and 14](./python_materials/learn-python3): complete the notebooks first then do exercises </ul>|Quiz#4 is out on [TODO] | <li> Quiz#4 due [TODO]  <li> [Project 1](https://docs.google.com/document/d/1LfAYkEqIO_fdRVsXhaahEP7Fjf-uOVqB5K-50kbYh60/edit?usp=sharing) out, milestone 1 due [TODO]
Week 5:<br>[Notes](https://jamboard.google.com/d/1t14AhwxK17gY9gHIzSBZXeXlZ6tCyo8_SlswNeAI4wE/edit?usp=sharing) and [final server code](./python_materials/web-server-s3.py) <br>Week of [TBD]| **Week 5: Build a simple web server from scratch** <ul> <li> Part 5.1: HTTP responses and requests <li> Part 5.2: Hello Word server <li> Part 5.3: RESTful API <li> Part 5.4: Background: LAMP stack and MVC <li> Part 5.5: study case of login(db persistence) </ul> |<ul><li>[5-1. TODO]() <li> [5-2. TODO]() </ul>|<ul> <li>[Learn python 3 **beginner** 13, 18 and 19](./python_materials/learn-python3): complete the notebooks first then do exercises <li> Optional: [Web server for multi-clients with IPC](https://ruslanspivak.com/lsbaws-part3/) </ul>|Quiz#5 is out on [TBD] | <ul><li> Quiz#5 due [TBD] 
Week 6:<br>Slides [6-1](./slides/6-1_transport-demultiplexing.pptx) and [6-2](./slides/6-2_transport-udp-error-detection.pptx)<br>Week of [TBD]| **Week 6: Intro to transport layer** <ul> <li>Part 6.1 Intro <li> Part 6.2 Demultiplexing packets <li> Part 6.3 UDP <li> Part 6.4 Error detection </ul> |<ul><li>[6-1. TODO]() <li> [6-2. TODO]() </ul>|<ul><li>[OER text](./OER_text.pdf) Chapter 3.4, 4.1-4.2 <li>[Learn python 3 **beginner** 12 and 15](./python_materials/learn-python3): complete the notebooks first then do exercises </ul>|Quiz#6 is out on [TBD] | <ul><li> Quiz#6 due [TBD] <li> [Project 1, milestone 2](https://docs.google.com/document/d/1LfAYkEqIO_fdRVsXhaahEP7Fjf-uOVqB5K-50kbYh60/edit?usp=sharing) is due [TBD] 
Week 7:<br>Slides [7-1](./slides/7-1_transport-tcp-reliability-basics.pptx) and [7-2](./slides/7-2_transport-tcp-reliability-sliding-window.pptx)<br>Week of [TBD] | **Week 7: Reliablity** <ul> <li>Part 7.1 Reliablity basics <li>Part 7.2 Stop and wait <li>Part 7.3 Sliding window <li> Part 7.4 Congestion control  </ul> |<ul><li>[7-1. TODO]() <li> [7-2. TODO]() </ul>|<ul><li>[OER text](./OER_text.pdf) Chapter 4.1, 4.3 <li>[Learn python 3 **beginner** 12 and 15](./python_materials/learn-python3): complete the notebooks first then do exercises </ul>|Quiz#7 is out on [TBD] | <ul><li> Quiz#7 due [TBD] <li> [Project 1, milestone 3](https://docs.google.com/document/d/1LfAYkEqIO_fdRVsXhaahEP7Fjf-uOVqB5K-50kbYh60/edit?usp=sharing) is due [TBD] <li>  [Project 2: Reliability](https://docs.google.com/document/d/12CtvA1fYfuO7pB95WSkA2IR_x0ddyq2CtyLt6kgIlac/edit?usp=sharing) is out, milestone1 due [TBD] </ul>
Week 8:<br>[Google slides](https://docs.google.com/presentation/d/1ng_74Z7xa--tV-4MSf36hbsgnC_smDZoiyRocAMsYW4/edit?usp=sharing) <br>Week of 03/15/2021 | **Week 8: TCP flow control and congestion control** <ul> <li>Part 8.1 Flow control and advised window <li>Part 8.2 Congestion control: program statement <li>Part 8.3 Congestion control: TCP new reno <li> Part 8.4 Wireshark on TCP header  </ul> |<ul><li>[8-1. Intro to flow control and congestion control](https://pace.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=bee8a6aa-5b2f-4bd6-9c07-aced0143da49) <li> [8-2. Congestion Control](https://pace.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=30a0b193-e87f-45c5-bbb0-acef0140f13d) </ul>|<ul>Finalized reading list: <li>Chapter 3.5-3.8  <li>[Using wireshark to analyze a tcp packet](http://courses.washington.edu/ee461/hw/lab4.pdf). You do not need to complete the questions, just read them to prep for next week </ul>|Quiz#7 this week | <ul><li> Quiz#7 is on gradescope.  
Week 9:<br>[Google slides](https://docs.google.com/presentation/d/1b7IZkRgX9gAKnRXtvSmYZN8UAqm6n5yS7JC_kIRiO98/edit?usp=sharing) <br>Week of 03/22/2021 | **Week 9: Network layer 1: addressing and router** <ul> <li>Part 9.1 Introduction to network layer <li>Part 9.2 Internet addressing <li>Part 9.3 Router design <li> Part 9.4 Longest prefix matching  </ul> |<ul><li>[9-1. Proj2 discussion](https://pace.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=98839572-74d0-4218-a026-acf4014cf40c) <li> [9-2. Network layer and IP address](https://pace.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=ed04dcdd-3fa4-4237-98c6-acf60142a376) </ul>|<ul>Reading list: <li>Chapter 4.1-4.4  </ul>|Quiz#8 is paused this week | <ul><li>  [Project 2: Reliability](https://docs.google.com/document/d/12CtvA1fYfuO7pB95WSkA2IR_x0ddyq2CtyLt6kgIlac/edit?usp=sharing) is out, milestone1 due 03/30
Week 10:<br>[Google slides](https://docs.google.com/presentation/d/1W_X0FtZl-VSj0BObP9N4OS3XvJuKHdfYaMtRi3VhqEw/edit?usp=sharing) <br>Week of 03/29/2021 | **Week 10: Network layer 2: IP protocol** <ul> Part 10.1 Router design <li> Part 10.2 Longest prefix matching  <li> Part 10.3 IP protocol <li> Part 10.4 Routing algorithm 1 </ul> |<ul><li>[10-1. Router design and IP match](https://pace.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=9e637d78-00db-4360-ae0d-acfb01406515) <li> [10-2: Network protocol, IPv4, ICMP, DHCP and NAT](https://pace.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=0f906d6a-d2c5-4f55-b4f2-acfd0151e90d) </ul>|<ul>Reading list: <li>Chapter 4.1-4.4  </ul>|Quiz#8 is resumed this week | <ul><li>  [Project 2 task 3 is extended to 04/08]() 
Week 11:<br>[Kami slides](https://kami.app/5UTT1axL4U2t) <br>Week of 04/06/2021 | **Week 11: Routing of the internet** <ul> Part 11.1 Intro to routing  <li> Part 11.2 Link state protocols  <li> Part 11.3 Distance vector protocols <li> Part 11.3 BGP <li> Part 11.4 Routing for the internet </ul> |<ul><li>[11-1. IPv6, ARP and Intro to routing](https://pace.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=08a5212b-a8db-494a-b3b5-ad02014f28ea) <li> [11-2. Routing algorithms](https://pace.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=821a78fa-389a-46aa-bf3d-ad0401505500) </ul>|<ul>Reading list: <li>Chapter 4.44 and 4.5-4.6  </ul>|Quiz#9 this week | <ul><li>  [Project 3](https://docs.google.com/document/d/1youo4dj2EI8ng42hxoC7TlqWm5XO5hVleElCxjukfMM/edit?usp=sharing) is out, possible milestone1(proposal) due 04/14/2021
Week 12:<br>[No slides]() <br>Week of 04/13/2021 | **Week 12: Final** <ul> Part 12.1 Review <li> Part 12.2 Final exam  </ul> |<ul><li>[12-1.Review](https://pace.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=c437b87e-223f-4e1b-947a-ad09015179c8) <li> [12-2. Final]() </ul>|<ul>Reading list: <li>Chapter 4.44 and 4.5-4.6  </ul>|No quiz | <ul><li>  [Project 3](https://docs.google.com/document/d/1youo4dj2EI8ng42hxoC7TlqWm5XO5hVleElCxjukfMM/edit?usp=sharing) is out, possible milestone1(proposal) due 04/14/2021
Week 13:<br>[Slides](https://kami.app/2jV-LjJ-E2u) <br>Week of 04/20/2021 | **Week 13: Final2 and DNS** <ul> Part 13.1 Final exam <li> Part 13.2 DNS  </ul> |<ul><li>[13-1. Final No recording]() <li> [13-2. DNS and application layer summary](https://pace.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=19b5e1ae-283d-42d4-ad2a-ad120146bb11) </ul>|<ul>Reading list: <li>Chapter 4.44 and 4.5-4.6  </ul>|No quiz | <ul><li>  [Project 3](https://docs.google.com/document/d/1youo4dj2EI8ng42hxoC7TlqWm5XO5hVleElCxjukfMM/edit?usp=sharing) is out, possible milestone1(proposal) due 04/14/2021
Week 14:<br>[Slides](https://drive.google.com/drive/folders/1v43wwYRrA_0-D-f77XpAu_U8MyJEO67Z?usp=sharing) <br>Week of 04/27/2021 | **Week 14: Data Link Layer and P2P ** <ul> Part 14.1 P2P <li> Part 14.2 Intro to data link layer <li> Part 14.3 Ethernet MAC  </ul> |<ul><li>[14-1. P2P](https://pace.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=69446af6-aa23-473d-ad2c-ad1701534097) <li> [14-2. Data link layer](https://pace.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=57bb9c4e-57ad-4ccd-8fbc-ad190144daa2) </ul>|<ul>Reading list: None  </ul>|Quiz 9 in-class | <ul><li>  [Project 3](https://docs.google.com/document/d/1youo4dj2EI8ng42hxoC7TlqWm5XO5hVleElCxjukfMM/edit?usp=sharing) is out, possible milestone1(proposal) due 04/14/2021
  
  
# Hands-out
* [Python 3 Cheating Sheet](./python_materials/python3cheatsheet.pdf)
* [Virtualize Python Execution](http://www.pythontutor.com/visualize.html#mode=edit)
